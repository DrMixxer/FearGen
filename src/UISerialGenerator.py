import customtkinter
import random
import string
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("256x256")
app.title("FearGen B2")

# Define a global variable to keep track of the generated serial keys
generated_serials = set()

def button_callback():
    prefix = entry_1.get()
    ammount = entry_2.get()
    path = entry_3.get()

    try:
        ammount = int(ammount)
    except ValueError:
        ErrorWindow.display_error("ERROR 1: Invalid amount")
        return

    if ammount > 9999:
        ErrorWindow.display_error("ERROR 1: Too many keys")
        return

    serials = generate_serials(prefix, ammount)

    try:
        with open(os.path.join(path, "Serials_Generated.txt"), "w") as file:
            for serial in serials:
                file.write(serial + "\n")
    except FileNotFoundError:
        errors.display_error("ERROR 1: Invalid path")
        return

    app.quit()

def generate_serials(prefix, ammount):
    serials = set()
    while len(serials) < ammount:
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        serial = prefix + random_chars
        if serial not in generated_serials:
            serials.add(serial)
            generated_serials.add(serial)
    return serials

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="FearGen B2")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Prefix: ")
entry_1.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Amount: ")
entry_2.pack(pady=10, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Path: ")
entry_3.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Generate")
button_1.pack(pady=10, padx=10)

app.mainloop()
