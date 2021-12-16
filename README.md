## Cloud Computing Course Final Project Documentation

*Team: Jeerthi Kannan, Dawson Lee, & Rooney Gao*

The following are the directories within our repository:
- `ansible_playbooks`: This directory contains Ansible .yaml and .yml playbooks to automate steps in our final project using Infrastructure as Code (IaC)
- `dockerfiles`: This directory contains necessary dockerfiles to build custom images for our containerized microservices and other processes
- `vagrant`: This directory contains the files necessary for Vagrant (i.e. Ansible config file, inventory file, Vagrantfile, and a bootstrapping script)
- `paper`: This directory contains the research paper we used as the basis for our final project idea, and our final report
- `scripts`: This directory contains python scripts for running our experiments to test insertion latency using a direct client connection to CouchDB from our local machine, and test read latency using a ZeroMQ server-client pattern
- `results`: This directory contains text files with results from our latency experiments with CouchDB and ZeroMQ

For the final project, we ran containerized CouchDB and ZeroMQ microservices in Kubernetes (K8s) pods. Our cluster was deployed on multiple virtual machines running on the Chameleon Cloud provider. The following is a general workflow for how to run the code:

1. Within the `vagrant` folder, we establish and provision our local Vagrant VM
2. Using a Vagrant `ansible_local` provisioner, we copy necessary configurations files (e.g. host alias files and dockerfiles) to our virtual machines hosted on Chameleon Cloud
3. Step 2 triggers the execution of the `playbook_master.yaml` file which runs its child Ansible playbooks (IaC) to create our K8s cluster and deploy our pods which hold containerized ZeroMQ and CouchDB microservices
4. The CouchDB microservice, once it reaches the running state, will enable a web-interface reachable using the floating ip address and port number of the machine in which its container is running
5. The ZeroMQ server microservice executes a python script in the `scripts` subdirectory called `pyzmq-server.py`, which continuously accepts incoming messages via a request-reply pattern
6. Finally, we execute `pyzmq-client-2.py` and `time_db_inserts.py` in the `scripts` folder to test read latency via ZeroMQ and write latency via direct client connection to CouchDB, respectively
7. Our python scripts print results and write results files, which are stored in the `results` folder
