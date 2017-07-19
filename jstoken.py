

tokens = (
    "IDENTIFIER",
    "NUMBER",
    "STRING",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "ASSIGN",
    "LPAREN",
    "RPAREN",
    "COMMA",
    "LBRACE",
    "RBRACE",
    "ANDAND",
    "ELSE",
    "EQUALEQUAL",
    "FALSE",
    "FUNCTION",
    "GE",
    "GT",
    "IF",
    "LE",
    "LT",
    "NOT",
    "OROR",
    "RETURN",
    "SEMICOLAN",
    "TRUE",
    "VAR"
    )
t_ignore = ' '
def t_NEWLINE(token):
    r'\n'
    token.lexer.lineno += 1
    pass
def t_eof_comment(token):
    r'//[^\n]*'
    pass

def t_ANDAND(token):
    r'\&\&'
    return token
def t_ELSE(token):
    r'else'
    return token
def t_EQUALEQUAL(token):
    r'\=\='
    return token
def t_FALSE(token):
    r'false'
    return token
def t_FUNCTION(token):
    r'function'
    return token
def t_GE(token):
    r'\>\='
    return token
def t_GT(token):
    r'\>'
    return token
def t_IF(token):
    r'if'
    return token
def t_LE(token):
    r'\<\='
    return token
def t_LT(token):
    r'\<'
    return token
def t_NOT(token):
    r'\!'
    return token
def t_OROR(token):
    r'\|\|'
    return token
def t_RETURN(token):
    r'return'
    return token
def t_SEMICOLAN(token):
    r'\;'
    return token
def t_TRUE(token):
    r'true'
    return token
def t_VAR(token):
    r'var'
    return token
def t_IDENTIFIER(token):
    r'[a-zA-Z][a-zA-Z_]*'
    return token
def t_NUMBER(token):
    r'[0-9]+'
    return token
def t_PLUS(token):
    r'\+'
    return token
def t_MINUS(token):
    r'\-'
    return token
def t_TIMES(token):
    r'\*'
    return token
def t_DIVIDE(token):
    r'\/'
    return token
def t_ASSIGN(token):
    r'\='
    return token
def t_LPAREN(token):
    r'\('
    return token
def t_RPAREN(token):
    r'\)'
    return token
def t_COMMA(token):
    r'\,'
    return token
def t_LBRACE(token):
    r'\{'
    return token
def t_RBRACE(token):
    r'\}'
    return token

def t_STRING(token):
    r'\"[^\n]+\"'
    token.value = token.value[1:-1]
    return token
def t_error(token):
    print "Error" + token.value

