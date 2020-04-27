# Snippets
## Install Azure Powershell Module
Installs the latest Azure Powershell module.
```powershell
Install-Module -Name Az -AllowClobber
```
## Silent Chrome Install
The script downloads the latest installer to your temp directory, then deletes it after silent installation.

I found this somewhere on the web a while ago. Just re-sharing!

```powershell
### Silently installs latest google chrome ###
$Path = $env:TEMP;
$Installer = "chrome_installer.exe"
Invoke-WebRequest "http://dl.google.com/chrome/install/latest/chrome_installer.exe" -OutFile $Path\$Installer
Start-Process -FilePath $Path\$Installer -Args "/silent /install" -Verb RunAs -Wait
Remove-Item $Path\$Installer
```