import tkinter as tk

class ErrorWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Error")
        self.root.geometry("300x100")
        self.error_label = tk.Label(self.root, text="", fg="red")
        self.error_label.pack(pady=20)
        self.ok_button = tk.Button(self.root, text="OK", command=self.close)
        self.ok_button.pack()
    
    def display_error(self, error_message):
        self.error_label.config(text=error_message)
        self.root.mainloop()
    
    def close(self):
        self.root.destroy()

errors = ErrorWindow()
