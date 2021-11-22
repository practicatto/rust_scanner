
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rustAND ANDAND ARROW AS ASIGNAR ASIGNATION_TYPE ASYNC AWAIT BRACKETL BRACKETR BREAK B_FALSE B_TRUE COMMA CONST CONTAINS_SLICE CONTIN CRATE DATATYPES DIFFERENT DIVISION DOLLAR DOT DOTDOTDOT DYN ELSE ENDLINE ENUM EQUAL ERRORPROP EXTERN FOR FROM FUNCTION GET_SLICE GREATEQ GREATER HASHSET IF IMPL IN INSERT_HASH LESSEQ LESST LET LLAVEDER LLAVEIZ LOOP LPAREN MAS MATCH MAYOR MAYORIGUAL MENOS MINUSEQ MOD MODULO MOVE MULT MUT NEWFUNC NOT NUMBER NUMDATATYPES OR OROR PATHSEP PLUSEQ POP_VEC PRINT PRINTS PUB PUSH_VEC READ REF RETURN RPAREN SELF SELFLOWERCASE SLASHEQ STAREQ STATIC STRING STRUCT SUPER TRAIT TUPLE TYPE U8 UNION_HASH UNIT UNSAFE USE VARIABLE VECT VECTMACRO WHERE WHILE\n    rust : asignacion\n         | prints\n         | hashset\n         | hashfunc\n         | conditional\n         | conditional_asigned\n         | for_loop\n         | struct_s\n         | while_loop\n         | empty_vector\n         | vector_methods\n         | data_vector\n    \n    asignacion : declarador ASIGNAR expresion ENDLINE\n                | other_operators ENDLINE\n    \n    other_operators : VARIABLE oper_asig expresion\n    \n    declarador : VARIABLE\n                | let_asig\n    \n    let_asig : LET var_tipo\n             | LET MUT var_tipo\n    \n    var_tipo : VARIABLE\n             | VARIABLE  ASIGNATION_TYPE tipos\n    \n    oper_asig : ASIGNAR\n                | PLUSEQ\n                | MINUSEQ\n                | STAREQ\n                | SLASHEQ\n    \n    prints : PRINTS LPAREN print_expresion RPAREN ENDLINE\n    \n    print_expresion : STRING\n                    | STRING COMMA print_args\n    \n    print_args : print_datos COMMA print_args \n                | print_datos\n    \n    print_datos : expresion\n    \n    hashset : LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE\n    \n    hashfunc : hashset_insert\n            | hashset_union\n    \n    hashset_insert : VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE\n    \n    hashset_union : VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE\n    \n    conditional_asigned : declarador ASIGNAR conditional ENDLINE\n    \n    conditional : if_type validations LLAVEIZ rust LLAVEDER\n    \n    if_type : IF\n            | ELSE IF\n            | ELSE\n    \n    validations : comparison\n                | comparison ANDAND validations\n                | comparison OROR validations\n    \n    comparison : VARIABLE signo_comp VARIABLE\n                | VARIABLE signo_comp U8\n                | U8 signo_comp VARIABLE\n    \n    signo_comp : GREATER\n                | LESST\n                | GREATEQ\n                | EQUAL\n                | DIFFERENT\n    \n    f_comparacion : U8 DOT DOT U8\n                    | VARIABLE\n    \n    for_loop : FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER\n    \n    struct_s : STRUCT sent_stru\n    \n    argumentos_juntos : VARIABLE ASIGNATION_TYPE tipos\n                        | VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos\n                        | PUB VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos\n    \n    argumentos_tipo : tipos\n                    | tipos COMMA argumentos_tipo\n    \n    sent_stru : UNIT ENDLINE\n                | TUPLE LPAREN argumentos_tipo RPAREN ENDLINE\n                | VARIABLE LLAVEIZ argumentos_juntos LLAVEDER\n    \n    while_loop : WHILE validations LLAVEIZ rust LLAVEDER\n    \n    empty_vector : declare_vector VECT types_vector empty_vec\n\n    \n    data_vector : declare_vector VECT types_vector vector_content\n                | declare_vector vector_content\n                | declare_vector ASIGNAR VECTMACRO LLAVEIZ element_type COMMA vector_elements LLAVEDER ENDLINE\n    \n    vector_content :  VECTMACRO LLAVEIZ vector_elements LLAVEDER ENDLINE\n                    | VECT PATHSEP FROM LPAREN LLAVEIZ vector_elements LLAVEDER RPAREN ENDLINE\n    \n    vector_elements : element\n                    | element COMMA vector_elements\n    \n    element : expresion\n    \n    element_type : U8 NUMDATATYPES\n    \n    types_vector : LESST DATATYPES GREATER\n                | LESST NUMDATATYPES GREATER\n    \n    declare_vector : LET MUT VARIABLE ASIGNATION_TYPE \n                    | LET VARIABLE ASIGNATION_TYPE\n\n    \n    empty_vec : ASIGNAR VECT PATHSEP NEWFUNC ENDLINE\n            | ASIGNAR VECTMACRO BRACKETL BRACKETR ENDLINE\n            | ASIGNAR VECT PATHSEP FROM LPAREN RPAREN ENDLINE\n    \n    vector_methods : VARIABLE DOT PUSH_VEC LPAREN expresion RPAREN\n                    | VARIABLE DOT POP_VEC LPAREN RPAREN\n    \n    expresion : STRING\n                | U8\n    \n    tipos : DATATYPES\n            | NUMDATATYPES\n    '
    
_lr_action_items = {'PRINTS':([0,71,85,140,],[16,16,16,16,]),'LET':([0,71,85,140,],[17,17,17,17,]),'FOR':([0,71,85,140,],[22,22,22,22,]),'STRUCT':([0,71,85,140,],[23,23,23,23,]),'WHILE':([0,71,85,140,],[24,24,24,24,]),'VARIABLE':([0,17,21,22,23,24,27,28,32,56,71,72,73,74,75,76,77,78,79,80,81,84,85,117,138,140,181,191,],[18,33,44,46,50,44,-40,-42,63,-41,18,44,44,107,-49,-50,-51,-52,-53,109,110,115,18,146,161,18,115,115,]),'IF':([0,28,29,71,85,140,],[27,56,27,27,27,27,]),'ELSE':([0,29,71,85,140,],[28,28,28,28,28,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,19,20,30,47,53,82,91,92,120,121,130,136,139,145,147,159,164,173,177,179,188,189,192,194,200,201,202,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-34,-35,-14,-57,-69,-63,-13,-38,-67,-68,-27,-85,-39,-65,-66,-84,-64,-71,-36,-56,-33,-37,-81,-82,-70,-83,-72,]),'LLAVEDER':([2,3,4,5,6,7,8,9,10,11,12,13,19,20,30,47,53,59,60,82,91,92,98,99,104,116,118,120,121,127,128,129,130,136,139,145,147,159,162,164,166,173,174,177,179,186,187,188,189,190,192,194,197,200,201,202,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-34,-35,-14,-57,-69,-86,-87,-63,-13,-38,-88,-89,139,145,147,-67,-68,155,-73,-75,-27,-85,-39,-65,-66,-84,179,-64,-58,-71,-74,-36,-56,195,196,-33,-37,-59,-81,-82,-60,-70,-83,-72,]),'ASIGNAR':([14,18,25,26,33,34,63,64,65,86,96,97,98,99,151,152,],[29,37,54,-17,-20,-18,95,-19,-80,122,-79,-21,-88,-89,-77,-78,]),'ENDLINE':([15,48,57,58,59,60,70,93,139,142,155,160,176,178,183,185,196,198,199,],[30,82,91,92,-86,-87,-15,130,-39,164,173,177,188,189,192,194,200,201,202,]),'LPAREN':([16,49,66,67,68,69,123,184,],[31,83,100,101,102,103,150,193,]),'MUT':([17,],[32,]),'DOT':([18,112,141,],[35,141,163,]),'PLUSEQ':([18,],[38,]),'MINUSEQ':([18,],[39,]),'STAREQ':([18,],[40,]),'SLASHEQ':([18,],[41,]),'U8':([21,24,27,28,29,36,37,38,39,40,41,56,72,73,74,75,76,77,78,79,81,90,94,100,102,126,156,157,163,170,171,],[45,45,-40,-42,60,60,-22,-23,-24,-25,-26,-41,45,45,108,-49,-50,-51,-52,-53,112,60,60,60,60,154,60,60,180,60,60,]),'UNIT':([23,],[48,]),'TUPLE':([23,],[49,]),'VECT':([25,65,86,96,122,151,152,],[52,-80,119,-79,148,-77,-78,]),'VECTMACRO':([25,54,65,86,96,122,151,152,],[55,89,-80,55,-79,149,-77,-78,]),'STRING':([29,31,36,37,38,39,40,41,90,94,100,102,156,157,170,171,],[59,62,59,-22,-23,-24,-25,-26,59,59,59,59,59,59,59,59,]),'ASIGNATION_TYPE':([33,63,115,146,],[65,96,144,167,]),'PUSH_VEC':([35,],[66,]),'POP_VEC':([35,],[67,]),'INSERT_HASH':([35,],[68,]),'UNION_HASH':([35,],[69,]),'LLAVEIZ':([42,43,50,51,55,89,105,106,107,108,109,110,111,150,180,],[71,-43,84,85,90,126,-44,-45,-46,-47,-48,-55,140,170,-54,]),'ANDAND':([43,107,108,109,],[72,-46,-47,-48,]),'OROR':([43,107,108,109,],[73,-46,-47,-48,]),'GREATER':([44,45,124,125,],[75,75,151,152,]),'LESST':([44,45,52,],[76,76,88,]),'GREATEQ':([44,45,],[77,77,]),'EQUAL':([44,45,],[78,78,]),'DIFFERENT':([44,45,],[79,79,]),'IN':([46,],[81,]),'PATHSEP':([52,119,134,148,],[87,87,158,168,]),'COMMA':([59,60,62,98,99,114,128,129,132,133,153,166,172,182,],[-86,-87,94,-88,-89,143,156,-75,157,-32,171,181,-76,191,]),'RPAREN':([59,60,61,62,98,99,101,113,114,131,132,133,135,137,161,165,175,193,195,],[-86,-87,93,-28,-88,-89,136,142,-61,-29,-31,-32,159,160,178,-62,-30,198,199,]),'DATATYPES':([65,83,88,96,143,144,167,],[98,98,124,98,98,98,98,]),'NUMDATATYPES':([65,83,88,96,143,144,154,167,],[99,99,125,99,99,99,172,99,]),'PUB':([84,181,191,],[117,117,117,]),'FROM':([87,168,],[123,184,]),'HASHSET':([95,],[134,]),'AND':([103,],[138,]),'BRACKETL':([149,],[169,]),'NEWFUNC':([158,168,],[176,183,]),'BRACKETR':([169,],[185,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rust':([0,71,85,140,],[1,104,118,162,]),'asignacion':([0,71,85,140,],[2,2,2,2,]),'prints':([0,71,85,140,],[3,3,3,3,]),'hashset':([0,71,85,140,],[4,4,4,4,]),'hashfunc':([0,71,85,140,],[5,5,5,5,]),'conditional':([0,29,71,85,140,],[6,58,6,6,6,]),'conditional_asigned':([0,71,85,140,],[7,7,7,7,]),'for_loop':([0,71,85,140,],[8,8,8,8,]),'struct_s':([0,71,85,140,],[9,9,9,9,]),'while_loop':([0,71,85,140,],[10,10,10,10,]),'empty_vector':([0,71,85,140,],[11,11,11,11,]),'vector_methods':([0,71,85,140,],[12,12,12,12,]),'data_vector':([0,71,85,140,],[13,13,13,13,]),'declarador':([0,71,85,140,],[14,14,14,14,]),'other_operators':([0,71,85,140,],[15,15,15,15,]),'hashset_insert':([0,71,85,140,],[19,19,19,19,]),'hashset_union':([0,71,85,140,],[20,20,20,20,]),'if_type':([0,29,71,85,140,],[21,21,21,21,21,]),'declare_vector':([0,71,85,140,],[25,25,25,25,]),'let_asig':([0,71,85,140,],[26,26,26,26,]),'var_tipo':([17,32,],[34,64,]),'oper_asig':([18,],[36,]),'validations':([21,24,72,73,],[42,51,105,106,]),'comparison':([21,24,72,73,],[43,43,43,43,]),'sent_stru':([23,],[47,]),'vector_content':([25,86,],[53,121,]),'expresion':([29,36,90,94,100,102,156,157,170,171,],[57,70,129,133,135,137,129,133,129,129,]),'print_expresion':([31,],[61,]),'signo_comp':([44,45,],[74,80,]),'types_vector':([52,],[86,]),'tipos':([65,83,96,143,144,167,],[97,114,97,114,166,182,]),'f_comparacion':([81,],[111,]),'argumentos_tipo':([83,143,],[113,165,]),'argumentos_juntos':([84,181,191,],[116,190,197,]),'empty_vec':([86,],[120,]),'vector_elements':([90,156,170,171,],[127,174,186,187,]),'element':([90,156,170,171,],[128,128,128,128,]),'print_args':([94,157,],[131,175,]),'print_datos':([94,157,],[132,132,]),'element_type':([126,],[153,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> rust","S'",1,None,None,None),
  ('rust -> asignacion','rust',1,'p_rust','sintactico.py',17),
  ('rust -> prints','rust',1,'p_rust','sintactico.py',18),
  ('rust -> hashset','rust',1,'p_rust','sintactico.py',19),
  ('rust -> hashfunc','rust',1,'p_rust','sintactico.py',20),
  ('rust -> conditional','rust',1,'p_rust','sintactico.py',21),
  ('rust -> conditional_asigned','rust',1,'p_rust','sintactico.py',22),
  ('rust -> for_loop','rust',1,'p_rust','sintactico.py',23),
  ('rust -> struct_s','rust',1,'p_rust','sintactico.py',24),
  ('rust -> while_loop','rust',1,'p_rust','sintactico.py',25),
  ('rust -> empty_vector','rust',1,'p_rust','sintactico.py',26),
  ('rust -> vector_methods','rust',1,'p_rust','sintactico.py',27),
  ('rust -> data_vector','rust',1,'p_rust','sintactico.py',28),
  ('asignacion -> declarador ASIGNAR expresion ENDLINE','asignacion',4,'p_asignacion','sintactico.py',34),
  ('asignacion -> other_operators ENDLINE','asignacion',2,'p_asignacion','sintactico.py',35),
  ('other_operators -> VARIABLE oper_asig expresion','other_operators',3,'p_other_operators','sintactico.py',41),
  ('declarador -> VARIABLE','declarador',1,'p_declarador','sintactico.py',47),
  ('declarador -> let_asig','declarador',1,'p_declarador','sintactico.py',48),
  ('let_asig -> LET var_tipo','let_asig',2,'p_let_asig','sintactico.py',54),
  ('let_asig -> LET MUT var_tipo','let_asig',3,'p_let_asig','sintactico.py',55),
  ('var_tipo -> VARIABLE','var_tipo',1,'p_var_tipo','sintactico.py',61),
  ('var_tipo -> VARIABLE ASIGNATION_TYPE tipos','var_tipo',3,'p_var_tipo','sintactico.py',62),
  ('oper_asig -> ASIGNAR','oper_asig',1,'p_oper_asig','sintactico.py',68),
  ('oper_asig -> PLUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',69),
  ('oper_asig -> MINUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',70),
  ('oper_asig -> STAREQ','oper_asig',1,'p_oper_asig','sintactico.py',71),
  ('oper_asig -> SLASHEQ','oper_asig',1,'p_oper_asig','sintactico.py',72),
  ('prints -> PRINTS LPAREN print_expresion RPAREN ENDLINE','prints',5,'p_prints','sintactico.py',78),
  ('print_expresion -> STRING','print_expresion',1,'p_print_expresion','sintactico.py',84),
  ('print_expresion -> STRING COMMA print_args','print_expresion',3,'p_print_expresion','sintactico.py',85),
  ('print_args -> print_datos COMMA print_args','print_args',3,'p_print_args','sintactico.py',91),
  ('print_args -> print_datos','print_args',1,'p_print_args','sintactico.py',92),
  ('print_datos -> expresion','print_datos',1,'p_print_datos','sintactico.py',98),
  ('hashset -> LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE','hashset',8,'p_hashset','sintactico.py',104),
  ('hashfunc -> hashset_insert','hashfunc',1,'p_hashfunc','sintactico.py',110),
  ('hashfunc -> hashset_union','hashfunc',1,'p_hashfunc','sintactico.py',111),
  ('hashset_insert -> VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE','hashset_insert',7,'p_hashset_insert','sintactico.py',117),
  ('hashset_union -> VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE','hashset_union',8,'p_hashset_union','sintactico.py',123),
  ('conditional_asigned -> declarador ASIGNAR conditional ENDLINE','conditional_asigned',4,'p_conditional_asigned','sintactico.py',131),
  ('conditional -> if_type validations LLAVEIZ rust LLAVEDER','conditional',5,'p_conditional','sintactico.py',137),
  ('if_type -> IF','if_type',1,'p_if_type','sintactico.py',143),
  ('if_type -> ELSE IF','if_type',2,'p_if_type','sintactico.py',144),
  ('if_type -> ELSE','if_type',1,'p_if_type','sintactico.py',145),
  ('validations -> comparison','validations',1,'p_validations','sintactico.py',151),
  ('validations -> comparison ANDAND validations','validations',3,'p_validations','sintactico.py',152),
  ('validations -> comparison OROR validations','validations',3,'p_validations','sintactico.py',153),
  ('comparison -> VARIABLE signo_comp VARIABLE','comparison',3,'p_comparison','sintactico.py',160),
  ('comparison -> VARIABLE signo_comp U8','comparison',3,'p_comparison','sintactico.py',161),
  ('comparison -> U8 signo_comp VARIABLE','comparison',3,'p_comparison','sintactico.py',162),
  ('signo_comp -> GREATER','signo_comp',1,'p_signoComparaion','sintactico.py',168),
  ('signo_comp -> LESST','signo_comp',1,'p_signoComparaion','sintactico.py',169),
  ('signo_comp -> GREATEQ','signo_comp',1,'p_signoComparaion','sintactico.py',170),
  ('signo_comp -> EQUAL','signo_comp',1,'p_signoComparaion','sintactico.py',171),
  ('signo_comp -> DIFFERENT','signo_comp',1,'p_signoComparaion','sintactico.py',172),
  ('f_comparacion -> U8 DOT DOT U8','f_comparacion',4,'p_condicionFor','sintactico.py',178),
  ('f_comparacion -> VARIABLE','f_comparacion',1,'p_condicionFor','sintactico.py',179),
  ('for_loop -> FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER','for_loop',7,'p_for','sintactico.py',185),
  ('struct_s -> STRUCT sent_stru','struct_s',2,'p_struct','sintactico.py',191),
  ('argumentos_juntos -> VARIABLE ASIGNATION_TYPE tipos','argumentos_juntos',3,'p_argumentos_juntos','sintactico.py',197),
  ('argumentos_juntos -> VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos','argumentos_juntos',5,'p_argumentos_juntos','sintactico.py',198),
  ('argumentos_juntos -> PUB VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos','argumentos_juntos',6,'p_argumentos_juntos','sintactico.py',199),
  ('argumentos_tipo -> tipos','argumentos_tipo',1,'p_argumento_tipo','sintactico.py',205),
  ('argumentos_tipo -> tipos COMMA argumentos_tipo','argumentos_tipo',3,'p_argumento_tipo','sintactico.py',206),
  ('sent_stru -> UNIT ENDLINE','sent_stru',2,'p_sentenciaStruct','sintactico.py',212),
  ('sent_stru -> TUPLE LPAREN argumentos_tipo RPAREN ENDLINE','sent_stru',5,'p_sentenciaStruct','sintactico.py',213),
  ('sent_stru -> VARIABLE LLAVEIZ argumentos_juntos LLAVEDER','sent_stru',4,'p_sentenciaStruct','sintactico.py',214),
  ('while_loop -> WHILE validations LLAVEIZ rust LLAVEDER','while_loop',5,'p_while','sintactico.py',232),
  ('empty_vector -> declare_vector VECT types_vector empty_vec','empty_vector',4,'p_empty_vector','sintactico.py',239),
  ('data_vector -> declare_vector VECT types_vector vector_content','data_vector',4,'p_data_vector','sintactico.py',246),
  ('data_vector -> declare_vector vector_content','data_vector',2,'p_data_vector','sintactico.py',247),
  ('data_vector -> declare_vector ASIGNAR VECTMACRO LLAVEIZ element_type COMMA vector_elements LLAVEDER ENDLINE','data_vector',9,'p_data_vector','sintactico.py',248),
  ('vector_content -> VECTMACRO LLAVEIZ vector_elements LLAVEDER ENDLINE','vector_content',5,'p_vector_content','sintactico.py',254),
  ('vector_content -> VECT PATHSEP FROM LPAREN LLAVEIZ vector_elements LLAVEDER RPAREN ENDLINE','vector_content',9,'p_vector_content','sintactico.py',255),
  ('vector_elements -> element','vector_elements',1,'p_vector_elements','sintactico.py',261),
  ('vector_elements -> element COMMA vector_elements','vector_elements',3,'p_vector_elements','sintactico.py',262),
  ('element -> expresion','element',1,'p_element','sintactico.py',268),
  ('element_type -> U8 NUMDATATYPES','element_type',2,'p_element_type','sintactico.py',274),
  ('types_vector -> LESST DATATYPES GREATER','types_vector',3,'p_types_vector','sintactico.py',280),
  ('types_vector -> LESST NUMDATATYPES GREATER','types_vector',3,'p_types_vector','sintactico.py',281),
  ('declare_vector -> LET MUT VARIABLE ASIGNATION_TYPE','declare_vector',4,'p_declare_vector','sintactico.py',287),
  ('declare_vector -> LET VARIABLE ASIGNATION_TYPE','declare_vector',3,'p_declare_vector','sintactico.py',288),
  ('empty_vec -> ASIGNAR VECT PATHSEP NEWFUNC ENDLINE','empty_vec',5,'p_assign_empty','sintactico.py',295),
  ('empty_vec -> ASIGNAR VECTMACRO BRACKETL BRACKETR ENDLINE','empty_vec',5,'p_assign_empty','sintactico.py',296),
  ('empty_vec -> ASIGNAR VECT PATHSEP FROM LPAREN RPAREN ENDLINE','empty_vec',7,'p_assign_empty','sintactico.py',297),
  ('vector_methods -> VARIABLE DOT PUSH_VEC LPAREN expresion RPAREN','vector_methods',6,'p_vector_methods','sintactico.py',303),
  ('vector_methods -> VARIABLE DOT POP_VEC LPAREN RPAREN','vector_methods',5,'p_vector_methods','sintactico.py',304),
  ('expresion -> STRING','expresion',1,'p_expresion','sintactico.py',313),
  ('expresion -> U8','expresion',1,'p_expresion','sintactico.py',314),
  ('tipos -> DATATYPES','tipos',1,'p_tipos','sintactico.py',320),
  ('tipos -> NUMDATATYPES','tipos',1,'p_tipos','sintactico.py',321),
]
