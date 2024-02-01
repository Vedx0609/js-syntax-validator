from ply import yacc
from lex_array import tokens

# Define precedence and associativity
precedence = (
    ('left', 'COMMA'),
)

def p_statement(p):
    '''statement : declaration SEMICOLON
                 | declaration'''  # Allow the semicolon to be optional
    p[0] = p[1]

def p_declaration(p):
    '''declaration : TYPE IDENTIFIER ASSIGN array'''
    p[0] = {p[1]: {p[2]: p[4]}}

def p_array(p):
    '''array : LBRACKET elements_opt RBRACKET'''
    p[0] = p[2]

def p_elements_opt(p):
    '''elements_opt : elements
                    | elements COMMA
                    | empty'''  # Allow an optional ending comma

def p_elements(p):
    '''elements : value
                | elements COMMA value'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_value(p):
    '''value : NUMBER
             | STRING
             | BOOLEAN
             | NULL
             | array'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

if __name__ == '__main__':
    from lex_array import lexer

    while(True) :
        check = input("Press Y/N to Validate Syntax : ")
        if(check=='N') :
            exit(0)
        else :
            data = input('Enter JavaScript code: ')
            if(not data) :
                continue
            lexer.input(data)
            result = parser.parse(lexer=lexer)
            if result is not None:
                print("Valid Syntax \n")