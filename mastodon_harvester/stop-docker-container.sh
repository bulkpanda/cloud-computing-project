#!/bin/bash

ansible-galaxy collection install community.docker

ansible-playbook -i inventory -v  stop-docker-container.yaml
