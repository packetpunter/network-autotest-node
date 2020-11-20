Vagrant.configure("2") do |config|
	config.vm.box = "geerlingguy/centos8"
	
	config.vm.define "blueTest" do |blueTest|
		blueTest.vm.hostname = "blueTester"
		blueTest.vm.network "public_network"
		blueTest.vm.synced_folder "./sync", "/app", create: true
		blueTest.vm.provision :shell, path: "bootstrap.sh"	
	end
end

