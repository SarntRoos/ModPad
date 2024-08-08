import customtkinter
from tkinter import filedialog

# Set the appearance mode to dark
customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("ModPad")
        self.geometry("600x400")
        self.grid_rowconfigure(0, weight=5)
        self.grid_columnconfigure(0, weight=5)

        # Create a CTkTextbox with a dark theme
        self.textbox = customtkinter.CTkTextbox(
            master=self,  # Attach the textbox directly to the main window
            width=400,
            height=200,
            corner_radius=1,
            fg_color="#242424",  # Dark grey background color for the textbox
            text_color="white"   # White text color for the textbox
        )

        self.textbox.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")  # Use grid for layout
        self.textbox.insert("0.0", "Welcome to ModPad!")

        # Create a frame to hold the buttons
        self.button_frame = customtkinter.CTkFrame(master=self)
        self.button_frame.grid(row=1, column=0, padx=8, pady=8, sticky="ew")

        # Create a save button
        self.save_button = customtkinter.CTkButton(
            master=self.button_frame,  # Attach to the button frame
            text="Save",
            command=self.save_file
        )
        self.save_button.pack(side="left", expand=True, fill="x", padx=5)

        # Create an open button
        self.open_button = customtkinter.CTkButton(
            master=self.button_frame,  # Attach to the button frame
            text="Open",
            command=self.open_file
        )
        self.open_button.pack(side="left", expand=True, fill="x", padx=5)

    def save_file(self):
        """Method to save the content of the textbox to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"),
                                                            ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textbox.get("0.0", "end"))

    def open_file(self):
        """Method to open a file and display its contents in the textbox."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),
                                                          ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox.delete("0.0", "end")  # Clear existing text
                self.textbox.insert("0.0", content)  # Insert new content

if __name__ == "__main__":
    app = App()
    app.mainloop()
