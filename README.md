Role Name
=========

Role for installing and configuring elasticsearch-curator for taking snaphots and deleting indices

Requirements
------------

Ansible version: 2.6

Role Variables
--------------
defaults: main.yml

---
        elasticsearch_curator_version: 5.7.6

        elasticsearch_curator_conf_dir: /etc/elasticsearch-curator

        elasticsearch_curator_client_hosts: "{{ ansible_default_ipv4.address }}"
        # OR a list of hosts
        elasticsearch_curator_client_port: 9200
        elasticsearch_curator_client_url_prefix:
        elasticsearch_curator_client_use_ssl: False
        elasticsearch_curator_client_certificate:
        elasticsearch_curator_client_client_cert:
        elasticsearch_curator_client_client_key:
        elasticsearch_curator_client_aws_key:
        elasticsearch_curator_client_aws_secret_key:
        elasticsearch_curator_client_aws_region:
        elasticsearch_curator_client_ssl_no_validate: False
        elasticsearch_curator_client_http_auth:
        elasticsearch_curator_client_timeout: 60
        elasticsearch_curator_client_master_only: False

        elasticsearch_curator_logging_loglevel: INFO
        elasticsearch_curator_logging_logfile: /var/log/curator/curator.log
        elasticsearch_curator_logging_logformat: default
        elasticsearch_curator_logging_blacklist: ['elasticsearch', 'urllib3']
        name_of_repository:
        s3_repository_path: s3_repository
        snapshot_filter_type: age
        snapshot_source_name: name
        snapshot_direction: older
        snapshot_unit: days
        snapshot_unit_count: 7

        delete1_unit_count: 1
        delete2_unit_count: 1
        elasticsearch_curator_cron_job: {}
        elasticsearch_curator_cron_command: "/usr/local/bin/curator --config /etc/elasticsearch-curator/curator.yml /etc/elasticsearch-curator/snapshot.yml && /usr/local/bin/curator --config /etc/elasticsearch-curator/curator.yml /etc/elasticsearch-curator/deleteindex.yml"


        elasticsearch_curator_cron_job:
                description: "Curate Elasticsearch Indices once every hour"
                minute: 0
                hour: 1
                weekday: '*'
                month: '*'
                year: '*'
        


The values of all the variables can be changed from here:
-> To change the cron command: Edit  elasticsearch_curator_cron_command variable.
-> To change the the unit count for  creating snapshot of indices change    snapshot_unit_count variable.
-> To change the unit count for deleting indices edit delete1_unit_count: variable for action 1 and delete2_unit_count:  for action 2 in deleteindex.yml.
-> To change the directory for storing curator files update the variable elasticsearch_curator_conf_dir
-> All the other variables are self explanatory.


