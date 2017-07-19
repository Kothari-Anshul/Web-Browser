import js_parser
import jstoken
import lex
import yacc

def env_lookup(identifier,env):

   if identifier in env[1]:
      return (env[1])[identifier]
   elif(env[0] == None):
      return None
   else:
      return env_lookup(identifier,env[0])
   
def env_update(identifier,value,env):
    if( identifier in env[1]):
       (env[1])[idenitifier] = value
    elif(env[0] == None):
       (env[1])[identifier] = value
    else:
       env_update(identifier,value,env[0])

env = (None,{})
dict = {"java script string" : ""}
    
def eval_exp(exp,env):
    if(exp[0] == "number"):
        return int(exp[1])
    elif(exp[0] == "identifier"):
        return env_lookup(exp[1],env)
    elif(exp[0] == "binop"):
        a = eval_exp(exp[1],env)
        op = exp[2]
        b = eval_exp(exp[3],env)
        if(op == "+"):
            return  a + b
    elif(exp[0] == "call"):
      #print "inside call"
      fname = exp[1]
      fargs = exp[2]
      if(fname == "write"):
         #print "Inside Write"
         #print (fargs[0])[1]
         if((fargs[0])[0] == "string"):
            dict["java script string"] += (fargs[0])[1]
         elif((fargs[0])[0] == "identifier"):
            value = env_lookup(identifier,env)    # function for converting int into string, google it
            dict["java script string"] += value
         elif((fargs[0])[0] == "number"):
            value =  (fargs[0])[1] # convert the int into string , google for the fucntion available for it.
            dict["java script string"] += value
         return None
      fvalue = env_lookup(fname,env)
      if(fvalue[0] == "function"):
         fparam = fvalue[1]
         fbody = fvalue[2]
         fenv = fvalue[3]
         #print fparam
         #print fbody
         #print fenv
         if (len(fparam) <> len(fargs)):
            print "Incorrect number of arguments"
         else:
            chart = {}
            for i in range(len(fparam)):
               chart[fparam[i]] = eval_exp(fargs[i],env)
            new_env = (fenv,chart)
            #print new_env
            try:
               interpret_js(fbody,new_env)
               return None
            except Exception as return_value:
               return  return_value
      else:
         print "Call to non function"

        
def interpret_js(tree,env):
    for node in tree:
        if(node[0] == "assign"):
            identifier = node[1]
            exp = eval_exp(node[2],env)
            
            env_update(identifier,exp,env)
            #print env
        elif(node[0] == "if-else"):
            if(eval_exp(node[1],env)):
                interpret_js(node[2])
            else:
                interpret_js(node[3])
        elif(node[0] == "function"):
            fname = node[1]
            fparams = node[2]
            fcompoundstmt = node[3]
            env_update(fname,("function",fparams,fcompoundstmt,env),env)
        elif(node[0] == "return"):
          raise Exception(eval_exp(node[1],env))
        elif(node[0] == "call"):
           #print "indide interept call"
           #print node
           eval_exp(node,env)
            
            
def interpret_js_wrapper(input_js):
   jslexer = lex.lex(module = jstoken)
   jslexer.input(input_js)
   jsparser = yacc.yacc(module = js_parser)
   parse_tree = jsparser.parse(input_js,lexer = jslexer)
   interpret_js(parse_tree,env)
   return dict["java script string"]


