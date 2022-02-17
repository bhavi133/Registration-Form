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

country_var = tk.StringVar()
country_entry = ttk.Combobox(label_frame, width=50, textvariable=country_var, state="readonly")
country_entry["values"] = (
    "United States", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Anguilla", "Antigua & Barbuda", "Argentina",
    "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia & Herzegovina", "Botswana", "Brazil", "Brunei Darussalam",
    "Bulgaria", "Burkina Faso", "Myanmar/Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde",
    "Cayman Islands", "Central African Republic", "Chad", "Chile", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia",
    "Cyprus", "Czech Republic", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France",
    "French Guiana", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Great Britain", "Greece", "Grenada", "Guadeloupe",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
    "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast (Cote d'Ivoire)", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kenya", "Kosovo", "Kuwait", "Kyrgyz Republic (Kyrgyzstan)", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Republic of Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Moldova, Republic of", "Monaco",
    "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pacific Islands", "Pakistan", "Panama", "Papua New Guinea",
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia",
    "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent's & Grenadines", "Samoa", "Sao Tome and Principe",
    "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovak Republic (Slovakia)", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "Korea, Republic of (South Korea)", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
    "Timor Leste", "Togo", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks & Caicos Islands", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam",
    "Virgin Islands (UK)", "Virgin Islands (US)", "Yemen", "Zambia", "Zimbabwe")

country_entry.set("Select...")
country_entry.grid(row=16, columnspan=2, padx=40, pady=2)

role_var = tk.StringVar()
role_entry = ttk.Combobox(label_frame, width=50, textvariable=role_var, state="readonly")
role_entry["values"] = (
    "Business Analyst", "Consultant", "Data Engineer", "Data Scientist", "Executive", "IT Professional",
    "Machine Learning Engineer", "Professor/Instructor/Researcher", "Researcher (Non-Academic)",
    "Software Engineer/Developer", "Student", "Other")

role_entry.set("Select...")
role_entry.grid(row=18, columnspan=2, padx=40, pady=2)

# check button

checkbtn_var = tk.BooleanVar()
checkbtn = ttk.Checkbutton(label_frame, text="Agree : *", variable=checkbtn_var)
checkbtn.grid(row=21, columnspan=3, sticky=tk.W, padx=10, pady=2)

# button

def action():
    user_name1 = fname_var.get()
    user_name2 = lname_var.get()
    user_email = email_var.get()
    user_phone = phone_var.get()
    company_name = company_var.get()
    company_size = companysize_var.get()
    user_country = country_var.get()
    user_role = role_var.get()
    other = other_var.get()
    check = checkbtn_var.get()
    if user_name1 == "" or user_name2 == "" or user_email == "" or user_phone == "" or company_name == "" or company_size == "" or user_country == "" or user_role == "" or other == "" or check == "":
        m_box.showerror("Error", "You have to fill every field!")
    elif check == 0:
        m_box.showwarning("Warning", "You must agree to terms and conditions!")
    elif len(user_phone) != 10:
        m_box.showerror("Error", "Phone number must be of 10 digits!")
    else:
        with open("document1.txt", "a") as f:
            f.write(f"First Name:{user_name1}\n"
                    f"Last Name:{user_name2}\n"
                    f"Email Address:{user_email}\n"
                    f"Phone Number:{user_phone}\n"
                    f"Company Name:{company_name}\n"
                    f"Company Size:{company_size}\n"
                    f"Country:{user_country}\n"
                    f"Role:{user_role}\n"
                    f"Other:{other}\n"
                    f"Check:{check}\n")

            
submit_button = tk.Button(label_frame, text="Submit", bg="blue", fg="white", command=action)
submit_button.grid(row=23, columnspan=3, padx=10, pady=2)

text_label = ttk.Label(label_frame, text='* By clicking "Agree", Anaconda has permission to process your \ninformation in accordance with our privacy policy.')
text_label.grid(row=22, column=0, pady=2)

window.mainloop()
