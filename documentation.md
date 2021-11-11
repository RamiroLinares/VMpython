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
12_We will create a non-root user in each server "sudo adduser <username>"
13_change password user with "sudo passwd -d <username>" and login with user "su - <username>"
14_We need to do the same from step 10-11, we use ssh-keygen
15_Now we arent a root user and we cant pass the id_rsa.pub with ssh-copy-id, we mount a python server in our host machine
, we open the host terminal, and mount a py server with "python -m http.server 3000" in the folder with ssh keys
(in windows C:\Users\username\.ssh, and open a terminal in this folder)
16_in each server with this non-root user we generate the ssh keys with "ssh-keygen"
17_Now, we have to connect to this py server, we ll make it with "curl http://iphost:3000" in vm
18_"wget http://iphost:3000/id_rsa.pub"
19_Now we get our public key, move it with
"cat id_rsa.pub >> .ssh/authorized_keys
20_In one of the machine (fedora server in this case), we 'll install docker with the following guide
https://developer.fedoraproject.org/tools/docker/docker-installation.html
21_ After that, we'll install jenkins from dockerhub
docker pull bitnami/jenkins
22_ Dont forget to give the docker permission to the non-root user, "sudo gpasswd -a <username> docker"


Extra Notes:
jenkins, written in java, multiplatform, accesible from the web, its a CI
that listen the repo, when this change jenkins make a build and if it have an error notify
the team or deploy the app

docker is an open source for automatize the app implementation, makes an image
have a cointainer like a vm but the difference is this "lift" independent machines with light os
can copy delete or more functions to this containers (and can run more apps with less hardware)
a container is an image instanced (have the code) and its running
docker build -t
docker run -d (use linux kernel)


