
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ANDAND ARROW AS ASIGNAR ASIGNATION_TYPE ASYNC AWAIT BRACKETL BRACKETR BREAK B_FALSE B_TRUE COMMA CONST CONTAINS_SLICE CONTIN CRATE DATATYPES DIFFERENT DIVISION DOLLAR DOT DOTDOTDOT DYN ELSE ENDLINE ENUM EQUAL ERRORPROP EXTERN FOR FUNCTION GET_SLICE GREATEQ GREATER HASHSET IF IMPL IN INSERT_HASH LESSEQ LESST LET LLAVEDER LLAVEIZ LOOP LPAREN MAS MATCH MAYOR MAYORIGUAL MENOS MINUSEQ MOD MODULO MOVE MULT MUT NEWFUNC NOT NUMBER NUMDATATYPES OR OROR PATHSEP PLUSEQ POP_VEC PRINT PRINTS PUB PUSH_VEC REF RETURN RPAREN SELF SELFLOWERCASE SLASHEQ STAREQ STATIC STRING STRUCT SUPER TRAIT TUPLE TYPE U8 UNION_HASH UNIT UNSAFE USE VARIABLE VECTOR WHERE WHILE\n    rust : asignacion\n         | prints\n         | hashset\n         | hashfunc\n         | conditional\n         | conditional_asigned\n         | for_loop\n         | struct_s\n         | asig_mate\n         | dec_slice\n         | slice_get\n         | slice_contains\n    \n    asignacion : declarador ASIGNAR expresion ENDLINE\n                | other_operators ENDLINE\n    \n    other_operators : VARIABLE oper_asig expresion\n    \n    declarador : VARIABLE\n                | let_asig\n    \n    let_asig : LET var_tipo\n             | LET MUT var_tipo\n    \n    var_tipo : VARIABLE\n             | VARIABLE  ASIGNATION_TYPE tipos\n    \n    tipos : DATATYPES\n            | NUMDATATYPES\n    \n    oper_asig : ASIGNAR\n                | PLUSEQ\n                | MINUSEQ\n                | STAREQ\n                | SLASHEQ\n    \n    expresion : STRING\n                | U8\n    \n    prints : PRINTS LPAREN print_expresion RPAREN ENDLINE\n    \n    print_expresion : STRING\n                    | STRING COMMA print_args\n    \n    print_args : print_datos COMMA print_args \n                | print_datos\n    \n    print_datos : expresion\n    \n    hashset : LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE\n    \n    hashfunc : hashset_insert\n            | hashset_union\n    \n    hashset_insert : VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE\n    \n    hashset_union : VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE\n    \n    conditional_asigned : declarador ASIGNAR conditional ENDLINE\n    \n    conditional : if_type validations LLAVEIZ rust LLAVEDER\n    \n    if_type : IF\n            | ELSE IF\n            | ELSE\n    \n    validations : comparison\n                | comparison ANDAND validations\n                | comparison OROR validations\n    \n    comparison : VARIABLE signo_comp VARIABLE\n                | VARIABLE signo_comp U8\n                | U8 signo_comp VARIABLE\n    \n    signo_comp : GREATER\n                | LESST\n                | GREATEQ\n                | EQUAL\n                | DIFFERENT\n    \n    f_comparacion : rango\n                    | VARIABLE\n    \n    for_loop : FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER\n    \n    struct_s : STRUCT sent_stru\n    \n    argumentos_juntos : VARIABLE ASIGNATION_TYPE tipos\n                        | VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos\n                        | PUB VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos\n    \n    argumentos_tipo : tipos\n                    | tipos COMMA argumentos_tipo\n    \n    sent_stru : UNIT ENDLINE\n                | TUPLE LPAREN argumentos_tipo RPAREN ENDLINE\n                | VARIABLE LLAVEIZ argumentos_juntos LLAVEDER\n    \n    asig_mate : VARIABLE ASIGNAR op_mat ENDLINE\n                | LET VARIABLE ASIGNAR op_mat ENDLINE\n                | LET MUT VARIABLE ASIGNAR op_mat ENDLINE\n    \n    op_mat : art_exp\n            | VARIABLE art_exp\n            | U8 art_exp\n    \n    art_exp : VARIABLE signo_arit VARIABLE\n            | U8 signo_arit VARIABLE\n            | VARIABLE signo_arit U8\n            | U8 signo_arit U8\n    \n    signo_arit : MAS\n                | MENOS\n                | MULT\n                | DIVISION\n                | MODULO\n    \n    rango : U8 DOT DOT U8\n    \n    dec_slice : LET VARIABLE ASIGNAR slice_exp ENDLINE\n                | LET MUT VARIABLE ASIGNAR slice_exp ENDLINE\n    \n    slice_exp : AND empty VARIABLE empty BRACKETL rango BRACKETR\n    \n    slice_get : VARIABLE empty DOT empty GET_SLICE empty LPAREN valor_get RPAREN\n    \n    valor_get : rango\n                | U8\n    \n    slice_contains : VARIABLE empty DOT empty CONTAINS_SLICE empty LPAREN AND U8 RPAREN\n    empty :'
    
_lr_action_items = {'PRINTS':([0,69,143,],[16,16,16,]),'LET':([0,69,143,],[17,17,17,]),'FOR':([0,69,143,],[22,22,22,]),'STRUCT':([0,69,143,],[23,23,23,]),'VARIABLE':([0,17,21,22,23,25,26,30,33,50,59,61,64,69,70,71,72,73,74,75,76,77,78,79,82,87,90,96,98,99,100,101,102,105,123,133,141,143,174,184,],[18,31,43,45,49,-44,-46,57,61,-45,61,94,94,18,43,43,112,-53,-54,-55,-56,-57,114,115,121,61,-93,134,-80,-81,-82,-83,-84,137,149,154,158,18,121,121,]),'IF':([0,26,27,69,143,],[25,50,25,25,25,]),'ELSE':([0,27,69,143,],[26,26,26,26,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,19,20,28,46,80,83,84,103,124,131,132,142,148,152,153,161,170,172,176,182,186,190,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-38,-39,-14,-61,-67,-13,-42,-70,-31,-71,-86,-43,-69,-72,-87,-68,-40,-60,-37,-41,-89,-92,]),'LLAVEDER':([2,3,4,5,6,7,8,9,10,11,12,13,19,20,28,46,80,83,84,92,93,103,109,122,124,131,132,142,148,152,153,159,161,163,170,172,176,182,183,186,188,190,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-38,-39,-14,-61,-67,-13,-42,-22,-23,-70,142,148,-31,-71,-86,-43,-69,-72,-87,172,-68,-62,-40,-60,-37,-41,-63,-89,-64,-92,]),'ASIGNAR':([14,18,24,31,32,57,58,91,92,93,],[27,33,-17,59,-18,87,-19,-21,-22,-23,]),'ENDLINE':([15,47,51,52,53,54,62,63,68,85,88,89,95,104,129,130,134,135,136,137,142,145,157,166,171,189,],[28,80,83,84,-29,-30,103,-73,-15,124,131,132,-74,-75,152,153,-76,-78,-79,-77,-43,161,170,176,182,-88,]),'LPAREN':([16,48,66,67,138,139,155,156,],[29,81,107,108,-93,-93,168,169,]),'MUT':([17,],[30,]),'DOT':([18,34,118,144,180,],[35,65,144,160,144,]),'PLUSEQ':([18,],[37,]),'MINUSEQ':([18,],[38,]),'STAREQ':([18,],[39,]),'SLASHEQ':([18,],[40,]),'U8':([21,25,26,27,33,36,37,38,39,40,50,59,61,64,70,71,72,73,74,75,76,77,79,86,87,96,98,99,100,101,102,105,107,150,160,168,177,181,],[44,-44,-46,54,64,54,-25,-26,-27,-28,-45,64,97,97,44,44,113,-53,-54,-55,-56,-57,118,54,64,135,-80,-81,-82,-83,-84,136,54,54,173,180,118,187,]),'UNIT':([23,],[47,]),'TUPLE':([23,],[48,]),'STRING':([27,29,33,36,37,38,39,40,86,107,150,],[53,56,-24,53,-25,-26,-27,-28,53,53,53,]),'ASIGNATION_TYPE':([31,57,121,149,],[60,60,147,164,]),'INSERT_HASH':([35,],[66,]),'UNION_HASH':([35,],[67,]),'LLAVEIZ':([41,42,49,110,111,112,113,114,115,116,117,173,],[69,-47,82,-48,-49,-50,-51,-52,-59,143,-58,-85,]),'ANDAND':([42,112,113,114,],[70,-50,-51,-52,]),'OROR':([42,112,113,114,],[71,-50,-51,-52,]),'GREATER':([43,44,],[73,73,]),'LESST':([43,44,],[74,74,]),'GREATEQ':([43,44,],[75,75,]),'EQUAL':([43,44,],[76,76,]),'DIFFERENT':([43,44,],[77,77,]),'IN':([45,],[79,]),'COMMA':([53,54,56,92,93,120,126,127,163,175,],[-29,-30,86,-22,-23,146,150,-36,174,184,]),'RPAREN':([53,54,55,56,92,93,119,120,125,126,127,140,158,162,165,173,178,179,180,187,],[-29,-30,85,-32,-22,-23,145,-65,-33,-35,-36,157,171,-66,-34,-85,186,-90,-91,190,]),'AND':([59,87,108,169,],[90,90,141,181,]),'DATATYPES':([60,81,146,147,164,],[92,92,92,92,92,]),'NUMDATATYPES':([60,81,146,147,164,],[93,93,93,93,93,]),'MAS':([61,64,94,97,],[98,98,98,98,]),'MENOS':([61,64,94,97,],[99,99,99,99,]),'MULT':([61,64,94,97,],[100,100,100,100,]),'DIVISION':([61,64,94,97,],[101,101,101,101,]),'MODULO':([61,64,94,97,],[102,102,102,102,]),'GET_SLICE':([65,106,],[-93,138,]),'CONTAINS_SLICE':([65,106,],[-93,139,]),'PUB':([82,174,184,],[123,123,123,]),'HASHSET':([87,],[128,]),'PATHSEP':([128,],[151,]),'NEWFUNC':([151,],[166,]),'BRACKETL':([154,167,],[-93,177,]),'BRACKETR':([173,185,],[-85,189,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'rust':([0,69,143,],[1,109,159,]),'asignacion':([0,69,143,],[2,2,2,]),'prints':([0,69,143,],[3,3,3,]),'hashset':([0,69,143,],[4,4,4,]),'hashfunc':([0,69,143,],[5,5,5,]),'conditional':([0,27,69,143,],[6,52,6,6,]),'conditional_asigned':([0,69,143,],[7,7,7,]),'for_loop':([0,69,143,],[8,8,8,]),'struct_s':([0,69,143,],[9,9,9,]),'asig_mate':([0,69,143,],[10,10,10,]),'dec_slice':([0,69,143,],[11,11,11,]),'slice_get':([0,69,143,],[12,12,12,]),'slice_contains':([0,69,143,],[13,13,13,]),'declarador':([0,69,143,],[14,14,14,]),'other_operators':([0,69,143,],[15,15,15,]),'hashset_insert':([0,69,143,],[19,19,19,]),'hashset_union':([0,69,143,],[20,20,20,]),'if_type':([0,27,69,143,],[21,21,21,21,]),'let_asig':([0,69,143,],[24,24,24,]),'var_tipo':([17,30,],[32,58,]),'empty':([18,65,90,138,139,154,],[34,106,133,155,156,167,]),'oper_asig':([18,],[36,]),'validations':([21,70,71,],[41,110,111,]),'comparison':([21,70,71,],[42,42,42,]),'sent_stru':([23,],[46,]),'expresion':([27,36,86,107,150,],[51,68,127,140,127,]),'print_expresion':([29,],[55,]),'op_mat':([33,59,87,],[62,88,129,]),'art_exp':([33,59,61,64,87,],[63,63,95,104,63,]),'signo_comp':([43,44,],[72,78,]),'slice_exp':([59,87,],[89,130,]),'tipos':([60,81,146,147,164,],[91,120,120,163,175,]),'signo_arit':([61,64,94,97,],[96,105,96,105,]),'f_comparacion':([79,],[116,]),'rango':([79,168,177,],[117,179,185,]),'argumentos_tipo':([81,146,],[119,162,]),'argumentos_juntos':([82,174,184,],[122,183,188,]),'print_args':([86,150,],[125,165,]),'print_datos':([86,150,],[126,126,]),'valor_get':([168,],[178,]),}

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
  ('rust -> asig_mate','rust',1,'p_rust','sintactico.py',22),
  ('rust -> dec_slice','rust',1,'p_rust','sintactico.py',23),
  ('rust -> slice_get','rust',1,'p_rust','sintactico.py',24),
  ('rust -> slice_contains','rust',1,'p_rust','sintactico.py',25),
  ('asignacion -> declarador ASIGNAR expresion ENDLINE','asignacion',4,'p_asignacion','sintactico.py',30),
  ('asignacion -> other_operators ENDLINE','asignacion',2,'p_asignacion','sintactico.py',31),
  ('other_operators -> VARIABLE oper_asig expresion','other_operators',3,'p_other_operators','sintactico.py',36),
  ('declarador -> VARIABLE','declarador',1,'p_declarador','sintactico.py',41),
  ('declarador -> let_asig','declarador',1,'p_declarador','sintactico.py',42),
  ('let_asig -> LET var_tipo','let_asig',2,'p_let_asig','sintactico.py',47),
  ('let_asig -> LET MUT var_tipo','let_asig',3,'p_let_asig','sintactico.py',48),
  ('var_tipo -> VARIABLE','var_tipo',1,'p_var_tipo','sintactico.py',53),
  ('var_tipo -> VARIABLE ASIGNATION_TYPE tipos','var_tipo',3,'p_var_tipo','sintactico.py',54),
  ('tipos -> DATATYPES','tipos',1,'p_tipos','sintactico.py',59),
  ('tipos -> NUMDATATYPES','tipos',1,'p_tipos','sintactico.py',60),
  ('oper_asig -> ASIGNAR','oper_asig',1,'p_oper_asig','sintactico.py',65),
  ('oper_asig -> PLUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',66),
  ('oper_asig -> MINUSEQ','oper_asig',1,'p_oper_asig','sintactico.py',67),
  ('oper_asig -> STAREQ','oper_asig',1,'p_oper_asig','sintactico.py',68),
  ('oper_asig -> SLASHEQ','oper_asig',1,'p_oper_asig','sintactico.py',69),
  ('expresion -> STRING','expresion',1,'p_expresion','sintactico.py',74),
  ('expresion -> U8','expresion',1,'p_expresion','sintactico.py',75),
  ('prints -> PRINTS LPAREN print_expresion RPAREN ENDLINE','prints',5,'p_prints','sintactico.py',80),
  ('print_expresion -> STRING','print_expresion',1,'p_print_expresion','sintactico.py',85),
  ('print_expresion -> STRING COMMA print_args','print_expresion',3,'p_print_expresion','sintactico.py',86),
  ('print_args -> print_datos COMMA print_args','print_args',3,'p_print_args','sintactico.py',91),
  ('print_args -> print_datos','print_args',1,'p_print_args','sintactico.py',92),
  ('print_datos -> expresion','print_datos',1,'p_print_datos','sintactico.py',97),
  ('hashset -> LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE','hashset',8,'p_hashset','sintactico.py',102),
  ('hashfunc -> hashset_insert','hashfunc',1,'p_hashfunc','sintactico.py',106),
  ('hashfunc -> hashset_union','hashfunc',1,'p_hashfunc','sintactico.py',107),
  ('hashset_insert -> VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE','hashset_insert',7,'p_hashset_insert','sintactico.py',112),
  ('hashset_union -> VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE','hashset_union',8,'p_hashset_union','sintactico.py',117),
  ('conditional_asigned -> declarador ASIGNAR conditional ENDLINE','conditional_asigned',4,'p_conditional_asigned','sintactico.py',123),
  ('conditional -> if_type validations LLAVEIZ rust LLAVEDER','conditional',5,'p_conditional','sintactico.py',128),
  ('if_type -> IF','if_type',1,'p_if_type','sintactico.py',133),
  ('if_type -> ELSE IF','if_type',2,'p_if_type','sintactico.py',134),
  ('if_type -> ELSE','if_type',1,'p_if_type','sintactico.py',135),
  ('validations -> comparison','validations',1,'p_validations','sintactico.py',140),
  ('validations -> comparison ANDAND validations','validations',3,'p_validations','sintactico.py',141),
  ('validations -> comparison OROR validations','validations',3,'p_validations','sintactico.py',142),
  ('comparison -> VARIABLE signo_comp VARIABLE','comparison',3,'p_comparison','sintactico.py',150),
  ('comparison -> VARIABLE signo_comp U8','comparison',3,'p_comparison','sintactico.py',151),
  ('comparison -> U8 signo_comp VARIABLE','comparison',3,'p_comparison','sintactico.py',152),
  ('signo_comp -> GREATER','signo_comp',1,'p_signoComparaion','sintactico.py',157),
  ('signo_comp -> LESST','signo_comp',1,'p_signoComparaion','sintactico.py',158),
  ('signo_comp -> GREATEQ','signo_comp',1,'p_signoComparaion','sintactico.py',159),
  ('signo_comp -> EQUAL','signo_comp',1,'p_signoComparaion','sintactico.py',160),
  ('signo_comp -> DIFFERENT','signo_comp',1,'p_signoComparaion','sintactico.py',161),
  ('f_comparacion -> rango','f_comparacion',1,'p_condicionFor','sintactico.py',166),
  ('f_comparacion -> VARIABLE','f_comparacion',1,'p_condicionFor','sintactico.py',167),
  ('for_loop -> FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER','for_loop',7,'p_for','sintactico.py',172),
  ('struct_s -> STRUCT sent_stru','struct_s',2,'p_struct','sintactico.py',178),
  ('argumentos_juntos -> VARIABLE ASIGNATION_TYPE tipos','argumentos_juntos',3,'p_argumentos_juntos','sintactico.py',184),
  ('argumentos_juntos -> VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos','argumentos_juntos',5,'p_argumentos_juntos','sintactico.py',185),
  ('argumentos_juntos -> PUB VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos','argumentos_juntos',6,'p_argumentos_juntos','sintactico.py',186),
  ('argumentos_tipo -> tipos','argumentos_tipo',1,'p_argumento_tipo','sintactico.py',192),
  ('argumentos_tipo -> tipos COMMA argumentos_tipo','argumentos_tipo',3,'p_argumento_tipo','sintactico.py',193),
  ('sent_stru -> UNIT ENDLINE','sent_stru',2,'p_sentenciaStruct','sintactico.py',199),
  ('sent_stru -> TUPLE LPAREN argumentos_tipo RPAREN ENDLINE','sent_stru',5,'p_sentenciaStruct','sintactico.py',200),
  ('sent_stru -> VARIABLE LLAVEIZ argumentos_juntos LLAVEDER','sent_stru',4,'p_sentenciaStruct','sintactico.py',201),
  ('asig_mate -> VARIABLE ASIGNAR op_mat ENDLINE','asig_mate',4,'p_asignacion_matematica','sintactico.py',206),
  ('asig_mate -> LET VARIABLE ASIGNAR op_mat ENDLINE','asig_mate',5,'p_asignacion_matematica','sintactico.py',207),
  ('asig_mate -> LET MUT VARIABLE ASIGNAR op_mat ENDLINE','asig_mate',6,'p_asignacion_matematica','sintactico.py',208),
  ('op_mat -> art_exp','op_mat',1,'p_operacion_matematica','sintactico.py',213),
  ('op_mat -> VARIABLE art_exp','op_mat',2,'p_operacion_matematica','sintactico.py',214),
  ('op_mat -> U8 art_exp','op_mat',2,'p_operacion_matematica','sintactico.py',215),
  ('art_exp -> VARIABLE signo_arit VARIABLE','art_exp',3,'p_aritmetic_expresion','sintactico.py',220),
  ('art_exp -> U8 signo_arit VARIABLE','art_exp',3,'p_aritmetic_expresion','sintactico.py',221),
  ('art_exp -> VARIABLE signo_arit U8','art_exp',3,'p_aritmetic_expresion','sintactico.py',222),
  ('art_exp -> U8 signo_arit U8','art_exp',3,'p_aritmetic_expresion','sintactico.py',223),
  ('signo_arit -> MAS','signo_arit',1,'p_signos_aritmeticos','sintactico.py',228),
  ('signo_arit -> MENOS','signo_arit',1,'p_signos_aritmeticos','sintactico.py',229),
  ('signo_arit -> MULT','signo_arit',1,'p_signos_aritmeticos','sintactico.py',230),
  ('signo_arit -> DIVISION','signo_arit',1,'p_signos_aritmeticos','sintactico.py',231),
  ('signo_arit -> MODULO','signo_arit',1,'p_signos_aritmeticos','sintactico.py',232),
  ('rango -> U8 DOT DOT U8','rango',4,'p_rango','sintactico.py',237),
  ('dec_slice -> LET VARIABLE ASIGNAR slice_exp ENDLINE','dec_slice',5,'p_declaracion_slice','sintactico.py',242),
  ('dec_slice -> LET MUT VARIABLE ASIGNAR slice_exp ENDLINE','dec_slice',6,'p_declaracion_slice','sintactico.py',243),
  ('slice_exp -> AND empty VARIABLE empty BRACKETL rango BRACKETR','slice_exp',7,'p_slice','sintactico.py',248),
  ('slice_get -> VARIABLE empty DOT empty GET_SLICE empty LPAREN valor_get RPAREN','slice_get',9,'p_slice_get','sintactico.py',253),
  ('valor_get -> rango','valor_get',1,'p_valor_get','sintactico.py',258),
  ('valor_get -> U8','valor_get',1,'p_valor_get','sintactico.py',259),
  ('slice_contains -> VARIABLE empty DOT empty CONTAINS_SLICE empty LPAREN AND U8 RPAREN','slice_contains',10,'p_contains','sintactico.py',264),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',268),
]
