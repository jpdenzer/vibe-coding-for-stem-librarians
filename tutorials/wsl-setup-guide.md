---
title: "Setting Up WSL on Windows"
parent: "Tutorials"
nav_order: 3
description: "Step-by-step guide to installing and configuring Windows Subsystem for Linux (WSL 2) on Windows 10 and 11."
---

# Setting Up WSL on Windows

Windows Subsystem for Linux (WSL) lets you run a real Linux environment directly on Windows, with no separate virtual machine to manage and no dual-boot setup. This guide covers installing WSL 2, choosing a distribution, configuring it, and fixing common problems.

> **Do you need WSL?** Probably not to get started. Claude Code runs directly on Windows. See [Set Up Claude Code on Windows](claude-code-windows.md). WSL is worth setting up if you want a Linux toolchain, want to follow tutorials written for Mac or Linux, or want Claude Code's [sandboxing](https://code.claude.com/docs/en/sandboxing) feature, which on Windows requires WSL 2.

## Rung

**Supports the High (agentic) rung. Beginner-friendly.** No prior Linux or command-line experience is required. You should be comfortable installing software on Windows and opening PowerShell.

## Time

**About 20 to 30 minutes**, including one restart. Downloads may take longer on a slow connection. Allow an extra 15 minutes if you also want to set up Git, SSH keys, and VS Code (Step 7).

## You Will Need

- A computer running Windows 11, or Windows 10 version 2004 (build 19041) or later
- Administrator access on that computer. **On a work computer, ask your IT office first.** Installing WSL turns on Windows features that may be restricted by institutional policy.
- Hardware virtualization enabled in BIOS/UEFI (see [Step 1](#step-1-enable-virtualization))
- At least 5 GB of free disk space
- A working internet connection
- Optional: a GitHub account, if you plan to set up SSH keys or clone repositories

## Last Check

**October 7, 2026.** Commands and options were written for Windows 11 and Windows 10 with a current version of WSL. WSL is updated often, so verify against the [official documentation](https://learn.microsoft.com/windows/wsl/) if something behaves differently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: Enable Virtualization](#step-1-enable-virtualization)
- [Step 2: Install WSL](#step-2-install-wsl)
- [Step 3: Restart and Finish Distribution Setup](#step-3-restart-and-finish-distribution-setup)
- [Step 4: Verify the Installation](#step-4-verify-the-installation)
- [Step 5: Update Your Linux Packages](#step-5-update-your-linux-packages)
- [Step 6: Install Windows Terminal (Recommended)](#step-6-install-windows-terminal-recommended)
- [Step 7: Set Up Your Development Environment](#step-7-set-up-your-development-environment)
- [Next: Install Claude Code Inside WSL](#next-install-claude-code-inside-wsl)
- [Working with Files](#working-with-files)
- [Configuration](#configuration)
- [Useful WSL Commands](#useful-wsl-commands)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Operating system | Windows 11 (any build), or Windows 10 version 2004 (build 19041) or later |
| Architecture | x64 or ARM64 |
| Virtualization | Hardware virtualization enabled in BIOS/UEFI |
| Permissions | Administrator access on the machine |
| Disk space | At least 5 GB free (more for development work) |

To check your Windows version, press **Win + R**, type `winver`, and press **Enter**.

---

## Step 1: Enable Virtualization

WSL 2 runs a lightweight virtual machine, so CPU virtualization must be turned on.

1. Open **Task Manager** (`Ctrl + Shift + Esc`).
2. Go to the **Performance** tab and select **CPU**.
3. Look for **Virtualization: Enabled** in the bottom right.

If it says **Disabled**, restart your computer, enter BIOS/UEFI setup (commonly by pressing `F2`, `F10`, `Del`, or `Esc` at startup), and enable the relevant option. It is usually called one of:

- Intel Virtualization Technology (VT-x)
- AMD-V or SVM Mode
- Virtualization Technology

Save changes and boot back into Windows.

> **On a work computer:** BIOS/UEFI settings are often locked by IT. If virtualization is disabled, ask your IT office to enable it rather than changing firmware settings yourself.

---

## Step 2: Install WSL

On current versions of Windows 10 and 11, a single command does everything.

1. Right-click the **Start** button and choose **Terminal (Admin)**, **Windows PowerShell (Admin)**, or search for PowerShell and select **Run as administrator**.
2. Run:

   ```powershell
   wsl --install
   ```

This command:

- Enables the required Windows features (Virtual Machine Platform and WSL)
- Downloads and installs the latest WSL Linux kernel
- Sets WSL 2 as the default version
- Installs **Ubuntu** as the default distribution

### Choosing a Different Distribution

To see the distributions available for installation:

```powershell
wsl --list --online
```

Then install one by name:

```powershell
wsl --install -d Debian
```

Common choices include `Ubuntu`, `Ubuntu-24.04`, `Debian`, `kali-linux`, `openSUSE-Leap-15.6`, and `AlmaLinux-9`. Names change over time, so use the output of `wsl --list --online` as the source of truth.

> **Tip:** You can install multiple distributions side by side and switch between them. If you're not sure which to pick, stay with the default, **Ubuntu**. Most tutorials assume it.

### If `wsl --install` Only Shows Help Text

This means WSL is already partly installed. Use the list command above, then install a distribution with `wsl --install -d <DistroName>`.

---

## Step 3: Restart and Finish Distribution Setup

1. **Restart your computer** when prompted.
2. After restart, the distribution launches automatically and finishes installing. This can take a few minutes the first time.
3. When asked, create a **Linux username** and **password**.

Notes on credentials:

- The Linux username and password are **separate** from your Windows account.
- Nothing appears on screen while you type the password. This is normal.
- You will use this password with `sudo` to run administrative commands.

If the distribution does not launch on its own, open the **Start** menu, search for your distribution (for example, "Ubuntu"), and open it.

---

## Step 4: Verify the Installation

In PowerShell or Command Prompt, run:

```powershell
wsl --list --verbose
```

Expected output looks like this:

```text
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

Confirm the **VERSION** column shows **2**. If it shows **1**, convert it:

```powershell
wsl --set-version Ubuntu 2
```

To make WSL 2 the default for any future installs:

```powershell
wsl --set-default-version 2
```

Check the overall WSL status and kernel version:

```powershell
wsl --status
wsl --version
```

---

## Step 5: Update Your Linux Packages

Open your Linux distribution and update its package lists and installed software. For Ubuntu and Debian:

```bash
sudo apt update && sudo apt upgrade -y
```

For other distributions, use their native package manager (`dnf`, `zypper`, `pacman`, and so on).

Also keep WSL itself current from PowerShell:

```powershell
wsl --update
```

---

## Step 6: Install Windows Terminal (Recommended)

Windows 11 includes **Windows Terminal** by default. On Windows 10, install it from the Microsoft Store or with winget:

```powershell
winget install --id Microsoft.WindowsTerminal -e
```

Windows Terminal automatically adds a profile for each installed WSL distribution. You can open a new tab with your Linux shell from the dropdown arrow next to the **+** button, and set it as your default profile in **Settings > Startup**.

---

## Step 7: Set Up Your Development Environment

### Install Essential Tools

Inside your Linux distribution (Ubuntu/Debian example):

```bash
sudo apt install -y build-essential git curl wget unzip
```

### Configure Git

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

#### Optional: Share Git Credentials with Windows

If you use Git for Windows, you can reuse its credential manager from WSL:

```bash
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager.exe"
```

#### Optional: SSH Keys

```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub
```

Add the printed public key to GitHub under **Settings > SSH and GPG keys**.

> **Keep the private key private.** Only ever share the file ending in `.pub`. Never paste `~/.ssh/id_ed25519` (no `.pub`) into an AI tool, a chat, or a repository. See [Guardrails](../guardrails.md).

### Use Visual Studio Code with WSL

1. Install [Visual Studio Code](https://code.visualstudio.com/) on **Windows** (not inside WSL).
2. Install the **WSL** extension (`ms-vscode-remote.remote-wsl`).
3. From your Linux terminal, navigate to a project folder and run:

   ```bash
   code .
   ```

VS Code opens on Windows but runs its server and extensions inside Linux, so you get Windows UI with a Linux toolchain.

---

## Next: Install Claude Code Inside WSL

Once WSL is working, install Claude Code **inside your Linux distribution**, not from PowerShell. Open Ubuntu (or Windows Terminal → your Ubuntu tab) and run the Linux installer:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Then open a new Ubuntu tab, make a practice folder in your Linux home directory, and start Claude Code there:

```bash
mkdir -p ~/projects/claude-practice
cd ~/projects/claude-practice
claude
```

Sign-in, first prompts, and safety habits are the same as in [Set Up Claude Code on Windows](claude-code-windows.md#step-6-start-claude-code-and-sign-in). See Anthropic's [setup guide](https://code.claude.com/docs/en/setup#set-up-on-windows) for current WSL-specific notes.

---

## Working with Files

### Accessing Windows Files from Linux

Windows drives are mounted under `/mnt`:

```bash
cd /mnt/c/Users/<YourWindowsUsername>/Documents
```

### Accessing Linux Files from Windows

In File Explorer, enter this in the address bar:

```text
\\wsl$
```

or, for a specific distribution:

```text
\\wsl.localhost\Ubuntu\home\<your-linux-username>
```

You can also open the current Linux directory in File Explorer from a Linux terminal:

```bash
explorer.exe .
```

### Performance Best Practice

> **Store your projects inside the Linux filesystem (for example, `~/projects`), not under `/mnt/c`.**

Cross-filesystem access is significantly slower, particularly for operations involving many small files such as `git status`, `npm install`, and builds. Avoid editing Linux files from Windows tools through the `\\wsl$` path for heavy workloads, and prefer working from within WSL.

---

## Configuration

WSL has two configuration files that serve different purposes.

| File | Location | Scope |
|------|----------|-------|
| `.wslconfig` | `C:\Users\<YourWindowsUsername>\.wslconfig` | Global settings for the WSL 2 virtual machine |
| `wsl.conf` | `/etc/wsl.conf` (inside each distribution) | Per-distribution settings |

### Global Settings: `.wslconfig`

Create or edit the file in your Windows user folder:

```ini
[wsl2]
memory=8GB
processors=4
swap=4GB

[experimental]
autoMemoryReclaim=gradual
```

By default WSL 2 can use up to 50% of your system memory. Set `memory` and `processors` if WSL is consuming too many resources, or if builds need more.

Apply changes by shutting WSL down completely and starting it again:

```powershell
wsl --shutdown
```

### Per-Distribution Settings: `/etc/wsl.conf`

Edit the file from inside Linux:

```bash
sudo nano /etc/wsl.conf
```

#### Enable systemd

Newer WSL versions support systemd, which is needed for services such as Docker (native install), snap, and many `systemctl` workflows. On some distributions it is already enabled. If not:

```ini
[boot]
systemd=true
```

Then restart from PowerShell:

```powershell
wsl --shutdown
```

#### Set the Default User

```ini
[user]
default=yourusername
```

#### Other Common Options

```ini
[automount]
enabled=true
options="metadata"

[interop]
enabled=true
appendWindowsPath=true
```

Setting `appendWindowsPath=false` keeps Windows executables out of your Linux `PATH`, which can speed up shell tab completion.

### Networking

On Windows 11 (22H2 and later) with a current WSL version, you can enable **mirrored networking mode**, which improves VPN compatibility, enables `localhost` access in both directions, and supports IPv6. Add to `.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
```

Restart WSL with `wsl --shutdown` afterward.

---

## Useful WSL Commands

Run these from PowerShell or Command Prompt.

| Command | Purpose |
|---------|---------|
| `wsl` | Launch the default distribution |
| `wsl -d <Distro>` | Launch a specific distribution |
| `wsl --list --verbose` | List installed distributions, their state, and WSL version |
| `wsl --list --online` | List distributions available to install |
| `wsl --set-default <Distro>` | Set the default distribution |
| `wsl --set-version <Distro> 2` | Convert a distribution to WSL 2 |
| `wsl --terminate <Distro>` | Stop a single distribution |
| `wsl --shutdown` | Stop all distributions and the WSL VM |
| `wsl --update` | Update WSL |
| `wsl --version` | Show WSL and component versions |
| `wsl --export <Distro> <file.tar>` | Back up a distribution |
| `wsl --import <Name> <InstallPath> <file.tar>` | Restore or clone a distribution |
| `wsl --unregister <Distro>` | **Permanently delete** a distribution and its data |

### Back Up and Restore a Distribution

```powershell
wsl --export Ubuntu D:\backups\ubuntu-backup.tar
wsl --import Ubuntu-Restored D:\WSL\Ubuntu-Restored D:\backups\ubuntu-backup.tar
```

> **Warning:** `wsl --unregister` deletes everything in that distribution, including all files, with no confirmation prompt. Export a backup first if there is anything you want to keep.

---

## Troubleshooting

### Error `0x80370102` or "Virtualization is not enabled"

Virtualization is disabled in BIOS/UEFI or Windows features are missing. Revisit [Step 1](#step-1-enable-virtualization). Then confirm the Windows features are enabled by running this in an elevated PowerShell:

```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

Restart the computer afterward.

### Error `0x80070003` or `0x80070002` on Distribution Launch

This often occurs when the default install location is on a drive other than `C:`, or when the Store-installed distribution is corrupted. Reinstall the distribution, or use `wsl --import` to place it on a drive you choose.

### "The WSL 2 requires an update to its kernel component"

Run:

```powershell
wsl --update
```

### Hyper-V or Third-Party Virtualization Conflicts

WSL 2 uses the Windows hypervisor platform. Older versions of VirtualBox, VMware, or Android emulators can conflict. Update these tools to current versions, which are compatible with the Windows Hypervisor Platform.

### No Internet Access Inside WSL, or DNS Failures

Common with VPNs. Try these in order:

1. Enable mirrored networking (see [Networking](#networking)).
2. Restart WSL with `wsl --shutdown`.
3. As a manual workaround, disable automatic DNS generation by adding this to `/etc/wsl.conf`:

   ```ini
   [network]
   generateResolvConf=false
   ```

   Then replace the symlinked file and set your own resolver:

   ```bash
   sudo rm /etc/resolv.conf
   echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
   ```

   Restart WSL afterward.

   > **On a campus network:** a public DNS server like `1.1.1.1` can't see campus-only hostnames (for example, internal library or proxy servers) and may conflict with institutional network policy. Ask your IT office which DNS server to use, and try steps 1 and 2 first.

### WSL Using Too Much Memory

Set limits in `.wslconfig` (see [Configuration](#configuration)). Consider enabling `autoMemoryReclaim=gradual` as shown above.

### Virtual Disk Growing Large

WSL stores each distribution in a `.vhdx` file that grows as you add data but does not always shrink automatically. To reclaim space after deleting files, shut WSL down and compact the disk. In an elevated PowerShell:

```powershell
wsl --shutdown
wsl --manage Ubuntu --set-sparse true
```

Sparse mode lets the disk release freed space automatically. Check `wsl --help` on your version to confirm the option is available.

### Slow File Operations

Move your project into the Linux filesystem (`~/`) rather than `/mnt/c`. See [Performance Best Practice](#performance-best-practice).

---

## Additional Resources

- [Microsoft Learn: WSL documentation](https://learn.microsoft.com/windows/wsl/)
- [Install WSL](https://learn.microsoft.com/windows/wsl/install)
- [Advanced settings configuration in WSL](https://learn.microsoft.com/windows/wsl/wsl-config)
- [Set up a WSL development environment](https://learn.microsoft.com/windows/wsl/setup/environment)
- [Troubleshooting WSL](https://learn.microsoft.com/windows/wsl/troubleshooting)
- [WSL GitHub repository and issue tracker](https://github.com/microsoft/WSL)

---

*Last updated: October 2026. WSL is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Claude Code on macOS](claude-code-macos-setup-guide.md) · [Next: Creating a GitHub Account →](creating-a-github-account.md)
