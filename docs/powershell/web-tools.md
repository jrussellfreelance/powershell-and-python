# Web Tools
## Downloading files from the web
In Powershell 2 and above, you can type the following commands:
```powershell
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile("https://www.website.com/file","C:\path\file")
```
In Powershell 3 and above, you can use the `Invoke-WebRequest` cmdlet:
```powershell
Invoke-WebRequest -Uri "http://www.website.com" -OutFile "C:\path\file"
```