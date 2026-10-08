---
title: "Setting Up [TOOL NAME] on [PLATFORM]"
parent: "Tutorials"
nav_order: 99
description: "Step-by-step guide to installing and configuring [TOOL NAME] on [PLATFORM], [one short phrase about what the reader will be able to do]."
published: false
---

<!--
=====================================================================
CONTRIBUTOR INSTRUCTIONS (delete this whole comment before publishing)
=====================================================================

HOW TO USE THIS TEMPLATE
1. Copy this file into the tutorials/ folder and rename it. Use lowercase
   words separated by hyphens, ending in "-setup-guide.md", for example:
   python-windows-setup-guide.md or codex-macos-setup-guide.md
   (Hyphens avoid "%20" characters in links and web addresses.)
2. In the front matter at the very top:
   - Replace the title and description.
   - Keep `parent: "Tutorials"` so the guide appears in the Tutorials menu.
   - Set nav_order to place the guide in the menu. Look at the nav_order
     values in the other tutorials and pick the right position. Guides for
     the same tool sit next to each other, Windows first, then macOS.
     Renumber the guides below yours if needed.
   - DELETE the line "published: false". It only keeps this blank template
     from appearing on the website.
3. Replace every [BRACKETED PLACEHOLDER] with real content.
4. Delete any section that does not apply. Keep the order of the sections
   that remain. Add sections where your topic needs them.
5. Delete these instructions.
6. Add your guide to the Tutorials page (tutorials/README.md): a linked
   title, a one- or two-sentence description, and this line:
   **Rung:** ... · **Time:** ... · **You'll need:** ... · **Last checked:** Month YYYY
7. Update the Previous / Next links at the bottom of your guide AND of the
   guides directly before and after it in the menu.
8. Run through the contributor checklist at the bottom of this file.

TITLE AND FILE NAMING
- Title pattern: "Setting Up [Tool] on [Platform]" (for example, "Setting Up
  Python on macOS"). Capitalize "Up" and use "on", to match the other
  tutorials. If the guide covers one tool on one platform, say both.
- The H1 heading (# ...) must match the title in the front matter.
- Write the platform name the way its vendor does: macOS, Windows, Linux, WSL.

WHO READS THESE GUIDES
- This site is for STEM and science librarians with little or no programming
  background. Many readers will be on a work computer managed by their
  institution's IT office, and many will be reading on a phone.
- Keep it jargon-light. Define a term the first time you use it.

HOW GUIDES IN THIS REPO ARE WRITTEN
- Audience: someone who has never done this before. Do not assume knowledge.
- Voice: plain, direct, second person ("you"). Short sentences. Use the
  imperative for steps ("Open Terminal").
- Verify before you write. Check every command, setting, menu name, and
  version number against the tool's OFFICIAL documentation, and test on a real
  machine when you can. Say in the pull request what you checked and what
  you did not.
- Do not invent facts. If you are unsure, say so in the guide ("Check the
  official docs for the current requirement") rather than guessing.
- Name the exact thing to click or type. Use **bold** for button and menu
  labels, `code formatting` for commands, file names, and settings.
- One path per step. If there are several ways to do something, pick a
  recommended one, then offer others as "Alternative" or "Option B" sections.
- Warn about risk before the risky step, not after it. Use a "Warning" block
  for anything that can delete data, expose secrets, or cost money.
- Never include real passwords, keys, tokens, personal paths, or account
  names. Use placeholders such as <your-username> or yourname.

LIBRARY-SPECIFIC CONVENTIONS (used in every guide on this site)
- IT permission: if the guide installs software or needs administrator
  rights, add "On a work computer, check with your IT office first." to the
  You Will Need list. Never tell readers to work around institutional
  security controls.
- Practice folder: first sessions with agentic tools (Claude Code, Codex, and
  similar) should start in a new, empty practice folder, never the whole home
  folder, Documents, or Desktop.
- Guardrails: if readers might put data or files into the tool, remind them
  to keep patron or student data, credentials, proxy details, and licensed
  vendor content out of it, and link to ../guardrails.md.
- Low-setup alternatives: if a no-install option exists (for example, Google
  Colab instead of installing Python), mention it near the top.
- Official docs: anything likely to change (install commands, prices, plan
  names, system requirements) needs a link to the official source.

FORMATTING CONVENTIONS
- Headings: # for the title (once), ## for major sections, ### for steps and
  subsections, #### for sub-parts. Do not skip levels.
- Steps are numbered in the heading ("Step 1: ...") so readers can find their
  place. Number steps continuously, even across Parts.
- Use a horizontal rule (---) between major sections.
- Code blocks: always give a language (bash, powershell, python, json, toml,
  text). Use "text" for expected output or example prompts.
  - Use "powershell" for Windows, "bash" for macOS and Linux.
  - Put only the commands in the block, with no leading $ or > prompt
    characters, so readers can copy and paste.
- Tables: use them to compare options, list commands, or list requirements.
  Keep each cell short. Wide tables are hard to read on phones, so prefer
  two or three columns.
- Callouts use blockquotes with a bold label. Use these labels only:
    > **Tip:** a helpful shortcut or best practice
    > **Note:** extra information the reader might want
    > **Important:** something the reader must not skip
    > **Warning:** something that can cause harm or data loss
    > **Check the official docs:** something likely to change over time
- Links:
  - Link to official documentation for anything you did not explain fully.
  - Link to other tutorials with a relative path, for example
    [Setting Up WSL on Windows](wsl-setup-guide.md). Link to the main guides
    one folder up, for example [Guardrails](../guardrails.md).
  - Link to .md files, not .html. The site converts them automatically, so
    the same link works on the website and on GitHub.
  - Internal links to headings use lowercase, hyphenated anchors:
    [Step 2](#step-2-install-the-tool). Check each one works.
- Keep guides platform-specific. If a tool needs a different install on
  another platform, make a separate guide instead of a giant combined one.

SECTION BY SECTION
- Rung: Where the guide fits on this site's vibe coding spectrum (see "Rung
  scale" below), plus a short difficulty note.
- Time: A realistic total, with a range. Say what is included (downloads,
  restarts) and what adds extra time.
- You Will Need: Everything the reader must have BEFORE starting, as a bullet
  list. Include account requirements, permissions, versions, hardware, and
  other guides they should finish first. Put optional items last, marked
  "Optional:".
- Last Check: The date YOU verified the content, in the form "Month D, YYYY",
  plus the version of the tool you checked against. Update it whenever you
  re-verify. Readers use this to decide how much to trust the guide.

RUNG SCALE
On this site, a "rung" is a step on the vibe coding spectrum from the talk,
not a difficulty level. Use one of these, then add a difficulty note such as
"Beginner-friendly." Examples from existing tutorials:
- **Low to Mid: running AI-written scripts on your own computer.**
  For tools that support copy-and-paste and iterative prompting (Python).
- **High (agentic). Beginner-friendly.**
  For agentic coding tools (Claude Code, Codex).
- **Supports High (agentic). Beginner-friendly.**
  For setup that agentic tools depend on (WSL).
- **Supports all rungs. Beginner-friendly.**
  For general skills used at every level (Git and GitHub).
The rungs are explained on the home page (../index.md).

=====================================================================
-->

# Setting Up [TOOL NAME] on [PLATFORM]

[One to three sentences. What is the tool? Why would someone use it? Then say exactly what this guide covers, for example: "This guide walks through installing X, signing in, verifying that it works, and fixing common problems."]

> **Do you need [TOOL NAME]?** [Optional. If there's a simpler, no-install alternative, mention it here and link to it.]

## Rung

**[Rung, for example "High (agentic)"]. [Difficulty note, for example "Beginner-friendly."]** [One sentence describing what the reader should already be comfortable with.]

## Time

**About [X to Y minutes].** [One sentence on what the time includes.] Allow **an extra [X minutes]** if you [optional extra, such as also set up Git or a virtual environment].

## You Will Need

- [Operating system and minimum version]
- [Hardware requirements, if any, such as RAM or processor type]
- [Account or subscription required, with the plan name and a link to current pricing]
- [Permissions required, such as administrator access.] **On a work computer, check with your IT office first.**
- [An internet connection, if the install downloads anything]
- [Any other guide the reader should finish first, linked, for example: [Setting Up WSL on Windows](wsl-setup-guide.md)]
- Optional: [Something helpful but not required]

## Last Check

**[Month D, YYYY].** [State what was verified and against which source, for example: "Commands and options were checked against the official [Tool] documentation on this date."] At that time the latest version was **[version number]**. [Tool] changes often, so verify against the [official documentation]([URL]) if something looks different on your system.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Step 1: [Verb phrase]](#step-1-verb-phrase)
- [Step 2: [Verb phrase]](#step-2-verb-phrase)
- [Step 3: Verify the Installation](#step-3-verify-the-installation)
- [Step 4: [First Use]](#step-4-first-use)
- [Keeping [Tool] Up to Date](#keeping-tool-up-to-date)
- [Uninstalling](#uninstalling)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Prerequisites

[Optional section. Use it when requirements need more detail than the You Will Need list, such as a table of supported versions.]

| Requirement | Details |
|-------------|---------|
| Operating system | [Version] |
| Hardware | [Details] |
| Account | [Details] |

[Explain how to check each requirement.] For example, to check your version, [exact steps or command].

---

## Step 1: [Verb Phrase, for Example "Open Terminal"]

[One or two sentences saying what this step accomplishes and why.]

1. [First action. Name the exact button, menu, or key.]
2. [Second action.]
3. [Third action.]

```bash
[command the reader should run]
```

[Say what the reader should see afterward.]

> **Tip:** [Optional shortcut or best practice.]

---

## Step 2: [Verb Phrase, for Example "Install [Tool]"]

[Explain the recommended method first.]

### Option A: [Recommended Method]

1. [Action.]
2. [Action.]

```powershell
[command]
```

### Option B: [Alternative Method]

[Say who this option is for and when to choose it.]

```bash
[command]
```

> **Warning:** [Only if there is real risk. Explain what could go wrong and how to avoid it.]

---

## Step 3: Verify the Installation

Open a **new** terminal window so it picks up any changes, then run:

```bash
[command that prints a version or status]
```

A working installation prints [describe the expected output]:

```text
[example of expected output]
```

If this fails, go to [Troubleshooting](#troubleshooting).

---

## Step 4: [First Use, for Example "Run Your First Task"]

[Walk the reader through one small, safe task that proves the tool works. Keep it short and give the exact input and expected result. For agentic tools, start in a new, empty practice folder.]

1. [Action.]
2. [Action.]

```text
[example prompt, command, or output]
```

---

## Keeping [Tool] Up to Date

[Explain how updates work for each install method.]

| Installed with | How to update |
|----------------|---------------|
| [Method 1] | [Automatic, or the exact command] |
| [Method 2] | [Exact command] |

---

## Uninstalling

[Give removal steps for each install method.]

```bash
[uninstall command]
```

> **Warning:** [Say exactly what is deleted, for example settings, history, or data, and how to back it up first.]

---

## Troubleshooting

### [Exact Error Message or Symptom]

[Explain the likely cause in one sentence. Then give the fix as numbered steps or a command.]

```bash
[fix command]
```

### [Second Symptom]

[Cause and fix.]

### The Install Is Blocked on a Work Computer

[If relevant. Tell the reader to contact their IT office, and mention any no-install alternative.]

### I Am Still Stuck

[Say where to get help: the tool's issue tracker, its community forum, or its support page. Mention what information to include, such as the operating system version, the tool version, and the exact error message. Remind readers to remove personal details from logs before posting them publicly.]

---

## Additional Resources

- [Official documentation: [Tool]]([URL])
- [Official installation or setup page]([URL])
- [Official troubleshooting page]([URL])
- [Related tutorial on this site](related-tutorial.md)

---

*Last updated: [Month YYYY]. [Tool] is updated frequently, so verify commands and options against the official documentation if something behaves differently on your system.*

---

[← Previous: [Title of the tutorial before this one]](previous-tutorial.md) · [Next: [Title of the tutorial after this one] →](next-tutorial.md)

<!--
=====================================================================
CONTRIBUTOR CHECKLIST (delete this comment before publishing)
=====================================================================

FRONT MATTER
[ ] Title follows "Setting Up [Tool] on [Platform]"
[ ] parent: "Tutorials" is present and nav_order places it in the right spot
[ ] Description is one sentence and mentions the tool and platform
[ ] "published: false" has been removed
[ ] H1 heading matches the title

REQUIRED SECTIONS (in this order)
[ ] Rung (using this site's spectrum, plus a difficulty note)
[ ] Time
[ ] You Will Need (including the IT note if software is installed)
[ ] Last Check (with date and tool version)
[ ] Table of Contents (every link works)
[ ] Numbered steps
[ ] Verify the Installation
[ ] Troubleshooting
[ ] Additional Resources
[ ] Closing "Last updated" line
[ ] Previous / Next links

ACCURACY
[ ] Every command was checked against the official documentation
[ ] Every command was tested on a real machine, or the pull request says which
    ones were not tested
[ ] Version numbers, menu labels, and URLs are current as of the Last Check date
[ ] No guesses are presented as facts

QUALITY
[ ] Written for a first-time reader; terms are defined when first used
[ ] Each step has one clear action, and says what the reader should see
[ ] Risky steps have a Warning before the step
[ ] Code blocks have a language and contain only copyable commands
[ ] Links to other pages in this repo use correct relative .md paths
[ ] No real passwords, tokens, usernames, or personal file paths
[ ] Guardrails reminder included if readers might put data into the tool

SITE INTEGRATION
[ ] Entry added to the Tutorials page (tutorials/README.md)
[ ] Previous / Next links updated in the neighboring tutorials
[ ] Site previewed locally or on a fork, if possible, to check the menu

CLEAN-UP
[ ] All [BRACKETED PLACEHOLDERS] are replaced
[ ] Unused sections are deleted
[ ] These instruction comments are deleted
[ ] File name is lowercase and hyphenated
=====================================================================
-->
