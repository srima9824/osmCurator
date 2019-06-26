# osm_curator

Role name: install_curator
=========

This role is created for :
1) installing and configuring elasticsearch curator on redhat and debian families
2) taking snapshot of the indices , uploading it to s3 repository 
3) deleting indices

Variables: 
----------
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
        elasticsearch_curator_cron_command: "/usr/local/bin/curator  --config /etc/elasticsearch-curator/curator.yml /etc/elasticsearch-curator/snapshot.yml && /usr/local/bin/curator --config /etc/elasticsearch-curator/curator.yml /etc/elasticsearch-curator/deleteindex.yml"


        elasticsearch_curator_cron_job:
                description: "Curate Elasticsearch Indices once every hour"
                minute: 0
                hour: 1
                weekday: '*'
                month: '*'
                year: '*'

The values of all the variables can be changed from here:
To change the cron command: Edit elasticsearch_curator_cron_command variable.
To change the the unit count for creating snapshot of indices: Change snapshot_unit_count variable.
To change the unit count for deleting indices: Edit delete1_unit_count variable for action 1 and delete2_unit_count for action 2 in deleteindex.yml.
To change the directory for storing curator files: Update the variable elasticsearch_curator_conf_dir
To specify path of repository: Update s3_repository_path:
To give name of the snapshot: Update name_of_repository:
All the other variables are self explanatory.


Playbook install_curator.yml
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

 ---
 - hosts: all
   become: yes
   roles:
    - /etc/ansible/roles/install_curator




