from jstoken import tokens
import jstoken
import lex
import yacc
start = 'js'

def p_js(p):
    'js : element js'
    p[0] = [p[1]] + p[2]

def p_js_empty(p):
    'js : '
    p[0] = []
def p_element_stmt(p):
    'element : stmt SEMICOLAN'
    p[0] = p[1]

def p_element_function(p):
    'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compound_stmt'
    p[0] = ("function",p[2],p[4],p[6])
def p_compound_stmt(p):
    'compound_stmt : LBRACE stmts RBRACE'
    p[0] = p[2]
def p_stmts(p):
    'stmts : stmt SEMICOLAN stmts'
    p[0] = [p[1]] + p[3]
def p_stmts_empty(p):
    'stmts : '
    p[0] = []
def p_optparams(p):
    'optparams : params'
    p[0] = p[1]
def p_optparams_empty(p):
    'optparams : '
    p[0] = []
def p_params(p):
    'params : IDENTIFIER COMMA params'
    p[0] = [p[1]] + p[3]
def p_params_empty(p):
    'params : IDENTIFIER'
    p[0] = [p[1]]
def p_stmt_assign(p):
    'stmt : IDENTIFIER ASSIGN exp'
    p[0] = ("assign",p[1],p[3])
def p_stmt_if_else(p):
    'stmt : IF exp compound_stmt ELSE compound_stmt'
    p[0] = ("if-else",p[2],p[3],p[5])
def p_stmt_exp(p):
    'stmt : exp'
    p[0] = p[1]
    
def p_exp_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN '
    p[0] = ("call",p[1],p[3])

def p_optargs(p):
    'optargs : args'
    p[0] = p[1]
def p_optargs_empty(p):
    'optargs : '
    p[0] =[]


def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]
def p_args_empty(p):
    'args : exp'
    p[0] = [p[1]]
    
def p_stmt_return(p):
    'stmt : RETURN exp'
    p[0] = ("return",p[2])

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number",p[1])
def p_exp_string(p):
    'exp : STRING'
    p[0] = ("string",p[1])
def p_exp_identifier(p):
    'exp : IDENTIFIER'
    p[0] = ("identifier",p[1])
def p_exp_binop(p):
    """exp : exp PLUS exp 
        | exp MINUS exp
        | exp TIMES exp
        | exp DIVIDE exp"""
    p[0] = ("binop",p[1],p[2],p[3])

#js_input  = """ x = sum(4,5);"""
#jslexer = lex.lex(module = jstoken)
#jslexer.input(js_input)
#js_parser = yacc.yacc()
#ast = js_parser.parse(js_input,lexer=jslexer)
#print ast

