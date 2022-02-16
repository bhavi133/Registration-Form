import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

window = tk.Tk()
window.title("GUI Form")
window.geometry("500x800")

# label frame

label_frame = ttk.LabelFrame(window, text="")
label_frame.pack(side=tk.TOP, padx=40, pady=4)

# labels

title_label1 = ttk.Label(label_frame, text="PRICING REQUEST")
title_label1.grid(row=0, column=0, padx=30, pady=2)

title_label2 = ttk.Label(label_frame, text="Data Science Starts Here", font=10)
title_label2.grid(row=1, column=0, padx=30, pady=2)

title_label3 = ttk.Label(label_frame, text="Fill out the form below and our sales team will be in touch.")
title_label3.grid(row=2, column=0, padx=30, pady=2)

fname_label = ttk.Label(label_frame, text="First Name : *")
fname_label.grid(row=3, column=0, padx=30, pady=2, sticky=tk.W)

lname_label = ttk.Label(label_frame, text="Last Name : *")
lname_label.grid(row=5, column=0, padx=30, pady=2, sticky=tk.W)

email_label = ttk.Label(label_frame, text="Email Address : *")
email_label.grid(row=7, column=0, padx=30, pady=2, sticky=tk.W)

phone_label = ttk.Label(label_frame, text="Phone Number : *")
phone_label.grid(row=9, column=0, padx=30, pady=2, sticky=tk.W)

company_label = ttk.Label(label_frame, text="Company Name : *")
company_label.grid(row=11, column=0, padx=30, pady=2, sticky=tk.W)

companysize_label = ttk.Label(label_frame, text="Company Size : *")
companysize_label.grid(row=13, column=0, padx=30, pady=2, sticky=tk.W)

country_label = ttk.Label(label_frame, text="Country : *")
country_label.grid(row=15, column=0, padx=30, pady=2, sticky=tk.W)

role_label = ttk.Label(label_frame, text="Role : *")
role_label.grid(row=17, column=0, padx=30, pady=2, sticky=tk.W)

other_label = ttk.Label(label_frame, text="Other Comments : *")
other_label.grid(row=19, column=0, padx=30, pady=2, sticky=tk.W)

# entry box

fname_var = tk.StringVar()
fname_entry = ttk.Entry(label_frame, width=53, textvariable=fname_var)
fname_entry.grid(row=4, columnspan=2, padx=40, pady=2)

lname_var = tk.StringVar()
lname_entry = ttk.Entry(label_frame, width=53, textvariable=lname_var)
lname_entry.grid(row=6, columnspan=2, padx=40, pady=2)

email_var = tk.StringVar()
email_entry = ttk.Entry(label_frame, width=53, textvariable=email_var)
email_entry.grid(row=8, columnspan=2, padx=40, pady=2)

phone_var = tk.StringVar()
phone_entry = ttk.Entry(label_frame, width=53, textvariable=phone_var)
phone_entry.grid(row=10, columnspan=2, padx=40, pady=2)

company_var = tk.StringVar()
company_entry = ttk.Entry(label_frame, width=53, textvariable=company_var)
company_entry.grid(row=12, columnspan=2, padx=40, pady=2)

other_var = tk.StringVar()
other_entry = ttk.Entry(label_frame, width=53, textvariable=other_var)
other_entry.grid(row=20, columnspan=2, padx=40, pady=2)

# combobox

companysize_var = tk.StringVar()
companysize_entry = ttk.Combobox(label_frame, width=50, textvariable=companysize_var, state="readonly")
companysize_entry["values"] = ("1 - 200", "201 - 1000", "1001 - 3000", "3000+")
companysize_entry.set("Select...")
companysize_entry.grid(row=14, columnspan=2, padx=40, pady=2)

window.mainloop()
