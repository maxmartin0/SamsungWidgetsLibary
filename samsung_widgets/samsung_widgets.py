# samsung_widgets.py
import customtkinter as ctk

# ----------------------------
# Frame
# ----------------------------
class SamsungFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color="#F9F9F9",
            corner_radius=12,
            **kwargs
        )

# ----------------------------
# Label
# ----------------------------
class SamsungLabel(ctk.CTkLabel):
    def __init__(self, master, text="", **kwargs):
        super().__init__(
            master,
            text=text,
            font=("Nunito Sans", 16, "bold"),
            text_color="#333333",
            **kwargs
        )

# ----------------------------
# Button
# ----------------------------
class SamsungButton(ctk.CTkButton):
    def __init__(self, master, text="", command=None, **kwargs):
        super().__init__(
            master,
            text=text,
            font=("Nunito Sans", 16, "bold"),
            fg_color="#0066FF",
            hover_color="#0052CC",
            text_color="white",
            corner_radius=20,
            command=command,
            **kwargs
        )

# ----------------------------
# Entry
# ----------------------------
class SamsungEntry(ctk.CTkEntry):
    def __init__(self, master, width=250, height=40, placeholder="", **kwargs):
        super().__init__(
            master,
            width=width,
            height=height,
            fg_color="#F9F9F9",
            border_width=1,
            border_color="#CCCCCC",
            corner_radius=8,
            font=("Nunito Sans", 16, "bold"),
            placeholder_text=placeholder,
            placeholder_text_color="#AAAAAA",
            **kwargs
        )

# ----------------------------
# Checkbox
# ----------------------------
class SamsungCheckbox(ctk.CTkCheckBox):
    def __init__(self, master, text="", **kwargs):
        super().__init__(
            master,
            text=text,
            fg_color="#007AFF",       # Background color
            checkmark_color="#F9F9F9", # Blue tick like Samsung
            text_color="#000000",
            font=("Nunito Sans", 16, "bold"),
            corner_radius=5,
            **kwargs
        )

# ----------------------------
# Slider
# ----------------------------
class SamsungSlider(ctk.CTkFrame):
    def __init__(self, master, from_=0, to=100, width=250, height=30, command=None, initial=0, **kwargs):
        super().__init__(master, width=width, height=height, fg_color="#F9F9F9", **kwargs)
        self.from_ = from_
        self.to = to
        self.width = width
        self.height = height
        self.command = command
        self.value = initial

        self.track_height = 6
        self.knob_radius = height // 2 - 3

        # Colors
        self.track_color = "#E5E5E5"
        self.progress_color = "#0066FF"
        self.knob_color = "white"
        self.knob_outline = "#CCCCCC"

        # Canvas
        self.canvas = ctk.CTkCanvas(self, width=width, height=height, highlightthickness=0, bg="#F9F9F9")
        self.canvas.pack()
        self.draw_slider()

        # Bind dragging
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.drag)

    def draw_slider(self):
        self.canvas.delete("all")
        # Track
        track_y = self.height // 2
        self.canvas.create_line(
            self.knob_radius, track_y, self.width - self.knob_radius, track_y,
            fill=self.track_color, width=self.track_height, capstyle="round"
        )

        # Progress
        knob_x = self.value_to_x(self.value)
        self.canvas.create_line(
            self.knob_radius, track_y, knob_x, track_y,
            fill=self.progress_color, width=self.track_height, capstyle="round"
        )

        # Knob (circle with outline)
        self.canvas.create_oval(
            knob_x - self.knob_radius, track_y - self.knob_radius,
            knob_x + self.knob_radius, track_y + self.knob_radius,
            fill=self.knob_color, outline=self.knob_outline, width=1
        )

    def value_to_x(self, value):
        ratio = (value - self.from_) / (self.to - self.from_)
        return self.knob_radius + ratio * (self.width - 2 * self.knob_radius)

    def x_to_value(self, x):
        ratio = min(max((x - self.knob_radius) / (self.width - 2 * self.knob_radius), 0), 1)
        return self.from_ + ratio * (self.to - self.from_)

    def click(self, event):
        self.value = self.x_to_value(event.x)
        self.draw_slider()
        if self.command:
            self.command(self.value)

    def drag(self, event):
        self.value = self.x_to_value(event.x)
        self.draw_slider()
        if self.command:
            self.command(self.value)



# ----------------------------
# Toggle
# ----------------------------
class SamsungToggle(ctk.CTkFrame):
    def __init__(self, master, width=50, height=25, command=None, initial=False, text=None, **kwargs):
        super().__init__(master, width=width, height=height, fg_color="#F9F9F9", **kwargs)
        self.command = command
        self.state = initial
        self.width = width
        self.height = height

        self.bg_off = "#E5E5E5"
        self.bg_on = "#0066FF"
        self.knob_color = "white"

        # Optional label
        if text:
            self.label = ctk.CTkLabel(self, text=text, font=("Nunito Sans", 16, "bold"), text_color="#333333")
            self.label.pack(side="left", padx=(0,10))

        # Canvas for drawing
        self.canvas = ctk.CTkCanvas(self, width=width, height=height, highlightthickness=0, bg="#F9F9F9")
        self.canvas.pack(side="left")
        self.knob_radius = height // 2 - 3

        self.draw_toggle()

        # Bind click
        self.canvas.bind("<Button-1>", self.toggle)
        self.bind("<Button-1>", self.toggle)

    def draw_toggle(self):
        self.canvas.delete("all")
        h = self.height
        w = self.width
        r = h // 2
        track_color = self.bg_on if self.state else self.bg_off

        # Track
        self.canvas.create_oval(0, 0, h, h, fill=track_color, outline=track_color)
        self.canvas.create_oval(w-h, 0, w, h, fill=track_color, outline=track_color)
        self.canvas.create_rectangle(r, 0, w-r, h, fill=track_color, outline=track_color)

        # Knob
        knob_x = w - r if self.state else r
        knob_y = h // 2
        self.canvas.create_oval(
            knob_x - self.knob_radius, knob_y - self.knob_radius,
            knob_x + self.knob_radius, knob_y + self.knob_radius,
            fill=self.knob_color, outline="#CCCCCC", width=1
        )

    def toggle(self, event=None):
        self.state = not self.state
        self.draw_toggle()
        if self.command:
            self.command(self.state)
