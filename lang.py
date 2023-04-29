from tkinter import *
from langdetect import detect
from langcodes import *

root = Tk()
root.title("Yarden's tiny language detector")
root.geometry("640x460")

# FUNCTIONS


def identify_lang():
    # Make sure text area is not empty
    if txt_area.compare("end-1c", "==", "1.0"):
        result_label.config(text="Please enter text")
    # Detect language and display it's name
    else:
        lang_code = detect(txt_area.get(1.0, END))
        identified_lang = Language.make(language=lang_code).display_name()
        result_label.config(text=f"This text is in {identified_lang}.")


# WIDGETS

txt_area = Text(root, height=10, width=50, font=("TkDefaultFont", 24))
txt_area.pack(pady=20)

submit_btn = Button(root, text="Identify language", command=identify_lang, font=("TkDefaultFont", 24))
submit_btn.pack(pady=10)

result_label = Label(root, font=("TkDefaultFont", 24))
result_label.pack(pady=10)

root.mainloop()