# Exercise 1:
# Create a simple Tkinter application that displays a label with the text "Hello, Tkinter!"

import tkinter as tk

root = tk.Tk()
root.title("Exercise 1")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()

# Exercise 2: Tkinter application with a button that changes the text of a label when clicked.


import tkinter as tk

def change_text():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Exercise 2")

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

root.mainloop()

# Exercise 3: Tkinter application with an entry field and a button that displays the entered text in a label.


import tkinter as tk

def display_text():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("Exercise 3")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Display Text", command=display_text)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

# Exercise 4: Tkinter application with two buttons that increase or decrease a counter displayed in a label.

import tkinter as tk

def increase_counter():
    global counter
    counter += 1
    update_label()

def decrease_counter():
    global counter
    counter -= 1
    update_label()

def update_label():
    label.config(text=f"Counter: {counter}")

counter = 0

root = tk.Tk()
root.title("Exercise 4")

label = tk.Label(root, text=f"Counter: {counter}")
label.pack()

increase_button = tk.Button(root, text="Increase", command=increase_counter)
increase_button.pack(side=tk.LEFT)

decrease_button = tk.Button(root, text="Decrease", command=decrease_counter)
decrease_button.pack(side=tk.RIGHT)

root.mainloop()