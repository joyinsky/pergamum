# -*- mode: ruby -*-
# vi: set ft=ruby :
API_VERSION = "2"

Vagrant.configure(API_VERSION) do |config|
  config.vm.box = "geerlingguy/ubuntu1604"

  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "public_network"

  config.ssh.forward_agent = true
  config.vm.synced_folder "./", "/var/www/djangoproject"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/vagrant.yml"
  end

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--name", "pergamum", "--memory", "512"]
  end
end