from ply import yacc
from lex_while import tokens

def p_statement_while(p):
    '''statement_while : WHILE LPAREN expressions RPAREN LBRACKET statements RBRACKET'''
    p[0] = 'Valid'

def p_expressions(p):
    '''expressions : expression
                   | expression LOGICAL expressions'''

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | BOOLEAN
                  | NULL
                  | STRING
                  | expression BITWISE expression
                  | UBITWISE expression
                  | expression COMPARISON expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | ULOGICAL expression'''

def p_statements(p):
    '''statements : statement
                  | statement statements'''

def p_statement(p):
    '''statement : assign_stmt
                 | c_log_stmt
                 | statement_while'''

def p_c_log_stmt(p):
    '''c_log_stmt : C_LOG LPAREN args RPAREN'''

def p_args(p):
    '''args : expression
            | expression COMMA args'''

def p_assign_stmt(p):
    '''assign_stmt : TYPE IDENTIFIER ASSIGN expressions
                   | TYPE IDENTIFIER ASSIGN expression COMMA multiple_assign
                   | IDENTIFIER ASSIGN expressions
                   | IDENTIFIER SHORTHAND expressions
                   | IDENTIFIER INCREMENT
                   | IDENTIFIER DECREMENT
                   | INCREMENT IDENTIFIER
                   | DECREMENT IDENTIFIER'''

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