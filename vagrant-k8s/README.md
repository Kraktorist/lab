# vagrant-k8s

install VirtualBox 
``` bash
sudo yum install kernel-devel kernel-devel-$(uname -r) kernel-headers kernel-headers-$(uname -r) make patch gcc
sudo wget https://download.virtualbox.org/virtualbox/rpm/el/virtualbox.repo -P /etc/yum.repos.d
sudo yum install VirtualBox-6.1
```
install vagrant
``` bash
sudo yum -y install https://releases.hashicorp.com/vagrant/2.2.10/vagrant_2.2.10_x86_64.rpm
```

generate a key which will be passed to nodes
``` bash
ssh-keygen
```

clone the repo and run vagrant
``` bash
mkdir lab
cd lab
git clone https://github.com/Kraktorist/lab.git
cd vagrant-k8s
vagrant up
```

to add metrics server download a mainfest edit it by adding ```--kubelet-insecure-tls``` and apply
``` bash
curl kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml>components.yaml
nano components.yaml
kubectl apply -f components.yaml
```
