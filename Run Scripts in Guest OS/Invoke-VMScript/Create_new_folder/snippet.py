function handler($context, $inputs) {
    #Define variable
    $vc = $inputs.vcenter_base_url
    $vcUsername = $inputs.vcenter_username
    $vcPassword = $context.getSecret($inputs."vcenter_password")
    $vmUsername = $inputs.vm_username
    $vmPassword = $context.getSecret($inputs."vm_password")
    $vmName = $inputs.resourceNames[0]
    #Pass the certificate
    Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -ParticipateInCeip:$false -Scope Session -Confirm:$false
    #Connect to vCenter
    Connect-VIServer -Server $vc -Protocol https -User $vcUsername -Password $vcPassword
    Write-Host "Connecting to vCenter server..."
    #Select a vm
    Write-Host "Determining virtual machine..."
    $vm = Get-VM -Name $vmName
    #Create a script
    Write-Host "Attempting to run commands to $vm..."
    $remoteScript = "New-Item -Path ‘C:\Users\MuhammedTurde\TestFolder' -ItemType Directory"
    #Run a script
    $runRemoteScript = Invoke-VMScript -VM $vm -ScriptText $remoteScript -GuestUser $vmUsername -GuestPassword $vmPassword -ScriptType Powershell -Confirm:$false
    if ($runRemoteScript.ScriptOutput.Length -eq 0) {
        Write-Host "Successfully create a new folder."
    }else {
        Write-Host "Attempt to create a folder to $vm failed with warnings:" $runRemoteScript.ScriptOutput
    }
}