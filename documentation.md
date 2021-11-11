1_ create virtual machine
2_ assign memory size (recommended 512mb)
3_create a hard disk (10gb)
4_ after that, go to settings, storage, in controller:ide mount the iso of the system we want to install
5_launch the VM
6_install and follow the wizard (dont forget the option to install openssh)

7_ one done, reboot and unmount the iso
8_ launch VM again
9_on terminal use ip a, see the ip
10_use ssh-keygen, all enter (in all machines)
11_ ssh-copy-id user@hostIP for all the remote machine we want to have access
 (in all machines)
now we can access passwordless and remote to the other machines

jenkins, written in java, multiplatform, accesible from the web, its a CI
that listen the repo, when this change jenkins make a build and if it have an error notify
the team or deploy the app

docker is an open source for automatize the app implementation, makes an image
have a cointainer like a vm but the difference is this "lift" independt machines with light os
can copy delete or more functions to this containers (and can run more apps with less hardware)
a container is an image instanced (have the code) and its running
docker build -t
docker run -d (use linux kernel)


