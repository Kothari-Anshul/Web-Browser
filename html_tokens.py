#import lex
tokens = ("LANGLE","RANGLE","LANGLESLASH","WORD","STRING","ASSIGN","JSTAG")

states = (
    ('htmlcomment','exclusive'),
    
)

t_ignore = ' '
t_htmlcomment_ignore = ' '


def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment')

def t_htmlcomment_end(token):
    r'-->'
    
    token.lexer.lineno += token.value.count('\n')
    token.lexer.begin('INITIAL')
def t_htmlcomment_error(token):
    token.lexer.skip(1)


def t_JSTAG(token):
    r'\<script\>(?:.|\n)*\<\/script\>'
    token.value = token.value[8:-9]
    return token

def t_NEWLINE(token):
    r'\n'
    token.lexer.lineno += 1
    pass
    
def t_LANGLESLASH(token):
    r'</'
    return token
def t_LANGLE(token):
    r'\<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_STRING(token):
    r'\"[^"]*\"'
    token.value = token.value[1:-1]
    return token
def t_WORD(token):
    r'[^<>\n]+'
    return token
def t_ASSIGN(token):
    r'\='
    return token
def t_error(token):
    print "Error" + token.value


    


