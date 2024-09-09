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

    # Bar charts
    fig1 = plt.figure(figsize = (4, 2))
    sns.barplot(data=df_filtered, x= "Product", y = "Sales", hue= "Product",
                estimator="sum", errorbar=None)
    plt.title("Sales by Product")
    plt.xticks(rotation = 20)    
    canvas1 = FigureCanvasTkAgg(fig1, root)
    canvas1.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nwes")

    fig2 = plt.figure(figsize = (4, 2))
    sns.barplot(data=df_filtered, x= "Product", y = "Profit", hue= "Product",
                estimator="sum", errorbar=None)
    plt.title("Profit by Product")
    plt.xticks(rotation = 20)    
    canvas2 = FigureCanvasTkAgg(fig2, root)
    canvas2.get_tk_widget().grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nwes")


    # Line charts
    fig3 = plt.figure(figsize = (4, 2))
    sns.lineplot(data=df_filtered, x= "Date", y = "Sales", estimator="sum", errorbar=None)
    plt.title("Sales over months")
    canvas3 = FigureCanvasTkAgg(fig3, root)
    canvas3.get_tk_widget().grid(row=3, column=2, columnspan=2, padx=10, pady=10, sticky="nwes")

    fig4 = plt.figure(figsize = (4, 2))
    sns.lineplot(data=df_filtered, x= "Date", y = "Profit", estimator="sum", errorbar=None)
    plt.title("Profits over months")
    canvas4 = FigureCanvasTkAgg(fig4, root)
    canvas4.get_tk_widget().grid(row=4, column=2, columnspan=2, padx=10, pady=10, sticky="nwes")
    
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

# Define a function to close all plots and terminate the app properly
def on_closing():
    # Close all matplotlib figures
    plt.close('all')
    # Destroy the Tkinter window and terminate the app
    root.destroy()

# Bind the close window event (when clicking the "X" button) to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)


# Run the app
root.mainloop()