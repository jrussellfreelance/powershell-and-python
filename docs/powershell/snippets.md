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

## Export Password to Encrypted File
* [Guide](https://www.pdq.com/blog/secure-password-with-powershell-encrypting-credentials-part-1)

The following line will export the entered password as a secure encrypted file.
```powershell
Read-Host "Enter Password" -AsSecureString |  ConvertFrom-SecureString | Out-File "C:\Temp\Password.txt"
```