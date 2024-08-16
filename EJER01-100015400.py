#mi primer analizador lexico que solo me reconocer 
# numeros enteros, identificadores, operadores
# librerias: lexico, re
# Luisa Maria Santiago Siliceo 100015400

import re

#crear tokens
token_patterns = [
    ('NUMERO', r'\d+'),                      # 1 Número entero
    ('IF', r'\bif\b'),                       # 2 Palabra clave if
    ('ELSE', r'\belse\b'),                   # 3 Palabra clave else
    ('WHILE', r'\bwhile\b'),                 # 4 Palabra clave while
    ('FOR', r'\bfor\b'),                     # 5 Palabra clave for
    ('RETURN', r'\breturn\b'),               # 6 Palabra clave return
    ('TRUE', r'\btrue\b'),                   # 7 Valor booleano true
    ('FALSE', r'\bfalse\b'),                 # 8 Valor booleano false
    ('NULL', r'\bnull\b'),                   # 9 Valor nulo
    ('FUNCTION', r'\bfunction\b'),           # 10 Palabra clave function
    ('IDENTIFICADOR', r'[A-Za-z]\w*'),       # 11 Identificador
    ('SUMA_ASIG', r'\+='),                   # 12 Suma y asignación
    ('RESTA_ASIG', r'-='),                   # 13 Resta y asignación
    ('MULTP_ASIG', r'\*='),                  # 14 Multiplicación y asignación
    ('DIV_ASIG', r'/='),                     # 15 División y asignación
    ('MODULO_ASIG', r'%='),                  # 16 Módulo y asignación  
    ('INCREMENTO', r'\++'),                  # 17 Incremento
    ('DECREMENTO', r'--'),                   # 18 Decremento
    ('SUMA', r'\+'),                         # 19 Operador de suma
    ('RESTA', r'-'),                         # 20 Operador de resta
    ('MULTIPLICACION', r'\*'),               # 21 Operador de multiplicación
    ('DIVISION', r'/'),                      # 22 Operador de división
    ('PARENTESIS_IZQ', r'\('),               # 23 Paréntesis izquierdo
    ('PARENTESIS_DER', r'\)'),               # 24 Paréntesis derecho
    ('ESPACIO', r'\s+'),                     # 25 Espacios
    ('LLAVE_IZQ', r'{'),                     # 26 Llave izquierda
    ('LLAVE_DER', r'}'),                     # 27 Llave derecha
    ('CORCHETE_IZQ', r'\['),                 # 28 Corchete izquierdo
    ('CHORCHETE_DER', r'\]'),                # 29 Corchete derecho
    ('DOS_PUNTOS', r':'),                    # 30 Dos puntos
    ('COMA', r','),                          # 31 Coma
    ('PUNT0_COMA', r';'),                    # 32 Punto y coma
    ('DIFERENTE', r'!='),                    # 33 Diferente  
    ('MENOR_IGUAL', r'<='),                  # 34 Menor igual
    ('MAYOR_IGUAL', r'>='),                  # 35 Mayor igual
    ('IGUAL_QUE', r'=='),                    # 36 Igualdad
    ('AND_LOG', r'&&'),                      # 37 AND lógico
    ('OR_LOG', r'\|\|'),                     # 38 OR lógico 
    ('OR', r'\|'),                           # 39 Símbolo o
    ('AMPER', r'&'),                         # 40 Amper
    ('MENOR_QUE', r'<'),                     # 41 Símbolo menor que
    ('MAYOR_QUE', r'>'),                     # 42 Símbolo mayor que
    ('IGUAL', r'='),                         # 43 Igual
    ('MODULO', r'%'),                        # 44 Módulo
    ('ARROBA', r'@'),                        # 45 Arroba
    ('AND', r'\^'),                          # 46 Símbolo y 
    ('GUION', r'_'),                         # 47 Guion
    ('TILDE', r'~'),                         # 48 Tilde
    ('EXCLAMACION_DER', r'¡'),               # 49 Exclamación derecha
    ('EXCLAMACION_IZQ', r'!'),               # 50 Exclamación izquierda           
    ('SIMBOLO', r'.'),                        

]

# token expresiones regulares patrones
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)
get_token = re.compile(token_regex).match

def tokenize(code):
    line_number = 1
    line_start = 0
    position = 0
    tokens = []

    while position < len(code):
        match = get_token(code, position)
        if not match:
            raise RuntimeError(f'Error de Analisis en posicion {position}')
        
        for name, value in match.groupdict().items():
            if value:
                if name != 'ESPACIO':
                    tokens.append((name, value))
                break
        position = match.end()

    return tokens  # Mover el return fuera del bucle while



code = "if (x == 10) { return x + 1; }" 
tokens = tokenize(code)
print(f"{'Token':<20} {'Lexema':<15} {'Patrón'}")
print('-' * 45)
for token in tokens:
    token_type, lexeme = token
    # Buscar el patrón correspondiente al token
    for name, pattern in token_patterns:
        if name == token_type:
            print(f"{token_type:<20} {lexeme:<15} {pattern}")
            break