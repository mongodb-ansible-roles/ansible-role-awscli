Ansible AWS Command Line Interface
==================================

Installs the AWS Command Line Interface (CLI)

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-awscli/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-awscli/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-awscli/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-awscli/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `awscli_url` | The URL of the awscli installer | string | `https://awscli.amazonaws.com/awscli-exe-linux-x86_64-{{ awscli_version }}.zip` | no |
| `awscli_version` | The version of the awscli to install | string | `""` | no |

Versions
--------

The versions of AWS CLI are available here: https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-awscli
      vars:
        awscli_version: 2.1.22
```

License
-------

Apache License
