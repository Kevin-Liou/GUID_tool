import tkinter as tk
import uuid

def generate_guids():
    num = int(entry.get())
    result = ""
    for i in range(num):
        result += str(uuid.uuid4()).upper() + "\n"
    text.delete(1.0, tk.END)
    text.insert(tk.END, result)

root = tk.Tk()
root.title("Random GUID Generator")

label = tk.Label(root, text="Enter number of GUIDs to generate:")
label.pack()

entry = tk.Entry(root)
entry.insert(0, "1")
entry.pack()

button = tk.Button(root, text="Generate", command=generate_guids)
button.pack()

text = tk.Text(root, height=10, width=50)
text.pack()

root.mainloop()
