simbolos_terminales = ['automata', 'alfabeto', 'aceptacion', 'q', '{', '}', ':', ';', ',','a-z', '0-9']
simbolos_no_terminales = ['S', 'A', 'V', 'B', 'AL', 'G', 'SM', 'RA', 'F', 'C', 'N', 'D', 'R', 'I', 'Q']

class TablaPredicitva():
    def __init__(self):
        self.tabla = {
            'S': {
                'automata': ['A', 'I', 'B', 'V'],
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'A': {
                'automata': ['automata'],
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'V': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': ['}'],
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'B': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': ['AL', 'F'],
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'AL': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': ['G', ':', 'SM', 'RA', ';'],
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'G': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': ['alfabeto'],
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'SM': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': ['a-z'],
                '0-9': ['0-9'],
            },
            'RA': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': [',', 'SM', 'RA'],
                'a-z': None,
                '0-9': None,
            },
            'F': {
                'automata': None,
                'aceptacion': ['C', ':', 'N', 'R', ';'],
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': ['a-z'],
                '0-9': ['0-9'],
            },
            'C': {
                'automata': None,
                'aceptacion': ['aceptacion'],
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'N': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': ['q', 'D'],
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'D': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': ['0-9'],
            },
            'R': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': [',', 'N', 'R'],
                'a-z': None,
                '0-9': None,
            },
            'I': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': None,
                '{': ['{'],
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            },
            'Q': {
                'automata': None,
                'aceptacion': None,
                'alfabeto': None,
                'q': ['q'],
                '{': None,
                '}': None,
                ':': None,
                ';': None,
                ',': None,
                'a-z': None,
                '0-9': None,
            }
        }

class Automata:
    def __init__(self, tabla_predicitva, cadena):
        self.pila = ['$', 'S']
        self.tabla_predicitva = tabla_predicitva
        self.cadena = cadena.split(' ')
        self.cadena.append('$')
        self.cadena.reverse()

    def verificar_cadena(self):
        while len(self.pila) > 0:

            print(self.pila, self.cadena)
            if self.pila[-1] == self.cadena[-1]:
                print(self.pila[-1], self.cadena[-1])
                self.pila.pop()
                self.cadena.pop()
            elif self.pila[-1] in simbolos_terminales:
                return False
            else:
                try:
                    if self.cadena[-1].isalpha() and self.cadena[-1] not in simbolos_terminales:
                        self.cadena.pop()
                        if self.pila[-1] == 'SM':
                            self.cadena.append('a-z')
                        continue

                    if self.cadena[-1].isdigit():
                        self.cadena.pop()
                        if self.pila[-1] == 'SM':
                            self.cadena.append('0-9')
                        if self.pila[-1] == 'D':
                            self.cadena.append('0-9')
                        continue

                    if self.pila[-1] == 'RA' and self.cadena[-1] == ';':
                        self.pila.pop()
                        continue

                    if self.pila[-1] == 'R' and self.cadena[-1] == ';':
                        self.pila.pop()
                        
                        continue

                    produccion = self.tabla_predicitva.tabla[self.pila[-1]][self.cadena[-1]]
                    print('produccion de ', self.pila[-1], self.cadena[-1], produccion)

                    if produccion == ['D', 'q']:
                        produccion.reverse()
                        continue

                    if not produccion:
                        return False
                    self.pila.pop()
                    produccion.reverse()
                    self.pila.extend(produccion)
                except:
                    return False
        return True
    
tabla_predicitva = TablaPredicitva()
automata = Automata(tabla_predicitva, 'automata { alfabeto : a , 2 , a ; aceptacion : q 2 , q 1 ; }')
print(automata.verificar_cadena())
