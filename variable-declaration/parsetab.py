
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BOOLEAN COMMA DIVIDE IDENTIFIER LOGICAL MINUS NULL NUMBER PLUS SEMICOLON STRING TIMES TYPEstatement_simple : TYPE IDENTIFIER ASSIGN expressions\n                        | TYPE IDENTIFIER ASSIGN expressions COMMA multiple_assign\n                        | IDENTIFIER ASSIGN expressionsexpressions : expression\n                   | expression SEMICOLON\n                   | expression LOGICAL expressionsexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | IDENTIFIER\n                  | NUMBER\n                  | BOOLEAN\n                  | NULL\n                  | STRINGmultiple_assign : IDENTIFIER ASSIGN expression\n                       | IDENTIFIER ASSIGN expression COMMA multiple_assign'
    
_lr_action_items = {'TYPE':([0,],[2,]),'IDENTIFIER':([0,2,5,6,16,17,18,19,20,21,29,31,],[3,4,7,7,7,7,7,7,7,27,7,27,]),'$end':([1,7,8,9,10,11,12,13,14,15,22,23,24,25,26,28,30,32,],[0,-11,-3,-4,-12,-13,-14,-15,-1,-5,-6,-7,-8,-9,-10,-2,-16,-17,]),'ASSIGN':([3,4,27,],[5,6,29,]),'NUMBER':([5,6,16,17,18,19,20,29,],[10,10,10,10,10,10,10,10,]),'BOOLEAN':([5,6,16,17,18,19,20,29,],[11,11,11,11,11,11,11,11,]),'NULL':([5,6,16,17,18,19,20,29,],[12,12,12,12,12,12,12,12,]),'STRING':([5,6,16,17,18,19,20,29,],[13,13,13,13,13,13,13,13,]),'SEMICOLON':([7,9,10,11,12,13,23,24,25,26,],[-11,15,-12,-13,-14,-15,-7,-8,-9,-10,]),'LOGICAL':([7,9,10,11,12,13,23,24,25,26,],[-11,16,-12,-13,-14,-15,-7,-8,-9,-10,]),'PLUS':([7,9,10,11,12,13,23,24,25,26,30,],[-11,17,-12,-13,-14,-15,17,17,17,17,17,]),'MINUS':([7,9,10,11,12,13,23,24,25,26,30,],[-11,18,-12,-13,-14,-15,18,18,18,18,18,]),'TIMES':([7,9,10,11,12,13,23,24,25,26,30,],[-11,19,-12,-13,-14,-15,19,19,19,19,19,]),'DIVIDE':([7,9,10,11,12,13,23,24,25,26,30,],[-11,20,-12,-13,-14,-15,20,20,20,20,20,]),'COMMA':([7,9,10,11,12,13,14,15,22,23,24,25,26,30,],[-11,-4,-12,-13,-14,-15,21,-5,-6,-7,-8,-9,-10,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_simple':([0,],[1,]),'expressions':([5,6,16,],[8,14,22,]),'expression':([5,6,16,17,18,19,20,29,],[9,9,9,23,24,25,26,30,]),'multiple_assign':([21,31,],[28,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_simple","S'",1,None,None,None),
  ('statement_simple -> TYPE IDENTIFIER ASSIGN expressions','statement_simple',4,'p_statement_simple','yacc_simple.py',5),
  ('statement_simple -> TYPE IDENTIFIER ASSIGN expressions COMMA multiple_assign','statement_simple',6,'p_statement_simple','yacc_simple.py',6),
  ('statement_simple -> IDENTIFIER ASSIGN expressions','statement_simple',3,'p_statement_simple','yacc_simple.py',7),
  ('expressions -> expression','expressions',1,'p_expressions','yacc_simple.py',11),
  ('expressions -> expression SEMICOLON','expressions',2,'p_expressions','yacc_simple.py',12),
  ('expressions -> expression LOGICAL expressions','expressions',3,'p_expressions','yacc_simple.py',13),
  ('expression -> expression PLUS expression','expression',3,'p_expression','yacc_simple.py',16),
  ('expression -> expression MINUS expression','expression',3,'p_expression','yacc_simple.py',17),
  ('expression -> expression TIMES expression','expression',3,'p_expression','yacc_simple.py',18),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','yacc_simple.py',19),
  ('expression -> IDENTIFIER','expression',1,'p_expression','yacc_simple.py',20),
  ('expression -> NUMBER','expression',1,'p_expression','yacc_simple.py',21),
  ('expression -> BOOLEAN','expression',1,'p_expression','yacc_simple.py',22),
  ('expression -> NULL','expression',1,'p_expression','yacc_simple.py',23),
  ('expression -> STRING','expression',1,'p_expression','yacc_simple.py',24),
  ('multiple_assign -> IDENTIFIER ASSIGN expression','multiple_assign',3,'p_multiple_assign','yacc_simple.py',27),
  ('multiple_assign -> IDENTIFIER ASSIGN expression COMMA multiple_assign','multiple_assign',5,'p_multiple_assign','yacc_simple.py',28),
]
