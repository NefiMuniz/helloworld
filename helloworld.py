import tkinter as tk
from tkinter import font
import datetime
import urllib.request
import json

def get_time_greeting():
    """
    Returns a greeting based on current time with appropriate emoji
    Morning: 5 AM - 11:59 AM 🌅
    Afternoon: 12 PM - 5:59 PM 🌇
    Night: 6 PM - 4:59 AM 🌙
    """
    now = datetime.datetime.now()
    hour = now.hour
    
    if 5 <= hour < 12:
        return "Have a great morning! 🌅"
    elif 12 <= hour < 18:
        return "Have a great afternoon! 🌇"
    else:
        return "Have a great night! 🌙"

def get_motivational_quote():
    """
    Fetches a random motivational quote from a free API
    Uses ZenQuotes API - no authentication required
    Returns the quote or a default message if offline
    """
    try:
        # ZenQuotes API - Free, no API key needed
        url = "https://zenquotes.io/api/random"
        
        # Set timeout to avoid hanging if offline
        with urllib.request.urlopen(url, timeout=3) as response:
            data = json.loads(response.read().decode())
            quote = data[0]['q']  # Quote text
            author = data[0]['a']  # Author name
            return f'"{quote}"\n— {author}'
    except Exception as e:
        # If offline or API fails, return a default message
        return "Stay positive and keep moving forward! 💪"

def close_window():
    """Close the application window"""
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Hello World! 🌍")
root.geometry("500x400")
root.configure(bg='#f0f0f0')

# Make window non-resizable for consistent layout
root.resizable(False, False)

# Create custom fonts
title_font = font.Font(family="Helvetica", size=24, weight="bold")
greeting_font = font.Font(family="Helvetica", size=14)
quote_font = font.Font(family="Helvetica", size=11, slant="italic")

# Title Label - "Hello World!"
title_label = tk.Label(
    root,
    text="Hello World! 👋",
    font=title_font,
    bg='#f0f0f0',
    fg='#2c3e50'
)
title_label.pack(pady=20)

# Time-based greeting
greeting = get_time_greeting()
greeting_label = tk.Label(
    root,
    text=greeting,
    font=greeting_font,
    bg='#f0f0f0',
    fg='#34495e'
)
greeting_label.pack(pady=10)

# Motivational quote section
quote_label = tk.Label(
    root,
    text="Loading inspiration...",
    font=quote_font,
    bg='#f0f0f0',
    fg='#7f8c8d',
    wraplength=450,  # Wrap text to fit window
    justify='center'
)
quote_label.pack(pady=20)

# Fetch quote in background (so window doesn't freeze)
def load_quote():
    quote = get_motivational_quote()
    quote_label.config(text=quote)

# Schedule quote loading after window is displayed
root.after(100, load_quote)

# "Let's go!" button
lets_go_button = tk.Button(
    root,
    text="Let's go! 🚀",
    command=close_window,
    font=font.Font(family="Helvetica", size=12, weight="bold"),
    bg='#3498db',
    fg='white',
    activebackground='#2980b9',
    activeforeground='white',
    relief='raised',
    bd=3,
    padx=20,
    pady=10,
    cursor='hand2'
)
lets_go_button.pack(pady=20)

# Add hover effect to button
def on_enter(e):
    lets_go_button.config(bg='#2980b9')

def on_leave(e):
    lets_go_button.config(bg='#3498db')

lets_go_button.bind("<Enter>", on_enter)
lets_go_button.bind("<Leave>", on_leave)

# Footer with current date/time
now = datetime.datetime.now()
footer_text = now.strftime("%A, %B %d, %Y • %I:%M %p")
footer_label = tk.Label(
    root,
    text=footer_text,
    font=font.Font(family="Helvetica", size=9),
    bg='#f0f0f0',
    fg='#95a5a6'
)
footer_label.pack(side='bottom', pady=10)

# Center the window on screen
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

# Start the GUI event loop
root.mainloop()