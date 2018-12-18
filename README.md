# Role Name

[![Build Status](https://travis-ci.org/OldCrowEW/ansible-openstack-etcd.svg?branch=master)](https://travis-ci.org/OldCrowEW/ansible-openstack-etcd)

Ansible role to install and configure etcd for OpenStack. This follows the install guide for better or worse :D

## Requirements

None

## Role Variables

None

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: oldcrowew.ansible_openstack_common }
         - { role: ansible-openstack-etcd }

## License

BSD

## Author Information

John Favorite