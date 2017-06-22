# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Data access object for Instance."""
from google.cloud.security.common.data_access import dao
from google.cloud.security.common.data_access.sql_queries import select_data
from google.cloud.security.common.gcp_type import instance
from google.cloud.security.common.gcp_type import resource
from google.cloud.security.common.util import log_util
from google.cloud.security.common.gcp_type import network
import json
import re


# TODO: The next editor must remove this disable and correct issues.
# pylint: disable=missing-type-doc,missing-return-type-doc


LOGGER = log_util.get_logger(__name__)


class InstanceDao(dao.Dao):
    """Instance DAO."""

    def get_instances(self, timestamp):
        """Get instances from a particular snapshot.

        Args:
            timestamp: The snapshot timestamp.

        Returns:
            A list of Instance.

        Raises:
            MySQLError if a MySQL error occurs.
        """
        query = select_data.INSTANCES.format(timestamp)
        rows = self.execute_sql_with_fetch(
            resource.ResourceType.INSTANCE, query, ())
        return [self.map_row_to_object(instance.Instance, row) for row in rows]

    def get_project_network_subnet(self, timestamp):
        all_instances = self.get_instances(timestamp)
        pns_list = []
        for instance in all_instances:
            network_interfaces  = instance.network_interfaces
            for network_interface in json.loads(network_interfaces):
                if 'network' in network_interface:
                    network_url = network_interface['network']
                    network_url_match_group = re.search('compute\/v1\/projects\/([^\/]*).*networks\/([^\/]*)', network_url)
                    project_id = network_url_match_group.group(1)
                    network_id = network_url_match_group.group(2)
                else:
                    project_id = None
                    network_id = None
                if 'subnetwork' in network_interface:
                    subnet_url  = network_interface['subnetwork']
                    subnet_url_match_group = re.search('compute\/v1\/projects\/[^\/]*\/regions\/([^\/]*)\/subnetworks\/([^\/]*)', subnet_url)
                    region = subnet_url_match_group.group(1)
                    subnet_id = subnet_url_match_group.group(2)
                else:
                    region = None
                    subnet_id = None

                access_config_flag = "accessConfigs" in network_interface
                tmp_network = network.Network(project_id = project_id,
                                                network_id = network_id,
                                                region = region,
                                                subnet_id = subnet_id,
                                                access_config_flag = access_config_flag)
                pns_list.append(tmp_network)
        #maybe i dont uniq this here
        pns_list = set(pns_list)
        return pns_list




