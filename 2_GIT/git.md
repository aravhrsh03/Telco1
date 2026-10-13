# Git & GitHub Notes

## 📌 Keywords Covered
- Git
- GitHub
- DVCS
- Version Control System (VCS)
- Distributed Version Control System
- Centralized Version Control System (CVCS)
- Repository
- Branch
- Staging Area
- Commit
- Git Config
- Git Commands
- GitLab
- GitBucket
- Azure DevOps
- AWS CodeCommit
- Apache Subversion (SVN)
- Fossil

---

## 🏷️ Tags & Keywords Used in Notes
- AL (Alias)
- `---` (Command Definition)
- `=` (Content Definition)

---

# Git

## Definition

- **Git** = Distributed Version Control System (DVCS)
- System-based version control tool.
- Used to track changes in source code.
- Allows multiple developers to work independently and merge changes later.
- Maintains complete repository history on every developer's machine.

---

## Abbreviations

| Symbol | Meaning |
|---------|---------|
| **AL** | Alias |
| **---** | Command Definition |
| **=** | Content Definition |

---

# GitHub

## Definition

- GitHub is a **cloud-based platform** that hosts Git repositories.
- Used to host source code.
- Enables collaboration with other developers.
- Tracks issues using an integrated Issue Tracker.
- Provides Pull Requests, Code Reviews, Actions, Discussions, and Project Management.

> **Correction**
>
> GitHub is **not an IDE**. It is a cloud-based Git hosting platform. It also provides **GitHub Codespaces**, which is a browser-based development environment (IDE).

---

## Other Git Hosting Platforms

### Apache Subversion (SVN) **[AL]**

- Centralized Version Control System (CVCS)

### Fossil **[AL]**

- Open Source
- Distributed Version Control System

### GitLab

- Cloud-based Git hosting platform
- Provides built-in DevOps features

### GitBucket

- Git hosting platform
- Supports collaboration and repository management

### Azure DevOps

- Cloud platform
- Git repository hosting
- Built-in DevOps features
- CI/CD support

### AWS CodeCommit

- Cloud-based Git repository service
- Integrated with AWS services
- Built-in DevOps capabilities

---

# Git Configuration

Configure Git with your GitHub account before making commits.

```bash
git config --global user.name <github-username>
git config --global user.email <github-email>
```

---

# Git Commands

## Check Git Version

```bash
git --version
git -v
```

**Definition**

- Checks the installed Git version.

---

## Initialize Git Repository

```bash
git init
```

**Definition**

- Initializes a new Git repository in the current directory.

---

## List Files Including Hidden Files

```bash
ls -a
```

**Definition**

- `-a` flag displays hidden files and directories.
- Useful for viewing the `.git` directory.

---

## Check Repository Status

```bash
git status
```

**Definition**

Displays the current state of the repository, including:

- Staged files
- Modified files
- Untracked files

---

## Staging Area

**Definition**

- Staging Area = **Ready for Commit**
- Files added to the staging area are prepared for the next commit.

---

## Commit Changes

```bash
git commit -m "<commit-message>"
```

**Definition**

- Commits the staged changes to the local repository.
- `-m` is used to provide the commit message.

---

## View Changes

```bash
git diff
```

**Definition**

- Displays the differences between file versions.
- Shows added and removed code.

---

# Branch

## Definition

- A **branch** is a separate line of development.
- It is a copy of the code from the main repository that allows independent development without affecting the main branch.

---

## View Available Branches

```bash
git branch
```

**Definition**

- Lists all available local branches.

---

## Switch Branch

```bash
git checkout <branch-name>
```

**Definition**

- Switches from the current branch to another branch.

---

## Create and Switch Branch

```bash
git checkout -b <branch-name>
```

**Definition**

- Creates a new branch.
- Immediately switches to the newly created branch.

---

## Restore Changes

```bash
git restore <file-name>
```

**Definition**

- Restores a file to its previous state.
- Discards uncommitted changes in the working directory.

> **Note**
>
> `git restore` restores files, not commits. To move to previous commits, commands such as `git reset` or `git checkout <commit-id>` are used depending on the requirement.

---

# Summary

| Command | Purpose |
|----------|---------|
| `git --version` | Check Git version |
| `git -v` | Version information (alias in notes) |
| `git config --global user.name` | Configure Git username |
| `git config --global user.email` | Configure Git email |
| `git init` | Initialize Git repository |
| `ls -a` | Show all files including hidden files |
| `git status` | Display repository status |
| `git commit -m` | Commit staged changes |
| `git diff` | Show code differences |
| `git branch` | List branches |
| `git checkout <branch>` | Switch branch |
| `git checkout -b <branch>` | Create and switch branch |
| `git restore <file>` | Restore previous file state |