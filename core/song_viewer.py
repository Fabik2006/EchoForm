
import tkinter as tk
import random
import pandas as pd

# ----------------- STATE -----------------
is_typing = False

# ----------------- LOAD CSV -----------------
df = pd.read_csv(
    "Database_Path",
    sep=None,
    engine="python",
    usecols=[1, 2]
)

music_dict = {
    int(k): str(v).replace("\\n", "\n")
    for k, v in zip(df.iloc[:, 0], df.iloc[:, 1])
    if pd.notna(k) and pd.notna(v)
}

# ----------------- TYPEWRITER -----------------
def sys_loop(items, label, item_idx=0, char_idx=0):
    # Define the typewriter style print here

    global is_typing

    # This if-statement fails currently -> During printing
    # the entry should be blocked but it is not.
    
    if item_idx >= len(items):
        is_typing = False
        entry.config(state="normal")
        entry.focus_set()
        return

    item = items[item_idx]


    # Grab the text from the database
    
    if char_idx < len(item):
        label.config(text=label.cget("text") + item[char_idx])
        delay = random.randint(80, 160)
        label.after(delay, sys_loop, items, label, item_idx, char_idx + 1)
    else:
        label.after(300, sys_loop, items, label, item_idx + 1, 0)

# ----------------- INPUT HANDLER -----------------
def add_new_text(event=None):
    # Enter sys_loop() and print the new value, when the key is entered
    
    global is_typing

    if is_typing:
        return

    raw = entry.get().strip()
    if not raw:
        return

    try:
        key = int(raw)
    except ValueError:
        sys_loop(["Invalid key\n\n"], label)
        return

    is_typing = True
    entry.config(state="disabled")
    entry.delete(0, tk.END)
    label.config(text="")

    if key in music_dict:
        sys_loop([music_dict[key] + "\n\n"], label)
    else:
        sys_loop([f"Key {key} not found.\n\n"], label)


# Define the basic design of the gui and the entry field for the keys
root = tk.Tk()
root.title("Dictionary Terminal")
root.geometry("1200x800")
root.configure(bg="black")

label = tk.Label(
    root,
    text="",
    fg="#eaa441",
    bg="black",
    font=("Courier New", 24),
    wraplength=1150,
    justify="left",
    anchor="nw"
)
label.pack(padx=20, pady=20, fill="both", expand=True)

entry = tk.Entry(
    root,
    font=("Courier New", 24),
    bg="black",
    fg="green",
    insertbackground="green"
)
entry.pack(fill="x", padx=20, pady=(0, 20))
entry.bind("<Return>", add_new_text)
entry.focus_set()

def main():
    
    first_key = min(music_dict.keys())
    sys_loop([music_dict[first_key] + "\n\n"], label)
    root.mainloop()
