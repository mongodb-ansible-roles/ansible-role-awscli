Ansible AWS Command Line Interface
==================================

Installs the AWS Command Line Interface (CLI)

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

- [`geerlingguy.pip`](https://galaxy.ansible.com/geerlingguy/pip)

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - { role: ansible-role-awscli }
```

License
-------

Apache License
