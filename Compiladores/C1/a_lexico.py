import tkinter as tk
from ply import lex

tokens = (
    'TYPE',
    'RESERVED_WORD',
    'IDENTIFIER',
    'EQUALS',
    'NUMBER',
    'STRING',
    'BOOLEAN',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'COLON',
    'OPERATOR',
    'CONTENT',
    'ILLEGAL_CHARACTER',
)

t_TYPE = r"(X|Y|B)"
t_RESERVED_WORD = r"LT|RT|RB|START"
t_EQUALS = r"="
t_IDENTIFIER = r"[a-z][a-z]*"
t_LEFT_PAREN = r"\("
t_RIGHT_PAREN = r"\)"
t_COLON = r":"
t_OPERATOR = r">|<|>=|<=|==|!="
t_CONTENT = r"C"
t_NUMBER = r"\d+"
t_BOOLEAN = r"True|False"
t_STRING = r'"[^"]*"'

t_ignore = ' \t'

token_elements = {token_type.lower(): [] for token_type in tokens}

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter no reconocido: '{t.value[0]}'")
    # agregar el caracter no reconocido a la lista de elementos
    token_elements['illegal_character'].append(t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def process_input():
    input_text = input_entry.get("1.0", "end-1c")

    for token_type in tokens:
        token_elements[token_type.lower()] = []
    
    lexer.input(input_text)

    while True:
        tok = lexer.token()
        if not tok:
            break
        token_elements[tok.type.lower()].append(tok.value)

    for i, token_type in enumerate(tokens):
        elements_str = ', '.join(map(str, token_elements[token_type.lower()]))
        count_label_vars[i].set(elements_str)

root = tk.Tk()
root.title("Elementos de Tokens")
# ancho x alto
root.geometry("700x550")
# tamaño de letra
root.option_add("*Font", "consolas 10")

# label para la entrada
input_entry = tk.Text(root, wrap="word", width=80, height=5)
input_entry.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=40)

# Botón
process_button = tk.Button(root, text="Procesar", command=process_input)
process_button.grid(row=1, column=0, columnspan=2, pady=(0, 20))

# etiqueta y una variable para cada tipo de token
count_label_vars = []
for i, token_type in enumerate(tokens):
    tk.Label(root, text=token_type, anchor="w").grid(row=i + 2, column=0)
    count_label_var = tk.StringVar()
    count_label_vars.append(count_label_var)
    tk.Label(root, textvariable=count_label_var).grid(row=i + 2, column=1)

root.mainloop()
