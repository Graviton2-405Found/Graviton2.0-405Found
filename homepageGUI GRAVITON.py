import tkinter as tk
from PIL import Image, ImageTk  # Pillow library for image support
import csv

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        print("Admin logged in")
        display_shopping_interface()
    elif username == "user" and password == "user123":
        print("User logged in")
        display_shopping_interface()
    else:
        print("Invalid username or password")

def display_shopping_interface():
    login_frame.pack_forget()  # Hide login frame
    homepage_frame.pack_forget()  # Hide homepage frame
    button_frame.pack(pady=10)  # Show shopping interface frame
    product_frame.pack(pady=(0, 10), padx=(50, 0), anchor='se')  # Show shopping interface frame

def add_product(price):
    global total_cost
    total_cost += price
    product_listbox.insert(tk.END, f"Product {len(product_listbox.get(0, tk.END))+1} - Rs. {price}")
    cost_label.config(text=f"Total: Rs. {total_cost}")
    checkout_button.config(state=tk.NORMAL)  # Enable checkout button once a product is added

def update_csv():
    username = username_entry.get()
    with open('shopping_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, total_cost])

def checkout():
    update_csv()
    checkout_button.config(state=tk.DISABLED)  # Disable checkout button after checkout
    print("Checkout successful. Data saved to CSV.")

# Create the main window
window = tk.Tk()
window.title("Shopping App")
window.geometry("800x600")  # Adjust window size

# Set colors and fonts
bg_color = "#ffe4e1"  # Misty Rose
button_bg_color = "#ff6b6b"  # Melon
button_fg_color = "white"
label_font = ("Arial", 12)

# Create a frame for the homepage
homepage_frame = tk.Frame(window, bg=bg_color)
homepage_frame.pack(pady=50)

# Create a title for the homepage
title_label = tk.Label(homepage_frame, text="Welcome to Shopping App", font=("Arial", 20, "bold"), bg=bg_color)
title_label.pack(pady=20)

# Create a frame for the login section
login_frame = tk.Frame(window, bg=bg_color)
login_frame.pack(pady=20)

# Create labels and entries for username and password
username_label = tk.Label(login_frame, text="Username:", font=label_font, bg=bg_color)
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

username_entry = tk.Entry(login_frame, font=label_font)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(login_frame, text="Password:", font=label_font, bg=bg_color)
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(login_frame, show="*", font=label_font)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a login button
login_button = tk.Button(login_frame, text="Login", font=label_font, bg=button_bg_color, fg=button_fg_color, command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create a frame for the shopping interface
button_frame = tk.Frame(window, bg=bg_color)
product_frame = tk.Frame(window, bg=bg_color)

# Function to create buttons for products with images
def create_product_button(text, price, image_path):
    button = tk.Button(button_frame, text=text, command=lambda: add_product(price), width=60, anchor="w", bg=button_bg_color, fg=button_fg_color, font=label_font)  
    button.pack(fill=tk.X, pady=5, padx=10)  
    
    img = Image.open(image_path)
    img = img.resize((30, 30), Image.ANTIALIAS)  
    img = ImageTk.PhotoImage(img)
    
    button.config(image=img, compound=tk.LEFT)
    button.image = img 

# Create buttons for products with images
create_product_button("Product 1 - Rs. 10.00", 10.0, "C:/Users/laksh/Downloads/png1.png")
create_product_button("Product 2 - Rs. 20.00", 20.0, "C:/Users/laksh/Downloads/png1.png")
create_product_button("Product 3 - Rs. 30.00", 30.0, "C:/Users/laksh/Downloads/png1.png")

# Create a listbox for products
product_listbox = tk.Listbox(product_frame, width=70, height=10, font=label_font, bg=bg_color, fg='black')
product_listbox.pack(side=tk.LEFT, padx=10)

# Initialize total cost
total_cost = 0.0

# Create a cost label
cost_label = tk.Label(button_frame, text=f"Total: Rs. {total_cost}", bg=bg_color, font=label_font)
cost_label.pack(side=tk.LEFT, padx=10)

# Create a checkout button
checkout_button = tk.Button(window, text="Checkout", state=tk.DISABLED, bg=button_bg_color, fg=button_fg_color, font=label_font, command=checkout)
checkout_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
