# 1. Set up your environment

pip install customtkinter

or

pip install customtkinter --break-system-packages



# 2. Basic imports and setup

import customtkinter as ctk
from samsung_widgets import SamsungToggle, SamsungSlider, SamsungEntry, SamsungButton


ctk.set_appearance_mode("light")  # Light mode
ctk.set_default_color_theme("blue")  # Samsung-like blue accents

root = ctk.CTk()
root.geometry("400x500")
root.title("Samsung Widgets Demo")



# 3. Add a SamsungEntry(Text Input)

entry = SamsungEntry(root, placeholder="Enter your name...")
entry.pack(pady=20)


def show_entry_text():
    print("Text in entry:", entry.get())

button_entry = SamsungButton(root, text="Show Text", command=show_entry_text)
button_entry.pack(pady=10)



# 4. Add a SamsungToggle

def toggle_action(state):
    print("Toggle state:", state)

toggle = SamsungToggle(root, command=toggle_action)
toggle.pack(pady=20)



# 5. Add a SamsungSlider

def slider_action(value):
    print("Slider value:", int(value))

slider = SamsungSlider(root, from_=0, to=100, command=slider_action, initial=50)
slider.pack(pady=20)



# 6. Add a SamsungButton

def button_click():
    print("Button clicked!")

button = SamsungButton(root, text="Click Me", command=button_click)
button.pack(pady=20)



# 7. Runthe application

root.mainloop()



# Tips

entry.get()       # Text input
toggle.state      # True/False
slider.value      # Current slider value
