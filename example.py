import customtkinter as ctk
from samsung_widgets import SamsungToggle, SamsungSlider, SamsungEntry, SamsungButton, SamsungCheckbox

# ---------- App Setup ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("400x700")
root.title("Samsung Widgets Full Demo")

frame = ctk.CTkFrame(root, width=380, height=680, fg_color="#F9F9F9")
frame.pack(padx=10, pady=10)
frame.pack_propagate(False)

# ---------- SamsungEntry ----------
entry_label = ctk.CTkLabel(frame, text="Entry Value:", font=("Nunito Sans", 16, "bold"))
entry_label.pack(pady=(10, 0))

entry = SamsungEntry(frame, placeholder="Enter your text...")
entry.pack(pady=5)

def update_entry_label():
    entry_label.configure(text=f"Entry Value: {entry.get()}")

entry_button = SamsungButton(frame, text="Update Entry Label", command=update_entry_label)
entry_button.pack(pady=5)

# ---------- SamsungToggle ----------
toggle_label = ctk.CTkLabel(frame, text="Toggle State: False", font=("Nunito Sans", 16, "bold"))
toggle_label.pack(pady=(20, 0))

def toggle_action(state):
    toggle_label.configure(text=f"Toggle State: {state}")

toggle = SamsungToggle(frame, command=toggle_action)
toggle.pack(pady=5)

# ---------- SamsungSlider ----------
slider_label = ctk.CTkLabel(frame, text="Slider Value: 50", font=("Nunito Sans", 16, "bold"))
slider_label.pack(pady=(20, 0))

def slider_action(value):
    slider_label.configure(text=f"Slider Value: {int(value)}")

slider = SamsungSlider(frame, from_=0, to=100, command=slider_action, initial=50)
slider.pack(pady=5)

# ---------- SamsungCheckbox ----------
checkbox_label = ctk.CTkLabel(frame, text="Checkbox State: False", font=("Nunito Sans", 16, "bold"))
checkbox_label.pack(pady=(20, 0))

def checkbox_action():
    if checkbox.get() == 0:
        checkbox_label.configure(text="Checkbox State: False")
    else:
        checkbox_label.configure(text="Checkbox State: True")

checkbox = SamsungCheckbox(frame, text="Enable Notifications", command=checkbox_action)
checkbox.pack(pady=5)

# ---------- SamsungButton ----------
def button_click():
    print("Samsung Button clicked!")

button = SamsungButton(frame, text="Click Me", command=button_click)
button.pack(pady=(30, 10))

# ---------- Run App ----------
root.mainloop()
