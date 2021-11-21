
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDAND ARROW AS ASIGNAR ASIGNATION_TYPE ASYNC AWAIT BRACKETL BRACKETR BREAK B_FALSE B_TRUE COMMA CONST CONTAINS_SLICE CONTIN CRATE DATATYPES DIFFERENT DIVISION DOLLAR DOT DOTDOTDOT DYN ELSE ENDLINE ENUM EQUAL ERRORPROP EXTERN FOR FUNCTION GET_SLICE GREATEQ GREATER HASHSET IF IMPL IN INSERT_HASH LESSEQ LESST LET LLAVEDER LLAVEIZ LOOP LPAREN MAS MATCH MAYOR MAYORIGUAL MENOS MINUSEQ MOD MODULO MOVE MULT MUT NEWFUNC NOT NUMBER NUMDATATYPES OR OROR PATHSEP PLUSEQ POP_VEC PRINT PRINTS PUB PUSH_VEC REF RETURN RPAREN SELF SELFLOWERCASE SLASHEQ STAREQ STATIC STRING STRUCT SUPER TRAIT TUPLE TYPE U8 UNION_HASH UNIT UNSAFE USE VARIABLE VECTOR WHERE WHILE\n    rust : asignacion\n         | prints\n         | hashset\n         | hashfunc\n         | conditional\n         | conditional_asigned\n         | for_loop\n         | struct_s\n    \n    asignacion : declarador ASIGNAR expresion ENDLINE\n                | other_operators ENDLINE\n    \n    other_operators : VARIABLE oper_asig expresion\n    \n    declarador : VARIABLE\n                | let_asig\n    \n    let_asig : LET var_tipo\n             | LET MUT var_tipo\n    \n    var_tipo : VARIABLE\n             | VARIABLE  ASIGNATION_TYPE tipos\n    \n    tipos : DATATYPES\n            | NUMDATATYPES\n    \n    oper_asig : ASIGNAR\n                | PLUSEQ\n                | MINUSEQ\n                | STAREQ\n                | SLASHEQ\n    \n    expresion : STRING\n                | U8\n    \n    prints : PRINTS LPAREN print_expresion RPAREN ENDLINE\n    \n    print_expresion : STRING\n                    | STRING COMMA print_args\n    \n    print_args : print_datos COMMA print_args \n                | print_datos\n    \n    print_datos : expresion\n    \n    hashset : LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE\n    \n    hashfunc : hashset_insert\n            | hashset_union\n    \n    hashset_insert : VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE\n    \n    hashset_union : VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE\n    \n    conditional_asigned : declarador ASIGNAR conditional ENDLINE\n    \n    conditional : if_type validations LLAVEIZ rust LLAVEDER\n    \n    if_type : IF\n            | ELSE IF\n            | ELSE\n    \n    validations : comparison\n                | comparison ANDAND validations\n                | comparison OROR validations\n    \n    comparison : VARIABLE signo_comp VARIABLE\n                | VARIABLE signo_comp U8\n                | U8 signo_comp VARIABLE\n    \n    signo_comp : GREATER\n                | LESST\n                | GREATEQ\n                | EQUAL\n                | DIFFERENT\n    \n    f_comparacion : U8 DOT DOT U8\n                    | VARIABLE\n    \n    for_loop : FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER\n    \n    struct_s : STRUCT sent_stru\n    \n    argumentos_juntos : VARIABLE ASIGNATION_TYPE tipos\n                        | VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos\n    \n    argumentos_tipo : tipos\n                    | tipos COMMA argumentos_tipo\n    \n    sent_stru : UNIT ENDLINE\n                | TUPLE LPAREN argumentos_tipo RPAREN ENDLINE\n                | LLAVEIZ argumentos_juntos LLAVEDER\n    '
    
_lr_action_items = {'PRINTS':([0,58,104,],[12,12,12,]),'LET':([0,58,104,],[13,13,13,]),'FOR':([0,58,104,],[18,18,18,]),'STRUCT':([0,58,104,],[19,19,19,]),'VARIABLE':([0,13,17,18,21,22,26,44,45,58,59,60,61,62,63,64,65,66,67,68,102,104,117,],[14,27,38,40,-40,-42,52,72,-41,14,38,38,86,-49,-50,-51,-52,-53,88,89,112,14,72,]),'IF':([0,22,23,58,104,],[21,45,21,21,21,]),'ELSE':([0,23,58,104,],[22,22,22,22,]),'$end':([1,2,3,4,5,6,7,8,9,15,16,24,41,69,73,74,94,96,103,115,120,122,125,126,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-34,-35,-10,-57,-62,-9,-38,-64,-27,-39,-63,-36,-56,-33,-37,]),'LLAVEDER':([2,3,4,5,6,7,8,9,15,16,24,41,69,71,73,74,79,80,83,94,96,103,108,113,115,120,122,124,125,126,],[-1,-2,-3,-4,-5,-6,-7,-8,-34,-35,-10,-57,-62,94,-9,-38,-18,-19,103,-64,-27,-39,-58,122,-63,-36,-56,-59,-33,-37,]),'ASIGNAR':([10,14,20,27,28,52,53,78,79,80,],[23,31,-13,-16,-14,77,-15,-17,-18,-19,]),'ENDLINE':([11,42,46,47,48,49,55,75,103,106,111,119,121,],[24,69,73,74,-25,-26,-11,96,-39,115,120,125,126,]),'LPAREN':([12,43,56,57,],[25,70,81,82,]),'MUT':([13,],[26,]),'DOT':([14,91,105,],[30,105,114,]),'PLUSEQ':([14,],[32,]),'MINUSEQ':([14,],[33,]),'STAREQ':([14,],[34,]),'SLASHEQ':([14,],[35,]),'U8':([17,21,22,23,29,31,32,33,34,35,45,59,60,61,62,63,64,65,66,68,76,81,109,114,],[39,-40,-42,49,49,-20,-21,-22,-23,-24,-41,39,39,87,-49,-50,-51,-52,-53,91,49,49,49,123,]),'UNIT':([19,],[42,]),'TUPLE':([19,],[43,]),'LLAVEIZ':([19,36,37,84,85,86,87,88,89,90,123,],[44,58,-43,-44,-45,-46,-47,-48,-55,104,-54,]),'STRING':([23,25,29,31,32,33,34,35,76,81,109,],[48,51,48,-20,-21,-22,-23,-24,48,48,48,]),'ASIGNATION_TYPE':([27,52,72,],[54,54,95,]),'INSERT_HASH':([30,],[56,]),'UNION_HASH':([30,],[57,]),'ANDAND':([37,86,87,88,],[59,-46,-47,-48,]),'OROR':([37,86,87,88,],[60,-46,-47,-48,]),'GREATER':([38,39,],[62,62,]),'LESST':([38,39,],[63,63,]),'GREATEQ':([38,39,],[64,64,]),'EQUAL':([38,39,],[65,65,]),'DIFFERENT':([38,39,],[66,66,]),'IN':([40,],[68,]),'COMMA':([48,49,51,79,80,93,98,99,108,],[-25,-26,76,-18,-19,107,109,-32,117,]),'RPAREN':([48,49,50,51,79,80,92,93,97,98,99,101,112,116,118,],[-25,-26,75,-28,-18,-19,106,-60,-29,-31,-32,111,121,-61,-30,]),'DATATYPES':([54,70,95,107,],[79,79,79,79,]),'NUMDATATYPES':([54,70,95,107,],[80,80,80,80,]),'HASHSET':([77,],[100,]),'AND':([82,],[102,]),'PATHSEP':([100,],[110,]),'NEWFUNC':([110,],[119,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rust':([0,58,104,],[1,83,113,]),'asignacion':([0,58,104,],[2,2,2,]),'prints':([0,58,104,],[3,3,3,]),'hashset':([0,58,104,],[4,4,4,]),'hashfunc':([0,58,104,],[5,5,5,]),'conditional':([0,23,58,104,],[6,47,6,6,]),'conditional_asigned':([0,58,104,],[7,7,7,]),'for_loop':([0,58,104,],[8,8,8,]),'struct_s':([0,58,104,],[9,9,9,]),'declarador':([0,58,104,],[10,10,10,]),'other_operators':([0,58,104,],[11,11,11,]),'hashset_insert':([0,58,104,],[15,15,15,]),'hashset_union':([0,58,104,],[16,16,16,]),'if_type':([0,23,58,104,],[17,17,17,17,]),'let_asig':([0,58,104,],[20,20,20,]),'var_tipo':([13,26,],[28,53,]),'oper_asig':([14,],[29,]),'validations':([17,59,60,],[36,84,85,]),'comparison':([17,59,60,],[37,37,37,]),'sent_stru':([19,],[41,]),'expresion':([23,29,76,81,109,],[46,55,99,101,99,]),'print_expresion':([25,],[50,]),'signo_comp':([38,39,],[61,67,]),'argumentos_juntos':([44,117,],[71,124,]),'tipos':([54,70,95,107,],[78,93,108,93,]),'f_comparacion':([68,],[90,]),'argumentos_tipo':([70,107,],[92,116,]),'print_args':([76,109,],[97,118,]),'print_datos':([76,109,],[98,98,]),}

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
  ('rust -> for_loop','rust',1,'p_rust','sintactico.py',20),
  ('rust -> struct_s','rust',1,'p_rust','sintactico.py',21),
  ('asignacion -> declarador ASIGNAR expresion ENDLINE','asignacion',4,'p_asignacion','sintactico.py',26),
  ('asignacion -> other_operators ENDLINE','asignacion',2,'p_asignacion','sintactico.py',27),
  ('other_operators -> VARIABLE oper_asig expresion','other_operators',3,'p_other_operators','sintactico.py',32),
  ('declarador -> VARIABLE','declarador',1,'p_declarador','sintactico.py',37),
  ('declarador -> let_asig','declarador',1,'p_declarador','sintactico.py',38),
  ('let_asig -> LET var_tipo','let_asig',2,'p_let_asig','sintactico.py',43),
  ('let_asig -> LET MUT var_tipo','let_asig',3,'p_let_asig','sintactico.py',44),
  ('var_tipo -> VARIABLE','var_tipo',1,'p_var_tipo','sintactico.py',49),
  ('var_tipo -> VARIABLE ASIGNATION_TYPE tipos','var_tipo',3,'p_var_tipo','sintactico.py',50),
  ('tipos -> DATATYPES','tipos',1,'p_tipos','sintactico.py',55),
  ('tipos -> NUMDATATYPES','tipos',1,'p_tipos','sintactico.py',56),
  ('oper_asig -> ASIGNAR','oper_asig',1,'p_oper_asig','sintactico.py',61),
  ('oper_asig -> PLUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',62),
  ('oper_asig -> MINUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',63),
  ('oper_asig -> STAREQ','oper_asig',1,'p_oper_asig','sintactico.py',64),
  ('oper_asig -> SLASHEQ','oper_asig',1,'p_oper_asig','sintactico.py',65),
  ('expresion -> STRING','expresion',1,'p_expresion','sintactico.py',70),
  ('expresion -> U8','expresion',1,'p_expresion','sintactico.py',71),
  ('prints -> PRINTS LPAREN print_expresion RPAREN ENDLINE','prints',5,'p_prints','sintactico.py',76),
  ('print_expresion -> STRING','print_expresion',1,'p_print_expresion','sintactico.py',81),
  ('print_expresion -> STRING COMMA print_args','print_expresion',3,'p_print_expresion','sintactico.py',82),
  ('print_args -> print_datos COMMA print_args','print_args',3,'p_print_args','sintactico.py',87),
  ('print_args -> print_datos','print_args',1,'p_print_args','sintactico.py',88),
  ('print_datos -> expresion','print_datos',1,'p_print_datos','sintactico.py',93),
  ('hashset -> LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE','hashset',8,'p_hashset','sintactico.py',98),
  ('hashfunc -> hashset_insert','hashfunc',1,'p_hashfunc','sintactico.py',102),
  ('hashfunc -> hashset_union','hashfunc',1,'p_hashfunc','sintactico.py',103),
  ('hashset_insert -> VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE','hashset_insert',7,'p_hashset_insert','sintactico.py',108),
  ('hashset_union -> VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE','hashset_union',8,'p_hashset_union','sintactico.py',113),
  ('conditional_asigned -> declarador ASIGNAR conditional ENDLINE','conditional_asigned',4,'p_conditional_asigned','sintactico.py',119),
  ('conditional -> if_type validations LLAVEIZ rust LLAVEDER','conditional',5,'p_conditional','sintactico.py',124),
  ('if_type -> IF','if_type',1,'p_if_type','sintactico.py',129),
  ('if_type -> ELSE IF','if_type',2,'p_if_type','sintactico.py',130),
  ('if_type -> ELSE','if_type',1,'p_if_type','sintactico.py',131),
  ('validations -> comparison','validations',1,'p_validations','sintactico.py',136),
  ('validations -> comparison ANDAND validations','validations',3,'p_validations','sintactico.py',137),
  ('validations -> comparison OROR validations','validations',3,'p_validations','sintactico.py',138),
  ('comparison -> VARIABLE signo_comp VARIABLE','comparison',3,'p_comparison','sintactico.py',146),
  ('comparison -> VARIABLE signo_comp U8','comparison',3,'p_comparison','sintactico.py',147),
  ('comparison -> U8 signo_comp VARIABLE','comparison',3,'p_comparison','sintactico.py',148),
  ('signo_comp -> GREATER','signo_comp',1,'p_signoComparaion','sintactico.py',153),
  ('signo_comp -> LESST','signo_comp',1,'p_signoComparaion','sintactico.py',154),
  ('signo_comp -> GREATEQ','signo_comp',1,'p_signoComparaion','sintactico.py',155),
  ('signo_comp -> EQUAL','signo_comp',1,'p_signoComparaion','sintactico.py',156),
  ('signo_comp -> DIFFERENT','signo_comp',1,'p_signoComparaion','sintactico.py',157),
  ('f_comparacion -> U8 DOT DOT U8','f_comparacion',4,'p_condicionFor','sintactico.py',162),
  ('f_comparacion -> VARIABLE','f_comparacion',1,'p_condicionFor','sintactico.py',163),
  ('for_loop -> FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER','for_loop',7,'p_for','sintactico.py',168),
  ('struct_s -> STRUCT sent_stru','struct_s',2,'p_struct','sintactico.py',174),
  ('argumentos_juntos -> VARIABLE ASIGNATION_TYPE tipos','argumentos_juntos',3,'p_argumentos_juntos','sintactico.py',180),
  ('argumentos_juntos -> VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos','argumentos_juntos',5,'p_argumentos_juntos','sintactico.py',181),
  ('argumentos_tipo -> tipos','argumentos_tipo',1,'p_argumento_tipo','sintactico.py',187),
  ('argumentos_tipo -> tipos COMMA argumentos_tipo','argumentos_tipo',3,'p_argumento_tipo','sintactico.py',188),
  ('sent_stru -> UNIT ENDLINE','sent_stru',2,'p_sentenciaStruct','sintactico.py',194),
  ('sent_stru -> TUPLE LPAREN argumentos_tipo RPAREN ENDLINE','sent_stru',5,'p_sentenciaStruct','sintactico.py',195),
  ('sent_stru -> LLAVEIZ argumentos_juntos LLAVEDER','sent_stru',3,'p_sentenciaStruct','sintactico.py',196),
]
