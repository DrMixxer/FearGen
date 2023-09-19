import customtkinter
import random
import string
import os
import hashlib

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("256x256")
app.title("FearGen B3")

# Define a global variable to keep track of the generated serial keys
generated_serials = set()

# Define a global variable for hashing option
hashing_option_var = None

def button_callback():
    prefix = entry_1.get()
    ammount = entry_2.get()
    path = entry_3.get()
    hashing_option = hashing_option_var.get()

    try:
        ammount = int(ammount)
    except ValueError:
        ErrorWindow.display_error("ERROR 1: Invalid amount")
        return

    if ammount > 9999:
        ErrorWindow.display_error("ERROR 1: Too many keys")
        return

    if not path:
        path = "Generated"  # Set a default path if it's empty

    # Create the folder if it doesn't exist
    os.makedirs(path, exist_ok=True)

    serials = generate_serials(prefix, ammount, hashing_option)

    try:
        with open(os.path.join(path, f"Serials_Generated_{hashing_option}.txt"), "w") as file:
            for serial in serials:
                file.write(serial + "\n")
    except FileNotFoundError:
        ErrorWindow.display_error(f"ERROR 1: Invalid path - {path}")
        return

    app.quit()

def generate_serials(prefix, ammount, hashing_option):
    serials = set()
    while len(serials) < ammount:
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        serial = prefix + random_chars

        if hashing_option == "SHA-256":
            hashed_serial = hashlib.sha256(serial.encode()).hexdigest()
            serials.add(f"{hashed_serial}-{serial}")
        elif hashing_option == "SHA-512":
            hashed_serial = hashlib.sha512(serial.encode()).hexdigest()
            serials.add(f"{hashed_serial}-{serial}")
        else:
            serials.add(serial)

        generated_serials.add(serial)
    return serials

def open_properties_window():
    global hashing_option_var  # Declare it as a global variable
    properties_window = customtkinter.CTk()
    properties_window.geometry("300x200")
    properties_window.title("Properties")

    # Create a custom checkbox for "Hashing"
    hashing_option_var = customtkinter.StringVar()
    hashing_checkbox = customtkinter.CTkCheckBox(master=properties_window, text="Hashing", variable=hashing_option_var)
    hashing_checkbox.pack(pady=10, padx=10)

    # Create a dropdown (OptionMenu) for hashing options
    hashing_options = ["NONE", "SHA-256", "SHA-512"]
    hashing_option_var.set("NONE")  # Default option
    hashing_dropdown = customtkinter.CTkOptionMenu(master=properties_window, values=hashing_options, variable=hashing_option_var)
    hashing_dropdown.pack(pady=10, padx=10)

    def apply_settings():
        properties_window.destroy()

    apply_button = customtkinter.CTkButton(master=properties_window, command=apply_settings, text="Apply")
    apply_button.pack(pady=10, padx=10)

    properties_window.mainloop()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="FearGen B3")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Prefix: ")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Amount: ")
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Path: ")
entry_3.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Generate")
button_1.pack(pady=10, padx=10)

settings_button = customtkinter.CTkButton(master=frame_1, command=open_properties_window, text="Settings")
settings_button.pack(pady=10, padx=10)

app.mainloop()
