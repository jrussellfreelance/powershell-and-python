# Strings
## Concatenation
There are several ways to concatenate strings:
```powershell
$wordone = "Hello"
$wordtwo = "person"
$wordthree = "$wordone $wordtwo"
$wordthree = $wordone + " " + $wordtwo
$wordthree = $wordone,$wordtwo -join " "
```
## Splitting
There are two ways to split strings: a method and an operator.  The method is better.
```powershell
$splitme = "Split|Me"
$result = $splitme.Split("|")
$result = $splitme.Split("|", 2)  # <-- specifies the maximum number of substrings created
```
## Substrings
```powershell
$subme = "split on three"
$result = $subme.Substring(0,4)  # --> "split"
$result = $subme.Remove(0,4)  # --> " on three"
```
## Searching and Replacing Characters
```powershell
$replaceme = "Replace Me"
$result = $replaceme.Replace("Me", "You")  # --> "Replace You"
$bool = $replaceme.Contains("Replace")  # --> $true
$index = $replaceme.IndexOf("R")  # --> 0
```