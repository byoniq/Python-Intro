# import tkinter as tk

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.hi_there = tk.Button(self)
#         self.hi_there["text"] = "Hello World\n(click me)"
#         self.hi_there["command"] = self.say_hi
#         self.hi_there.pack(side="top")

#         self.quit = tk.Button(self, text="QUIT", fg="red",
#                               command=self.master.destroy)
#         self.quit.pack(side="bottom")

#     def say_hi(self):
#         print("hi there, everyone!")

# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()


# import tkinter as tk
# import webbrowser



# def open_url():
#     url = entry.get()
#     webbrowser.open_new(url)

# # Create the main window
# root = tk.Tk()
# background_color = '#001f3f'
# root.configure(bg=background_color)
# root.title('Web Page Opener')
# root.configure(bg=background_color)

# # Create a label
# label = tk.Label(root, text="Enter URL:", fg='#ffffff', bg=background_color)
# label.pack()


# # Create a label
# label = tk.Label(root, text="Enter URL:")
# label.pack()

# # Create an entry widget for URL input
# entry = tk.Entry(root, width=50)
# entry.pack()

# # Create a button to open the URL
# button = tk.Button(root, text="Open", command=open_url)
# button.pack()

# # Run the main event loop
# root.mainloop()

import tkinter as tk
import webbrowser

def open_url():
    url = entry.get()
    if url.strip():  # Check if URL is not empty
        webbrowser.open_new(url)
    else:
        status_var.set("Please enter a valid URL")

# Create the main window
root = tk.Tk()
background_color = '#001f3f'
root.configure(bg=background_color)
root.title("Web Page Opener")

# Create a title label
title_label = tk.Label(root, text="Web Page Opener", bg=background_color, fg='#ffffff', font=("android", 20, "bold"))
title_label.pack()

# Create a label
label = tk.Label(root, text="Enter URL:", bg=background_color, fg='#ffffff')
label.pack()

# Create a status label
status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var, fg="red", bg=background_color)
status_label.pack()

# Create an entry widget for URL input
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button to open the URL
button = tk.Button(root, text="Open", command=open_url, bg=background_color, fg='#ffffff')
button.pack()

# Run the main event loop
root.mainloop()