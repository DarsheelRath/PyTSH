import tkinter as tk
import os
import json
from pathlib import Path

path = Path('PyTSH-Shell-ConfigPrompt.json')

if path.exists():
    contents = path.read_text()
    pytsh_prompt = json.loads(contents)
else:
    print('Welcome to the PyTSH Prompt Naming Shell ')
    pytsh_prompt = input('Pytsh:Enter-Pytsh-Prompt-Name> ')
    contents = json.dumps(pytsh_prompt)
    path.write_text(contents)
root = tk.Tk()
root.title('PyTSH Terminal')
root.configure(bg='black')
text_box = tk.Text(root, font=('Helvetica', 12), bg='black', fg='white')
text_box.pack()
entry = tk.Entry(root, width=60)
entry.pack(pady=20)
text_box.insert(tk.END, f"{pytsh_prompt}")


def run():
    entered_text = entry.get()
    os.system(entered_text)


while True:
    try:
        button = tk.Button(root, text="Run", command=run)
        button.pack(pady=10)
        root.mainloop()
    except Exception as e:
        print(f'An error occurred with the Shell. This is the errror: {e}')
