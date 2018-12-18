import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_etcd_is_installed(host):
    package = host.package('etcd')

    assert package.is_installed


def test_python_etcd_is_installed(host):
    package = host.package('etcd')

    assert package.is_installed


def test_sysconfig_etcd_file(host):
    f = host.file('/etc/etcd/etcd.conf')

    assert f.exists


def test_etcd_running_and_enabled(host):
    service = host.service('etcd')

    assert service.is_running
    assert service.is_enabled
