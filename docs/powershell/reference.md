# Reference
## Commands And Modules
### Commands
You can get a list of all available commands by typing:
```powershell
Get-Command
```
You can get a list of all available commands for a certain module by typing:
```powershell
Get-Command -Module ActiveDirectory
```
### Modules
You can get a list of the available modules by typing:
```powershell
Get-Module -ListAvailable
```
## Strings
### Concatenation
There are several ways to concatenate strings:
```powershell
$wordone = "Hello"
$wordtwo = "person"
$wordthree = "$wordone $wordtwo"
$wordthree = $wordone + " " + $wordtwo
$wordthree = $wordone,$wordtwo -join " "
```
### Splitting
There are two ways to split strings: a method and an operator.  The method is better.
```powershell
$splitme = "Split|Me"
$result = $splitme.Split("|")
$result = $splitme.Split("|", 2)  # <-- specifies the maximum number of substrings created
```
### Substrings
```powershell
$subme = "split on three"
$result = $subme.Substring(0,4)  # --> "split"
$result = $subme.Remove(0,4)  # --> " on three"
```
### Searching and Replacing Characters
```powershell
$replaceme = "Replace Me"
$result = $replaceme.Replace("Me", "You")  # --> "Replace You"
$bool = $replaceme.Contains("Replace")  # --> $true
$index = $replaceme.IndexOf("R")  # --> 0
```
## Web Tools
### Downloading files from the web
In Powershell 2 and above, you can type the following commands:
```powershell
$WebClient = New-Object System.Net.WebClient
$WebClient.DownloadFile("https://www.website.com/file","C:\path\file")
```
In Powershell 3 and above, you can use the `Invoke-WebRequest` cmdlet:
```powershell
Invoke-WebRequest -Uri "http://www.website.com" -OutFile "C:\path\file"
```