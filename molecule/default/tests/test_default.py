import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_node_exporter(host):
    assert host.file("/usr/local/bin/aws").exists
    cmd = host.run("/usr/local/bin/aws --version")
    assert cmd.succeeded
