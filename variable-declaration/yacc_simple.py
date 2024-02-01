from ply import yacc
from lex_simple import tokens

def p_statement_simple(p):
    '''statement_simple : TYPE IDENTIFIER ASSIGN expressions
                        | TYPE IDENTIFIER ASSIGN expressions COMMA multiple_assign
                        | IDENTIFIER ASSIGN expressions'''
    p[0] = 'Valid'

def p_expressions(p):
    '''expressions : expression
                   | expression SEMICOLON
                   | expression LOGICAL expressions'''

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | IDENTIFIER
                  | NUMBER
                  | BOOLEAN
                  | NULL
                  | STRING'''

def p_multiple_assign(p):
    '''multiple_assign : IDENTIFIER ASSIGN expression
                       | IDENTIFIER ASSIGN expression COMMA multiple_assign'''

def p_error(p):
    print(f"Syntax error at {p.value}\n")

parser = yacc.yacc()

while True:
    try:
        check = input("Press Y/N to Validate Syntax : ")
        if(check=='N') :
            exit(0)
        else :
            s = input('Enter JavaScript code: ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    if(result=="Valid") :
        print("Valid syntax \n")