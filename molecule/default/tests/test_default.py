import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_configuration_directory_created(host):
    '''Check if curator configuration file created'''
    host.file('/etc/elasticsearch-curator').is_directory

def test_configuration_file_created(host):
    '''Check if curator configuration file created'''
    host.file('/etc/elasticsearch-curator/curator.yml').exists

def test_delete_index_file_created(host):
    '''Check if curator configuration file created'''
    host.file('/etc/elasticsearch-curator/deleteindex.yml').exists

def test_snapshot_file_created(host):
    '''Check if curator configuration file created'''
    host.file('/etc/elasticsearch-curator/snapshot.yml').exists




