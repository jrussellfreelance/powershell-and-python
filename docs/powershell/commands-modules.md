# Commands And Modules
## Commands
You can get a list of all available commands by typing:
```powershell
Get-Command
```
You can get a list of all available commands for a certain module by typing:
```powershell
Get-Command -Module <module_name>
# Example:
Get-Command -Module ActiveDirectory
```
## Modules
You can get a list of the available modules by typing:
```powershell
Get-Module -ListAvailable
```