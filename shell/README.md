# Shell Scripting Labs

A practical progression through shell scripting, from basic terminal usage to process and file operations.

These twelve labs were created as part of a Digital Forensics & Cyber Security shell-scripting course. Each lab keeps the learning material, scripts, write-up, and screenshots together so the progression can be followed and revisited.

## Labs

| Lab | Topic | Write-up |
|---|---|---|
| 01 | Introduction to the Shell | [lab01_intro_to_shell/](lab01_intro_to_shell/) |
| 02 | Scripting Basics — directories, permissions, aliases | [lab02_scripting_basics/](lab02_scripting_basics/) |
| 03 | Variables | [lab03_variables/](lab03_variables/) |
| 04 | Command-Line Arguments | [lab04_arguments/](lab04_arguments/) |
| 05 | Wildcards & File Tests | [lab05_wildcards_filetests/](lab05_wildcards_filetests/) |
| 06 | Conditionals | [lab06_conditionals/](lab06_conditionals/) |
| 07 | Loops | [lab07_loops/](lab07_loops/) |
| 08 | Functions & Libraries | [lab08_functions/](lab08_functions/) |
| 09 | Arrays — Basics | [lab09_arrays_basics/](lab09_arrays_basics/) |
| 10 | Arrays — Practical Applications | [lab10_arrays_advanced/](lab10_arrays_advanced/) |
| 11 | Process Management | [lab11_process_management/](lab11_process_management/) |
| 12 | File Operations | [lab12_file_operations/](lab12_file_operations/) |

## Learning Flow

```text
Shell basics
    ↓
Variables & arguments
    ↓
Files, tests & conditionals
    ↓
Loops, functions & arrays
    ↓
Processes & file operations
```

## Usage

From the repository root:

```bash
git clone https://github.com/awais-sec/learnstack.git
cd learnstack
chmod +x shell/*/*.sh
./shell/lab01_intro_to_shell/lab01.sh
```

Some scripts, including labs 06, 07, 11, and 12, use `read` for interactive input. Run those directly in a terminal.

## Screenshots

Lab screenshots are stored in [`assets/`](assets/) and referenced by the individual lab write-ups.

## What This Section Demonstrates

- Linux command-line familiarity
- Shell scripting fundamentals
- Variables, arguments, conditions, loops, and functions
- File and process handling
- Learning through small, explainable practical exercises

[Back to LearnStack](../README.md)
