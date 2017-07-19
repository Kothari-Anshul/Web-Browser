
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'htmlLANGLE RANGLE LANGLESLASH WORD STRING ASSIGN JSTAGhtml : element html html : element : WORDelement : LANGLE WORD tag_arg RANGLE html LANGLESLASH WORD RANGLE tag_arg : WORD ASSIGN STRINGtag_arg : element : JSTAG'
    
_lr_action_items = {'LANGLE':([0,2,3,4,10,16,],[1,-3,-7,1,1,-4,]),'WORD':([0,1,2,3,4,6,10,14,16,],[2,6,-3,-7,2,9,2,15,-4,]),'STRING':([11,],[13,]),'JSTAG':([0,2,3,4,10,16,],[3,-3,-7,3,3,-4,]),'RANGLE':([6,8,13,15,],[-6,10,-5,16,]),'LANGLESLASH':([2,3,4,7,10,12,16,],[-3,-7,-2,-1,-2,14,-4,]),'ASSIGN':([9,],[11,]),'$end':([0,2,3,4,5,7,16,],[-2,-3,-7,-2,0,-1,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tag_arg':([6,],[8,]),'html':([0,4,10,],[5,7,12,]),'element':([0,4,10,],[4,4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> html","S'",1,None,None,None),
  ('html -> element html','html',2,'p_html','html_parser.py',6),
  ('html -> <empty>','html',0,'p_html_empty','html_parser.py',9),
  ('element -> WORD','element',1,'p_element_word','html_parser.py',13),
  ('element -> LANGLE WORD tag_arg RANGLE html LANGLESLASH WORD RANGLE','element',8,'p_element_tag','html_parser.py',16),
  ('tag_arg -> WORD ASSIGN STRING','tag_arg',3,'p_tag_arg','html_parser.py',19),
  ('tag_arg -> <empty>','tag_arg',0,'p_tag_arg_empty','html_parser.py',22),
  ('element -> JSTAG','element',1,'p_element_javascript','html_parser.py',26),
]
