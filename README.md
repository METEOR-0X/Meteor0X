# Cybercat 🐈‍⬛

A very simple and easy command-line tool to save, manage, and remember your cybersecurity tools and commands. 

## What you need
Before you start, make sure you have:
1. A computer running Linux (like Debian, Ubuntu, or Kali).
2. **Python 3** installed on your system. 

## How to install

Follow these simple steps to install Cybercat on your computer:

**1. Create a folder for the project:**
Open your terminal and type:
    
    mkdir ~/Cybercat
    cd ~/Cybercat

*(Make sure to put the `cybercat.py` file inside this folder).*

**2. Make the file executable:**
You need to give the file permission to run:
    
    chmod +x ~/Cybercat/cybercat.py

**3. Create a shortcut:**
Add the tool to your system so you can just type `cybercat` from anywhere:
    
    echo "alias cybercat='~/Cybercat/cybercat.py'" >> ~/.bashrc
    source ~/.bashrc

## How to use it

Cybercat is very easy to use. Here are the commands you can type in your terminal:

### Manage Your Tools
* **Add a new tool:**
  `cybercat add nmap "Used for network scanning and port enumeration."`
* **Read about a tool:**
  `cybercat show nmap`
* **Change a tool's description:**
  `cybercat edit nmap "New description here."`
* **Delete a tool:**
  `cybercat delete nmap`
* **See all your saved tools:**
  `cybercat list`

### Manage Your Commands
* **Add a specific command:**
  `cybercat add-cmd "nmap -sV target" "Scan for open ports and services."`
* **Read about a command:**
  `cybercat show-cmd "nmap -sV target"`
* **See all your saved commands:**
  `cybercat list-cmd`

### Export Your Data
* **Save all your tools and commands to a text file:**
  `cybercat export`
