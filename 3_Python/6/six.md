# Python Notes

## 📌 Keywords Covered
- Files
- File Handling
- Text Files
- Binary Files
- `open()`
- File Modes
- `with` Statement
- `read()`
- `write()`
- `seek()`
- `readline()`
- `readlines()`
- `close()`
- CSV
- `csv` Module
- `writer()`
- `writerow()`
- `writerows()`
- `reader()`
- Excel
- `openpyxl`
- `Workbook`
- Worksheet
- PIL
- Pillow
- Image Processing
- `Image.open()`
- `show()`

---

## 🏷️ Python Abbreviations (Always Available)

| Abbreviation | Meaning |
|--------------|---------|
| **LIB** | Library |
| **USA** | Usage (Example Code) |
| **PAR** | Parameters |
| **SYN** | Syntax |
| **WHY** | Why this is used |
| **EXA** | Example |
| **MET** | Methods |
| **CAT** | Cannot Have It / Limitations |
| **ALI** | Alias |
| **RES** | Expected Result |
| **OPT** | Optional |
| **ANE** | Another Example |
| **FUN** | Functions Used |
| **DAM** | Data Members |
| **TYS** | Types |
| **VER** | Python Version |
| **USC** | Use Cases |

---

## 🏷️ Tags & Keywords Used in Notes

- LIB
- USA
- PAR
- MET
- DAM
- FUN
- NOTE

---

## Date

**12/07/2026**

---

# File Handling

## Definition

File handling is the process of creating, reading, writing, updating, and managing files stored on a system.

---

## Types of Files

### Readable Files (Text Files)

Human-readable files.

Examples:

- `.txt`
- `.csv`
- `.json`
- `.xml`
- `.log`

> **Note**
>
> Excel files (`.xlsx`, `.xls`) are **not plain text**. They are structured binary/ZIP-based document formats, although their contents can be viewed using spreadsheet software.

---

### Non-Readable Files (Binary Files)

Stored in binary format.

Examples:

- Images
- Audio
- Video
- Executables
- PDF
- Excel (`.xlsx`)

---

# File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (File must exist) |
| `w` | Write (Creates file if it doesn't exist, otherwise overwrites) |
| `r+` | Read and Write (File must exist) |
| `w+` | Write, Read (Creates or overwrites the file) |
| `a` | Append (Creates file if it doesn't exist) |
| `a+` | Append and Read (Creates file if it doesn't exist) |
| `rb` | Read Binary |

---

# `open()`

## Definition

Opens a file and returns a file object.

### FUN

`open()`

### SYN

```python
open(path, mode)
```

### PAR

| Parameter | Description |
|-----------|-------------|
| `path` | File path |
| `mode` | File operation mode (`r`, `w`, `a`, etc.) |

### USA

```python
file = open(
    "data.txt",
    "r"
)
```

---

# `with` Statement

## Definition

Automatically closes the file after use, even if an exception occurs.

### WHY

Preferred over manually calling `close()`.

### USA

```python
with open(
    "data.txt",
    "r"
) as file:

    print(file.read())
```

---

# File Object Methods

## `write()`

### Definition

Writes data into a file.

### USA

```python
with open(
    "data.txt",
    "w"
) as file:

    file.write("Hello")
```

---

## `read()`

### Definition

Reads the file contents.

### SYN

```python
read(size=-1)
```

> **Note**
>
> If `size` is omitted, the entire file is read.

---

## `seek()`

### Definition

Moves the file pointer to a specified position.

### SYN

```python
seek(position)
```

### USA

```python
file.seek(0)
```

---

## `readline()`

### Definition

Reads **one line** at a time.

### WHY

Useful for large files because it avoids loading the entire file into memory.

---

## `readlines()`

### Definition

Reads all lines and returns them as a list.

### SYN

```python
readlines(hint=-1)
```

> **Correction**
>
> The parameter is called **`hint`**, not `pos`.
>
> `hint` specifies approximately how many bytes to read before stopping.

### RES

```python
[
    "Line1\n",
    "Line2\n",
    "Line3\n"
]
```

---

## `close()`

### Definition

Closes the opened file and releases system resources.

### NOTE

Using the `with` statement is recommended because it automatically closes the file.

> **Correction**
>
> Forgetting to close a file generally does **not** cause an "encryption problem." It can lead to:
>
> - Resource leaks
> - File locking
> - Unsaved buffered data
> - Too many open file handles

---

# CSV (Comma-Separated Values)

## Definition

A text file format used to store tabular data.

### LIB

```python
csv
```

---

# `csv.writer()`

## Definition

Creates a writer object for writing CSV data.

### PAR

| Parameter | Description |
|-----------|-------------|
| `file` | File object returned by `open()` |

### USA

```python
import csv

with open(
    "students.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)
```

---

## `writerow()`

### Definition

Writes a single row.

### USA

```python
writer.writerow(
    ["Name", "Age"]
)
```

---

## `writerows()`

### Definition

Writes multiple rows.

### USA

```python
writer.writerows(
    [
        ["John", 20],
        ["Alice", 22]
    ]
)
```

---

# `csv.reader()`

## Definition

Creates a reader object for reading CSV data.

### PAR

| Parameter | Description |
|-----------|-------------|
| `file` | File object returned by `open()` |

### USA

```python
import csv

with open(
    "students.csv"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# Excel

## LIB

```python
openpyxl
```

---

## USA

```python
from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws.title = "Students"

ws["A1"] = "Name"
ws["B1"] = "ID"

ws["A2"] = "Madhan"
ws["B2"] = 1

wb.save("studs.xlsx")
```

---

## DAM

### `title`

Represents the worksheet name.

---

### `active`

Returns the currently active worksheet.

---

## MET

### `save()`

Saves the workbook.

### PAR

| Parameter | Description |
|-----------|-------------|
| `path` | Output Excel file path |

---

# Image Handling

## Definition

Images are handled as **binary files**.

---

## LIB

```python
PIL (Pillow)
```

> **Note**
>
> `PIL` originally stood for **Python Imaging Library**. The actively maintained library used today is **Pillow**, which is imported as `PIL`.

---

## USA

```python
from PIL import Image

img = Image.open(
    "img.jpeg"
)

img.show()
```

---

## MET

### `Image.open()`

#### Definition

Opens an image file.

#### PAR

| Parameter | Description |
|-----------|-------------|
| `path` | Image file path |

---

### `show()`

#### Definition

Displays the image using the operating system's default image viewer.

---

# Summary

| Topic | Purpose |
|--------|---------|
| File Handling | Read and write files |
| `open()` | Open a file |
| File Modes | Specify read/write/append operations |
| `with` | Automatically close files |
| `read()` | Read file contents |
| `write()` | Write to a file |
| `seek()` | Move the file pointer |
| `readline()` | Read one line |
| `readlines()` | Read all lines as a list |
| `close()` | Close the file |
| CSV | Store tabular text data |
| `csv.writer()` | Write CSV data |
| `csv.reader()` | Read CSV data |
| Excel (`openpyxl`) | Create and edit Excel workbooks |
| Pillow (`PIL`) | Open and display image files |