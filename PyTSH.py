from pathlib import Path
import json
import os

cli_system = os.system

path = Path('PyTSH-Shell-ConfigPrompt.json')

if path.exists():
    contents = path.read_text()
    pytsh_prompt = json.loads(contents)
else:
    print('Welcome to the PyTSH Prompt Naming Shell ')
    pytsh_prompt = input('Pytsh:Enter-Pytsh-Prompt-Name> ')
    contents = json.dumps(pytsh_prompt)
    path.write_text(contents)

print("Welcome to PyTSH")
while True:
    
    pytsh_command = input(f'{pytsh_prompt} ')
    if pytsh_command == 'delete_data':
        cli_system('rm  PyTSH-Shell-ConfigPrompt.json') #Change to module path file
        exit()
    if pytsh_command == 'sudo su':
        print('Sorry, we cannot directly go root.')
    else:
        cli_system(pytsh_command)
