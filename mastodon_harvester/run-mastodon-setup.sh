#!/bin/bash

ansible-galaxy collection install openstack.cloud
ansible-galaxy collection install community.docker

ansible-playbook -i inventory -v run-mastodon-setup.yaml

