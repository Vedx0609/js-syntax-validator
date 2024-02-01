from ply import lex

# List of token names
tokens = (
    'TYPE',
    'IDENTIFIER',
    'ASSIGN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'NUMBER',
    'STRING',
    'BOOLEAN',
    'NULL',
    'SEMICOLON',
)

# Regular expression rules for simple tokens
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'

def t_TYPE(t):
    r'const|let|var'
    return t

def t_NUMBER(t):
    r'\d+\.\d+|\d+'  # Matches both float and integer numbers
    try:
        t.value = int(t.value)  # Try to convert to int
    except ValueError:
        t.value = float(t.value)  # If conversion to int fails, convert to float
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()