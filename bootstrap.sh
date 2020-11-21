#!/bin/bash
sudo yum -y update;
sudo yum -y install epel-release && sudo yum -y update;
sudo yum -y install mtr nmap traceroute iperf3;
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install -r /vagrant/requirements.txt
sudo ip route del default dev enp0s3
sudo timedatectl set-timezone America/Denver
netstat -nr
