# First Steps
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

# Second Steps
 
 After this steps we'll use VAGRANT to help the management of our VM's
 
 We have our docker and jenkins running in a VM called "agent-1", we will create a dev VM who will run all our services
 called "dev-1" (look to VAGRANTFILE.CI). This VM will run in his docker a software of Movies contained in containers. For this
 we'll download the main server (the server) image build it in our pipeline (see jenkinsFile in https://github.com/RamiroLinares/Dose/tree/enable_ci) and
 a Content Server(Client or movies libraries). After pulling this images to our "dev-1" we'll pull postgres too (all this can be seen in VAGRANTFILE.CI)
 
 The next steps are for adding the tables and the databases needed for running this library of movies:
 
 1_Copy the sql needed(db_schema.sql in contentServer and in mainServer) to a folder and mount py server 
"python -m http.server 3000"
 
get om vm
 
wget http://iphost:3000/db_schema.sql
 
wget http://iphost:3000/db_schema2.sql
 
 You need the next special dir for postgres:
 
 2_In dev-1, sudo mkdir /docker-entrypoint-initdb.d
 
 3_In dev-1, you can look your pulled images with "docker images"
 
 4_ Docker run ll make your images as container and running services
 
 docker run -d -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust postgres:latest
 
 5_docker run -d -p 3000:3000 jalafoundation/dose-main-server:latest
 
 6_This will not run because you dont have the db
 
docker run -d -p 3001:3001 jalafoundation/dose-content-server
 
 7_you can see the cointainer names and ids with:
 
"docker ps"
 
 8_next you need to go to the psql (postgres sql)
 
 "docker exec -it idPostgresCointainer bash"
 
 "su postgres"
 
 "psql"
 
 9_Create the dbs needed (in Dose documentation says you need dose and MovieServer)
 
CREATE DATABASE dose;
 
CREATE DATABASE MovieServer;
 
 10_
Go back to dev-1 again and go to the postgres special dir
 
 "cd /docker-entrypoint-initdb.d"
 
 11_execute both sql (db_schema.sql and db_schema2.sql or any name)
 
 "docker cp ./localfile.sql containername:/container/path/file.sql"
 
 "docker exec -u postgresuser containername psql dbname postgresuser -f /container/path/file.sql"
 
 For our case:
 
docker cp ./db_schema.sql stoic_franklin:/docker-entrypoint-initdb.d/db_schema.sql
 
docker exec -u postgres stoic_franklin psql movieServer postgres -f docker-entrypoint-initdb.d/db_schema.sql
 
docker cp ./db_schema2.sql stoic_franklin:/docker-entrypoint-initdb.d/db_schema2.sql
 
docker exec -u postgres stoic_franklin psql movieServer postgres -f docker-entrypoint-initdb.d/db_schema2.sql

 This 'll create the tables needed for our Dose project (but empty)
 
 12_go back to psql and insert a user_server (Dose documentation) (step 8)
 
use your ip of your vm but the next its for example
 
INSERT INTO server (server_id,server_ip,server_name) VALUES (1,'10.0.10.11', 'dose');
 
INSERT INTO users (username,password,salt,email,id) VALUES ('25ramy','linares123','salt','ramirolinares_09@hotmail.com',1);
 
INSERT INTO user_server (user_id,server_id) VALUES (1,1);
 
 13_Restart containers
 
docker restart containerName
 
 
Extra Notes:
jenkins, its written in java, multiplatform, accesible from the web, its a CI
that listen the repo, when this change jenkins make a build and if it have an error notify
the team or deploy the app

docker is an open source for automatize the app implementation, makes an image,
have a cointainer like a vm but the difference is this "lift" independent machines with light os
can copy delete or more functions to this containers (and can run more apps with less hardware)
a container is an image instanced (have the code) and its running
docker build -t
docker run -d (use linux kernel)


