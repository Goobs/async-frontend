# encoding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.provider :virtualbox do |vb|
    vb.customize ['modifyvm', :id, '--memory', '2048', '--ioapic', 'on']
  end

  config.vm.box            = 'ubuntu/trusty64'
  config.ssh.forward_agent = true

  config.vm.network :private_network, ip: '10.11.12.15'
  config.vm.hostname = 'realty-front'
  config.vm.synced_folder '.', '/home/vagrant/realty-front'

  config.vm.provision :ansible do |ansible|
    ansible.playbook = 'provisioning/playbook.yml'
    ansible.inventory_path = 'vagrant_ansible_inventory'
    ansible.host_key_checking = false
    ansible.verbose = 'vv'
    ansible.limit = 'realty'
  end
end
