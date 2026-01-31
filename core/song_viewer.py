
import tkinter as tk
import random
import pandas as pd

# ----------------- STATE -----------------
is_typing = False
current_after_id = None
construction_frame = 0

# ----------------- LOAD CSV -----------------
df = pd.read_csv(
    "database/ListeningSession.csv",
    sep=None,
    engine="python",
    usecols=[1, 2]
)

music_dict = {
    int(k): str(v).replace("\\n", "\n").replace("\\r\\n", "\n").replace("\\r", "\n")
    for k, v in zip(df.iloc[:, 0], df.iloc[:, 1])
    if pd.notna(k) and pd.notna(v)
}

# ----------------- TYPEWRITER -----------------
def sys_loop(items, label, item_idx=0, char_idx=0):
    # Define the typewriter style print here

    global is_typing, current_after_id

    if item_idx >= len(items):
        is_typing = False
        current_after_id = None
        entry.focus_set()
        return

    item = items[item_idx]

    # Grab the text from the database

    if char_idx < len(item):
        # Enable text widget, insert character, auto-scroll, then disable
        label.config(state="normal")
        label.insert("end", item[char_idx])
        label.see("end")  # Auto-scroll to bottom
        label.config(state="disabled")

        delay = random.randint(80, 160)
        current_after_id = label.after(delay, sys_loop, items, label, item_idx, char_idx + 1)
    else:
        current_after_id = label.after(300, sys_loop, items, label, item_idx + 1, 0)

# ----------------- INPUT HANDLER -----------------
def add_new_text(event=None):
    # Enter sys_loop() and print the new value, when the key is entered

    global is_typing, current_after_id

    # Cancel any ongoing typewriter animation
    if current_after_id is not None:
        label.after_cancel(current_after_id)
        current_after_id = None

    raw = entry.get().strip()
    if not raw:
        return

    try:
        key = int(raw)
    except ValueError:
        entry.delete(0, tk.END)
        label.config(state="normal")
        label.delete("1.0", "end")
        label.config(state="disabled")
        sys_loop(["Invalid key\n\n"], label)
        return

    is_typing = True
    entry.delete(0, tk.END)
    label.config(state="normal")
    label.delete("1.0", "end")
    label.config(state="disabled")

    if key in music_dict:
        sys_loop([music_dict[key] + "\n\n"], label)
    else:
        sys_loop([f"Key {key} not found.\n\n"], label)


# ----------------- CONSTRUCTION ANIMATION -----------------
def animate_construction():
    global construction_frame

    frames = [
        """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏗️  VIDEO PLAYER UNDER CONSTRUCTION  🏗️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


╔════════════════════════════════════╗
║                                    ║
║      ⚠️  UNDER CONSTRUCTION  ⚠️     ║
║                                    ║
╚════════════════════════════════════╝


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Working hard... ⚙️""",
        """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏗️  VIDEO PLAYER UNDER CONSTRUCTION  🏗️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


╔════════════════════════════════════╗
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░  ⚠️  UNDER CONSTRUCTION  ⚠️  ░░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
╚════════════════════════════════════╝


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Building... 🔨""",
        """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏗️  VIDEO PLAYER UNDER CONSTRUCTION  🏗️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


╔════════════════════════════════════╗
║                                    ║
║      ⚠️  UNDER CONSTRUCTION  ⚠️     ║
║                                    ║
╚════════════════════════════════════╝


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Almost there... 🔧""",
        """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏗️  VIDEO PLAYER UNDER CONSTRUCTION  🏗️
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


╔════════════════════════════════════╗
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░  ⚠️  UNDER CONSTRUCTION  ⚠️  ░░░░║
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
╚════════════════════════════════════╝


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
In progress... ⚡"""
    ]

    video_placeholder.config(text=frames[construction_frame])
    construction_frame = (construction_frame + 1) % len(frames)
    video_placeholder.after(500, animate_construction)


# Define the basic design of the gui and the entry field for the keys
root = tk.Tk()
root.title("Dictionary Terminal")
root.configure(bg="black")

# Maximize the window (same as double-clicking the title bar)
root.state('zoomed')

# Get window dimensions for text wrapping
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()

# ----------------- TOP FRAME (Video Player) -----------------
top_frame = tk.Frame(root, bg="black", height=window_height // 2)
top_frame.pack(side="top", fill="both", expand=False)
top_frame.pack_propagate(False)  # Prevent frame from resizing to fit content

# Placeholder for video player (to be added later)
video_placeholder = tk.Label(
    top_frame,
    text="Video Player\n(Coming Soon)",
    fg="#666666",
    bg="black",
    font=("Courier New", 16),
    justify="center",
    anchor="center"
)
video_placeholder.pack(fill="both", expand=True)

# ----------------- BOTTOM FRAME (Text Display) -----------------
bottom_frame = tk.Frame(root, bg="black")
bottom_frame.pack(side="bottom", fill="both", expand=True)

# Pack entry field first to ensure it's always visible at the bottom
entry = tk.Entry(
    bottom_frame,
    font=("Courier New", 24),
    bg="black",
    fg="green",
    insertbackground="green"
)
entry.pack(side="bottom", fill="x", padx=20, pady=(0, 20))
entry.bind("<Return>", add_new_text)

# Use Text widget instead of Label for scrolling capability
label = tk.Text(
    bottom_frame,
    fg="#eaa441",
    bg="black",
    font=("Courier New", 24),
    wrap="word",
    state="disabled",
    relief="flat",
    borderwidth=0
)
label.pack(padx=20, pady=20, fill="both", expand=True)

entry.focus_set()

def main():
    # Start construction animation
    animate_construction()

    first_key = min(music_dict.keys())
    sys_loop([music_dict[first_key] + "\n\n"], label)
    root.mainloop()
