#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import textwrap

# Set up paths to ensure data remains with the script
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = os.path.join(APP_DIR, "meteor0x_db.json")

def load_db():
    # Seamless migration from the old Cybercat DB to Meteor0x DB
    old_db_file = os.path.join(APP_DIR, "cybercat_db.json")
    if os.path.exists(old_db_file) and not os.path.exists(DB_FILE):
        os.rename(old_db_file, DB_FILE)
        print("[*] Info: Database automatically migrated from Cybercat to Meteor0x.")

    if not os.path.exists(DB_FILE):
        data = {"tools": {}, "commands": {}}
        with open(DB_FILE, 'w') as f:
            json.dump(data, f)
        return data
        
    with open(DB_FILE, 'r') as f:
        data = json.load(f)
        
        # Auto-migrate structure if needed
        if "tools" not in data and "commands" not in data:
            new_data = {"tools": data, "commands": {}}
            save_db(new_data)
            return new_data
            
        return data

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def print_logo():
    # Massive, bold ASCII art for METEOR0X
    logo = r"""
 ███╗   ███╗ ███████╗ ████████╗ ███████╗ ██████╗  ██████╗  ██████╗  ██╗  ██╗
 ████╗ ████║ ██╔════╝ ╚══██╔══╝ ██╔════╝ ██╔══██╗ ██╔══██╗ ██╔═████╗╚██╗██╔╝
 ██╔████╔██║ █████╗      ██║    █████╗   ██║  ██║ ██████╔╝ ██║██╔██║ ╚███╔╝ 
 ██║╚██╔╝██║ ██╔══╝      ██║    ██╔══╝   ██║  ██║ ██╔══██╗ ████╔╝██║ ██╔██╗ 
 ██║ ╚═╝ ██║ ███████╗    ██║    ███████╗ ╚██████╔╝██║  ██║ ╚██████╔╝██╔╝ ██╗
 ╚═╝     ╚═╝ ╚══════╝    ╚═╝    ╚══════╝  ╚═════╝ ╚═╝  ╚═╝  ╚═════╝ ╚═╝  ╚═╝
    """
    # ANSI escape code for Hex #3492ad (RGB: 52, 146, 173)
    color_start = "\033[38;2;52;146;173m"
    color_reset = "\033[0m"
    print(f"{color_start}{logo}{color_reset}")

def draw_table(title, col1_name, col2_name, data_dict):
    # Get terminal width, leaving a safe margin of 2 characters to prevent auto-wrapping
    term_width = shutil.get_terminal_size().columns - 2
    
    # Fallback for extremely small terminals
    if term_width < 40:
        term_width = 80 
        
    # The borders use exactly 7 characters: "| " + " | " + " |"
    border_width = 7
    available_width = term_width - border_width
    
    # Calculate maximum needed width for column 1
    max_col1_content = max((len(k) for k in data_dict.keys()), default=0)
    col1_width_needed = max(len(col1_name), max_col1_content)
    
    # Cap column 1 width to 30% of available space
    col1_width = min(col1_width_needed, int(available_width * 0.30))
    
    # Remaining space goes to column 2
    col2_width = available_width - col1_width
    
    separator = f"+{'-' * (col1_width + 2)}+{'-' * (col2_width + 2)}+"

    print(f"  {title}")
    print(separator)
    print(f"| {col1_name.ljust(col1_width)} | {col2_name.ljust(col2_width)} |")
    print(separator)
    
    for key, value in data_dict.items():
        key_lines = textwrap.wrap(key, col1_width) if key else [""]
        val_lines = textwrap.wrap(value, col2_width) if value else [""]
        
        max_lines = max(len(key_lines), len(val_lines))
        
        for i in range(max_lines):
            k_str = key_lines[i] if i < len(key_lines) else ""
            v_str = val_lines[i] if i < len(val_lines) else ""
            print(f"| {k_str.ljust(col1_width)} | {v_str.ljust(col2_width)} |")
            
        print(separator)
        
    print()

# --- TOOLS FUNCTIONS ---

def add_tool(name, description):
    db = load_db()
    name = name.lower()
    if name in db["tools"]:
        print(f"[-] Error: Tool '{name}' already exists. Use 'edit' to modify it.")
    else:
        db["tools"][name] = description
        save_db(db)
        print(f"[+] Success: Tool '{name}' added successfully to Meteor0x.")

def show_tool(name):
    db = load_db()
    name = name.lower()
    if name in db["tools"]:
        draw_table("TOOL DETAILS", "TOOL NAME", "DESCRIPTION", {name: db["tools"][name]})
    else:
        print(f"[-] Error: Tool '{name}' not found.")

def edit_tool(name, description):
    db = load_db()
    name = name.lower()
    if name in db["tools"]:
        db["tools"][name] = description
        save_db(db)
        print(f"[+] Success: Tool '{name}' updated successfully.")
    else:
        print(f"[-] Error: Tool '{name}' not found. Use 'add' to create it.")

def delete_tool(name):
    db = load_db()
    name = name.lower()
    if name in db["tools"]:
        del db["tools"][name]
        save_db(db)
        print(f"[+] Success: Tool '{name}' deleted successfully from Meteor0x.")
    else:
        print(f"[-] Error: Tool '{name}' not found.")

def list_tools():
    db = load_db()
    if not db["tools"]:
        print("[!] The tools database is empty. Add some tools first.")
        return
    print_logo()
    draw_table("METEOR0X TOOLS LIST", "TOOL NAME", "DESCRIPTION", db["tools"])

# --- COMMANDS FUNCTIONS ---

def add_cmd(cmd, description):
    db = load_db()
    if cmd in db["commands"]:
        print(f"[-] Error: Command '{cmd}' already exists. Use 'edit-cmd' to modify it.")
    else:
        db["commands"][cmd] = description
        save_db(db)
        print(f"[+] Success: Command added successfully to Meteor0x.")

def show_cmd(cmd):
    db = load_db()
    if cmd in db["commands"]:
        draw_table("COMMAND DETAILS", "COMMAND", "DESCRIPTION", {cmd: db["commands"][cmd]})
    else:
        print(f"[-] Error: Command '{cmd}' not found.")

def edit_cmd(cmd, description):
    db = load_db()
    if cmd in db["commands"]:
        db["commands"][cmd] = description
        save_db(db)
        print(f"[+] Success: Command updated successfully.")
    else:
        print(f"[-] Error: Command not found. Use 'add-cmd' to create it.")

def delete_cmd(cmd):
    db = load_db()
    if cmd in db["commands"]:
        del db["commands"][cmd]
        save_db(db)
        print(f"[+] Success: Command deleted successfully from Meteor0x.")
    else:
        print(f"[-] Error: Command not found.")

def list_cmds():
    db = load_db()
    if not db["commands"]:
        print("[!] The commands database is empty. Add some commands first.")
        return
    print_logo()
    draw_table("METEOR0X COMMANDS LIST", "COMMAND", "DESCRIPTION", db["commands"])

# --- EXPORT FUNCTION ---

def export_data(filename):
    db = load_db()
    if not db["tools"] and not db["commands"]:
        print("[!] The database is empty. Nothing to export.")
        return

    export_path = os.path.join(os.getcwd(), filename)
    
    try:
        with open(export_path, 'w') as f:
            f.write("=" * 80 + "\n")
            f.write(" " * 30 + "METEOR0X EXPORT\n")
            f.write("=" * 80 + "\n\n")
            
            if db["tools"]:
                f.write("### TOOLS ###\n\n")
                for name, desc in db["tools"].items():
                    f.write(f"Tool        : {name.upper()}\n")
                    f.write(f"Description : {desc}\n")
                    f.write("-" * 80 + "\n\n")
            
            if db["commands"]:
                f.write("### COMMANDS ###\n\n")
                for cmd, desc in db["commands"].items():
                    f.write(f"Command     : {cmd}\n")
                    f.write(f"Description : {desc}\n")
                    f.write("-" * 80 + "\n\n")
                
        print(f"[+] Success: Data exported successfully to '{export_path}'.")
    except Exception as e:
        print(f"[-] Error: Could not write to file. Details: {e}")

def main():
    parser = argparse.ArgumentParser(description="Meteor0x - Cybersecurity Tools and Commands Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Tool commands
    add_parser = subparsers.add_parser("add", help="Add a new tool")
    add_parser.add_argument("name", help="Tool name")
    add_parser.add_argument("desc", help="Tool description")
    
    show_parser = subparsers.add_parser("show", help="Show tool details")
    show_parser.add_argument("name", help="Tool name")
    
    edit_parser = subparsers.add_parser("edit", help="Edit tool description")
    edit_parser.add_argument("name", help="Tool name")
    edit_parser.add_argument("desc", help="New description")
    
    delete_parser = subparsers.add_parser("delete", help="Delete a tool")
    delete_parser.add_argument("name", help="Tool name")

    subparsers.add_parser("list", help="List all tools")

    # Command commands
    add_cmd_parser = subparsers.add_parser("add-cmd", help="Add a new command snippet")
    add_cmd_parser.add_argument("cmd", help="The exact command (enclose in quotes)")
    add_cmd_parser.add_argument("desc", help="Command description")
    
    show_cmd_parser = subparsers.add_parser("show-cmd", help="Show command details")
    show_cmd_parser.add_argument("cmd", help="The exact command")
    
    edit_cmd_parser = subparsers.add_parser("edit-cmd", help="Edit command description")
    edit_cmd_parser.add_argument("cmd", help="The exact command")
    edit_cmd_parser.add_argument("desc", help="New description")
    
    delete_cmd_parser = subparsers.add_parser("delete-cmd", help="Delete a command")
    delete_cmd_parser.add_argument("cmd", help="The exact command")

    subparsers.add_parser("list-cmd", help="List all stored commands")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export tools and commands to a text file")
    export_parser.add_argument("--file", default="meteor0x_export.txt", help="Output file name (optional)")

    args = parser.parse_args()

    if args.command == "add":
        add_tool(args.name, args.desc)
    elif args.command == "show":
        show_tool(args.name)
    elif args.command == "edit":
        edit_tool(args.name, args.desc)
    elif args.command == "delete":
        delete_tool(args.name)
    elif args.command == "list":
        list_tools()
    elif args.command == "add-cmd":
        add_cmd(args.cmd, args.desc)
    elif args.command == "show-cmd":
        show_cmd(args.cmd)
    elif args.command == "edit-cmd":
        edit_cmd(args.cmd, args.desc)
    elif args.command == "delete-cmd":
        delete_cmd(args.cmd)
    elif args.command == "list-cmd":
        list_cmds()
    elif args.command == "export":
        export_data(args.file)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
