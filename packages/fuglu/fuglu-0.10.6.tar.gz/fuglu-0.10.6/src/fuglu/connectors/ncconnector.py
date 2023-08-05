#   Copyright 2009-2019 Oli Schacher, Fumail Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

import logging
import tempfile
from fuglu.shared import Suspect
from fuglu.protocolbase import ProtocolHandler, BasicTCPServer
from fuglu.connectors.smtpconnector import buildmsgsource
from fuglu.stringencode import force_bString, force_uString
import os
import socket

class NCHandler(ProtocolHandler):
    protoname = 'NETCAT'

    def __init__(self, socket, config):
        ProtocolHandler.__init__(self, socket, config)
        self.sess = NCSession(socket, config)
        try:
            self._att_mgr_cachesize = config.getint('performance','att_mgr_cachesize')
        except Exception:
            self._att_mgr_cachesize = None

    def get_suspect(self):
        success = self.sess.getincomingmail()
        if not success:
            self.logger.error('incoming smtp transfer did not finish')
            return None

        sess = self.sess
        fromaddr = "unknown@example.org"
        toaddr = "unknown@example.org"

        tempfilename = sess.tempfilename

        suspect = Suspect(fromaddr, [toaddr, ], tempfilename, att_cachelimit=self._att_mgr_cachesize)
        return suspect

    def commitback(self, suspect):
        self.sess.send("DUNNO:")
        self.sess.endsession(buildmsgsource(suspect))

    def defer(self, reason):
        self.sess.endsession('DEFER:%s' % reason)

    def discard(self, reason):
        self.sess.endsession('DISCARD:%s' % reason)

    def reject(self, reason):
        self.sess.endsession('REJECT:%s' % reason)

class NCServer(BasicTCPServer):
    def __init__(self, controller, port=10125, address="127.0.0.1"):
        BasicTCPServer.__init__(self, controller, port, address, NCHandler)


class NCSession(object):

    def __init__(self, socket, config):
        self.config = config
        self.from_address = None
        self.recipients = []
        self.helo = None

        self.socket = socket
        self.logger = logging.getLogger("fuglu.ncsession")
        self.tempfile = None

    def send(self, message):
        self.socket.sendall(force_bString(message))

    def endsession(self, message):
        try:
            self.send(message)
            self.closeconn()
        except Exception as e:
            self.logger.error(str(e))

    def closeconn(self):
        self.socket.shutdown(socket.SHUT_WR)
        self.socket.close()

    def getincomingmail(self):
        """return true if mail got in, false on error Session will be kept open"""
        self.socket.send(force_bString("fuglu scanner ready - please pipe your message\r\n"))
        try:
            (handle, tempfilename) = tempfile.mkstemp(
                prefix='fuglu', dir=self.config.get('main', 'tempdir'))
            self.tempfilename = tempfilename
            self.tempfile = os.fdopen(handle, 'w+b')
        except Exception as e:
            self.endsession('could not write to tempfile')

        while True:
            data = self.socket.recv(1024)
            if len(data) < 1:
                break
            self.tempfile.write(data)
        self.tempfile.close()
        self.logger.debug('Incoming message received')
        return True
