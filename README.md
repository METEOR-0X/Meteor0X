
# Meteor0x ☄️

A very simple and easy command-line tool to save, manage, and remember your cybersecurity tools and commands. 

## What you need
Before you start, make sure you have:
1. A computer running Linux (like Debian, Ubuntu, or Kali).
2. **Python 3** installed on your system. 

## How to install

Follow these simple steps to install Meteor0x on your computer:

**1. Create a folder for the project:**
Open your terminal and type:
```bash
mkdir ~/Meteor0x
cd ~/Meteor0x

```

*(Make sure to put the `meteor0x.py` file inside this folder).*

**2. Make the file executable:**
You need to give the file permission to run:

```bash
chmod +x ~/Meteor0x/meteor0x.py

```

**3. Create a shortcut:**
Add the tool to your system so you can just type `meteor0x` from anywhere:

```bash
echo "alias meteor0x='~/Meteor0x/meteor0x.py'" >> ~/.bashrc
source ~/.bashrc

```

## How to use it

Meteor0x is very easy to use. Here are the commands you can type in your terminal:

### Manage Your Tools

* **Add a new tool:**
`meteor0x add nmap "Used for network scanning and port enumeration."`
* **Read about a tool:**
`meteor0x show nmap`
* **Change a tool's description:**
`meteor0x edit nmap "New description here."`
* **Delete a tool:**
`meteor0x delete nmap`
* **See all your saved tools:**
`meteor0x list`

### Manage Your Commands

* **Add a specific command:**
`meteor0x add-cmd "nmap -sV target" "Scan for open ports and services."`
* **Read about a command:**
`meteor0x show-cmd "nmap -sV target"`
* **See all your saved commands:**
`meteor0x list-cmd`

### Export Your Data

* **Save all your tools and commands to a text file:**
`meteor0x export`

