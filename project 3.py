from tkinter import *
from tkinter import messagebox

# Function to save details
def submit():
    bin_id = entry_bin.get()
    location = entry_location.get()
    waste = waste_type.get()
    level = fill_level.get()

    if bin_id == "" or location == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        output.config(
            text=f"Bin ID : {bin_id}\n"
                 f"Location : {location}\n"
                 f"Waste Type : {waste}\n"
                 f"Fill Level : {level}%\n\n"
                 "Status : Data Submitted Successfully!"
        )

        entry_bin.delete(0, END)
        entry_location.delete(0, END)
        fill_level.set(0)

# Main Window
root = Tk()
root.title("Smart Waste Management System")
root.geometry("500x500")
root.configure(bg="lightgreen")

title = Label(root,
              text="SMART WASTE MANAGEMENT SYSTEM",
              font=("Arial", 16, "bold"),
              bg="green",
              fg="white")
title.pack(fill=X)

Label(root, text="Bin ID", bg="lightgreen", font=("Arial", 12)).pack(pady=5)
entry_bin = Entry(root, width=30)
entry_bin.pack()

Label(root, text="Location", bg="lightgreen", font=("Arial", 12)).pack(pady=5)
entry_location = Entry(root, width=30)
entry_location.pack()

Label(root, text="Waste Type", bg="lightgreen", font=("Arial", 12)).pack(pady=5)

waste_type = StringVar()
waste_type.set("Dry Waste")

OptionMenu(root, waste_type,
           "Dry Waste",
           "Wet Waste",
           "Plastic",
           "Metal",
           "Glass").pack()

Label(root, text="Fill Level (%)", bg="lightgreen", font=("Arial", 12)).pack(pady=5)

fill_level = IntVar()
Scale(root,
      from_=0,
      to=100,
      orient=HORIZONTAL,
      variable=fill_level,
      length=250).pack()

Button(root,
       text="Submit",
       bg="blue",
       fg="white",
       font=("Arial", 12),
       command=submit).pack(pady=15)

output = Label(root,
               text="",
               bg="lightgreen",
               font=("Arial", 11),
               justify=LEFT)
output.pack()

root.mainloop()
