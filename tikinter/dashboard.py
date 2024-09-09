import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from data import *

# Function to create and update charts

def update_chart(selected_year = None):
    if selected_year :
        if selected_year in years :
            df_filtered = df[df["Year"] == selected_year]
        else:
                df_filtered = df.copy()
    else:
        df_filtered = df.copy()
        
    total_sales = df_filtered["Sales"].sum()
    total_profits = df_filtered["Profit"].sum()
    
    # Displaying totals
    sales_label = tk.Label(root, text= f"Total Sales - ${total_sales}", 
                   font=("Arial", 18), background="#6a9481", foreground="Black")
    sales_label.grid(row=2, column=0, sticky="nsew")
    
    profit_label = tk.Label(root, text= f"Total Profits - ${total_profits}", 
                   font=("Arial", 18), background="#6a9481", foreground="Black")
    profit_label.grid(row=2, column=1, sticky="nsew")

    
    



# Initialise the app
root = tk.Tk()
root.title("Dashboard")
root.geometry('2000x2000')
root.configure(background="#d0f7e5")

# Defining the Grid 
root.columnconfigure((0,1,2,3), weight=1)
root.rowconfigure((0,1,2), weight=1)
root.rowconfigure((3,4), weight=2)

# Heading widget
heading = tk.Label(root, text= "Sales Dashboard", 
                   font=("Arial", 36), background="#d0f7e5", foreground="Black")
heading.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Year dropdown filter
yr_var = tk.StringVar()
yr_var.set(" --- Select Year --- ")
yr_dropdown = tk.OptionMenu(root, yr_var, "All Years", *years, 
                            command = update_chart)
yr_dropdown.configure(font=("Arial", 18), background="#d0f7e5", foreground="Black", width=10)
yr_dropdown["menu"].configure(font=("Arial", 18), background="#d0f7e5", foreground="Black")
yr_dropdown.grid(row=1, column=0, sticky="nswe", padx=15, pady=20)

update_chart()

# Run the app
root.mainloop()