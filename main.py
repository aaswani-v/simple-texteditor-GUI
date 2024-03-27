import tkinter as tk

def takingInput():
    print("[Start writing, Write '/done' to terminate]...\n")
    lines = []
    while True:
        line = inputText.get("1.0", "end-1c")
        if line == '/done':
            break
        lines.append(line + "\n")
        inputText.delete("1.0", "end")
    text = ''.join(lines)
    return text

def updateDoc():
    fileName = fileNameEntry.get()
    with open(fileName, 'a') as file:
        wrt = takingInput()
        file.write(wrt)

def createFile():
    fileName = fileNameEntry.get()
    with open(fileName, 'w') as file:
        print(f"{fileName} has been created")
        wrt = takingInput()
        file.write(wrt)

def emptyFile():
    fileName = fileNameEntry.get()
    with open(fileName, 'w') as file:
        print(f"{fileName} empty has been created")

def readFile():
    fileName = fileNameEntry.get()
    with open(fileName, 'r') as file:
        print(file.read())

root = tk.Tk()
root.title("File Editor")

fileNameLabel = tk.Label(root, text="File Name:")
fileNameLabel.grid(row=0, column=0, padx=5, pady=5)

fileNameEntry = tk.Entry(root, width=50)
fileNameEntry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

inputText = tk.Text(root, wrap="word", width=50, height=10)
inputText.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

openButton = tk.Button(root, text="Open")
openButton.grid(row=2, column=0, padx=5, pady=5)

saveButton = tk.Button(root, text="Save As")
saveButton.grid(row=2, column=1, padx=5, pady=5)

createButton = tk.Button(root, text="Create", command=createFile)
createButton.grid(row=3, column=0, padx=5, pady=5)

emptyButton = tk.Button(root, text="Empty", command=emptyFile)
emptyButton.grid(row=3, column=1, padx=5, pady=5)

updateButton = tk.Button(root, text="Update", command=updateDoc)
updateButton.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()
