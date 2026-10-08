---
title: "Setting Up Python on Windows"
parent: "Tutorials"
nav_order: 5
description: "Step-by-step guide to installing Python on Windows with the Python install manager, creating virtual environments, and fixing common problems."
---

# Setting Up Python on Windows

Python is a popular, free programming language used for scripting, data work, web development, automation, and more. Windows does not come with a system-supported copy of Python, so you need to install one. This guide walks through installing the official Python from the Python Software Foundation using the **Python install manager**, checking that it works, creating a virtual environment for a project, and fixing common problems.

> **Do you need to install Python?** Not to get started. You can run Python in your browser with Google Colab. See [01 · Conversational Prompting](../01-chatgpt-gemini-prompting.md#step-3-run-a-simple-python-script-with-google-colab). Install Python on your computer when you want to run scripts on your own files, work offline, or use an agentic tool like Claude Code or Codex on a Python project.

## Rung

**Low to Mid: running AI-written scripts on your own computer. Beginner-friendly.** No programming experience is required. You should be comfortable installing an app on Windows and pasting a command into PowerShell or Command Prompt.

## Time

**About 15 to 20 minutes.** The install itself takes a few minutes. Allow extra time if you also set up a virtual environment and Visual Studio Code (Steps 6 and 8).

## You Will Need

- A computer running **Windows 10 or newer**. Python 3.14 supports Windows 10 and newer. See [Older Versions of Windows](#older-versions-of-windows) if you are on something older.
- An internet connection
- Permission to install apps on your computer. A per-user install does not normally require administrator rights. **On a work computer, check with your IT office first.** Some institutions block Microsoft Store apps, or offer Python through a software center.
- A terminal: **Windows Terminal**, **PowerShell**, or **Command Prompt**
- About 1 GB of free disk space is a comfortable minimum for Python and a few project packages
- Optional: [Visual Studio Code](https://code.visualstudio.com/), a free editor that works well with Python
- Optional: [Git](creating-a-github-account.md), for saving and sharing your code

## Last Check

**October 8, 2026.** Commands and options were checked against the official Python documentation and python.org downloads page on this date. At that time the latest Python release was **3.14.8** (September 30, 2026) and the latest Python install manager was **26.3**. Python updates often, so verify against [python.org](https://www.python.org/downloads/windows/) and the [Python on Windows documentation](https://docs.python.org/3/using/windows.html) if something looks different on your system.

## Table of Contents

- [How Python Works on Windows](#how-python-works-on-windows)
- [Step 1: Check Whether Python Is Already Installed](#step-1-check-whether-python-is-already-installed)
- [Step 2: Install the Python Install Manager](#step-2-install-the-python-install-manager)
- [Step 3: Install Python](#step-3-install-python)
- [Step 4: Verify the Installation](#step-4-verify-the-installation)
- [Step 5: Run Your First Python Program](#step-5-run-your-first-python-program)
- [Step 6: Create a Virtual Environment](#step-6-create-a-virtual-environment)
- [Step 7: Install Packages with pip](#step-7-install-packages-with-pip)
- [Step 8: Use Python in Visual Studio Code](#step-8-use-python-in-visual-studio-code)
- [Try It: Run the A–Z List Demo](#try-it-run-the-az-list-demo)
- [Managing Python Versions](#managing-python-versions)
- [Optional Settings](#optional-settings)
- [Python and WSL](#python-and-wsl)
- [Uninstalling](#uninstalling)
- [Troubleshooting](#troubleshooting)
- [A Note About the Old Installer](#a-note-about-the-old-installer)
- [Additional Resources](#additional-resources)

---

## How Python Works on Windows

A few terms make the rest of this guide easier to follow.

| Term | Meaning |
|------|---------|
| **Python install manager** | The official tool from the Python team for getting Python on Windows. It adds the `python`, `py`, and `pymanager` commands to your computer and handles installing and updating Python versions |
| **Runtime** | One installed version of Python, such as 3.14 |
| `python` | The command that launches your default Python. It uses the latest stable version unless you configure otherwise |
| `py` | A command that does what `python` does, plus options for choosing a specific version and managing installs. Use it when you have more than one version of Python |
| `pymanager` | An unambiguous alias for the install manager. It is useful in scripts, because `py` may be taken by an older launcher |
| **Virtual environment** | A private folder of Python packages for one project, so projects do not interfere with each other |
| **pip** | Python's package installer, used to add libraries |

The Python documentation recommends creating a virtual environment for each project.

> **Tip:** Windows has many ways to get Python, including the Microsoft Store's older Python apps, Anaconda, and other bundles. The Python documentation recommends checking whether tools you already use can provide Python for you, since staying consistent with your other tools is worthwhile. This guide covers the official route.

---

## Step 1: Check Whether Python Is Already Installed

Open a terminal. In Windows 11, right-click the **Start** button and choose **Terminal**. Then run:

```powershell
python --version
py --version
```

What you might see:

| Result | What it means |
|--------|---------------|
| A version number such as `Python 3.14.8` | Python is already installed. You can skip to [Step 4](#step-4-verify-the-installation) to check it, but consider reading [Step 2](#step-2-install-the-python-install-manager) to make sure you have the install manager |
| The Microsoft Store opens, or the command is not found | Python is not installed. Continue to Step 2 |

If you have older Python installations, they may conflict with the install manager. See [Troubleshooting](#troubleshooting).

---

## Step 2: Install the Python Install Manager

Choose **one** method. The Store version and the python.org version are identical.

### Option A: Microsoft Store

1. Open the [Python install manager page in the Microsoft Store](https://apps.microsoft.com/detail/9NQ7512CXL7T).
2. Click **Install**.
3. When it finishes, open a new terminal.

### Option B: Download from python.org

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the **Python install manager** (an `.msix` file).
2. Double-click the file and select **Install**.

You can also install it from PowerShell:

```powershell
Add-AppxPackage <path to the downloaded MSIX file>
```

### Option C: winget (Command Line)

```powershell
winget install 9NQ7512CXL7T -e --accept-package-agreements --disable-interactivity
```

Then, optionally, run the configuration checker and accept all changes:

```powershell
py install --configure -y
```

After installing, the `python`, `py`, and `pymanager` commands should be available. The install manager updates itself automatically, and updating it does not change your Python versions.

---

## Step 3: Install Python

The install manager installs Python versions on demand.

### The Easy Way

If no Python is installed yet, simply type this in a terminal:

```powershell
python
```

The install manager downloads and installs the current latest release for you, then starts it. (This is controlled by an `automatic_install` setting that is on by default.) Type `exit()` and press **Enter** to leave the Python prompt.

### The Explicit Way

To choose what to install, first see what is available:

```powershell
py list --online
```

Then install a version:

```powershell
py install 3.14
```

The first time you install a version, the install manager may ask whether to add a folder to your `PATH`. This is optional:

- If you plan to use the `py` command, you can skip it.
- If you want the full set of command names such as `python3.14.exe` to work, add it. The folder is `%LocalAppData%\Python\bin` by default.

To add it later, click **Start**, search for **Edit environment variables for your account**, and add the folder to your `Path` variable.

> **Which version should I install?** For most people, the latest stable release is the right choice. If a tutorial, course, or project requires a specific version, install that one alongside it. See [Managing Python Versions](#managing-python-versions).

---

## Step 4: Verify the Installation

Open a **new** terminal window and run:

```powershell
python --version
```

You should see a version number, such as `Python 3.14.8`. Then check what the install manager knows about:

```powershell
py list
```

This lists your installed Python versions and shows which one is your default. Also confirm that `pip` works:

```powershell
python -m pip --version
```

If any of these fail, see [Troubleshooting](#troubleshooting).

---

## Step 5: Run Your First Python Program

### Interactive Mode

Type `python` and press **Enter** to open the Python prompt:

```powershell
python
```

Then try:

```python
>>> print("Hello, world!")
Hello, world!
>>> 2 + 3
5
>>> exit()
```

### Running a Script

1. Make a folder for practice work, such as `C:\Users\<you>\python-practice`, and open a terminal there:

   ```powershell
   mkdir $HOME\python-practice
   cd $HOME\python-practice
   ```

2. Create a file named `hello.py`. You can use Notepad:

   ```powershell
   notepad hello.py
   ```

3. Type this into the file, then save it:

   ```python
   name = input("What is your name? ")
   print(f"Hello, {name}! Welcome to Python.")
   ```

4. Run it:

   ```powershell
   python hello.py
   ```

If you have more than one Python installed and want a specific one, use `py` with the version:

```powershell
py -V:3.14 hello.py
```

---

## Step 6: Create a Virtual Environment

A **virtual environment** gives each project its own packages. This avoids version conflicts and keeps your main Python clean.

1. In your project folder, create one named `.venv`:

   ```powershell
   python -m venv .venv
   ```

2. Activate it.

   **PowerShell:**

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   **Command Prompt:**

   ```batch
   .venv\Scripts\activate.bat
   ```

3. Your prompt now starts with `(.venv)`. While it is active, `python` and `pip` refer to the environment's own copies.

4. When you are finished, leave the environment with:

   ```powershell
   deactivate
   ```

> **PowerShell blocks the activation script?** If you see an error saying that running scripts is disabled on this system, PowerShell's execution policy is stopping `Activate.ps1`. Either use Command Prompt and `activate.bat`, or allow locally created scripts for your user account:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
>
> Read Microsoft's [execution policy guide](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) before changing this setting. On a work computer, this may be controlled by IT policy.

If you use Git, add `.venv/` to your `.gitignore` file so you do not commit the environment. See the [Creating a GitHub Account](creating-a-github-account.md) tutorial.

---

## Step 7: Install Packages with pip

With your virtual environment active, install a package:

```powershell
python -m pip install requests
```

Useful pip commands:

| Command | What it does |
|---------|--------------|
| `python -m pip install <package>` | Installs a package |
| `python -m pip install --upgrade <package>` | Upgrades a package |
| `python -m pip list` | Lists installed packages |
| `python -m pip show <package>` | Shows details about one package |
| `python -m pip freeze > requirements.txt` | Saves the exact packages in the environment to a file |
| `python -m pip install -r requirements.txt` | Installs everything listed in a requirements file |
| `python -m pip uninstall <package>` | Removes a package |

Using `python -m pip` rather than plain `pip` is recommended, because it guarantees you are using the pip that belongs to the Python you intend. Check a package's name on [pypi.org](https://pypi.org/) before installing, and only install packages you trust.

> **AI-suggested packages:** AI tools sometimes suggest packages that don't exist, and attackers register fake packages under those names. Before installing anything an AI recommends, look it up on pypi.org. See [Guardrails: security-sensitive code](../guardrails.md#security-sensitive-code).

---

## Step 8: Use Python in Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a popular free editor for Python.

1. Install VS Code if you have not already, from [code.visualstudio.com](https://code.visualstudio.com/).
2. Open the Extensions view (`Ctrl + Shift + X`), search for **Python** (published by Microsoft), and click **Install**.
3. Open your project folder with **File > Open Folder...**.
4. Open the Command Palette (`Ctrl + Shift + P`) and run **Python: Select Interpreter**.
5. Choose the interpreter inside your virtual environment, which is usually listed as `.venv`.
6. Open a `.py` file and click the **Run** button in the upper right, or open the integrated terminal with `` Ctrl + ` `` and run `python hello.py`.

---

## Try It: Run the A–Z List Demo

This site's [demo script](../examples/#demo-compare-two-az-database-lists) compares two fake A–Z database lists. It uses only Python's standard library, so there's nothing to install.

1. Go to the [repository on GitHub](https://github.com/jpdenzer/vibe-coding-for-stem-librarians), click the green **Code** button, and choose **Download ZIP**.
2. In File Explorer, right-click the ZIP in your Downloads folder and choose **Extract All**, then **Extract**.
3. In PowerShell:

   ```powershell
   cd "$HOME\Downloads\vibe-coding-for-stem-librarians-main\vibe-coding-for-stem-librarians-main\examples"
   python compare_az_lists.py
   ```

   Windows usually extracts into a folder with the same name nested inside, which is why the name appears twice. If you get "cannot find path", open the extracted folder in File Explorer to see where `examples` ended up.

You should see the titles that are only in list A, only in list B, and in both. Compare the result with the [expected output](../examples/#expected-output).

---

## Managing Python Versions

You can have several Python versions installed at once. Use `py` to manage and choose among them.

| Command | What it does |
|---------|--------------|
| `py list` | Lists installed versions |
| `py list --online` | Lists versions available to install |
| `py list --online 3.14` | Filters available versions by tag |
| `py install 3.14` | Installs a version |
| `py install --update` | Updates all installs managed by the install manager, if newer versions are available |
| `py -V:3.14` | Launches a specific version |
| `py -V:3.14 script.py` | Runs a script with a specific version |
| `py uninstall 3.14` | Removes a version |
| `py install --refresh` | Rebuilds shortcuts and global commands, for example after installing packages |
| `py help` | Shows all commands |

The default runtime is your latest stable release unless you configure otherwise. To change it, set the `PYTHON_MANAGER_DEFAULT` environment variable, or `default_tag` in the configuration file at `%AppData%\Python\pymanager.json`.

> **Note:** `py install --update` replaces existing installs with newer ones and removes modifications made to the install, including packages installed globally. Virtual environments continue to work. This is another reason to keep project packages in virtual environments.

### Free-Threaded Python (Advanced)

Pre-built free-threaded versions are available by adding a `t` to the tag, for example `py install 3.14t`. Most beginners do not need this.

---

## Optional Settings

### Turn On Long File Paths

Windows historically limits paths to 260 characters, which can cause errors with deeply nested projects. Newer versions of Windows can lift this limit. An administrator must either enable the **Enable Win32 long paths** group policy, or set `LongPathsEnabled` to `1` under this registry key:

```text
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
```

After changing it, Python can use long paths. Only edit the registry if you are comfortable doing so, or ask your IT team. On a work computer, always ask IT.

### UTF-8 Mode

Windows still uses a legacy encoding for text files by default, which can cause trouble when you share files with macOS, Linux, or WSL, which use UTF-8. You can make Python default to UTF-8 for a single run:

```powershell
python -X utf8 myscript.py
```

Or for the current terminal session:

```powershell
$env:PYTHONUTF8 = "1"
```

Setting `PYTHONUTF8=1` globally affects all Python 3.7+ programs on your system, so be careful if you rely on older programs that expect the legacy encoding.

> **Library data tip:** Title lists, vendor exports, and catalog records often contain accented characters (é, ü, ñ). If a script garbles them or fails with a `UnicodeDecodeError`, encoding is the likely cause. Try UTF-8 mode, or ask the AI to open files with `encoding="utf-8"` (or `"utf-8-sig"` for CSVs saved from Excel).

---

## Python and WSL

If you also use Windows Subsystem for Linux, remember that Python on Windows and Python inside WSL are **separate installations**. Packages, virtual environments, and settings in one do not carry over to the other. Install Python inside your Linux distribution using its own package manager, for example:

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
```

For setting up WSL itself, see the [Setting Up WSL on Windows](wsl-setup-guide.md) tutorial.

---

## Uninstalling

### Remove Python Versions

To remove one version:

```powershell
py uninstall 3.14
```

To remove every version the install manager manages, and clean up Start menu entries, registry entries, and download caches:

```powershell
py uninstall --purge
```

The `--purge` option does not affect Python installs that were not made by the install manager.

### Remove the Install Manager

Open **Settings > Apps > Installed apps**, find the **Python install manager**, and choose **Uninstall**. This does **not** remove your Python versions. They stay usable, but the global `python` and `py` commands go away. To clean up completely, run `py uninstall --purge` **before** uninstalling the install manager.

---

## Troubleshooting

### `python` Opens the Microsoft Store or Says "Command Not Found"

1. Confirm you installed the Python install manager ([Step 2](#step-2-install-the-python-install-manager)).
2. Click **Start**, search for **Manage app execution aliases**, and check that the aliases for **Python (default)** are turned on. If they already are, try turning them off and on again to refresh the command. The **Python (default windowed)** and **Python install manager** aliases may also need refreshing.
3. Check that the `py` and `pymanager` commands work.
4. Make sure your `PATH` includes `%UserProfile%\AppData\Local\Microsoft\WindowsApps`. Windows includes it by default, and removing it breaks the shortcuts.

### `py` Says "Command Not Found"

Follow the same checks as above: confirm the install manager is installed, check the app execution aliases, and make sure `WindowsApps` is on your `PATH`.

### `py` Says "Can't Open File"

You probably have the older Python launcher installed and it is taking priority over the install manager. Click **Start**, open **Installed apps**, search for **Python launcher**, and uninstall it.

### `python` and `py` Start Different Versions

- Click **Start**, open **Installed apps**, look for older Python installs, and either remove them or choose **Modify** and turn off their `PATH` options.
- Open **Manage app execution aliases** and check that `python.exe` is set to **Python (default)**.
- Run `py list` to see your default. Check the `PYTHON_MANAGER_DEFAULT` environment variable or the `default_tag` setting if it is not what you expect.

### `pip` Says "Command Not Found"

- If you have a virtual environment, make sure it is activated.
- Use `python -m pip` instead of `pip`.
- Run `py install --refresh` and make sure the global shortcuts folder is on your `PATH`. The command output tells you if it is not.

### I Installed a Package but Its Command Is Not Found

Make sure your virtual environment is activated. For global installs, the install manager does not create shortcuts for new packages automatically. Run:

```powershell
py install --refresh
```

### Typing `script.py` Opens a New Window

This is a known Windows limitation. Run scripts with `python script.py` or `py script.py` instead.

### Older Versions of Windows

Each Python release supports a Windows version only while Microsoft supports it. Python 3.14 supports Windows 10 and newer. If you need Windows 8.1, use Python 3.12. If you need Windows 7, use Python 3.8. These older versions no longer receive current features, so upgrading Windows is the better long-term fix.

### Windows Server 2019 or Environments Without MSIX Support

Windows Server 2019 is the one supported Windows version that cannot install MSIX packages. Use the **MSI** version of the install manager from the python.org downloads page instead. It has no user interface and installs per machine.

### The Install Is Blocked by a Company Policy

Some institution-managed computers block Store apps or MSIX installs. Ask your IT team, or ask them about the Python documentation's [advanced installation options](https://docs.python.org/3/using/windows.html#advanced-installation) and offline installs. Until then, you can use [Google Colab](../01-chatgpt-gemini-prompting.md#step-3-run-a-simple-python-script-with-google-colab) in your browser.

### Reporting a Problem

If you still have trouble, the Python install manager's issue tracker is at [github.com/python/pymanager/issues](https://github.com/python/pymanager/issues). Include any relevant log files, which are written to your `%TEMP%` folder by default. Issues there are public, so check logs for usernames, file paths, or other details you don't want to share before attaching them.

---

## A Note About the Old Installer

You may find older tutorials that tell you to download an `.exe` installer and check **Add python.exe to PATH**. The full installer is deprecated since Python 3.14 and will not be produced for Python 3.16 or later. The Python install manager described in this guide is the replacement. If you follow an older tutorial, you may end up with two competing installs, which causes the problems listed under [Troubleshooting](#troubleshooting).

---

## Additional Resources

- [Python downloads for Windows](https://www.python.org/downloads/windows/)
- [Using Python on Windows (official documentation)](https://docs.python.org/3/using/windows.html)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Virtual environments and packages (official tutorial)](https://docs.python.org/3/tutorial/venv.html)
- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Python Package Index (PyPI)](https://pypi.org/)
- [pip documentation](https://pip.pypa.io/)
- [Python install manager issue tracker](https://github.com/python/pymanager/issues)
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

---

*Last updated: October 2026. Python and the Python install manager are updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Codex on macOS](codex-macos-setup-guide.md) · [Next: Setting Up Python on macOS →](python-macos-setup-guide.md)
