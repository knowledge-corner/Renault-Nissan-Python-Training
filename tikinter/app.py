import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd


# Main Program --------------

# Adding main window
root = tk.Tk()
root.title("Export data from excel")
root.geometry("500x500")
root.configure(background="#abe5eb")

# Adding Components
# Load Button
def load_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path :
        sheet_var.set(" --- Select Plan --- ")
        plan_var.set(" --- Select Design --- ")
        global excel_file
        excel_file = pd.ExcelFile(file_path)
        sheets = excel_file.sheet_names

        # POPULATE THE SHEET NAMES IN THE DROPDOWN
        menu = sheet_dropdown["menu"]
        menu.delete(0, "end")
        menu.add_command(label = " --- Select Plan --- ")
        for s in sheets :
            menu.add_command(label = s, command = tk._setit(sheet_var, s, on_sheet_select))        
    else:
        messagebox.showerror("Error", "Failed to read the file")

load_button = tk.Button(root, text="Load Excel", command=load_excel,
                        background="#0b6a73", foreground="#62d9a1", font=("Arial", 12), width=20, height=2)
# load_button.pack(anchor="w", fill="both", pady=10, padx=10)  - just for reference
load_button.pack(anchor="w", pady=10, padx=15)


# Adding dropdown to select sheet
def on_sheet_select(selected_sheet):
    plan_var.set(" --- Select Design --- ")
    df = pd.read_excel(excel_file, sheet_name = selected_sheet)
    df.set_index(df.columns[0], inplace=True)
    cols = list(df.columns)
    if cols :
    # POPULATE THE COLUMN NAMES IN THE DROPDOWN
        menu = plan_dropdown["menu"]
        menu.delete(0, "end")
        menu.add_command(label = " --- Select Design --- ")
        for c in cols :
            menu.add_command(label = c, command = tk._setit(plan_var, c, on_plan_select))        
    else:
        messagebox.showerror("Error", "Failed to read the columns")
    

sheet_var = tk.StringVar()
sheet_var.set(" --- Select Plan --- ")
sheet_dropdown = tk.OptionMenu(root, sheet_var, " --- Select Plan --- ", command=on_sheet_select)
# element.configure is for applying formatting
sheet_dropdown.configure(background="#0b6a73", foreground="#62d9a1", font=("Arial", 12), width=20, height=2)
sheet_dropdown.pack(anchor="w", pady=10, padx=15)

# Adding dropdown to select plan
def on_plan_select(selected_value):
    messagebox.showinfo("Succees", selected_value)
    
plan_var = tk.StringVar()
plan_var.set(" --- Select Design --- ")
plan_dropdown = tk.OptionMenu(root, plan_var, " --- Select Design --- ", command = on_plan_select)
plan_dropdown.configure(background="#0b6a73", foreground="#62d9a1", font=("Arial", 12), width=20, height=2)
plan_dropdown.pack(anchor="w", pady=10, padx=15)



# Run application --------------
root.mainloop()
