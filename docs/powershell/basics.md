# Basics
### Parameter Syntax
```powershell
param (
    [Parameter(Mandatory=$true)]
    [string]
    $ParameterName = "test-server"
)
```
### Where Syntax
```powershell
$workspace = (Get-AzOperationalInsightsWorkspace).Where( { $_.Name -eq $workspaceName })
$workspace = Get-AzOperationalInsightsWorkspace | Where { $_.Name -eq $workspaceName }
```
### For Each Loops Syntax
```powershell
$WindowsVMs = Get-AzVM | where-object { $_.StorageProfile.OSDisk.OSType -eq "Windows" } | Sort-Object Name | ForEach-Object {$_.Name} | Out-String -Stream | Select-Object
$WindowsVMs = Get-AzVM | where-object { $_.StorageProfile.OSDisk.OSType -eq "Windows" } | Sort-Object Name | ForEach-Object {$_.Name} | Select-Object -ExpandProperty Name
```
```powershell
$WindowsVMs = Get-AzVM | where-object { $_.StorageProfile.OSDisk.OSType -eq "Windows" } | Sort-Object Name
$names = @()
foreach($WindowsVM in $WindowsVMs) {
    $vmname = $WindowsVM.Name
    $names += $vmname
}
```