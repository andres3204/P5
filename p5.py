# p5.py
# Andres Jimenez
# spring 2025
# p5 assignment
# GUI demonstrates saving data as text, CSV, XML, JSON, binary, and object
# I needed some help from AI to make the save and open functions work as intended as it was a challenge to do them manually just from Dr. Lehman's code.

import json, os, csv, struct, pickle # Imported Json, os, csv, struct for binary, and picle for object.
import tkinter as tk
from tkinter import *
from tkinter import Menu
import xml.etree.ElementTree as ET # Imported this for the XML saving and opening data.


# *** To Do ***
# update each of the following functions to open/save data related to your project

def new_file():
    print("GUI Reset")
    incomeText.delete(0, tk.END)   # Clear the income textbox
    expensesText.delete(0, tk.END)  # Clears the expenses textbox
    typeText.delete(0, tk.END)  # Clears the type textBox
    var.set(False) # Unchecks the radioButton that was selected
    
def exit_app():
    print("Exit Application")
    root.destroy() # Destroys Application and stops program.

def open_text():
    print("Opening Text file...")
    filename = "finance.txt"
    
    with open(filename, "r") as f:  # opens file in read mode.
        lines = f.readlines() # reads all the lines from the f file and saves them as a list of strings.
        if lines:             
            income = lines[0].split(": ")[1].strip()    # income extracted and stripped
            expenses = lines[1].split(": ")[1].strip()      # expenses extracted and stripped
            category = int(lines[2].split(": ")[1].strip()) # profit extracted, stripped, and converted to int
            types = lines[3].split(": ")[1].strip()         # entry extracted and stripped

            # Show up in the GUI interface
            incomeText.delete(0, tk.END)  # Clear the field
            incomeText.insert(0, income)  # Insert income

            expensesText.delete(0, tk.END)      # Clears field
            expensesText.insert(0, expenses)    # Inserts saved expenses

            var.set(int(category))  # Set the category radio button

            typeText.delete(0, tk.END)  # Clears type
            typeText.insert(0, types)   # Inserts Type

            print(f"Income: {income}, Expenses: {expenses}, Type: {types}, Category: {category}") # prints values in terminal
        else:
            print("No data for this Text file.")

def open_csv():
    print("Opening CSV file...")
    filename = "finance.csv"

    with open(filename, mode='r') as f:
        header = f.readline().strip()
        print(header)

        for line in f:
            values = line.strip().split(",") # Splits CSV values

            income = int(values[0])
            expenses = int(values[1])
            category = values[2]
            types = values[3]

            # Show up in the GUI interface
            incomeText.delete(0, tk.END)  # Clear the field
            incomeText.insert(0, income)  # Insert income

            expensesText.delete(0, tk.END) # Clears field
            expensesText.insert(0, expenses) # Inserts saved expenses

            var.set(int(category))  # Set the category radio button

            typeText.delete(0, tk.END) # Clears type
            typeText.insert(0, types) # Inserts Type

            print(f"Income: {income}, Expenses: {expenses}, Type: {types}, Category: {category}") # prints values in terminal

def open_xml():
    print("Opening XML file...")
    filename = "finance.xml"

    # Parse the XML file and get the root element
    tree = ET.parse(filename)
    root = tree.getroot()

    # Extract the data from the XML elements
    income = root.find('income').text
    expenses = root.find('expenses').text
    category = root.find('category').text
    types = root.find('type').text

    # Populate the GUI fields with the extracted values
    incomeText.delete(0, tk.END)
    incomeText.insert(0, income)

    expensesText.delete(0, tk.END)
    expensesText.insert(0, expenses)

    category_map = {
        "Housing": 1,
        "Transport": 2,
        "Food": 3,
        "Utilities": 4,
        "Investments": 5,
        "Savings": 6,
        "Gifts": 7,
        "Work": 8,
        "Personal Caring": 9,
        "Entertainment": 10
    }

    # Convert category name to corresponding number
    if category in category_map:
        var.set(category_map[category])  # Set the corresponding radio button selection
    else:
        print(f"Warning: Unknown category '{category}'")

    typeText.delete(0, tk.END)
    typeText.insert(0, types)

    print(f"Income: {income}, Expenses: {expenses}, Type: {types}, Category: {category}") # prints values in terminal

def open_json():
    print("Opening JSON file...")
    filename = "finance.json"

    with open(filename, "r") as f:
        data = json.load(f)

    if isinstance(data, dict): # Got from AI as it was not working wit previos if statements.
        income = int(data["Income"])
        expenses = int(data["Expenses"])
        category = data["Category"]
        types = data["Type"]

        # Populate the GUI fields
        incomeText.delete(0, tk.END)
        incomeText.insert(0, data["Income"])

        expensesText.delete(0, tk.END)
        expensesText.insert(0, data["Expenses"])

        var.set(category)  # Set the selected category radio button

        typeText.delete(0, tk.END)
        typeText.insert(0, data["Type"])

        print(f"Income: {income}, Expenses: {expenses}, Type: {types}, Category: {category}") # prints values in terminal
    else:
        print("Data not found for JSON file")

def open_binary():
    print("Opening Binary File...")
    filename = "finance.bin"

    with open(filename, "rb") as f:
        # Read Income & Expenses (each 4 bytes)
        income = struct.unpack("i", f.read(4))[0]
        expenses = struct.unpack("i", f.read(4))[0]

        # Read Type (String with length prefix)
        types_length = struct.unpack("I", f.read(4))[0]  # Read type length
        types = f.read(types_length).decode("utf-8")  # Read types data

        # Read Category (4 bytes)
        category = struct.unpack("i", f.read(4))[0]
    
    # Show up in the GUI interface
    incomeText.delete(0, tk.END)  # Clear the field
    incomeText.insert(0, income)  # Insert income

    expensesText.delete(0, tk.END) # Clears field
    expensesText.insert(0, expenses) # Inserts saved expenses

    var.set(int(category))  # Set the category radio button

    typeText.delete(0, tk.END) # Clears type
    typeText.insert(0, types) # Inserts Type

    print(f"Income: {income}, Expenses: {expenses}, Type: {types}, Category: {category}") # prints values in terminal

    return {
        "Income": income,
        "Expenses": expenses,
        "Type": types,
        "Category": category
    }

def open_object():
    print("Opening Object file...")
    filename = "finance.pkl"

    with open(filename, "rb") as file:
        data = pickle.load(file)

    # Assuming the data is a dictionary with "Income", "Expenses", "Type", "Category"
    income = data.get("Income")
    expenses = data.get("Expenses")
    types = data.get("Type")
    category = data.get("Category")

    # Populate the GUI fields
    incomeText.delete(0, tk.END)  # Clear existing text
    incomeText.insert(0, income)  # Insert the income value

    expensesText.delete(0, tk.END)  # Clear existing text
    expensesText.insert(0, expenses)  # Insert the expenses value

    var.set(category)  # Set the selected category radio button

    typeText.delete(0, tk.END)  # Clear existing text
    typeText.insert(0, types)  # Insert the types value

    print("Loaded Data:", data)

def save_text():
    print("Saving Text file...")
    filename = "finance.txt"

    with open(filename, mode='w') as f:
        # Retrieve values from GUI input fields
        income = incomeText.get()
        expenses = expensesText.get()
        category = var.get()
        types = typeText.get()

        # Write values to file
        f.write(f"Income: {income}\n")
        f.write(f"Expenses: {expenses}\n")
        f.write(f"Category: {category}\n") 
        f.write(f"Type: {types}\n")  
    
    # Get file size and confirm save
    size_bytes = os.path.getsize(filename)
    print(f"Text data saved ({size_bytes} bytes) to {filename}")

def save_csv():
    print("Saving CSV file...")
    filename = "finance.csv"

    income = incomeText.get()
    expenses = expensesText.get()
    category = var.get()
    types = typeText.get()

    # Open file in append mode to preserve existing data
    with open(filename, mode='w', newline='') as f:
        # Retrieve values from GUI input fields
        writer = csv.writer(f)
        
        # Write header only if file is empty
        if os.path.getsize(filename) == 0:
            writer.writerow(["Income", "Expenses", "Category", "Type"])
        
        # Write data to file
        writer.writerow([income, expenses, category, types])

    print(f"Data saved: Income={income}, Expenses={expenses}, Category={category}, Type={types}")

    size_bytes = os.path.getsize(filename)
    print(f"CSV data ({size_bytes} bytes) saved to {filename}")

def save_xml():
    print("Save XML file.")
    
    # Retrieve values from GUI input fields
    income_value = incomeText.get()
    expenses_value = expensesText.get()
    category_value = var.get()  # The category radio button
    type_value = typeText.get()

    # Map the category number to its name
    category_dict = {
        1: "Housing",
        2: "Transport",
        3: "Food",
        4: "Utilities",
        5: "Investments",
        6: "Savings",
        7: "Gifts",
        8: "Work",
        9: "Personal Caring",
        10: "Entertainment"
    }
    category_name = category_dict.get(category_value, "Unknown")  # Default to "Unknown" if not found

    # Create the root element
    root = ET.Element("data")

    # Create and populate child elements
    incomeElem = ET.SubElement(root, "income")
    incomeElem.text = income_value

    expensesElem = ET.SubElement(root, "expenses")
    expensesElem.text = expenses_value

    categoryElem = ET.SubElement(root, "category")
    categoryElem.text = category_name  # Save the category name, not the number

    typesElem = ET.SubElement(root, "type")
    typesElem.text = type_value

    # Build the XML tree and write it to a file
    tree = ET.ElementTree(root)
    tree.write("finance.xml", encoding="utf-8", xml_declaration=True)

    print("XML file saved as 'finance.xml'.")

def save_json():
    print("Saving to JSON file...")
    
    # Retrieve values from GUI input fields
    income = incomeText.get()
    expenses = expensesText.get()
    category = var.get()
    types = typeText.get()

    # Data to be written to JSON
    data = {
        "Income": income,
        "Expenses": expenses,
        "Category": category,
        "Type": types
    }

    # File name
    filename = "finance.json"

    # Write data to JSON file
    with open(filename, mode='w') as f:
        json.dump(data, f, indent=4)  # Pretty-print JSON with indentation

    print(f"JSON data saved to {filename}")

    size_bytes = os.path.getsize(filename)
    print(f"JSON data saved ({size_bytes} bytes) to {filename}")

def save_binary():
    print("Saving finance data to binary file...")

    # Retrieve values from GUI input fields
    income = int(incomeText.get())
    expenses = int(expensesText.get())
    category = var.get()  # Selected category radio button value
    types = typeText.get()

    filename = "finance.bin"

    with open(filename, "wb") as file:
        # Write Income & Expenses (4 bytes each)
        file.write(struct.pack("i", income))   
        file.write(struct.pack("i", expenses)) 

        # Write Type (String with length prefix)
        types_bytes = types.encode("utf-8")  
        file.write(struct.pack("I", len(types_bytes))) 
        file.write(types_bytes) 

        # Write Category (4 bytes)
        file.write(struct.pack("i", category))  

    size_bytes = os.path.getsize(filename)
    print(f"Binary data saved ({size_bytes} bytes) to {filename}")


def save_object():
    print("Save Object file.")

    # Retrieve values from GUI input fields
    income = incomeText.get()
    expenses = expensesText.get()
    category = var.get()
    types = typeText.get()

    # Data to be saved as an object
    data = {
        "Income": income,
        "Expenses": expenses,
        "Category": category,
        "Type": types
    }

    filename = "finance.pkl"

    with open(filename, "wb") as file:
        pickle.dump(data, file)

    size_bytes = os.path.getsize(filename)
    print(f"Finance data saved ({size_bytes} bytes) to {filename}")

# --- Create GUI ---
root = tk.Tk()
root.title("Finance Tracker")
root.geometry("600x500")

# *** To Do ***
# add/update GUI components here 

# Create a frame that is in charge of holding the Income & Expenses data.
inAndOutFrame = tk.Frame(root)
inAndOutFrame.pack(padx=10, pady=5, fill="x", anchor="w")

# Income Section
incomeLabel = tk.Label(inAndOutFrame, text="Enter your Income: ")
incomeLabel.grid(row=0, column=0, padx=(0, 5))
incomeText = tk.Entry(inAndOutFrame, width=5)
incomeText.grid(row=0, column=1, padx=(0, 5))
incomeSave = tk.Button(inAndOutFrame, text="Save")
incomeSave.grid(row=0, column=2, padx=(5, 15))

# Expenses Section
expensesLabel = tk.Label(inAndOutFrame, text="Enter your Expenses: ")
expensesLabel.grid(row=0, column=3, padx=(0, 5))
expensesText = tk.Entry(inAndOutFrame, width=5)
expensesText.grid(row=0, column=4, padx=(0, 5))
expensesSave = tk.Button(inAndOutFrame, text="Save")
expensesSave.grid(row=0, column=5)

# Frame for Category & Type
chooseFrame = tk.Frame(root)
chooseFrame.pack(padx=10, fill="x", anchor="w")

# Category Section (aligned with Income)
categoryLabel = tk.Label(chooseFrame, text="Choose Category: ")
categoryLabel.grid(row=0, column=0, padx=(0, 5))

# Radio Buttons Options for Category
var = IntVar()

categoryRadio1 = tk.Radiobutton(chooseFrame, text="Housing", variable=var, value=1)
categoryRadio1.grid(row=0, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio2 = tk.Radiobutton(chooseFrame, text="Transport", variable=var, value=2)
categoryRadio2.grid(row=1, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio3 = tk.Radiobutton(chooseFrame, text="Food", variable=var, value=3)
categoryRadio3.grid(row=2, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio4 = tk.Radiobutton(chooseFrame, text="Utilities", variable=var, value=4)
categoryRadio4.grid(row=3, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio5 = tk.Radiobutton(chooseFrame, text="Investments", variable=var, value=5)
categoryRadio5.grid(row=4, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio6 = tk.Radiobutton(chooseFrame, text="Savings", variable=var, value=6)
categoryRadio6.grid(row=5, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio7 = tk.Radiobutton(chooseFrame, text="Gifts", variable=var, value=7)
categoryRadio7.grid(row=6, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio8 = tk.Radiobutton(chooseFrame, text="Work", variable=var, value=8)
categoryRadio8.grid(row=7, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio9 = tk.Radiobutton(chooseFrame, text="Personal Caring", variable=var, value=9)
categoryRadio9.grid(row=8, column=1, sticky="w", padx=(10, 5), pady=2)

categoryRadio10 = tk.Radiobutton(chooseFrame, text="Entertainment", variable=var, value=10)
categoryRadio10.grid(row=9, column=1, sticky="w", padx=(10, 5), pady=2)

# Type Section (aligned with Expenses)
typeLabel = tk.Label(chooseFrame, text="Choose your Type: ")
typeLabel.grid(row=0, column=3, padx=(0, 5))
typeText = tk.Entry(chooseFrame, width=5)
typeText.grid(row=0, column=4, padx=(0, 5))
typeSave = tk.Button(chooseFrame, text="Save")
typeSave.grid(row=0, column=5)

# Create the menu bar
menubar = Menu(root)
root.config(menu=menubar)

# File menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Open menu
open_menu = Menu(menubar, tearoff=0)
open_menu.add_command(label="Open Text", command=open_text)
open_menu.add_separator()
open_menu.add_command(label="Open CSV", command=open_csv)
open_menu.add_separator()
open_menu.add_command(label="Open XML", command=open_xml)
open_menu.add_separator()
open_menu.add_command(label="Open JSON", command=open_json)
open_menu.add_separator()
open_menu.add_command(label="Open Binary", command=open_binary)
open_menu.add_separator()
open_menu.add_command(label="Open Object", command=open_object)
menubar.add_cascade(label="Open", menu=open_menu)

# Save menu
save_menu = Menu(menubar, tearoff=0)
save_menu.add_command(label="Save Text", command=save_text)
save_menu.add_separator()
save_menu.add_command(label="Save CSV", command=save_csv)
save_menu.add_separator()
save_menu.add_command(label="Save XML", command=save_xml)
save_menu.add_separator()
save_menu.add_command(label="Save JSON", command=save_json)
save_menu.add_separator()
save_menu.add_command(label="Save Binary", command=save_binary)
save_menu.add_separator()
save_menu.add_command(label="Save Object", command=save_object)
menubar.add_cascade(label="Save", menu=save_menu)

# Run the application
root.mainloop()

# -- end --
