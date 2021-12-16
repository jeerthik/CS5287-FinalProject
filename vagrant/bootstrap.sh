#!/bin/bash

# install apache2
apt-get update
apt-get install -y apache2

# install ansible
#apt-get install -y software-properties-common
#apt-add-repository ppa:ansible/ansible
#apt-get update
#apt-get install -y ansible

# install pip and kafka-python
apt-get update
apt-get install -y python3-pip
pip install kafka-python

# install openstack-sdk
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade openstacksdk

# install openstack.cloud collection
ansible-galaxy collection install openstack.cloud