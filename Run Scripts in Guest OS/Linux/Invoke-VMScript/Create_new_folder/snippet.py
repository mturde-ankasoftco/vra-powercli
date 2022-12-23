import paramiko
import time
def handler(context, inputs):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # set variables
    vm_ip_address = inputs["addresses"][0][0]
    vm_usr = inputs["vc_usr"]
    vm_pwd = context.getSecret(inputs["vc_pwd"])
    CreateFolder(vm_usr, vm_pwd, vm_ip_address)

def CreateFolder(vm_usr, vm_pwd, vm_ip_address):
    # Connect to target using username/password authentication.
    ssh.connect(hostname=vm_ip_address, 
                username=vm_usr, 
                password=vm_pwd, 
                look_for_keys=False)
    # Command to run on the target
    command = "mkdir test-folder-001"
    
    # Run command.
    _stdin, _stdout,_stderr = ssh.exec_command(command)
    output = _stdout.read().decode()
    print(output)
    ssh.close()
    return output