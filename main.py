import pyshorteners
import tkinter as tk
from tkinter import ttk

def shorten_urls():
    """
    Shorten multiple URLs using pyshorteners
    """
    urls = []
    while True:
        url = input_box.get()
        if url.lower() == "q":
            break
        urls.append(url)
        input_box.delete(0, tk.END)

    s = pyshorteners.Shortener()
    shortened_urls = []
    for url in urls:
        shortened_url = s.tinyurl.short(url)
        shortened_urls.append(shortened_url)

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    for i, url in enumerate(shortened_urls):
        output_box.insert(tk.END, f"{i+1}. {url}\n")
    output_box.config(state=tk.DISABLED)

window = tk.Tk()
window.title("URL Shortener")
window.geometry("400x400")
window.configure(bg="#F5F5F5")

title_label = tk.Label(window, text="URL Shortener", font=("Arial", 24, "bold"), bg="#F5F5F5")
title_label.pack(pady=10)

input_frame = tk.Frame(window, bg="#F5F5F5")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter URLs to shorten:", font=("Arial", 12), bg="#F5F5F5")
input_label.pack(side=tk.LEFT)

input_box = tk.Entry(input_frame, width=40, font=("Arial", 12), bd=0, bg="#E0E0E0")
input_box.pack(side=tk.LEFT, padx=10)

submit_button = tk.Button(window, text="Shorten URLs", font=("Arial", 12), bg="#FFC107",
                          fg="white", activebackground="#FFA000", bd=0, command=shorten_urls)
submit_button.pack(pady=10)

output_label = tk.Label(window, text="Shortened URLs:", font=("Arial", 12), bg="#F5F5F5")
output_label.pack()

output_box = tk.Text(window, height=10, font=("Arial", 12), bd=0, bg="#E0E0E0", state=tk.DISABLED)
output_box.pack()

window.mainloop()
