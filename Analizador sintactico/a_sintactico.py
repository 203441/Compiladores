import ply.yacc as yacc

def check_syntax(input_text, tokens):
    tokens = tokens

    # Definición de las reglas de la gramática
    def p_statement(p):
        '''statement : variable_declaration
                     | function_declaration
                     | condition_declaration
                     | start_declaration'''
        p[0] = p[1]

    def p_variable_declaration(p):
        '''variable_declaration : TYPE IDENTIFIER EQUALS value'''
        value_type = p[4]['type']
        if p[1] == 'X' and value_type != 'NUMBER':
            print("Error: Se esperaba un valor entero para la variable tipo X.")
            p[0] = False
        elif p[1] == 'Y' and value_type != 'STRING':
            print("Error: Se esperaba una cadena para la variable tipo Y.")
            p[0] = False
        elif p[1] == 'B' and value_type != 'BOOLEAN':
            print("Error: Se esperaba un valor boleano para la variable tipo B.")
            p[0] = False
        else:
            p[0] = True

    def p_function_declaration(p):
        '''function_declaration : RESERVED_WORD IDENTIFIER LEFT_PAREN RIGHT_PAREN COLON CONTENT'''
        if p[1] != 'LT':
            print("Error: La funcion debe comenzar con la palabra reservada 'LT'.")
            p[0] = False
        else:
            p[0] = True 

    def p_condition_declaration(p):
        '''condition_declaration : RESERVED_WORD expression COLON CONTENT'''
        if p[1] != 'RB' and p[1] != 'RT':
            print("Error: Debe comenzar con la palabra reservada 'RB' o 'RT'.")
            p[0] = False
        else:
            p[0] = True

    def p_start_declaration(p):
        '''start_declaration : RESERVED_WORD COLON CONTENT'''
        if p[1] != 'START':
            print("Error: La funcion main debe comenzar con la palabra reservada 'START'.")
            p[0] = False
        else:
            p[0] = True

    def p_expression(p):
        '''expression : value_exp OPERATOR value_exp'''
        p[0] = True

    def p_value_expression(p):
        '''value_exp : IDENTIFIER
                    | NUMBER
                    | BOOLEAN'''
        p[0] = {'type': p.slice[1].type}

    def p_value(p):
        '''value : NUMBER
                 | STRING
                 | BOOLEAN'''
        p[0] = {'type': p.slice[1].type}

    def p_error(p):
        print("Error de sintaxisZZ")

    parser = yacc.yacc()

    try:
        result = parser.parse(input_text)
        return result
    except Exception as e:
        print("Error:", e)
        return False
