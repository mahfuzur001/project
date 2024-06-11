import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Function to perform the translation
def translate_text():
    try:
        source_text = text_input.get("1.0", tk.END).strip()
        src_lang = source_lang_var.get()
        dest_lang = target_lang_var.get()
        
        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate")
            return
        
        translated = translator.translate(source_text, src=src_lang, dest=dest_lang)
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated.text)
        text_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Translator")
root.geometry("750x400")
root.configure(bg="black")  # Set background color to black

# Set window icon
root.iconphoto(True, tk.PhotoImage(file="google.jpg"))

# Source Language Label and Dropdown
source_lang_var = tk.StringVar(value="en")
source_lang_label = ttk.Label(root, text="Source Language:", foreground="white", background="black")
source_lang_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
source_lang_menu = ttk.Combobox(root, textvariable=source_lang_var, values=list(LANGUAGES.values()))
source_lang_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Target Language Label and Dropdown
target_lang_var = tk.StringVar(value="bn")
target_lang_label = ttk.Label(root, text="Target Language:", foreground="white", background="black")
target_lang_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
target_lang_menu = ttk.Combobox(root, textvariable=target_lang_var, values=list(LANGUAGES.values()))
target_lang_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Source Text Label
source_label = ttk.Label(root, text="Source Text:", foreground="white", background="black")
source_label.grid(row=2, column=0, padx=5, pady=10, sticky="w")

# Translated Text Label
translated_label = ttk.Label(root, text="Translated Text:", foreground="white", background="black")
translated_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Source Text
text_input = tk.Text(root, height=10, width=40, bg="blue", fg="black", font=("Arial", 12), relief="solid", bd=2)  # Set background color, font color, font family, and border
text_input.grid(row=3, column=0, padx=5, pady=5)

# Translated Text
text_output = tk.Text(root, height=10, width=40, state=tk.DISABLED, bg="blue", fg="black", font=("Arial", 12), relief="solid", bd=2)  # Set background color, font color, font family, and border
text_output.grid(row=3, column=1, padx=5, pady=20)

# Translate Button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=20)
# Create a style object
style = ttk.Style()

# Configure the style with a custom background color
style.configure('Custom.TButton', background='blue')

# Run the application
root.mainloop()
