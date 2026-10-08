---
title: "Setting Up Python on macOS"
parent: "Tutorials"
nav_order: 6
description: "Step-by-step guide to installing Python on a Mac with the official python.org installer or Homebrew, creating virtual environments, and fixing common problems."
---

# Setting Up Python on macOS

Python is a popular, free programming language used for scripting, data work, web development, automation, and more. Your Mac includes a small copy of Python for Apple's own tools, but you should install your own current version for everyday work. This guide walks through installing Python from the official python.org installer (with Homebrew as an alternative), checking that it works, creating a virtual environment for a project, and fixing common problems.

> **Do you need to install Python?** Not to get started. You can run Python in your browser with Google Colab. See [01 · Conversational Prompting](../01-chatgpt-gemini-prompting.md#step-3-run-a-simple-python-script-with-google-colab). Install Python on your Mac when you want to run scripts on your own files, work offline, or use an agentic tool like Claude Code or Codex on a Python project.

## Rung

**Low to Mid: running AI-written scripts on your own computer. Beginner-friendly.** No programming experience is required. You should be comfortable installing an app on your Mac and pasting a command into Terminal.

## Time

**About 15 to 20 minutes.** The install itself takes a few minutes. Allow extra time if you also set up a virtual environment and Visual Studio Code (Steps 7 and 9).

## You Will Need

- A Mac running a macOS version supported by the current Python installer. The python.org page for Python 3.14.8 lists the installer as supporting macOS 10.15 and later, and the installer's own **Read Me** shows the exact supported versions.
- An Apple silicon or Intel Mac. The official installer runs natively on both.
- An administrator account on the Mac, because the official installer installs Python for all users. **On a work computer, check with your IT office first.** IT may already offer Python through a software center.
- An internet connection
- Terminal (already on your Mac)
- Optional: [Homebrew](https://brew.sh/), if you prefer to install Python that way
- Optional: [Visual Studio Code](https://code.visualstudio.com/), a free editor that works well with Python
- Optional: [Git](creating-a-github-account.md), for saving and sharing your code

## Last Check

**October 8, 2026.** Commands and options were checked against the official Python documentation and python.org on this date. At that time the latest Python release was **3.14.8** (September 30, 2026). Python updates often, so verify against [python.org](https://www.python.org/downloads/macos/) and the [Python on macOS documentation](https://docs.python.org/3/using/mac.html) if something looks different on your system.

## Table of Contents

- [Choose Your Install Method](#choose-your-install-method)
- [Step 1: Open Terminal](#step-1-open-terminal)
- [Step 2: Check Whether Python Is Already Installed](#step-2-check-whether-python-is-already-installed)
- [Step 3: Install Python](#step-3-install-python)
- [Step 4: Verify the Installation](#step-4-verify-the-installation)
- [Step 5: Run Your First Python Program](#step-5-run-your-first-python-program)
- [Step 6: Understand python and python3](#step-6-understand-python-and-python3)
- [Step 7: Create a Virtual Environment](#step-7-create-a-virtual-environment)
- [Step 8: Install Packages with pip](#step-8-install-packages-with-pip)
- [Step 9: Use Python in Visual Studio Code](#step-9-use-python-in-visual-studio-code)
- [Try It: Run the A–Z List Demo](#try-it-run-the-az-list-demo)
- [Updating Python](#updating-python)
- [Uninstalling](#uninstalling)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Choose Your Install Method

| Method | Best for | Notes |
|--------|----------|-------|
| **python.org installer** (recommended for beginners) | Most people | A standard macOS installer from the Python release team. Includes IDLE, a built-in editor, and Python Launcher |
| **Homebrew** | People who already use Homebrew to manage tools | Can install several Python versions. Not maintained by the core Python team |
| **Other distributions** (Anaconda, MacPorts, ActivePython) | Specific needs, such as the `conda` package manager for scientific work | Not maintained by the core Python team, and may not include the latest Python |

This guide focuses on the python.org installer and covers Homebrew as an alternative. Pick **one** method. Mixing several can leave you with more than one Python and confusion about which one runs.

---

## Step 1: Open Terminal

1. Press **Command + Space** to open Spotlight.
2. Type `Terminal` and press **Return**.

You can also find Terminal in **Applications > Utilities**. Modern Macs use the `zsh` shell by default, which is what the commands in this guide assume.

---

## Step 2: Check Whether Python Is Already Installed

In Terminal, run:

```bash
python3 --version
which python3
```

What you might see:

| Result | What it means |
|--------|---------------|
| `/usr/bin/python3` | This is the copy of Python that comes with Apple's developer tools. It is usually older and incomplete. **Do not modify or delete it.** Apple's tools and other software depend on it |
| macOS offers to install the **command line developer tools** | Python is not installed yet, and macOS is offering Apple's version. You can decline and install the official Python in Step 3 instead |
| `/Library/Frameworks/Python.framework/...` or `/usr/local/bin/python3` | The python.org Python is already installed |
| `/opt/homebrew/bin/python3` or similar | A Homebrew Python is already installed |

You can have Apple's Python and your own Python installed side by side without trouble. The python.org installer is set up so that its `python3` is used instead of the system one.

---

## Step 3: Install Python

Choose **one** option.

### Option A: The python.org Installer (Recommended)

1. Go to [python.org/downloads/macos](https://www.python.org/downloads/macos/) and download the latest **macOS installer** (a `.pkg` file). For Python 3.14.8 the file is `python-3.14.8-macos11.pkg`.

   The installer is a *universal2* build, which runs natively on all supported Macs, both Apple silicon and Intel. It is signed and notarized by the Python Software Foundation to meet macOS Gatekeeper requirements.

2. Double-click the downloaded `.pkg` file to start the standard macOS Installer.
3. Click **Continue** to reach the **Read Me**. It shows which Python version will be installed and which macOS versions are supported. Scroll through it.
4. Click **Continue**, read the license, then click **Agree**.
5. On the **Installation Type** screen, the standard install is right for most people. The **Customize** button lets you leave out components or add the optional free-threaded Python, which beginners do not need.
6. Click **Install**. macOS asks for an administrator name and password, since Python is installed for all users of the Mac.
7. When the installation finishes, a **Summary** window appears. **Do not close it yet.** Finish the next step first.

#### Install the Security Certificates (Important)

After installation, a Finder window opens at `/Applications/Python 3.14/`. Run the certificate script that completes the install:

1. Double-click **Install Certificates.command** in that folder.
2. A Terminal window opens and downloads SSL root certificates for the new Python.
3. When you see `Successfully installed certifi` and `update complete`, the installation is complete. Close the Terminal window and the installer.

Without this step, Python programs that make secure web connections may fail with certificate errors.

> **If macOS blocks `Install Certificates.command`:** Run it from Terminal instead. Adjust the version number to match yours:
>
> ```bash
> "/Applications/Python 3.14/Install Certificates.command"
> ```
>
> On older versions of macOS, you can also right-click (or Control-click) the file, choose **Open**, then confirm.

#### What the Installer Adds

| Item | Location |
|------|----------|
| **IDLE** (a basic Python editor and shell) and **Python Launcher** | `/Applications/Python 3.14/` |
| The Python framework (the interpreter and libraries) | `/Library/Frameworks/Python.framework` |
| Shortcuts to the interpreter | `/usr/local/bin/` |

The installer also adds the framework's location to your shell path.

### Option B: Homebrew

If you already use [Homebrew](https://brew.sh/):

```bash
brew install python
```

To install a specific version side by side, look up the available versions with `brew search python` and install, for example:

```bash
brew install python@3.14
```

Homebrew's Python is maintained by Homebrew, not the Python core team, and may trail the newest release slightly. Homebrew also manages updates (see [Updating Python](#updating-python)).

### Option C: Install from the Command Line (Optional, Advanced)

If you want to script the python.org installer, the macOS `installer` tool can install the downloaded package. Python's documentation notes that current installers only install to fixed locations (`/Library/Frameworks/`, `/Applications`, and `/usr/local/bin`) and that you cannot choose a different location with the `-domain` option.

```bash
sudo installer -pkg ~/Downloads/python-3.14.8-macos11.pkg -target /
```

Afterward, run `Install Certificates.command` as described above. See `man installer` and the [Python documentation](https://docs.python.org/3/using/mac.html#installing-using-the-command-line) for more.

---

## Step 4: Verify the Installation

Close Terminal and open a **new** window so it picks up the changes, then run:

```bash
python3 --version
which python3
```

You should see a version number such as `Python 3.14.8`. For the python.org install, `which python3` should point somewhere under `/Library/Frameworks/Python.framework/` or `/usr/local/bin/`. For Homebrew it should point into the Homebrew folder. If it shows `/usr/bin/python3` you are still using Apple's copy. See [Troubleshooting](#troubleshooting).

Also confirm that `pip` works:

```bash
python3 -m pip --version
```

---

## Step 5: Run Your First Python Program

### Interactive Mode

Type `python3` and press **Return** to open the Python prompt:

```bash
python3
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

1. Make a folder for practice work and move into it:

   ```bash
   mkdir -p ~/python-practice
   cd ~/python-practice
   ```

2. Create a file named `hello.py`. You can use TextEdit in plain-text mode, or the built-in `nano` editor:

   ```bash
   nano hello.py
   ```

3. Type this into the file:

   ```python
   name = input("What is your name? ")
   print(f"Hello, {name}! Welcome to Python.")
   ```

   In `nano`, press `Control + O` then **Return** to save, and `Control + X` to exit.

4. Run it:

   ```bash
   python3 hello.py
   ```

### Using IDLE

If you installed from python.org, you also have **IDLE**, a simple editor with a built-in Python shell. Open **Applications > Python 3.14 > IDLE**, choose **File > New File**, type your code, save it, and press **F5** to run it. It also has a **Help** menu with Python documentation.

---

## Step 6: Understand python and python3

On macOS, use **`python3`** for the interpreter and **`pip3`** or **`python3 -m pip`** for packages. The shorter `python` command may not exist on a fresh Mac, depending on how you installed Python. Once a virtual environment is active (Step 7), `python` and `pip` work inside it and point to that environment's copies.

> **Running code from an AI chat?** AI tools often write `python script.py`. On a Mac without an active virtual environment, type `python3 script.py` instead.

You can also run a specific version, such as:

```bash
python3.14 hello.py
```

To see which Python a command actually runs, use `which`:

```bash
which python3
which python3.14
```

---

## Step 7: Create a Virtual Environment

A **virtual environment** gives each project its own packages. This avoids version conflicts and keeps your main Python clean. The Python documentation recommends using virtual environments when working with multiple Python environments, because they avoid command-name conflicts and confusion about which Python is in use.

1. In your project folder, create one named `.venv`:

   ```bash
   python3 -m venv .venv
   ```

2. Activate it:

   ```bash
   source .venv/bin/activate
   ```

3. Your prompt now starts with `(.venv)`. While it is active, `python` and `pip` refer to the environment's own copies. Check with:

   ```bash
   which python
   ```

4. When you are finished, leave the environment with:

   ```bash
   deactivate
   ```

If you use Git, add `.venv/` to your `.gitignore` file so you do not commit the environment. See the [Creating a GitHub Account](creating-a-github-account.md) tutorial.

---

## Step 8: Install Packages with pip

With your virtual environment active, install a package:

```bash
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

Using `python -m pip` rather than plain `pip` guarantees you are using the pip that belongs to the Python you intend. If you are *not* inside a virtual environment, use `python3 -m pip` instead. Check a package's name on [pypi.org](https://pypi.org/) before installing, and only install packages you trust. For more, see the [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/).

> **AI-suggested packages:** AI tools sometimes suggest packages that don't exist, and attackers register fake packages under those names. Before installing anything an AI recommends, look it up on pypi.org. See [Guardrails: security-sensitive code](../guardrails.md#security-sensitive-code).

---

## Step 9: Use Python in Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) is a popular free editor for Python.

1. Install VS Code if you have not already, from [code.visualstudio.com](https://code.visualstudio.com/).
2. Open the Extensions view (`Cmd + Shift + X`), search for **Python** (published by Microsoft), and click **Install**.
3. Open your project folder with **File > Open...**.
4. Open the Command Palette (`Cmd + Shift + P`) and run **Python: Select Interpreter**.
5. Choose the interpreter inside your virtual environment, which is usually listed as `.venv`.
6. Open a `.py` file and click the **Run** button in the upper right, or open the integrated terminal with `` Ctrl + ` `` (the backtick key, usually above Tab) and run `python hello.py`.

---

## Try It: Run the A–Z List Demo

This site's [demo script](../examples/#demo-compare-two-az-database-lists) compares two fake A–Z database lists. It uses only Python's standard library, so there's nothing to install.

1. Go to the [repository on GitHub](https://github.com/jpdenzer/vibe-coding-for-stem-librarians), click the green **Code** button, and choose **Download ZIP**.
2. Double-click the ZIP in your Downloads folder to unzip it.
3. In Terminal:

   ```bash
   cd ~/Downloads/vibe-coding-for-stem-librarians-main/examples
   python3 compare_az_lists.py
   ```

You should see the titles that are only in list A, only in list B, and in both. Compare the result with the [expected output](../examples/#expected-output).

---

## Updating Python

How you update depends on how you installed.

| Installed with | How to update |
|----------------|---------------|
| python.org installer | Download the newest installer from [python.org/downloads/macos](https://www.python.org/downloads/macos/) and run it, then run **Install Certificates.command** again. Releases of the same minor version (for example, 3.14.7 to 3.14.8) replace the previous one. A new minor version (for example, 3.15) installs alongside the old one |
| Homebrew | `brew update && brew upgrade python` |

Because you keep project packages in virtual environments, updating Python does not change those packages. After a major update you may need to re-create a virtual environment with the new Python:

```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

---

## Uninstalling

### python.org Installation

Python's documentation says you can uninstall the python.org installation by removing three things:

1. The `Python 3.14` folder in `/Applications`
2. The framework folder `/Library/Frameworks/Python.framework`
3. The shortcuts to the Python executable in `/usr/local/bin/`

Always check what you are deleting. In Terminal, for Python 3.14:

```bash
sudo rm -rf "/Applications/Python 3.14"
sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.14
ls -l /usr/local/bin | grep "Python.framework/Versions/3.14"
```

The last command lists the shortcuts that point to the version you are removing. Delete those with `sudo rm`, naming each file. If you are removing the last Python version, you can remove the entire `Python.framework` folder.

Do **not** touch `/usr/bin/python3`. It belongs to Apple.

> **Careful with `sudo rm -rf`:** it deletes without asking and can't be undone. Type the paths exactly as shown, and if an AI tool suggests a different `rm -rf` command, check it carefully before running it.

You may also want to remove any lines that Python's installer added to your shell profile (for example, in `~/.zprofile`).

### Homebrew Installation

```bash
brew uninstall python
```

Replace `python` with the formula name you installed, such as `python@3.14`.

---

## Troubleshooting

### `python3` Still Shows Apple's Version (`/usr/bin/python3`)

- Close Terminal and open a new window so it picks up the installer's changes.
- Run `which -a python3` to list every `python3` on your path in order.
- Make sure the installer's shell profile update worked. The python.org install includes an **Update Shell Profile.command** file in `/Applications/Python 3.14/`. Double-click it, then open a new Terminal window.
- As a quick workaround, run the version you want explicitly, for example `python3.14`.

### `python: command not found`

This is normal on a fresh Mac. Use `python3`, or activate a virtual environment, where `python` works. See [Step 6](#step-6-understand-python-and-python3).

### macOS Offers to Install Command Line Developer Tools When I Type `python3`

That is Apple's version being offered. You do not need it for the python.org Python. Decline, and complete [Step 3](#step-3-install-python). Note that the command line developer tools are separately useful if you plan to use Git or compile packages.

### "Certificate Verify Failed" or SSL Errors

You probably skipped `Install Certificates.command`. Run it from `/Applications/Python 3.14/`, as described in [Step 3](#step-3-install-python).

### `externally-managed-environment` Error When Using pip

Some installs, including Homebrew's Python, refuse `pip install` outside a virtual environment, to protect the system's own packages. Create and activate a virtual environment ([Step 7](#step-7-create-a-virtual-environment)), then install your packages there.

### IDLE or `tkinter` Hangs on macOS 27.0

The Python 3.14.8 release notes warn that on macOS 27.0, IDLE and other `tkinter` programs may hang, with a spinning beach ball, when a menu command opens a dialog. For example, **About IDLE**, **Settings**, and **Open Module** are affected. The release notes attribute this to an operating system behavior change that is believed to affect current versions of the Tk graphics toolkit across current Python versions. If you depend on Tk-based programs, test your workflow before upgrading to macOS 27.0, or use a different editor such as VS Code. Follow [issue #158053](https://github.com/python/cpython/issues/158053) for updates.

### A Script Behaves Differently When Opened from Finder

If you run a script from Finder with **Python Launcher**, it does not run in your usual shell environment, so settings in your shell profile (such as environment variables) are not applied. Run it from Terminal instead if you need that environment.

### I Have Several Pythons and Cannot Tell Which Is Running

Use `which python3` and `which -a python3` to see them, and prefer virtual environments so each project uses a known Python. You can also create shell aliases for specific versions if you like.

### The Installer Says It Cannot Be Opened

The python.org installer is signed and notarized by the Python Software Foundation, so macOS should open it normally. If you see a warning, make sure you downloaded it from python.org. Then open **System Settings > Privacy & Security**, scroll down to the message about the blocked file, and click **Open Anyway**. On older versions of macOS, you can instead right-click (or Control-click) the file and choose **Open**.

### The macOS Version Is Too Old

Check the installer's **Read Me** and the python.org release page for the supported macOS versions. If your Mac is too old for the current installer, an older Python release may support it. Check the [macOS downloads page](https://www.python.org/downloads/macos/).

### The Install Is Blocked on a Work Computer

If you don't have administrator rights or the installer is blocked, ask your IT office. They may be able to install Python for you or offer it through a managed software catalog. Until then, you can use [Google Colab](../01-chatgpt-gemini-prompting.md#step-3-run-a-simple-python-script-with-google-colab) in your browser.

---

## Additional Resources

- [Python downloads for macOS](https://www.python.org/downloads/macos/)
- [Using Python on macOS (official documentation)](https://docs.python.org/3/using/mac.html)
- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Virtual environments and packages (official tutorial)](https://docs.python.org/3/tutorial/venv.html)
- [IDLE documentation](https://docs.python.org/3/library/idle.html)
- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Homebrew](https://brew.sh/)
- [Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

---

*Last updated: October 2026. Python is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: Setting Up Python on Windows](python-windows-setup-guide.md) · [Next: Setting Up WSL on Windows →](wsl-setup-guide.md)
