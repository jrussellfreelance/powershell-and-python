# Basics
### Parameter Syntax
```powershell
param (
    [Parameter(Mandatory=$true)]
    [ValidateNotNullOrEmpty()]
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

### Objects
- [Read me!](https://www.itprotoday.com/powershell/powershell-basics-introduction-objects)

List properties and methods for the results of a command:
```powershell
Get-Process | Get-Member
```
#### 4 ways to create a Powershell object
1. Convert hashtable to `[PSCustomObject]`
```powershell
[pscustomobject]@{
firstname = 'Jesse'
lastname = 'Russell'
}
```
2. Using `Select-Object` cmdlet
```powershell
Select-Object @{n='firstname';e={'Jesse'}},@{n='lastname';e={'Russell'}} -InputObject ''
```
3. Using `New-Object` and `Add-Member`
```powershell
$obj = New-Object -TypeName psobject
$obj | Add-Member -MemberType NoteProperty -Name firstname -Value 'Jesse'
$obj | Add-Member -MemberType NoteProperty -Name lastname -Value 'Russell'
$obj | Add-Member -MemberType ScriptMethod -Name "GetName" -Value {$this.firstname +' '+$this.lastname}
```
4. Using `New-Object` and hashtables
```powershell
# Using New-Object and hashtables
$properties = @{
firstname = 'Jesse'
lastname = 'Russell'
}
$o = New-Object psobject -Property $properties; $o
```
#### Filtering Objects
```powershell
Get-Service | Where-Object {$_.Status -eq "Running" `
  -and $_.ServiceType -eq "Win32OwnProcess"} |
  Format-Table -Autosize
```
#### Creating .NET class object
```powershell
$ping = New-Object -TypeName Net.NetworkInformation.Ping
```
## Jobs
### start job
```powershell
Start-Job -ScriptBlock { hostname }
```