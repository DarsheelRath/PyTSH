FROM python:3.13-alpine3.23
WORKDIR /usr/local/PyTSH

COPY PyTSH.py ./
COPY PyTSH-Tkinter-Simple.py ./
COPY PyTSH-INTSALLER.py ./
EXPOSE 8000
CMD ["python", "PyTSH.py"]