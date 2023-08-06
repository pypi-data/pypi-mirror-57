"""
This program is a library to communicate with the Centreon REST API

Copyright (C) 2019 Niklas Pfister, contact@omikron.pw

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
import urllib3

from centreon_sdk.builder.field_builder import FieldBuilder
from centreon_sdk.builder.host_builder import HostBuilder
from centreon_sdk.centreon import Centreon
from centreon_sdk.network.network import HTTPVerb
from centreon_sdk.objects.base.acl_group import ACLGroupParam
from centreon_sdk.objects.base.host import HostParam

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    cent = Centreon("TEST-Niklas", open("../../CentreonScripts/credentials_downtimes_acknowledgements").read(),
                    "https://monitoring-web.ccs-h.de/centreon/api/index.php", verify=False)
   # centreon = Centreon("REST", "1lCNqIvU", "https://centreon.omikron.pw/centreon/api/index.php", verify=False)
    result = cent.service_status_get(fields="host_name, description, acknowledged, host_acknowledged", limit=5000, viewType="all", status="all")
    print(result)
    if isinstance(result, list):
        for item in result:
            if item["acknowledged"] == "1" or item["host_acknowledged"] == "1":
                print(item.__dict__) if not isinstance(item, dict) else print(item)
    else:
        print(result)
