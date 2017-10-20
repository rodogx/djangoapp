# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "wks-django"
  config.vm.box_check_update = false
  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.network "forwarded_port", guest: 8000, host: 8080
  config.vm.network "forwarded_port", guest: 5432, host: 8432


  config.vm.synced_folder "./holamundo", "/home/vagrant/holamundo"  
  config.vm.synced_folder "./app", "/home/vagrant/app"  


  config.vm.provider "virtualbox" do |vb|
     vb.name = "wks-django"
     vb.memory = "512"
  end
  config.vm.provision :shell, path: "scripts/bootstrap.sh"
end
