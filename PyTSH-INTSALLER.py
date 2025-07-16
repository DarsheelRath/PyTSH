import os
cli = os.system

#Install 

installertype = input("Do you have wget? (yN): ").strip().lower()
if installertype == "y":
    cli("wget https://raw.githubusercontent.com/DarsheelRath/PyTSH/refs/heads/main/PyTSH-Tkinter-Simple.py  && wget https://raw.githubusercontent.com/DarsheelRath/PyTSH/refs/heads/main/PyTSH.py ")
if installertype == "n":
    brew = input("Do you have brew? (yN): ").strip().lower()
    if brew == "y":
        cli("brew install wget && wget https://raw.githubusercontent.com/DarsheelRath/PyTSH/refs/heads/main/PyTSH-Tkinter-Simple.py  && wget https://raw.githubusercontent.com/DarsheelRath/PyTSH/refs/heads/main/PyTSH.py ")
    if brew == "n":
        print("Please install wget manually and run this script again. Or download the websites in the file manually.")

print("PyTSH has been installed successfully. You can now run PyTSH-Tkinter-Simple.py to use the PyTSH Terminal or PyTSH.py for the CLI version.")