import tkinter as tk

simbolos_terminales = ['automata', 'alfabeto', 'aceptacion', 'q', '{', '}', ':', ';', ',', 'a-z', '0-9']
simbolos_no_terminales = ['S', 'A', 'V', 'B', 'AL', 'G', 'SM', 'RA', 'F', 'C', 'N', 'D', 'R', 'I', 'Q']

tabla = {
    'S': {'automata': ['A', 'I', 'B', 'V']},
    'A': {'automata': ['automata']},
    'V': {'}': ['}']},
    'B': {'alfabeto': ['AL', 'F']},   
    'AL': {'alfabeto': ['G', ':', 'SM', 'RA', ';']},
    'G': {'alfabeto': ['alfabeto']},
    'SM': {'a...z': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 
           '0...9': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']},
    'RA': {',': [',', 'SM', 'RA']},
    'F': {'aceptacion': ['C', ':', 'N', 'R', ';']},
    'C': {'aceptacion': ['aceptacion']},
    'N': {'q': ['q', 'D']},
    'D': {'0-9': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']},
    'R': {',': [',', 'N', 'R']},
    'I': {'{': ['{']},
    'Q': {'q': ['q']}
}

def validar_cadena():
    cadena = cadena_entry.get()
    resultado = automata(cadena)
    resultado_label.config(text=resultado)

def automata(entrada):
    pila = ['$', 'S']
    entrada = entrada.split()
    while True:
        if not entrada:     
            if pila[-1] == '$':
                return 'Cadena aceptada'
            else:
                return 'Cadena no aceptada'
        if entrada:
            if pila[-1] == '$':
                return 'Cadena no aceptada'

        if pila[-1] in simbolos_terminales:
            if pila[-1] == entrada[0]:
                pila.pop()
                entrada.pop(0)
            else:
                return 'Cadena no aceptada'
        else:
            if pila[-1] == 'N' and entrada[0].isalpha():
                if entrada[0] != 'q':
                    return 'Cadena no aceptada'
                    break

            if entrada[0].isalpha() and entrada[0] not in simbolos_terminales:
                if pila[-1] != 'D':
                    pila.pop()
                    entrada.pop(0)
                    continue

            if entrada[0].isdigit() and entrada[0] not in simbolos_terminales:
                pila.pop()
                entrada.pop(0)
                if entrada[0] == ';':
                    continue
            if entrada[0] == ';' and pila[-1] == 'RA':
                pila.pop()
                continue
            if entrada[0] == ';' and pila[-1] == 'R':
                pila.pop()
                continue
            producciones = tabla[pila[-1]].get(entrada[0])
            if producciones:
                pila.pop()
                for produccion in producciones[::-1]:
                    pila.append(produccion)
            else:
                return 'Cadena no aceptada'

root = tk.Tk()
root.title("Automata")
root.geometry("500x250")

nota_label = tk.Label(root, text="Introduzca una cadena:", font=("Arial", 12))
nota_label.pack(pady=10) 

cadena_entry = tk.Entry(root, font=("Arial", 12), width=50) 
cadena_entry.pack()

validar_button = tk.Button(root, text="Validar", command=validar_cadena, font=("Arial", 12))
validar_button.pack(pady=20)

resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.pack()

root.mainloop()
