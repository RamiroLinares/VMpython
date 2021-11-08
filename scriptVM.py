import virtualbox

vbox = virtualbox.VirtualBox()
print("List of available machines: ")
i=0
for m in vbox.machines:
    print(str(i)+"."+str(m))
    i=i+1

opt = input("Select an option \n 1.Create VM \n 2.Delete VM \n 3.Launch VM \n")    

if(opt=="1"):
    #name= input("Write the new VM name \n")
    #vbox.create_machine(vbox.machines[0].settings_file_path,name,groups,vbox.machines[0].os_type_id,vbox.machines[0].__uuid__)
    #vbox.create_machine(vbox.machines[0].settings_file_path,"test_vm",[],"Linux","")
    idClone=input("enter the id of the VM you want to clone \n")
    vbox.machines[int(idClone)].clone(name="test")
elif(opt=="2"):
    idDel=input("enter the id of the VM you want to delete \n")
    vbox.machines[int(idDel)].remove()
elif(opt=="3"):
    session = virtualbox.Session()
    idLaunch=input("enter the id of the VM you want to launch \n")
    name=vbox.machines[int(idLaunch)]
    machine = vbox.find_machine(str(name))
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()
else:
    print("No Valid Option, restart script")