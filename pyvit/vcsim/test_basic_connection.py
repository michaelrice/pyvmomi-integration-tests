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

import atexit

from pyvit.common import tests
from pyVim import connect

class BasicConnection(tests.BaseTest):

    def test_smart_connect(self):
        con = self.connections.vcsim
        service_instance = connect.SmartConnect(host=con.host,
                                                user=con.user,
                                                pwd=con.password,
                                                port=con.port)
        atexit.register(connect.Disconnect, service_instance)
        session_id = service_instance.content.sessionManager.currentSession.key
        self.assertIsNotNone(session_id)