import tkinter as tk
from tkinter import ttk, simpledialog
import os
import json

# Sample  buttons
json_data = """
{

    "docker System Purge": {
        "cmd": "docker system prune -f",
        "tab": "Docker"
    },
     "docker Builder Purge": {
        "cmd": "docker builder prune -f",
        "tab": "Docker"
    },
     "docker image Purge": {
        "cmd": "docker image prune -f",
        "tab": "Docker"
    },
    "docker system df": {
        "cmd": "docker system df",
        "tab": "Docker"
    },
    "docker info": {
        "cmd": "docker info",
        "tab": "Docker"
    },
    "docker ps": {
        "cmd": "docker ps",
        "tab": "Docker"
    },
    "docker images": {
        "cmd": "docker images",
        "tab": "Docker"
    },
    "docker network ls": {
        "cmd": "docker network ls",
        "tab": "Docker"
    },
    "docker volume ls": {
        "cmd": "docker volume ls",
        "tab": "Docker"
    },
    "docker stats": {
        "cmd": "docker stats",
        "tab": "Docker"
    },
    "docker version": {
        "cmd": "docker version",
        "tab": "Docker"
    },
    "docker help": {
        "cmd": "docker help",
        "tab": "Docker"
    },
    "dir": {
        "cmd": "dir <additionalparameter>",
        "tab": "CMD",
        "parameter":"<additionalparameter>"
    },
    "hack": {
        "cmd": "<additionalparameter>",
        "tab": "CMD",
        "parameter":"<additionalparameter>"
    },
    "dir /b /s": {
        "cmd": "dir /b /s",
        "tab": "CMD"
    },
    "npm list":{
        "cmd":"npm list",
        "tab":"npm"
    },
    "npm list global":{
        "cmd":"npm list -g",
        "tab":"npm"
    },
    "npm list all modules":{
        "cmd":"npm ls --all",
        "tab":"npm",
        "color":"#FFAA00"
    },
    "system Hibernate": {
        "cmd": "shutdown /h",
        "tab": "System",
        "color":"#ff7b00"
    },
    "dotnet new list": {
        "cmd": "dotnet new list",
        "tab": "dotnet",
        "color":"#007bff"
    },
    "dotnet --info": {
        "cmd": "dotnet --info",
        "tab": "dotnet",
        "color":"#007bff"
    },
    "create playwright project":{
        "cmd":"dotnet new nunit-playwright",
        "tab": "dotnet",
        "color":"#007bff"
    },
    "llama-bench":{
        "cmd":"llama-bench <gguf file>",
        "tab": "llama.cpp",
        "parameter":"<gguf file>"
    }
}
"""

hyphen = "\u2501" * 10
hyp2 = "\u2500" * 10
print(f"{hyphen}\u001b[38;2;{255};{255};{100}m useless is controlling this console \u001b[0m {hyphen}")

defaultButtonColor = "#373B77" #"#0859b6"
defaultBAckgroundColor = "#313244"
defaultFontColor = "#bec9ec"

# Parse the JSON string
data = json.loads(json_data)

def run_command(cmd_details):
    command = cmd_details["cmd"]

    if "parameter" in cmd_details:
        parameter = cmd_details["parameter"]
        input_value = ask_input("Input", f"Enter value for {parameter}: \t\t")
        
        if input_value is None:
            command = command.replace(parameter,"")
        elif len(input_value) > 0:
            command = command.replace(parameter, input_value)
        else:
            command = command.replace(parameter,"")

    #print(f'\u001b[38;2;{255};{255};{100}m')
    print(f"\u2699  Executing:[\u001b[38;2;{255};{255};{100}m {command} \u001b[0m ] {hyphen}")

    try:
        os.system(command)
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        print()

def render_button(parent_frame, command, cmd_details, row, column,bg):
    button = tk.Button(
        parent_frame,
        text=command,
        command=lambda: run_command(cmd_details),
        relief=tk.FLAT,
        borderwidth=2,
        bg=bg,#"#0859b6",
        fg="white",
        activebackground="#b41a1a",
        activeforeground="white",
        font=("Segoe UI", 10, "bold"),
        cursor="hand2",
        padx=4,
        pady=4,
        takefocus=0
    )
    button.grid(row=row, column=column, padx=6, pady=6, sticky="nsew")
    button.bind("<Enter>", lambda e, b=button: b.config(bg="#7eb41a", relief=tk.FLAT))
    button.bind("<Leave>", lambda e, b=button: b.config(bg=bg, relief=tk.FLAT))
    return button

def create_dynamic_buttons(notebook, data):
    max_columns = 5
    tab_frames = {}   # tab_name -> (frame, row_tracker)

    for command, details in data.items():
        tab_name = details.get("tab", "Default")
        but_color = details.get("color",defaultButtonColor)
        #print(but_color)

        if tab_name not in tab_frames:
            frame = tk.Frame(notebook, bg=defaultBAckgroundColor, padx=4, pady=4)
            notebook.add(frame, text=tab_name)
            for i in range(max_columns):
                frame.columnconfigure(i, weight=1)
            tab_frames[tab_name] = {"frame": frame, "row": 0, "col": 0}

        entry = tab_frames[tab_name]
        render_button(entry["frame"], command, details, entry["row"], entry["col"],but_color)
        entry["col"] += 1
        if entry["col"] >= max_columns:
            entry["col"] = 0
            entry["row"] += 1

root = tk.Tk()
root.title("useless")
root.geometry("800x600")
#root.configure(bg="#313244")

# Style the notebook tabs
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TNotebook",
    background=defaultBAckgroundColor,
    borderwidth=0,
    relief="flat",
)
style.configure(
    "TNotebook.Tab",
    background=defaultBAckgroundColor,
    foreground=defaultFontColor,
    padding=[14, 8],
    font=("Segoe UI", 10, "bold"),
    borderwidth=0,
    relief="flat",
    bordercolor="#313244",
    lightcolor="#313244",
    darkcolor="#313244",
)
style.map(
    "TNotebook.Tab",
    background=[("selected", "#7eb41a"), ("active", "#45475a")],
    foreground=[("selected", "white"), ("active", "#cdd6f4")],
    relief=[("selected", "flat")],
    padding=[("selected", [14, 4, 14, 4]), ("!selected", [14, 4, 14, 4])],
    expand=[("selected", [2, 2, 2, 0])],
    bordercolor=[("selected", "#313244"), ("!selected", "#313244")],
    lightcolor=[("selected", "#313244"), ("!selected", "#313244")],
    darkcolor=[("selected", "#313244"), ("!selected", "#313244")],
)
#style.configure("TFrame", background="#313244")

# Create a notebook (tabbed layout)
notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(expand=True, fill="both", padx=2, pady=6)

create_dynamic_buttons(notebook, data)

def ask_input(title, prompt):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.configure(bg=defaultBAckgroundColor)
    dialog.resizable(False, False)
    dialog.grab_set()   # 👈 blocks input to main window (like a modal)

    # center it
    dialog.geometry("360x150")
    dialog.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - 180
    y = root.winfo_y() + (root.winfo_height() // 2) - 75
    dialog.geometry(f"+{x}+{y}")

    result = [None]   # 👈 use list to capture value from inner function

    tk.Label(
        dialog, text=prompt,
        bg=defaultBAckgroundColor, fg="#ffffff",
        font=("Segoe UI", 10), pady=10
    ).pack()

    entry = tk.Entry(
        dialog,
        bg="#1e1e2e", fg="white",
        insertbackground="white",
        font=("Segoe UI", 10),
        relief=tk.FLAT,
        width=50
    )
    entry.pack(ipady=6, padx=20)
    entry.focus_set()

    btn_frame = tk.Frame(dialog, bg=defaultBAckgroundColor, pady=10)
    btn_frame.pack()

    def on_ok():
        result[0] = entry.get()
        dialog.destroy()

    def on_cancel():
        result[0] = None
        dialog.destroy()

    tk.Button(
        btn_frame, text="OK",
        bg="#7eb41a", fg="white",
        font=("Segoe UI", 9, "bold"),
        relief=tk.FLAT, padx=12, pady=4,
        cursor="hand2", takefocus=0,
        command=on_ok
    ).pack(side="left", padx=6)

    tk.Button(
        btn_frame, text="Cancel",
        bg="#b41a1a", fg="white",
        font=("Segoe UI", 9, "bold"),
        relief=tk.FLAT, padx=12, pady=4,
        cursor="hand2", takefocus=0,
        command=on_cancel
    ).pack(side="left", padx=6)

    entry.bind("<Return>", lambda e: on_ok())       # 👈 Enter = OK
    entry.bind("<Escape>", lambda e: on_cancel())   # 👈 Escape = Cancel

    dialog.wait_window()   # 👈 wait until dialog closes
    return result[0]

root.mainloop()

#print(f"{hyphen} [\u001b[38;2;{255};{255};{100}m This control is now given back to user \u001b[0m ]")
#print(f"{hyphen}{hyphen}{hyphen}{hyphen}")
