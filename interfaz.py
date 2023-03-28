from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from sistemasNumericos import *
from NRZI import *
from Hamming import *



hexNumber = 0
binaryNumber = 0
octalNumber = 0
decimalNumber = 0

SMALL_GEOMETRY_WIDTH = "500"
SMALL_GEOMETRY_HEIGHT = "300"

LARGE_GEOMETRY_WIDTH = "800"

app = Tk()
hexContainer = Frame(app)
menuContainer = Frame(app)
conversionsContainer = Frame(app)
hammingContainer = Frame(app)
decodingContainer = Frame(app)

print(str(font.families()))



def unpackContainers():
    hexContainer.pack_forget()
    menuContainer.pack_forget()
    conversionsContainer.pack_forget()
    hammingContainer.pack_forget()
    decodingContainer.pack_forget()
    app.geometry(SMALL_GEOMETRY_WIDTH + "x" + SMALL_GEOMETRY_HEIGHT)


def hexWindow():
    unpackContainers()
    hexContainer.pack()

    instructionLabel = Label(hexContainer, text="Por favor ingrese un número hexadecimal válido no mayor a 7FF:")
    instructionLabel.grid(row=0, column=0, sticky="s", pady=(50, 0))

    hexEntry = Entry(hexContainer)
    hexEntry.grid(row=1, column=0)

    confirmButton = Button(hexContainer, text="Ingresar", command=lambda: validateHexEntry(hexEntry.get().upper()))
    confirmButton.grid(row=2, column=0)


def validateHexEntry(pHexNumber):
    global hexNumber, binaryNumber, octalNumber, decimalNumber
    try:
        hexNumber = pHexNumber
        binaryNumber = hexadecimal_a_binario(hexNumber)
        octalNumber = hex_a_octal(hexNumber)
        decimalNumber = hex_to_decimal(hexNumber)
        menuWindow()
    except ValueError as e:
        messagebox.showerror('Error en hexadecimal', e.args[0])
        hexWindow()


def menuWindow():
    unpackContainers()
    menuContainer.pack()

    navigateToConversionsButton = Button(menuContainer, text="Ver conversiones numéricas",
                                         command=lambda: conversionsWindow())
    navigateToConversionsButton.grid(row=0, column=0)

    navigateToNRZI = Button(menuContainer, text="Ver codificación NRZI",
                            command=lambda: nrzi_signal(binaryNumber))
    navigateToNRZI.grid(row=1, column=0)

    navigateToHamming = Button(menuContainer, text="Ver código Hamming",
                               command=lambda: hammingCodingWindow())
    navigateToHamming.grid(row=2, column=0)

    navigateToHexButton = Button(menuContainer, text="Volver a página de inicio",
                                 command=lambda: hexWindow())
    navigateToHexButton.grid(row=3, column=0)


def conversionsWindow():
    unpackContainers()
    conversionsContainer.pack()

    table = ttk.Treeview(conversionsContainer, columns=("Hexadecimal", "Decimal", "Octal", "Binary"), show="headings",
                         height=1)
    table.grid(row=0, column=0, pady=100)

    table.heading("Hexadecimal", text="Hexadecimal")
    table.heading("Decimal", text="Decimal")
    table.heading("Octal", text="Octal")
    table.heading("Binary", text="Binario")

    table.column("Hexadecimal", width=int(SMALL_GEOMETRY_WIDTH) // 6)
    table.column("Decimal", width=int(SMALL_GEOMETRY_WIDTH) // 6)
    table.column("Octal", width=int(SMALL_GEOMETRY_WIDTH) // 6)
    table.column("Binary", width=int(SMALL_GEOMETRY_WIDTH) // 6)

    table.insert("", "end", values=(hexNumber, decimalNumber, octalNumber, binaryNumber))

    navigateToMenuButton = Button(conversionsContainer, text="Volver a menú",
                                  command=lambda: menuWindow())
    navigateToMenuButton.grid(row=1, column=0)


def hammingCodingWindow():
    unpackContainers()
    hammingContainer.pack()
    app.geometry(LARGE_GEOMETRY_WIDTH + "x" + SMALL_GEOMETRY_HEIGHT)

    table = ttk.Treeview(hammingContainer, columns=(" ", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p4", "d5", "d6",
                                                    "d7", "d8", "d9", "d10", "d11"), show="headings", height=6)
    table.grid(row=0, column=0)

    table.heading(" ", text=" ")
    table.heading("p1", text="p1")
    table.heading("p2", text="p2")
    table.heading("d1", text="d1")
    table.heading("p3", text="p3")
    table.heading("d2", text="d2")
    table.heading("d3", text="d3")
    table.heading("d4", text="d4")
    table.heading("p4", text="p4")
    table.heading("d5", text="d5")
    table.heading("d6", text="d6")
    table.heading("d7", text="d7")
    table.heading("d8", text="d8")
    table.heading("d9", text="d9")
    table.heading("d10", text="d10")
    table.heading("d11", text="d11")

    table.column(" ", width=180)
    table.column("p1", width=25)
    table.column("p2", width=25)
    table.column("d1", width=25)
    table.column("p3", width=25)
    table.column("d2", width=25)
    table.column("d3", width=25)
    table.column("d4", width=25)
    table.column("p4", width=25)
    table.column("d5", width=25)
    table.column("d6", width=25)
    table.column("d7", width=25)
    table.column("d8", width=25)
    table.column("d9", width=25)
    table.column("d10", width=30)
    table.column("d11", width=30)

    tableRows = createHammingTable(hamming(binaryNumber), ["Palabra de datos (sin paridad):", "p1",
                                                           "p2", "p3", "p4", "Palabra de datos (con paridad):"])

    table.insert("", "end", values=tableRows[0])
    table.insert("", "end", values=tableRows[1])
    table.insert("", "end", values=tableRows[2])
    table.insert("", "end", values=tableRows[3])
    table.insert("", "end", values=tableRows[4])
    table.insert("", "end", values=tableRows[5])


    # hammingMatrix = hammingCode(binaryNumber)
    codedBinary = "".join(tableRows[5][1:])

    instructionLabel = Label(hammingContainer,
                             text="Puede modificar un bit del número codificado para verificar el Hamming: ")
    instructionLabel.grid(row=1, column=0)

    codedEntry = Entry(hammingContainer)
    codedEntry.grid(row=2, column=0)

    codedEntry.insert(0, codedBinary)

    confirmButton = Button(hammingContainer, text="Decodificar código",
                           command=lambda: validateModifiedBinary(codedEntry.get(), codedBinary))
    confirmButton.grid(row=3, column=0)


def createHammingTable(matrix, rowTitles):
    tableRows = []
    for i in range(len(matrix)):
        tableRow = [rowTitles[i]]
        for elem in matrix[i]:
            tableRow.append(elem)
        tableRows.append(tableRow)
    return tableRows

def validateModifiedBinary(modifiedBinary, codedBinary):
    try:
        if len(modifiedBinary) != len(codedBinary):
            raise ValueError("Error: El binario debe de ser de 15 dígitos")

        contModifications = 0
        for i in range(len(modifiedBinary)):
            if modifiedBinary[i] != codedBinary[i]:
                contModifications += 1

        if contModifications > 1:
            raise ValueError("Error: Se modificó más de un dígito del binario")
        decodingWindow(modifiedBinary)

    except ValueError as e:
        messagebox.showerror('Error en entrada', e.args[0])
        hammingCodingWindow()


def decodingWindow(modifiedBinary):
    unpackContainers()
    decodingContainer.pack()
    app.geometry(LARGE_GEOMETRY_WIDTH + "x" + SMALL_GEOMETRY_HEIGHT)

    style = ttk.Style()
    style.configure('MyCustom.Treeview.Heading', padding=(0, 15))

    table = ttk.Treeview(decodingContainer, columns=(" ", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p4", "d5", "d6",
                                                     "d7", "d8", "d9", "d10", "d11", "Prueba de paridad",
                                                     "Bit de paridad"), show="headings", height=6)
    table.configure(style="MyCustom.Treeview")
    table.grid(row=0, column=0)

    table.heading(" ", text=" ")
    table.heading("p1", text="p1")
    table.heading("p2", text="p2")
    table.heading("d1", text="d1")
    table.heading("p3", text="p3")
    table.heading("d2", text="d2")
    table.heading("d3", text="d3")
    table.heading("d4", text="d4")
    table.heading("p4", text="p4")
    table.heading("d5", text="d5")
    table.heading("d6", text="d6")
    table.heading("d7", text="d7")
    table.heading("d8", text="d8")
    table.heading("d9", text="d9")
    table.heading("d10", text="d10")
    table.heading("d11", text="d11")
    table.heading("Prueba de paridad", text="Prueba de paridad")
    table.heading("Bit de paridad", text="Bit de\nparidad")

    table.column(" ", width=180)
    table.column("p1", width=25)
    table.column("p2", width=25)
    table.column("d1", width=25)
    table.column("p3", width=25)
    table.column("d2", width=25)
    table.column("d3", width=25)
    table.column("d4", width=25)
    table.column("p4", width=25)
    table.column("d5", width=25)
    table.column("d6", width=25)
    table.column("d7", width=25)
    table.column("d8", width=25)
    table.column("d9", width=25)
    table.column("d10", width=30)
    table.column("d11", width=30)
    table.column("Prueba de paridad", width=105)
    table.column("Bit de paridad", width=50)

    tableRows = createHammingTable(decodificar(modifiedBinary), ["Palabra de datos recibida:", "p1", "p2", "p3", "p4"])

    table.insert("", "end", values=tableRows[0])
    table.insert("", "end", values=tableRows[1])
    table.insert("", "end", values=tableRows[2])
    table.insert("", "end", values=tableRows[3])
    table.insert("", "end", values=tableRows[4])

    navigateToMenuButton = Button(decodingContainer, text="Volver a menú",
                                  command=lambda: menuWindow())
    navigateToMenuButton.grid(row=1, column=0)


hexWindow()
app.mainloop()
