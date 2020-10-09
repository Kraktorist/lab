$install_docker = <<-'SCRIPT'
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum -y install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker
SCRIPT

$kubernetes_prerequisites = <<-'SCRIPT'
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
modprobe br_netfilter
sed -i --follow-symlinks 's/net.bridge.bridge-nf-call-ip6tables = 0/net.bridge.bridge-nf-call-iptables = 1/g' /usr/lib/sysctl.d/00-system.conf
sed -i --follow-symlinks 's/net.bridge.bridge-nf-call-iptables = 0/net.bridge.bridge-nf-call-iptables = 1/g' /usr/lib/sysctl.d/00-system.conf
sed -i --follow-symlinks 's/net.bridge.bridge-nf-call-arptables = 0/net.bridge.bridge-nf-call-arptables = 1/g' /usr/lib/sysctl.d/00-system.conf
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
swapoff -a
sed -i '/swap/d' /etc/fstab
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[Kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
yum install kubeadm docker -y
systemctl start docker.service
systemctl enable docker.service
systemctl enable kubelet
SCRIPT

$install_k8s = <<-'SCRIPT'
mkdir -p ~/.ssh
ssh-keyscan -H 192.168.1.51 >> /home/vagrant/.ssh/known_hosts
ssh-keyscan -H 192.168.1.52 >> /home/vagrant/.ssh/known_hosts
cp /home/vagrant/.ssh/id_rsa /root/.ssh/
cp /home/vagrant/.ssh/known_hosts /root/.ssh/known_hosts

kubeadm init --apiserver-advertise-address=192.168.1.53 --pod-network-cidr=10.244.0.0/16
export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
token=`kubeadm token create`
hash=`openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | \
   openssl dgst -sha256 -hex | sed 's/^.* //'`
ssh vagrant@192.168.1.51 sudo kubeadm join --token ${token} 192.168.1.53:6443 --discovery-token-ca-cert-hash sha256:${hash}
ssh vagrant@192.168.1.52 sudo kubeadm join --token ${token} 192.168.1.53:6443 --discovery-token-ca-cert-hash sha256:${hash}
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.define 'hmdck01' do |config|
    config.vm.box = "centos/7"
    config.vm.hostname = "hmdck01.local"
    config.vm.network "private_network", ip: "192.168.1.51"
    config.vm.provision "shell", inline: $kubernetes_prerequisites
    ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
    config.vm.provision :shell, :inline =>"
     echo 'Copying public SSH Keys to the VM'
     mkdir -p /home/vagrant/.ssh
     chmod 700 /home/vagrant/.ssh
     echo '#{ssh_pub_key}' >> /home/vagrant/.ssh/authorized_keys
     chmod -R 600 /home/vagrant/.ssh/authorized_keys
     echo 'Host 192.168.*.*' >> /home/vagrant/.ssh/config
     echo 'StrictHostKeyChecking no' >> /home/vagrant/.ssh/config
     echo 'UserKnownHostsFile /dev/null' >> /home/vagrant/.ssh/config
     chmod -R 600 /home/vagrant/.ssh/config
     ", privileged: false
  end
end

Vagrant.configure("2") do |config|
  config.vm.define 'hmdck02' do |config|
    config.vm.box = "centos/7"
    config.vm.hostname = "hmdck02.local"
    config.vm.network "private_network", ip: "192.168.1.52"
    config.vm.provision "shell", inline: $kubernetes_prerequisites
    ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
    config.vm.provision :shell, :inline =>"
     echo 'Copying public SSH Keys to the VM'
     mkdir -p /home/vagrant/.ssh
     chmod 700 /home/vagrant/.ssh
     echo '#{ssh_pub_key}' >> /home/vagrant/.ssh/authorized_keys
     chmod -R 600 /home/vagrant/.ssh/authorized_keys
     echo 'Host 192.168.*.*' >> /home/vagrant/.ssh/config
     echo 'StrictHostKeyChecking no' >> /home/vagrant/.ssh/config
     echo 'UserKnownHostsFile /dev/null' >> /home/vagrant/.ssh/config
     chmod -R 600 /home/vagrant/.ssh/config
     ", privileged: false
  end
end

Vagrant.configure("2") do |config|
  config.vm.define 'hmkbs01' do |config|
    config.vm.provider "virtualbox" do |vb|
      vb.cpus = "2"
      vb.memory = "2048"
    end
    config.vm.box = "centos/7"
    config.vm.hostname = "hmkbs01.local"
    config.vm.network "private_network", ip: "192.168.1.53"
    config.vm.provision "file", source: "~/.ssh/id_rsa", destination: "~/.ssh/id_rsa"
    config.vm.provision "shell", inline: $kubernetes_prerequisites
    config.vm.provision "shell", inline: $install_k8s
  end
end

