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