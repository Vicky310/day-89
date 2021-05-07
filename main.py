from tkinter import *

GREEN = "#d8f8b7"
BLACK = "#1b1a17"
FONT_NAME = "Courier"
timer = None
passed = 0


# ---------------- FUNCTIONALITY SETUP ---------------- #
def check_entry(previous_entry):
    global passed, timer
    first_entry = text_area.get("1.0", END).split("\n")[0]
    if len(first_entry) - len(previous_entry) == 0:
        passed += 1
        if passed > 0 and passed % 5 == 0:
            text_area.delete("1.0", END)
            passed = 0
            timer = window.after(1000, check_entry, "")
        else:
            timer = window.after(1000, check_entry, first_entry)
    else:
        passed = 0
        timer = window.after(1000, check_entry, first_entry)


def clean_text():
    text_area.delete("1.0", END)


# ------------------ UI --------------------- #
window = Tk()
window.minsize(width=500, height=500)
window.config(bg=GREEN, padx=20, pady=20)

title_label = Label(text="Welcome to the Disappearing Text Editor", font=(FONT_NAME, 15), pady=10, bg=GREEN)
title_label.grid(column=0, row=0, columnspan=2)

instructions = Label(text="Instructions: \n1. You can write anything you want. It doesn't even has to be grammati"
                          "cally correct.\n2. You must not stop writing. If you stop writing for 5 seconds than all"
                          "of your work will disappear.", bg=GREEN, fg=BLACK, pady=10)
instructions.grid(column=0, row=1, columnspan=2)

text_area = Text(height=10, width=50, font=("Times New Roman", 12), fg=BLACK)
text_area.grid(column=0, row=2, columnspan=2)

check_entry("")
window.mainloop()