from ply import lex

tokens = (
    'TYPE',
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'BOOLEAN',
    'ASSIGN',
    'LOGICAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'NULL',
    'SEMICOLON',
    'COMMA',
)

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ASSIGN = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_COMMA = r','
t_SEMICOLON = r';'

t_ignore = ' \t'

def t_TYPE(t):
    r'''const|let|var'''
    return t

def t_NUMBER(t):
    r'''\d+\.\d+|\d+'''
    return t

def t_STRING(t):
    r'''\"([^\\\n]|(\\.))*?\"'''
    return t

def t_BOOLEAN(t):
    r'''true|false'''
    return t

def t_NULL(t):
    r'''null'''
    return t

def t_LOGICAL(t):
    r'''\&\&|\|\|'''
    return t

def t_newline(t):
    r'''\n+'''
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'\n")
    t.lexer.skip(1)

lexer = lex.lex()   