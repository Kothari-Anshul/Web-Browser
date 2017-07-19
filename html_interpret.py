import lex
import yacc
import html_parser
import html_tokens
import graphics
import js_interpret
from jstoken import tokens
import js_parser

import jstoken

def interpret_html(tree):
    for node in tree:
        if(node[0] == "word"):
            graphics.word(node[1])
        elif(node[0] == "tag-element"):
            tag_open = node[1]
            tag_args = node[2]
            inner_html = node[3]
            tag_close = node[4]
            if(tag_open == tag_close):
                graphics.begintag(tag_open,tag_args)
                interpret_html(inner_html)
                graphics.endtag()
            else:
                graphics.warning("Invalid Web Page!")
        elif(node[0] == "javascript"):
            str = js_interpret.interpret_js_wrapper(node[1])
            print str
            #graphics.word(str)
                
web_page = """<script> write("hello worlbjiobjfipbjfibjiobjfd!");</script>"""
html_lexer = lex.lex(module=html_tokens)
html_parser = yacc.yacc(module=html_parser)
html_lexer.input(web_page)
parse_tree = html_parser.parse(web_page,lexer=html_lexer)
#print parse_tree
#graphics.initialize()
interpret_html(parse_tree)
#graphics.finalize()
#print parse_tree

