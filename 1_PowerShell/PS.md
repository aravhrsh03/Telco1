# PowerShell Notes

## 📌 Keywords Covered
- PowerShell
- Windows Administration
- Command-Line Interface (CLI)
- Cmdlets
- File Management
- Folder Management
- Working Directory
- File Content Operations
- Get-Location
- Get-ChildItem
- New-Item
- Get-Content
- Set-Content
- Add-Content
- Multi-line Content
- System32
- Administrator Privileges

---

## 🏷️ Tags & Keywords Used in Notes
- OFF (Official)
- IMP (Important)
- `---` (Command Definition)

---

# PowerShell

## Definition

- **PowerShell** is a command-line shell and scripting language developed by Microsoft.
- Primarily used for **administrative purposes**.
- Works specifically on **Windows** operating systems.
- Mainly used to interact closely with the operating system, including managing:
  - Files
  - Folders
  - Processes
  - System configurations
  - Administrative tasks

---

# Abbreviations

| Symbol | Meaning |
|---------|---------|
| **OFF** | Official Command |
| **IMP** | Important |
| **---** | Command Definition |

---

# PowerShell Commands

## Get Current Working Directory

### Commands

```powershell
pwd
Get-Location
```

**Official Command:** `Get-Location`

**Definition**

- Displays the current working directory (current location).

---

## List Files and Folders

### Commands

```powershell
ls
Get-ChildItem
```

**Official Command:** `Get-ChildItem`

**Definition**

- Lists all files and subfolders in the current directory.

---

## Create File or Folder

### Commands

```powershell
ni
New-Item
```

**Official Command:** `New-Item`

### Syntax

```powershell
ni -ItemType <type> -Path <file-name>
```

### Parameters

| Parameter | Description |
|-----------|-------------|
| `<type>` | `File` or `Directory` (Folder) |
| `-Path` | Name or path of the file/folder to create |

**Definition**

- Creates a new file or folder.

---

## Write Content to a File

### Syntax

```powershell
<content> > <file-name>
```

### Example

```powershell
"Hello Data" > file.txt
```

**Definition**

- Writes content into a file.
- If the file already contains data, it is overwritten.

---

## Read File Content

### Command

```powershell
Get-Content <file-name>
```

**Definition**

- Displays the contents of the specified file.

---

## Override File Content

### Command

```powershell
Set-Content -Path <path/to/file-name> <content>
```

**Definition**

- Replaces the existing content of the file with the new content.

---

## Append Content to a File

### Command

```powershell
Add-Content -Path <path/to/file-name> <content>
```

**Definition**

- Appends the specified content to the end of the file without removing existing data.

---

## Insert Multi-line Content

### Syntax

```powershell
@"
<multi-line-content>
<multi-line-content>
"@ | Set-Content <file-name>
```

> **Correction**
>
> A pipeline (`|`) is required before `Set-Content` when using a here-string.

**Definition**

- Inserts multiple lines of text into a file using a PowerShell **here-string**.

---

# Important Notes

> **IMP**
>
> Folder creation inside protected system directories such as **`C:\Windows\System32`** requires **Administrator privileges**.
>
> This restriction applies because `System32` is a protected system folder in Windows.

---

# Summary

| Command | Official Command | Purpose |
|----------|------------------|---------|
| `pwd` | `Get-Location` | Display current working directory |
| `ls` | `Get-ChildItem` | List files and folders |
| `ni` | `New-Item` | Create a file or folder |
| `>` | — | Write content to a file |
| `Get-Content` | `Get-Content` | Read file content |
| `Set-Content` | `Set-Content` | Replace file content |
| `Add-Content` | `Add-Content` | Append content to a file |
| `@"..."@ \| Set-Content` | `Set-Content` | Write multi-line content to a file |