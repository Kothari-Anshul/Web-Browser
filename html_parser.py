
from html_tokens import tokens
start = 'html'
# parsing rules for html
def p_html(p):
    'html : element html '
    p[0] = [p[1]] + p[2]  
def p_html_empty(p):
    'html : '
    p[0] = []    
    
def p_element_word(p):
    'element : WORD'
    p[0] = ("word",p[1])
def p_element_tag(p):
    'element : LANGLE WORD tag_arg RANGLE html LANGLESLASH WORD RANGLE '
    p[0] = ("tag-element",p[2],p[3],p[5],p[7])
def p_tag_arg(p):
    'tag_arg : WORD ASSIGN STRING'
    p[0] = {WORD:STRING}
def p_tag_arg_empty(p):
    'tag_arg : '
    p[0] = {}
  
def p_element_javascript(p):
    'element : JSTAG'
    p[0] = ("javascript",p[1])


    
