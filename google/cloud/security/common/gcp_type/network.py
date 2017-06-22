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

"""An AppEngine Application.

See: https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps
"""

# TODO: The next editor must remove this disable and correct issues.
# pylint: disable=missing-param-doc

# pylint: disable=too-many-instance-attributes
class Network(object):
    """Represents Network resource."""

    def __init__(self, **kwargs):
        """Network resource."""
        self.project_id = kwargs.get('project_id')
        self.network_id = kwargs.get('network_id')
        self.region = kwargs.get('region')
        self.subnet_id = kwargs.get('subnet_id')
        self.access_config_flag = kwargs.get('access_config_flag')

    def __repr__(self):
        return 'Project: %s Network: %s Region: %s Subnet: %s Public: %s' % (self.project_id, self.network_id, self.region, self.subnet_id, self.access_config_flag)

    def __hash__(self):
        return hash(self.__repr__())

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __eq__(self, other):
        if isinstance(other, Network):
            return ((self.project_id == other.project_id) and 
                    (self.network_id == other.network_id) and 
                    (self.region == other.region) and
                    (self.subnet_id == other.subnet_id) and
                    (self.access_config_flag == other.access_config_flag))
        else:
            return False