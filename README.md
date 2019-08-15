Ansible AWS Command Line Interface
==================================

Installs the AWS Command Line Interface (CLI)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| awscli\_version | The version of the awscli to install | string | `""` | no |

Dependencies
------------

- [`geerlingguy.pip`](https://galaxy.ansible.com/geerlingguy/pip)

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - { role: ansible-role-awscli, vars: { awscli_version: "1.16.218" } }
```

License
-------

Apache License
