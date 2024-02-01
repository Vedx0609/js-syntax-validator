from ply import yacc
from lex_if_final import tokens

def p_if_else(p):
    '''if_else : IF LPAREN expressions RPAREN LBRACKET statements RBRACKET ELSE LBRACKET statements RBRACKET
               | IF LPAREN expressions RPAREN LBRACKET statements RBRACKET'''
    p[0] = "Valid"

def p_expressions(p):
    '''expressions : expression LOGICAL expression
                   | expression'''

def p_expression(p):
    '''expression : expression COMPARISON expression
                  | expression BITWISE expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression DIVIDE expression
                  | expression TIMES expression
                  | ULOGICAL expression
                  | UBITWISE expression
                  | LPAREN expression RPAREN
                  | IDENTIFIER
                  | NUMBER
                  | BOOLEAN
                  | NULL
                  | STRING'''

def p_statements(p):
    '''statements : statement statements
                  | statement
                  |'''

def p_statement(p):
    '''statement : assign_stmt
                 | c_log_stmt
                 | IDENTIFIER'''

def p_c_log_stmt(p):
    '''c_log_stmt : C_LOG LPAREN args RPAREN'''

def p_args(p):
    '''args : expression
            | expression COMMA args'''

def p_assign_stmt(p):
    '''assign_stmt : TYPE IDENTIFIER ASSIGN expressions
                   | TYPE IDENTIFIER ASSIGN expression COMMA multiple_assign
                   | IDENTIFIER ASSIGN expressions
                   | IDENTIFIER SHORTHAND expressions'''

def p_multiple_assign(p):
    '''multiple_assign : IDENTIFIER ASSIGN expressions
                       | IDENTIFIER ASSIGN expressions COMMA multiple_assign'''

def p_error(p):
    if p:
        print("Syntax error at token : ",p.value,"\n")
    else:
        print("Syntax error at EOF \n")

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