import testinfra

def test_os_release(host):
    assert host.file("/etc/redhat-release").contains("CentOS")

def test_sshd_inactive(host):
    assert host.service("sshd").is_running is False
