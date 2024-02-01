from ply import lex

tokens = (
    'IF',
    'ELSE',
    'TYPE',
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'ASSIGN',
    'SHORTHAND',
    'LOGICAL',
    'ULOGICAL',
    'BITWISE',
    'UBITWISE',
    'COMPARISON',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'C_LOG',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'NULL',
    'BOOLEAN',
    'COMMA',
)

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ASSIGN = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_COMMA = r','

t_ignore = ' \t'

def t_IF(t):
    r'''if'''
    return t

def t_ELSE(t):
    r'''else'''
    return t

def t_TYPE(t):
    r'''const|let|var'''
    return t

def t_C_LOG(t):
    r'''console\.log'''
    return t

def t_NUMBER(t):
    r'''\d+\.\d+|\d+'''
    return t

def t_STRING(t):
    r'''\"([^\\\n]|(\\.))*?\"'''
    return t

def t_BOOLEAN(t):
    r'''true | false'''
    return t

def t_NULL(t):
    r'''null'''

def t_LOGICAL(t):
    r'''\&\& | \|\|'''
    return t

def t_SHORTHAND(t):
    r'''\^\= | \&\= | \|\= | \~\= | \>\>\= | \<\<\= | \>\>\>\= | \+\= | \-\= | \*\= | \/\='''
    return t

def t_ULOGICAL(t):
    r'''\!'''
    return t

def t_BITWISE(t):
    r'''\& | \| | \^ | \>\> | \<\< | \>\>\>'''
    return t

def t_UBITWISE(t):
    r'''\~'''
    return t

def t_COMPARISON(t):
    r'''\=\=| \=\=\= | \>|\<|\>\=|\<\=|\!\='''
    return t

def t_newline(t):
    r'''\n+'''
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()   