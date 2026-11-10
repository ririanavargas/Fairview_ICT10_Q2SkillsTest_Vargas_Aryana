
from pyscript import document

# Dictionary containing information about non-metal elements
nonmetals = {
    "Hydrogen": ("H", "Hydrogen", 1, "1.008 u"),
    "Helium": ("He", "Helium", 2, "4.0026 u"),
    "Carbon": ("C", "Carbon", 6, "12.011 u"),
    "Nitrogen": ("N", "Nitrogen", 7, "14.007 u"),
    "Oxygen": ("O", "Oxygen", 8, "15.999 u"),
    "Fluorine": ("F", "Fluorine", 9, "18.998 u"),
    "Neon": ("Ne", "Neon", 10, "20.180 u"),
    "Phosphorus": ("P", "Phosphorus", 15, "30.974 u"),
    "Sulfur": ("S", "Sulfur", 16, "32.06 u"),
    "Chlorine": ("Cl", "Chlorine", 17, "35.45 u"),
    "Argon": ("Ar", "Argon", 18, "39.95 u"),
    "Selenium": ("Se", "Selenium", 34, "78.971 u"),
    "Bromine": ("Br", "Bromine", 35, "79.904 u"),
    "Krypton": ("Kr", "Krypton", 36, "83.80 u"),
    "Iodine": ("I", "Iodine", 53, "126.90 u"),
    "Xenon": ("Xe", "Xenon", 54, "131.29 u"),
    "Astatine": ("At", "Astatine", 85, "210 u"),
    "Radon": ("Rn", "Radon", 86, "222 u"),
    "Tennessine": ("Ts", "Tennessine", 117, "294 u"),
    "Oganesson": ("Og", "Oganesson", 118, "294 u")
}

# Function that searches for the entered element
def Search(e):
    Element1 = document.getElementById("element1").value.strip().title()

    if Element1 in nonmetals:
        result = nonmetals[Element1]

        document.getElementById("name").innerText = Element1
        document.getElementById("symbol").innerText = result[0]
        document.getElementById("number").innerText = result[2]
        document.getElementById("mass").innerText = result[3]

    else:
        document.getElementById("name").innerText = "Element is not found"
        document.getElementById("symbol").innerText = "-"
        document.getElementById("number").innerText = "-"
        document.getElementById("mass").innerText = "-"
