# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |django_config|
  django_config.vm.box = "xenial64"

  # The URL from where the 'django_config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  django_config.vm.box_url = "https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-vagrant.box"

  # Configure virtual machine specs. Keep it simple, single user.
  django_config.vm.provider :virtualbox do |p|
    p.customize ["modifyvm", :id, "--memory", 2048]
    p.customize ["modifyvm", :id, "--cpus", 2]
    p.customize ["modifyvm", :id, "--cpuexecutioncap", 50]
    p.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  # Configure a synced folder between HOST and GUEST
  # django_config.vm.synced_folder ".", "/srv/webapp", id: "vagrant-root", :mount_options => ["dmode=777","fmode=777"]

  # Config hostname and IP address so entry can be added to HOSTS file
  django_config.vm.hostname = "pergamum"
  django_config.vm.network "private_network", ip: "10.0.13.17"

  # Forward a port from the guest to the host, which allows for outside
  # computers to access the VM, whereas host only networking does not.
  django_config.vm.network "forwarded_port", guest: 80, host: 8888
  django_config.vm.network "forwarded_port", guest: 8000, host: 8000
  django_config.vm.network "forwarded_port", guest: 8080, host: 8080

  # kickoff a shell script to install Python essentials
  django_config.vm.provision :shell, path: "vagrant_bootstrap.sh"
end
