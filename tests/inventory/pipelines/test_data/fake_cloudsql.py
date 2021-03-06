# Copyright 2017 The Forseti Security Authors. All rights reserved.
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

"""Fake cloudsql data."""

from copy import deepcopy

FAKE_CLOUDSQL_MAP = [{
    'project_number':
        11111,
    'instances': [{
        u'backendType':
            u'SECOND_GEN',
        u'connectionName':
            u'project-1:us-east1:cloudsql-instance',
        u'databaseVersion':
            u'MYSQL_5_7',
        u'etag':
            u'"CAE="',
        u'instanceType':
            u'CLOUD_SQL_INSTANCE',
        u'ipAddresses': [{
            u'ipAddress': u'1.2.3.4',
            u'type': u'PRIMARY'
        }],
        u'kind':
            u'sql#instance',
        u'name':
            u'cloudsql-instance',
        u'project':
            u'project-1',
        u'region':
            u'us-east1',
        u'selfLink':
            u'https://www.googleapis.com/sql/v1beta4/projects/project-1/instances/cloudsql-instance',
        u'serverCaCert': {},
        u'serviceAccountEmailAddress':
            u'serviceaccount1@iam.gserviceaccount.com',
        u'settings': {
            u'activationPolicy': u'ALWAYS',
            u'authorizedGaeApplications': [],
            u'backupConfiguration': {
                u'binaryLogEnabled': True,
                u'enabled': True,
                u'kind': u'sql#backupConfiguration',
                u'startTime': u'03:00'
            },
            u'dataDiskSizeGb': u'10',
            u'dataDiskType': u'PD_SSD',
            u'ipConfiguration': {
                u'authorizedNetworks': [],
                u'ipv4Enabled': True,
                u'requireSsl': True
            },
            u'kind': u'sql#settings',
            u'pricingPlan': u'PER_USE',
            u'replicationType': u'SYNCHRONOUS',
            u'settingsVersion': u'28',
            u'storageAutoResize': False,
            u'storageAutoResizeLimit': u'0',
            u'tier': u'db-n1-standard-1'
        },
        u'state':
            u'RUNNABLE'
    }, {
        u'backendType':
            u'SECOND_GEN',
        u'connectionName':
            u'project-1:europe-west1:test-forseti',
        u'databaseVersion':
            u'MYSQL_5_7',
        u'etag':
            u'"CAE="',
        u'instanceType':
            u'CLOUD_SQL_INSTANCE',
        u'ipAddresses': [{
            u'ipAddress': u'4.3.2.1',
            u'type': u'PRIMARY'
        }],
        u'kind':
            u'sql#instance',
        u'name':
            u'test-forseti',
        u'project':
            u'project-1',
        u'region':
            u'europe-west1',
        u'selfLink':
            u'https://www.googleapis.com/sql/v1beta4/projects/project-1/instances/test-forseti',
        u'serverCaCert': {},
        u'serviceAccountEmailAddress':
            u'serviceaccount2@iam.gserviceaccount.com',
        u'settings': {
            u'activationPolicy': u'ALWAYS',
            u'authorizedGaeApplications': [],
            u'backupConfiguration': {
                u'binaryLogEnabled': False,
                u'enabled': False,
                u'kind': u'sql#backupConfiguration',
                u'startTime': u'03:00'
            },
            u'dataDiskSizeGb': u'250',
            u'dataDiskType': u'PD_SSD',
            u'ipConfiguration': {
                u'authorizedNetworks': [{
                    u'kind': u'sql#aclEntry',
                    u'name': u'test',
                    u'value': u'0.0.0.0/0'
                }],
                u'ipv4Enabled':
                    True
            },
            u'kind': u'sql#settings',
            u'maintenanceWindow': {
                u'day': 0,
                u'hour': 0,
                u'kind': u'sql#maintenanceWindow'
            },
            u'pricingPlan': u'PER_USE',
            u'replicationType': u'SYNCHRONOUS',
            u'settingsVersion': u'6',
            u'storageAutoResize': True,
            u'storageAutoResizeLimit': u'0',
            u'tier': u'db-n1-standard-1'
        },
        u'state':
            u'RUNNABLE'
    }, {
        u'backendType':
            u'SECOND_GEN',
        u'connectionName':
            u'project-1:us-central1:forsetitest-2',
        u'databaseVersion':
            u'MYSQL_5_7',
        u'etag':
            u'"CAE="',
        u'instanceType':
            u'CLOUD_SQL_INSTANCE',
        u'ipAddresses': [{
            u'ipAddress': u'192.168.1.2',
            u'type': u'PRIMARY'
        }],
        u'kind':
            u'sql#instance',
        u'name':
            u'forsetitest-2',
        u'project':
            u'project-1',
        u'region':
            u'us-central1',
        u'selfLink':
            u'https://www.googleapis.com/sql/v1beta4/projects/project-1/instances/forsetitest-2',
        u'serverCaCert': {},
        u'serviceAccountEmailAddress':
            u'serviceaccount3@iam.gserviceaccount.com',
        u'settings': {
            u'activationPolicy': u'ALWAYS',
            u'authorizedGaeApplications': [],
            u'backupConfiguration': {
                u'binaryLogEnabled': True,
                u'enabled': True,
                u'kind': u'sql#backupConfiguration',
                u'startTime': u'11:00'
            },
            u'dataDiskSizeGb': u'25',
            u'dataDiskType': u'PD_HDD',
            u'ipConfiguration': {
                u'authorizedNetworks': [{
                    u'kind': u'sql#aclEntry',
                    u'name': u'127.7.7.7',
                    u'value': u'127.0.214.3/32'
                }],
                u'ipv4Enabled':
                    True
            },
            u'kind': u'sql#settings',
            u'maintenanceWindow': {
                u'day': 0,
                u'hour': 0,
                u'kind': u'sql#maintenanceWindow'
            },
            u'pricingPlan': u'PER_USE',
            u'replicationType': u'SYNCHRONOUS',
            u'settingsVersion': u'57',
            u'storageAutoResize': True,
            u'storageAutoResizeLimit': u'0',
            u'tier': u'db-n1-standard-1'
        },
        u'state':
            u'RUNNABLE'
    }]
}]

EXPECTED_LOADED_AUTHORIZEDNETWORKS = [
  {'expiration_time': '1972-01-01 00:00:00',
   'instance_name': u'test-forseti',
   'kind': u'sql#aclEntry',
   'name': u'test',
   'project_number': 11111,
   'value': u'0.0.0.0/0'},
  {'expiration_time': '1972-01-01 00:00:00',
   'instance_name': u'forsetitest-2',
   'kind': u'sql#aclEntry',
   'name': u'127.7.7.7',
   'project_number': 11111,
   'value': u'127.0.214.3/32'}
]
EXPECTED_LOADED_IPADDRESSES = [
  {'instance_name': u'cloudsql-instance',
   'ip_address': u'1.2.3.4',
   'project_number': 11111,
   'time_to_retire': '1972-01-01 00:00:00',
   'type': u'PRIMARY'},
  {'instance_name': u'test-forseti',
   'ip_address': u'4.3.2.1',
   'project_number': 11111,
   'time_to_retire': '1972-01-01 00:00:00',
   'type': u'PRIMARY'},
  {'instance_name': u'forsetitest-2',
   'ip_address': u'192.168.1.2',
   'project_number': 11111,
   'time_to_retire': '1972-01-01 00:00:00',
   'type': u'PRIMARY'}
]

EXPECTED_LOADED_INSTANCES = [
  {'backend_type': u'SECOND_GEN',
   'connection_name': u'project-1:us-east1:cloudsql-instance',
   'current_disk_size': 0,
   'database_version': u'MYSQL_5_7',
   'failover_replica_available': None,
   'failover_replica_name': None,
   'instance_type': u'CLOUD_SQL_INSTANCE',
   'ipv6_address': None,
   'kind': u'sql#instance',
   'master_instance_name': None,
   'max_disk_size': 0,
   'name': u'cloudsql-instance',
   'on_premises_configuration_host_port': None,
   'on_premises_configuration_kind': None,
   'project': u'project-1',
   'project_number': 11111,
   'region': u'us-east1',
   'replica_configuration': 'null',
   'replica_names': 'null',
   'self_link': u'https://www.googleapis.com/sql/v1beta4/projects/\
project-1/instances/cloudsql-instance'
,
   'server_ca_cert': '{}',
   'service_account_email_address': u'serviceaccount1@iam.gserviceaccount.com',
   'settings_activation_policy': u'ALWAYS',
   'settings_authorized_gae_applications': '[]',
   'settings_availability_type': None,
   'settings_backup_configuration_binary_log_enabled': True,
   'settings_backup_configuration_enabled': True,
   'settings_backup_configuration_kind': u'sql#backupConfiguration',
   'settings_backup_configuration_start_time': u'03:00',
   'settings_crash_safe_replication_enabled': None,
   'settings_data_disk_size_gb': 10,
   'settings_data_disk_type': u'PD_SSD',
   'settings_database_flags': 'null',
   'settings_database_replication_enabled': {},
   'settings_ip_configuration_ipv4_enabled': True,
   'settings_ip_configuration_require_ssl': True,
   'settings_kind': u'sql#settings',
   'settings_labels': 'null',
   'settings_location_preference_follow_gae_application': None,
   'settings_location_preference_kind': None,
   'settings_location_preference_zone': None,
   'settings_maintenance_window': 'null',
   'settings_pricing_plan': u'PER_USE',
   'settings_replication_type': u'SYNCHRONOUS',
   'settings_settings_version': 28,
   'settings_storage_auto_resize': False,
   'settings_storage_auto_resize_limit': 0,
   'settings_tier': u'db-n1-standard-1',
   'state': u'RUNNABLE',
   'suspension_reason': 'null',
   'raw_cloudsql_instance': '{"backendType": "SECOND_GEN", "serviceAccountEmailAddress": "serviceaccount1@iam.gserviceaccount.com", "ipAddresses": [{"type": "PRIMARY", "ipAddress": "1.2.3.4"}], "connectionName": "project-1:us-east1:cloudsql-instance", "databaseVersion": "MYSQL_5_7", "instanceType": "CLOUD_SQL_INSTANCE", "kind": "sql#instance", "name": "cloudsql-instance", "serverCaCert": {}, "region": "us-east1", "settings": {"storageAutoResizeLimit": "0", "activationPolicy": "ALWAYS", "ipConfiguration": {"requireSsl": true, "ipv4Enabled": true, "authorizedNetworks": []}, "pricingPlan": "PER_USE", "replicationType": "SYNCHRONOUS", "tier": "db-n1-standard-1", "settingsVersion": "28", "storageAutoResize": false, "dataDiskSizeGb": "10", "kind": "sql#settings", "dataDiskType": "PD_SSD", "authorizedGaeApplications": [], "backupConfiguration": {"kind": "sql#backupConfiguration", "enabled": true, "startTime": "03:00", "binaryLogEnabled": true}}, "project": "project-1", "state": "RUNNABLE", "etag": "\\"CAE=\\"", "selfLink": "https://www.googleapis.com/sql/v1beta4/projects/project-1/instances/cloudsql-instance"}'},
   {'backend_type': u'SECOND_GEN',
   'connection_name': u'project-1:europe-west1:test-forseti',
   'current_disk_size': 0,
   'database_version': u'MYSQL_5_7',
   'failover_replica_available': None,
   'failover_replica_name': None,
   'instance_type': u'CLOUD_SQL_INSTANCE',
   'ipv6_address': None,
   'kind': u'sql#instance',
   'master_instance_name': None,
   'max_disk_size': 0,
   'name': u'test-forseti',
   'on_premises_configuration_host_port': None,
   'on_premises_configuration_kind': None,
   'project': u'project-1',
   'project_number': 11111,
   'region': u'europe-west1',
   'replica_configuration': 'null',
   'replica_names': 'null',
   'self_link': u'https://www.googleapis.com/sql/v1beta4/projects/project-1/\
instances/test-forseti'
,
   'server_ca_cert': '{}',
   'service_account_email_address': u'serviceaccount2@iam.gserviceaccount.com',
   'settings_activation_policy': u'ALWAYS',
   'settings_authorized_gae_applications': '[]',
   'settings_availability_type': None,
   'settings_backup_configuration_binary_log_enabled': False,
   'settings_backup_configuration_enabled': False,
   'settings_backup_configuration_kind': u'sql#backupConfiguration',
   'settings_backup_configuration_start_time': u'03:00',
   'settings_crash_safe_replication_enabled': None,
   'settings_data_disk_size_gb': 250,
   'settings_data_disk_type': u'PD_SSD',
   'settings_database_flags': 'null',
   'settings_database_replication_enabled': {},
   'settings_ip_configuration_ipv4_enabled': True,
   'settings_ip_configuration_require_ssl': {},
   'settings_kind': u'sql#settings',
   'settings_labels': 'null',
   'settings_location_preference_follow_gae_application': None,
   'settings_location_preference_kind': None,
   'settings_location_preference_zone': None,
   'settings_maintenance_window': '{"kind": "sql#maintenanceWindow", \
"day": 0, "hour": 0}'
,
   'settings_pricing_plan': u'PER_USE',
   'settings_replication_type': u'SYNCHRONOUS',
   'settings_settings_version': 6,
   'settings_storage_auto_resize': True,
   'settings_storage_auto_resize_limit': 0,
   'settings_tier': u'db-n1-standard-1',
   'state': u'RUNNABLE',
   'suspension_reason': 'null',
   'raw_cloudsql_instance': '{"backendType": "SECOND_GEN", "serviceAccountEmailAddress": "serviceaccount2@iam.gserviceaccount.com", "ipAddresses": [{"type": "PRIMARY", "ipAddress": "4.3.2.1"}], "connectionName": "project-1:europe-west1:test-forseti", "databaseVersion": "MYSQL_5_7", "instanceType": "CLOUD_SQL_INSTANCE", "kind": "sql#instance", "name": "test-forseti", "serverCaCert": {}, "region": "europe-west1", "settings": {"storageAutoResizeLimit": "0", "activationPolicy": "ALWAYS", "ipConfiguration": {"ipv4Enabled": true, "authorizedNetworks": [{"kind": "sql#aclEntry", "name": "test", "value": "0.0.0.0/0"}]}, "pricingPlan": "PER_USE", "replicationType": "SYNCHRONOUS", "tier": "db-n1-standard-1", "settingsVersion": "6", "storageAutoResize": true, "dataDiskSizeGb": "250", "kind": "sql#settings", "dataDiskType": "PD_SSD", "authorizedGaeApplications": [], "backupConfiguration": {"kind": "sql#backupConfiguration", "enabled": false, "startTime": "03:00", "binaryLogEnabled": false}, "maintenanceWindow": {"kind": "sql#maintenanceWindow", "day": 0, "hour": 0}}, "project": "project-1", "state": "RUNNABLE", "etag": "\\"CAE=\\"", "selfLink": "https://www.googleapis.com/sql/v1beta4/projects/project-1/instances/test-forseti"}'},
   {'backend_type': u'SECOND_GEN',
   'connection_name': u'project-1:us-central1:forsetitest-2',
   'current_disk_size': 0,
   'database_version': u'MYSQL_5_7',
   'failover_replica_available': None,
   'failover_replica_name': None,
   'instance_type': u'CLOUD_SQL_INSTANCE',
   'ipv6_address': None,
   'kind': u'sql#instance',
   'master_instance_name': None,
   'max_disk_size': 0,
   'name': u'forsetitest-2',
   'on_premises_configuration_host_port': None,
   'on_premises_configuration_kind': None,
   'project': u'project-1',
   'project_number': 11111,
   'region': u'us-central1',
   'replica_configuration': 'null',
   'replica_names': 'null',
   'self_link': u'https://www.googleapis.com/sql/v1beta4/projects/project-1/\
instances/forsetitest-2'
,
   'server_ca_cert': '{}',
   'service_account_email_address': u'serviceaccount3@iam.gserviceaccount.com',
   'settings_activation_policy': u'ALWAYS',
   'settings_authorized_gae_applications': '[]',
   'settings_availability_type': None,
   'settings_backup_configuration_binary_log_enabled': True,
   'settings_backup_configuration_enabled': True,
   'settings_backup_configuration_kind': u'sql#backupConfiguration',
   'settings_backup_configuration_start_time': u'11:00',
   'settings_crash_safe_replication_enabled': None,
   'settings_data_disk_size_gb': 25,
   'settings_data_disk_type': u'PD_HDD',
   'settings_database_flags': 'null',
   'settings_database_replication_enabled': {},
   'settings_ip_configuration_ipv4_enabled': True,
   'settings_ip_configuration_require_ssl': {},
   'settings_kind': u'sql#settings',
   'settings_labels': 'null',
   'settings_location_preference_follow_gae_application': None,
   'settings_location_preference_kind': None,
   'settings_location_preference_zone': None,
   'settings_maintenance_window': '{"kind": "sql#maintenanceWindow", "day": 0, \
"hour": 0}'
,
   'settings_pricing_plan': u'PER_USE',
   'settings_replication_type': u'SYNCHRONOUS',
   'settings_settings_version': 57,
   'settings_storage_auto_resize': True,
   'settings_storage_auto_resize_limit': 0,
   'settings_tier': u'db-n1-standard-1',
   'state': u'RUNNABLE',
   'suspension_reason': 'null',
   'raw_cloudsql_instance': '{"backendType": "SECOND_GEN", "serviceAccountEmailAddress": "serviceaccount3@iam.gserviceaccount.com", "ipAddresses": [{"type": "PRIMARY", "ipAddress": "192.168.1.2"}], "connectionName": "project-1:us-central1:forsetitest-2", "databaseVersion": "MYSQL_5_7", "instanceType": "CLOUD_SQL_INSTANCE", "kind": "sql#instance", "name": "forsetitest-2", "serverCaCert": {}, "region": "us-central1", "settings": {"storageAutoResizeLimit": "0", "activationPolicy": "ALWAYS", "ipConfiguration": {"ipv4Enabled": true, "authorizedNetworks": [{"kind": "sql#aclEntry", "name": "127.7.7.7", "value": "127.0.214.3/32"}]}, "pricingPlan": "PER_USE", "replicationType": "SYNCHRONOUS", "tier": "db-n1-standard-1", "settingsVersion": "57", "storageAutoResize": true, "dataDiskSizeGb": "25", "kind": "sql#settings", "dataDiskType": "PD_HDD", "authorizedGaeApplications": [], "backupConfiguration": {"kind": "sql#backupConfiguration", "enabled": true, "startTime": "11:00", "binaryLogEnabled": true}, "maintenanceWindow": {"kind": "sql#maintenanceWindow", "day": 0, "hour": 0}}, "project": "project-1", "state": "RUNNABLE", "etag": "\\"CAE=\\"", "selfLink": "https://www.googleapis.com/sql/v1beta4/projects/project-1/instances/forsetitest-2"}'}
]
