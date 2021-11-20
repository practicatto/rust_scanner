
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDAND ARROW AS ASIGNAR ASIGNATION_TYPE ASYNC AWAIT BRACKETL BRACKETR BREAK B_FALSE B_TRUE COMMA CONST CONTAINS_SLICE CONTIN CRATE DATATYPES DIFFERENT DIVISION DOLLAR DOT DOTDOTDOT DYN ELSE ENDLINE ENUM EQUAL ERRORPROP EXTERN FOR FUNCTION GET_SLICE GREATEQ GREATER HASHSET IF IMPL IN INSERT_HASH LESSEQ LESST LET LLAVEDER LLAVEIZ LOOP LPAREN MAS MATCH MAYOR MAYORIGUAL MENOS MINUSEQ MOD MODULO MOVE MULT MUT NEWFUNC NOT NUMBER NUMDATATYPES OR OROR PATHSEP PLUSEQ POP_VEC PRINT PRINTS PUB PUSH_VEC REF RETURN RPAREN SELF SELFLOWERCASE SLASHEQ STAREQ STATIC STRING STRUCT SUPER TRAIT TYPE U8 UNION_HASH UNSAFE USE VARIABLE VECTOR WHERE WHILE\n    rust : asignacion\n         | prints\n         | hashset\n         | hashfunc\n         | conditional\n         | conditional_asigned\n\n    \n    asignacion : declarador ASIGNAR expresion ENDLINE\n                | other_operators ENDLINE\n    \n    other_operators : VARIABLE oper_asig expresion\n    \n    declarador : VARIABLE\n                | let_asig\n    \n    let_asig : LET var_tipo\n             | LET MUT var_tipo\n    \n    var_tipo : VARIABLE\n             | VARIABLE  ASIGNATION_TYPE tipos\n    \n    tipos : DATATYPES\n            | NUMDATATYPES\n    \n    oper_asig : ASIGNAR\n                | PLUSEQ\n                | MINUSEQ\n                | STAREQ\n                | SLASHEQ\n    \n    expresion : STRING\n                | U8\n    \n    prints : PRINTS LPAREN print_expresion RPAREN ENDLINE\n    \n    print_expresion : STRING\n                    | STRING COMMA print_args\n    \n    print_args : print_datos COMMA print_args \n                | print_datos\n    \n    print_datos : expresion\n    \n    hashset : LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE\n    \n    hashfunc : hashset_insert\n            | hashset_union\n    \n    hashset_insert : VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE\n    \n    hashset_union : VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE\n    \n    conditional_asigned : declarador ASIGNAR conditional ENDLINE\n    \n    conditional : if_type validations LLAVEIZ rust LLAVEDER\n    \n    if_type : IF\n            | ELSE IF\n            | ELSE\n    \n    validations : comparison\n                | comparison ANDAND validations\n                | comparison OROR validations\n    \n    comparison : VARIABLE GREATER VARIABLE\n    '
    
_lr_action_items = {'PRINTS':([0,48,],[10,10,]),'LET':([0,48,],[11,11,]),'VARIABLE':([0,11,15,17,18,22,35,48,49,50,51,72,],[12,23,34,-38,-40,42,-39,12,34,34,65,77,]),'IF':([0,18,19,48,],[17,35,17,17,]),'ELSE':([0,19,48,],[18,18,18,]),'$end':([1,2,3,4,5,6,7,13,14,20,52,53,66,73,80,82,83,],[0,-1,-2,-3,-4,-5,-6,-32,-33,-8,-7,-36,-25,-37,-34,-31,-35,]),'LLAVEDER':([2,3,4,5,6,7,13,14,20,52,53,62,66,73,80,82,83,],[-1,-2,-3,-4,-5,-6,-32,-33,-8,-7,-36,73,-25,-37,-34,-31,-35,]),'ASIGNAR':([8,12,16,23,24,42,43,57,58,59,],[19,27,-11,-14,-12,56,-13,-15,-16,-17,]),'ENDLINE':([9,36,37,38,39,45,54,73,76,79,81,],[20,52,53,-23,-24,-9,66,-37,80,82,83,]),'LPAREN':([10,46,47,],[21,60,61,]),'MUT':([11,],[22,]),'DOT':([12,],[26,]),'PLUSEQ':([12,],[28,]),'MINUSEQ':([12,],[29,]),'STAREQ':([12,],[30,]),'SLASHEQ':([12,],[31,]),'STRING':([19,21,25,27,28,29,30,31,55,60,74,],[38,41,38,-18,-19,-20,-21,-22,38,38,38,]),'U8':([19,25,27,28,29,30,31,55,60,74,],[39,39,-18,-19,-20,-21,-22,39,39,39,]),'ASIGNATION_TYPE':([23,42,],[44,44,]),'INSERT_HASH':([26,],[46,]),'UNION_HASH':([26,],[47,]),'LLAVEIZ':([32,33,63,64,65,],[48,-41,-42,-43,-44,]),'ANDAND':([33,65,],[49,-44,]),'OROR':([33,65,],[50,-44,]),'GREATER':([34,],[51,]),'COMMA':([38,39,41,68,69,],[-23,-24,55,74,-30,]),'RPAREN':([38,39,40,41,67,68,69,71,77,78,],[-23,-24,54,-26,-27,-29,-30,76,81,-28,]),'DATATYPES':([44,],[58,]),'NUMDATATYPES':([44,],[59,]),'HASHSET':([56,],[70,]),'AND':([61,],[72,]),'PATHSEP':([70,],[75,]),'NEWFUNC':([75,],[79,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rust':([0,48,],[1,62,]),'asignacion':([0,48,],[2,2,]),'prints':([0,48,],[3,3,]),'hashset':([0,48,],[4,4,]),'hashfunc':([0,48,],[5,5,]),'conditional':([0,19,48,],[6,37,6,]),'conditional_asigned':([0,48,],[7,7,]),'declarador':([0,48,],[8,8,]),'other_operators':([0,48,],[9,9,]),'hashset_insert':([0,48,],[13,13,]),'hashset_union':([0,48,],[14,14,]),'if_type':([0,19,48,],[15,15,15,]),'let_asig':([0,48,],[16,16,]),'var_tipo':([11,22,],[24,43,]),'oper_asig':([12,],[25,]),'validations':([15,49,50,],[32,63,64,]),'comparison':([15,49,50,],[33,33,33,]),'expresion':([19,25,55,60,74,],[36,45,69,71,69,]),'print_expresion':([21,],[40,]),'tipos':([44,],[57,]),'print_args':([55,74,],[67,78,]),'print_datos':([55,74,],[68,68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> rust","S'",1,None,None,None),
  ('rust -> asignacion','rust',1,'p_rust','sintactico.py',14),
  ('rust -> prints','rust',1,'p_rust','sintactico.py',15),
  ('rust -> hashset','rust',1,'p_rust','sintactico.py',16),
  ('rust -> hashfunc','rust',1,'p_rust','sintactico.py',17),
  ('rust -> conditional','rust',1,'p_rust','sintactico.py',18),
  ('rust -> conditional_asigned','rust',1,'p_rust','sintactico.py',19),
  ('asignacion -> declarador ASIGNAR expresion ENDLINE','asignacion',4,'p_asignacion','sintactico.py',25),
  ('asignacion -> other_operators ENDLINE','asignacion',2,'p_asignacion','sintactico.py',26),
  ('other_operators -> VARIABLE oper_asig expresion','other_operators',3,'p_other_operators','sintactico.py',31),
  ('declarador -> VARIABLE','declarador',1,'p_declarador','sintactico.py',36),
  ('declarador -> let_asig','declarador',1,'p_declarador','sintactico.py',37),
  ('let_asig -> LET var_tipo','let_asig',2,'p_let_asig','sintactico.py',42),
  ('let_asig -> LET MUT var_tipo','let_asig',3,'p_let_asig','sintactico.py',43),
  ('var_tipo -> VARIABLE','var_tipo',1,'p_var_tipo','sintactico.py',48),
  ('var_tipo -> VARIABLE ASIGNATION_TYPE tipos','var_tipo',3,'p_var_tipo','sintactico.py',49),
  ('tipos -> DATATYPES','tipos',1,'p_tipos','sintactico.py',54),
  ('tipos -> NUMDATATYPES','tipos',1,'p_tipos','sintactico.py',55),
  ('oper_asig -> ASIGNAR','oper_asig',1,'p_oper_asig','sintactico.py',60),
  ('oper_asig -> PLUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',61),
  ('oper_asig -> MINUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',62),
  ('oper_asig -> STAREQ','oper_asig',1,'p_oper_asig','sintactico.py',63),
  ('oper_asig -> SLASHEQ','oper_asig',1,'p_oper_asig','sintactico.py',64),
  ('expresion -> STRING','expresion',1,'p_expresion','sintactico.py',69),
  ('expresion -> U8','expresion',1,'p_expresion','sintactico.py',70),
  ('prints -> PRINTS LPAREN print_expresion RPAREN ENDLINE','prints',5,'p_prints','sintactico.py',75),
  ('print_expresion -> STRING','print_expresion',1,'p_print_expresion','sintactico.py',80),
  ('print_expresion -> STRING COMMA print_args','print_expresion',3,'p_print_expresion','sintactico.py',81),
  ('print_args -> print_datos COMMA print_args','print_args',3,'p_print_args','sintactico.py',86),
  ('print_args -> print_datos','print_args',1,'p_print_args','sintactico.py',87),
  ('print_datos -> expresion','print_datos',1,'p_print_datos','sintactico.py',92),
  ('hashset -> LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE','hashset',8,'p_hashset','sintactico.py',97),
  ('hashfunc -> hashset_insert','hashfunc',1,'p_hashfunc','sintactico.py',101),
  ('hashfunc -> hashset_union','hashfunc',1,'p_hashfunc','sintactico.py',102),
  ('hashset_insert -> VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE','hashset_insert',7,'p_hashset_insert','sintactico.py',107),
  ('hashset_union -> VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE','hashset_union',8,'p_hashset_union','sintactico.py',112),
  ('conditional_asigned -> declarador ASIGNAR conditional ENDLINE','conditional_asigned',4,'p_conditional_asigned','sintactico.py',118),
  ('conditional -> if_type validations LLAVEIZ rust LLAVEDER','conditional',5,'p_conditional','sintactico.py',123),
  ('if_type -> IF','if_type',1,'p_if_type','sintactico.py',128),
  ('if_type -> ELSE IF','if_type',2,'p_if_type','sintactico.py',129),
  ('if_type -> ELSE','if_type',1,'p_if_type','sintactico.py',130),
  ('validations -> comparison','validations',1,'p_validations','sintactico.py',135),
  ('validations -> comparison ANDAND validations','validations',3,'p_validations','sintactico.py',136),
  ('validations -> comparison OROR validations','validations',3,'p_validations','sintactico.py',137),
  ('comparison -> VARIABLE GREATER VARIABLE','comparison',3,'p_comparison','sintactico.py',142),
]
