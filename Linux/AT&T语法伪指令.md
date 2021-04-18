```cucumber
以“.”开头的是伪指令，不会被翻译成机器码，起到特殊指示的作用：
.abort ： 立即终止汇编过程
.align abs, abs, abs： abs表示数字参数，指令后可以带三个参数，分别表示边界基准(假设参数是8，表示位置计数器需要向后移动到8的倍数)；位置计数器越过的地方；允许越过字节数的最大值(可缺省)。 
.ascii "string"： 将汇编好的字符串存入连续地址，可带多个string
.asciz "string"：与ascii功能差不多，只是在string后多加了一个零字节
.balign/balignw/balignl abs, abs, abs：balign和align相似，balignw使用两个字节来填充空白，balignl用四个。
.byte expressions 将表达式汇编成一个字节存入下一个地址，可以有多个参数
.comm symbol , length ： 声明一个符号名为symbol的通用符号
.data subsection .data通知as汇编后续语句，将它们追加在编号为subsection数据段末。
.def name / .endef ：开始定义符号'name'的调试信息;定义区延伸至遇到.endef命令。 
.desc symbol, abs-expression ： 用一个纯粹表达式的低16位的值设置符号symbol的描述符
.dim :由编译器生成，以便在符号表中加入辅助调试信息。只可以在.def/.endef对之间使用此命令。
.double flonums ： 将浮点数汇编成01码
.eject ：当生成汇编清单时，强制清单页在此点中断。
.if absolute expression / .else / .elseif / .endif : 条件汇编指令
.end ： 标记着汇编文件的结束。不再处理后面的指令
.equ symbol, expression : 把符号symbol值设置为expression。它等同与'.set'命令。
.equiv symbol, expression : .equiv 类似与.equ, 但如果符号已经定义过，as会发出错误信号。
.err : 打印一条错误信息，不会生成目标文件
.exitm : 从当前宏定义体中提前退出。
.extern : 可以在源程序中使用，将所有未定义的符号都当作外部符号处理。
.fail expression : 根据表达式生成一个错误(error)或警告(warning)。
.file string : 通告as我们准备开启一个新的逻辑文件。 string 是新文件名。
.fill repeat , size , value : 重复填充size个字节
.float flonums ： 将浮点数汇编成01码
.func name[,label] / .endfunc  : 发出一个调试信息用以指示函数name。
.global/globl symbol : 使符号symbol对连接器ld可见。
.hidden names : 把可见度设置为hidden,使本符号对其他部分不可见。
.hword expressions : 等同与'.short'命令，为每个参数生成一个16位数
.ident : 本命令被某些汇编器用来在目标文件中加入标饰。
.incbin "file"[,skip[,count]] :  在当前位置逐字地引入file文件的内容。参数skip表示需要从文件头跳过的字节数目。参数count表示读入的最大字节数目。
.include "file" : 在源程序中指定点引入支撑文件
.int expressions : 将每个参数都生成一个数
.internal names : 把指定符号可见度设置为internal
.irp/irpc symbol, values  : 加工一个需要用values替代symbol的语句序列。语句序列从.irp命令开始，在.endr命令前结束。
.lcomm symbol , length : 为一个本地通用符号symbol预留length个字节的内存。
.line/ln line-number : 更改逻辑行号，参数line-number必须是个纯粹的表达式。
.mri val : 根据val是否为0，同时as进入或者退出MRI模式
.list/.nolist : 控制是否生成汇编清单。
.long expressions : 为每个参数生成一个long型数
.macro : .macro和.endm命令允许您定义宏来生成汇编输出。
.octa bignums : 针对每个巨数bignum,它生成一个16个字节的整数。
.org new-lc , fill : 向后移动当前段的位置计数器至new-lc。当（当前语句块）位置计数器到达指定位置，用fill填充该字节，fill必须是纯粹的表达式。如果没有给出逗号和fill，fill值缺省为0。
.previous : 交换当前段（及其子段）和最近访问过的段（及其子段）。
.popsection : 用堆栈顶段（及其子段）替代当前段（及其子段）。
.print string : 在标准输出上打印string字符串。
.protected names : 把指定符号可见度设置为protected
.psize lines, columns : 当生成清单列表时，使用本命令声明每页的行数—还可以可选地声明列数。
.purgem name : 取消name的宏定义，后面使用字符串name不会被宏扩展。
.pushsection/.section  name , subsection : 将当前段（及子段）推入段堆栈的顶部。并使用name和subsection来替代当前段和子段。
.quad bignums : 对于每个bignum都汇编成一个8字节的整数。
.rept count : .rept和.endr之间的语句count次。
.sbttl "subheading" : 生成汇编清单时，使用subheading作为标题
.scl class :  设置一个符号的存储类型值,只能在.def/.endef之间使用。
.section name ： 声明段，bss 段 (未初始化的数据)，text文本段
.set symbol, expression : 把符号symbol值设置为expression。它等同与'.equ'命令。
.short expressions :  为每个参数生成一个16位数
.size : 以在符号表中加入辅助调试信息。本命令只能在.def/.endef命令对之间使用。
.size name , expression : 设置符号name的内存大小。内存大小的单位是字节, 通过计算参数expression得到
.sleb128 expressions : 这是一个紧凑的，变长的数字表示方法，当使用DWARF符号调试格式时使用。
.single flonums :  和.float相同
.skip size , fill : 生成size个字节，每个字节的值都是fill。
.space size , fill : 生成size个字节，每个字节的值都是fill。
.stabd, .stabn, .stabs : 
.string "str" : 参数str中的字符复制到目标文件中去。
.struct expression : 切换到独立地址段，并用expression设定段的偏移量
.subsection name : 用name子段替换当前子段。当前段并不改变。被替换的子段入段堆栈，成为段堆栈的新栈顶
.symver : 把符号装订到在源文件里指定的节点。
.tag structname : 由编译器生成，用来在符号表中增加调试辅助的信息
.text subsection : 把后续语句汇编到编号为subsection的正文子段的末尾
.title "heading" : 生成汇编清单时，把heading作为标题使用（
.type : 把整数int作为类型属性记录进符号表表项
.uleb128 : 是一个紧凑的，变长的数字表示方法，当使用DWARF符号调试格式时使用。
.val : 把addr的地址作为值属性存入符号表的表项中
.version "string" : 创建一个.note段，并把一个NT VERSION类型ELF格式的note放入该.note段。Note的名字被设置为string。
.vtable_entry table, offset : 寻找或创建一个符号表，并用offset作偏移量的增量，为此符号表产生一个VTABLE_ENTRY重定位。
.vtable_inherit child, parent : 寻找符号child, 并寻找或创建符号parent，为符号parent产生一个VTABLE_INHERIT重定位，
.weak names : 设置names中每个符号（由逗号分隔）的weak属性。
.word expressions : 为每个参数生成一个16/32位数,看机器位数
```

7 Assembler Directives
All assembler directives have names that begin with a period (‘.’). The rest
of the name is letters, usually in lower case.
This chapter discusses directives that are available regardless of the target
machine configuration for the gnu assembler. Some machine configurations provi
de additional directives. See Chapter 8 [Machine Dependencies], page 61.

7 汇编器命令
所有的汇编器命令名都由句号（'.'）开头。命令名的其余是字母,通常使用小写。
本章讨论可用命令，不理会gnu汇编器针对目标机器配置。某些机器的配置提供附加的命令
。见第8章[机器相关性],第61页。

7.1 .abort
This directive stops the assembly immediately. It is for compatibility with ot
her assemblers. The original idea was that the assembly language source would
be piped into the assembler. If the sender of the source quit, it could use th
is directive tells as to quit also. One day .abort will not be supported.

7.1 .abort
本命令立即终止汇编过程。这是为了兼容其它的汇编器。早期的想法是汇编语言的源码会
被输送进汇编器。如果发送源码的程序要退出，它可以使用本命令通知as退出。将来可能
不再支持使用.abort


7.2 .ABORT
When producing COFF output, as accepts this directive as a synonym for ‘.abor
t’.
When producing b.out output, as accepts this directive, but ignores it.

7.2 .ABORT
当生成COFF输出时，汇编器把这条命令作为.abort接受。
当产成b.out输出时，汇编器允许使用这条命令，但忽略它。


7.3 .align abs-expr, abs-expr, abs-expr
Pad the location counter (in the current subsection) to a particular storage b
oundary. The first expression (which must be absolute) is the alignment requir
ed, as described below.
The second expression (also absolute) gives the fill value to be stored in the
padding bytes. It (and the comma) may be omitted. If it is omitted, the paddi
ng bytes are normally zero. However, on some systems, if the section is marked
as containing code and the fill value is omitted, the space is filled with no
-op instructions.
The third expression is also absolute, and is also optional. If it is present,
it is the maximum number of bytes that should be skipped by this alignment di
rective. If doing the alignment would require skipping more bytes than the spe
cified maximum, then the alignment is not done at all. You can omit the fill v
alue (the second argument) entirely by simply using two commas after the requi
red alignment; this can be useful if you want the alignment to be filled with
no-op instructions when appropriate.
The way the required alignment is specified varies from system to system. For
the a29k, hppa, m68k, m88k, w65, sparc, and Hitachi SH, and i386 using ELF for
mat, the first expression is the alignment request in bytes. For example ‘.al
ign 8’ advances the location counter until it is a multiple of 8. If the loca
tion counter is already a multiple of 8, no change is needed.
For other systems, including the i386 using a.out format, and the arm and stro
ngarm, it is the number of low-order zero bits the location counter must have
after advancement. For example ‘.align 3’ advances the location counter unti
l it a multiple of 8. If the location counter is already a multiple of 8, no c
hange is needed.
This inconsistency is due to the different behaviors of the various native ass
emblers for these systems which GAS must emulate. GAS also provides .balign an
d .p2align directives, described later, which have a consistent behavior acros
s all architectures (but are specific to GAS).


7.3 .align abs-expr, abs-expr, abs-expr
增加位置计数器(在当前的子段)使它指向规定的存储边界。第一个表达式参数(结果必须是
纯粹的数字)是必需参数：边界基准,见后面的描述。
第二个表达式参数(结果必须是纯粹的数字)给出填充字节的值，用这个值填充位置计数器
越过的地方。这个参数(和逗点)可以省略，如果省略它，填充字节的值通常是0。但在某些
系统上，如果本段标识为包含代码，而填充值被省略,则使用no-op指令填充这个空间。

第3个参数表达式的结果也必须是纯粹的数字，这个参数是可选的。如果存在第3个参数，
它代表本对齐命令允许越过字节数的最大值。如果完成这个对齐需要跳过的字节比指定的
最大值还多,则根本无法完成对齐。您可以在边界基准后简单地使用两个逗号，以省略填充
值参数(第二参数)；如果您想在适当的时候，对齐操作自动使用no-op指令填充，这个方法
将非常奏效。
边界基准的定义因系统而有差异。a29k，hppa，m68k，m88k，w65，sparc，Hitachi SH,
和使用ELF格式的i386,第一个表达式是边界基准，单位是字节。例如‘.align 8’向后移
动位置计数器至8的倍数。如果地址已经是8的倍数，则无需移动。
有些其它系统，包括使用a.out格式的i386，ARM和strongarm,这代表位置计数器移动后，
计数器中连续为0的低序位数量。例如‘.align 3’向后移动位置计数器直至8的倍数（计
数器的最低的3位为0）。如果地址已经是8倍数，则无需移动。
之所以存在这样的区别，是因为GAS需要模仿各种汇编器的不同动作。GAS还提供.balign和
.p2align命令，在以后详细讲述，这两条命令在所有的机型上使用相同的动作 (但需要向
GAS明确说明机型)。


7.4 .ascii "string". . .
.ascii expects zero or more string literals (see Section 3.6.1.1 [Strings], pa
ge 19) separated by commas. It assembles each string (with no automatic traili
ng zero byte) into consecutive addresses.

7.4 .ascii "string"...
.ascii可不带参数或者带多个由逗点分开的字符串(见3.6.1.1节[Strings],第19页)。它把
汇编好的每个字符串(在字符串末不自动追加零字节)存入连续的地址。


7.5 .asciz "string". . .
.asciz is just like .ascii, but each string is followed by a zero byte. The “
z” in ‘.asciz’ stands for “zero”.

7.5 .asciz "string"...
.asciz类似与.ascii,但在每个字符串末自动追加一个零字节。‘.asciz’中的‘z’代表
“zero”。


7.6 .balign[wl] abs-expr, abs-expr, abs-expr
Pad the location counter (in the current subsection) to a particular storage b
oundary. The first expression (which must be absolute) is the alignment reques
t in bytes. For example ‘.balign 8’ advances the location counter until it i
s a multiple of 8. If the location counter is already a multiple of 8, no chan
ge is needed.
The second expression (also absolute) gives the fill value to be stored in the
padding bytes. It (and the comma) may be omitted. If it is omitted, the paddi
ng bytes are normally zero. However, on some systems, if the section is marked
as containing code and the fill value is omitted, the space is filled with no
-op instructions.
The third expression is also absolute, and is also optional. If it is present,
it is the maximum number of bytes that should be skipped by this alignment di
rective. If doing the alignment would require skipping more bytes than the spe
cified maximum, then the alignment is not done at all. You can omit the fill v
alue (the second argument) entirely by simply using two commas after the requi
red alignment; this can be useful if you want the alignment to be filled with
no-op instructions when appropriate.
The .balignw and .balignl directives are variants of the .balign directive. Th
e .balignw directive treats the fill pattern as a two byte word value. The .ba
lignl directives treats the fill pattern as a four byte longword value. For ex
ample, .balignw 4,0x368d will align to a multiple of 4. If it skips two bytes,
they will be filled in with the value 0x368d (the exact placement of the byte
s depends upon the endianness of the processor). If it skips 1 or 3 bytes, the
fill value is undefined.

7.6
.balign[wl] abs-expr, abs-expr, abs-expr
增加位置计数器(在当前子段)使它指向规定的存储边界。第一个表达式参数(结果必须是纯
粹的数字)是必需参数：边界基准,单位为字节。例如，‘.balign 8’向后移动位置计数器
直至计数器的值等于8的倍数。如果位置计数器已经是8的倍数，则无需移动。
第2个表达式参数(结果必须是纯粹的数字)给出填充字节的值，用这个值填充位置计数器越
过的地方。第2个参数(和逗点)可以省略。如果省略它，填充字节的值通常是0。但在某些
系统上，如果本段标识为包含代码，而填充值被省略,则使用no-op指令填充空白区。
第3个参数的结果也必须是纯粹的数字，这个参数是可选的。如果存在第3个参数，它代表
本对齐命令允许跳过字节数的最大值。如果完成这个对齐需要跳过的字节数比规定的最大
值还多,则根本无法完成对齐。您可以在边界基准参数后简单地使用两个逗号，以省略填充
值参数(第二参数)；如果您在想在适当的时候，对齐操作自动使用no-op指令填充，本方法
将非常奏效。

.balignw和.balignl是.balign命令的变化形式。.balignw使用2个字节来填充空白区。.b
alignl使用4字节来填充。例如,.balignw 4,0x368d将地址对齐到4的倍数，如果它跳过2个
字节，GAS将使用0x368d填充这2个字节(字节的确切存放位置视处理器的存储方式而定)。
如果它跳过1或3个字节,则填充值不明确。


7.7 .byte expressions
.byte expects zero or more expressions, separated by commas. Each expression i
s assembled into the next byte.

7.7.byte expressions
.byte可不带参数或者带多个表达式参数，表达式之间由逗点分隔。每个表达式参数都被汇
编成下一个字节。


7.8 .comm symbol , length
.comm declares a common symbol named symbol. When linking, a common symbol in
one object file may be merged with a defined or common symbol of the same name
in another object file. If ld does not see a definition for the symbol–just
one or more common symbols–then it will allocate length bytes of uninitialize
d memory. length must be an absolute expression. If ld sees multiple common sy
mbols with the same name, and they do not all have the same size, it will allo
cate space using the largest size.
When using ELF, the .comm directive takes an optional third argument. This is
the desired alignment of the symbol, specified as a byte boundary (for example
, an alignment of 16 means that the least significant 4 bits of the address sh
ould be zero). The alignment must be an absolute expression, and it must be a
power of two. If ld allocates uninitialized memory for the common symbol, it w
ill use the alignment when placing the symbol. If no alignment is specified, a
s will set the alignment to the largest power of two less than or equal to the
size of the symbol, up to a maximum of 16.
The syntax for .comm differs slightly on the HPPA. The syntax is ‘symbol .com
m, length’;symbol is optional.

7.8 .comm symbol , length
.comm声明一个符号名为symbol的通用符号(common symbol)。当连接时，目标文件中的通
用符号可能被并入其它目标文件中已定义的符号，或者被并入其他目标文件中同名通用符
号。如果ld无法找到该符号的定义——只有一个或多个通用符号——则分配length个字节
的未初始化内存。Length必须是一个纯粹的表达式。如果ld发现多个同名的通用符号，并
且它们的长度不同，ld将按照它们之中最大的length值为符号分配内存。
当使用ELF格式时，.comm可以使用第3个参数。它代表符号需要对齐的边界基准(例如,边界
基准为16时意味着符号存放地址的最低4位应该是零)。第3个参数表达式结果必须是纯粹的
数字，而且一定是2的幂。当ld为通用符号分配未初始化内存时，在存放符号时要使用到这
个参数。如果没有规定边界基准，as将把边界基准设置成以2为底的该符号长度的对数，并
向下取整。最大值为16。
.comm的语法在HPPA上稍微有些不同。语法是‘symbol .comm, length’;其中参数symbol
是可选的。


7.9 .data subsection
.data tells as to assemble the following statements onto the end of the data s
ubsection numbered subsection (which is an absolute expression). If subsection
is omitted, it defaults to zero.

7.9 .data subsection
.data通知as汇编后续语句，将它们追加在编号为subsection(subsection必须是纯粹的表
达式)数据段末。如果参数subsection省略，则默认是0。


7.10 .def name
Begin defining debugging information for a symbol name; the definition extends
until the .endef directive is encountered. This directive is only observed wh
en as is configured for COFF format output; when producing b.out, ‘.def’ is
recognized, but ignored.

7.10 .def name
开始定义符号'name'的调试信息;定义区延伸至遇到.endef命令。本命令只在as被配置成C
OFF格式输出时才使用;当输出为b.out格式时，可以使用‘.def’命令，但被忽略。

7.11 .desc symbol, abs-expression
This directive sets the descriptor of the symbol (see Section 5.5 [Symbol Attr
ibutes],page 30) to the low 16 bits of an absolute expression.
The ‘.desc’ directive is not available when as is configured for COFF output
; it is only for a.out or b.out object format. For the sake of compatibility,
as accepts it, but produces no output, when configured for COFF.

7.11 .desc symbol, abs-expression
本命令用一个纯粹表达式的低16位的值设置符号symbol的描述符(见5.5[符号属性],第30页
)。当as被配置成COFF输出时，‘.desc’命令无效;它只适用于a.out或b.out目标格式。为
兼容起见，当配置为COFF时，as接受此命令，但不产生输出。


7.12 .dim
This directive is generated by compilers to include auxiliary debugging inform
ation in the symbol table. It is only permitted inside .def/.endef pairs.
‘.dim’ is only meaningful when generating COFF format output; when as is gen
erating b.out, it accepts this directive but ignores it.

7.12 .dim
这条命令由编译器生成的，以便在符号表中加入辅助调试信息。只可以在.def/.endef对之
间使用此命令。
'.dim'仅仅在生成COFF格式输出时是有意义的;当生成b.out时,as接受这条命令,但忽略它
。


7.13 .double flonums
.double expects zero or more flonums, separated by commas. It assembles floati
ng point numbers. The exact kind of floating point numbers emitted depends on
how as is configured. See Chapter 8 [Machine Dependencies], page 61.

7.13 .double flonums
.double后跟着零个或由逗点分开多个的浮点数。本指令汇编出浮点数字。生成的浮点数的
确切类型视as的配置而定。见第8章[机器相关性],第61页。


7.14 .eject
Force a page break at this point, when generating assembly listings.

7.14 .eject
当生成汇编清单时，强制清单页在此点中断。


7.15 .else
.else is part of the as support for conditional assembly; see Section 7.35 [.i
f], page 43. It marks the beginning of a section of code to be assembled if th
e condition for the preceding
.if was false.

7.15 .else
.else 是支持as进行的条件汇编指令之一;见7.35[.if],第43页。如果前面.if命令的条件
不成立，则表示需要汇编.else后的一段代码。


7.16 .elseif
.elseif is part of the as support for conditional assembly; see Section 7.35 [
.if],page 43. It is shorthand for beginning a new .if block that would otherwi
se fill the entire .else section.

7.16 .elseif
.elseif 是支持as进行的条件汇编指令之一。见7.35节 [.if],第43页。它可以在.esle段
中快速产生一个新的.if块。


7.17 .end
.end marks the end of the assembly file. as does not process anything in the f
ile past the .end directive.

7.17 .end
.end标记着汇编文件的结束。as不处理.end命令后的任何语句。


7.18 .endef
This directive flags the end of a symbol definition begun with .def.
‘.endef’ is only meaningful when generating COFF format output; if as is con
figured to generate b.out, it accepts this directive but ignores it.

7.18 .endef
这条命令标志着从.def开始的符号定义结束。
‘.endef’命令仅仅在生成COFF格式的输出有意义;如果as被配置为生成b.out输出,虽然a
s接受这条命令，但忽略它。


7.19 .endfunc
.endfunc marks the end of a function specified with .func.

7.19 .endfunc
.endfunc标志着一个由.func命令定义的函数的结束。


7.20 .endif
.endif is part of the as support for conditional assembly; it marks the end of
a block of code that is only assembled conditionally. See Section 7.35 [.if],
page 43.

7.20 .endif
.endif是支持as进行的条件汇编的指令之一.它标志着条件汇编代码块的结束。见7.35节[
.if],第43页。


7.21 .equ symbol, expression
This directive sets the value of symbol to expression. It is synonymous with ‘
.set’; see Section 7.68 [.set], page 53.
The syntax for equ on the HPPA is ‘symbol .equ expression’.

7.21 .equ symbol, expression
本命令把符号symbol值设置为expression。它等同与'.set'命令。见7.68[.set],第53页。

在HPPA上的equ语法是‘symbol .equ expression’。


7.22 .equiv symbol, expression
The .equiv directive is like .equ and .set, except that the assembler will sig
nal an error if symbol is already defined.
Except for the contents of the error message, this is roughly equivalent to

.ifdef SYM
.err
.endif
.equ SYM,VAL

7.22 .equiv symbol, expression
.equiv 类似与.equ & .set命令, 不同之处在于，如果符号已经定义过，as会发出错误信
号。
除了错误信息的内容之外，它大体上等价与：
.ifdef SYM
.err
.endif
.equ SYM,VAL

7.23 .err
If as assembles a .err directive, it will print an error message and, unless t
he -Z option was used, it will not generate an object file. This can be used t
o signal error an conditionally compiled code.

7.23 .err
如果as汇编一条.err命令, 将打印一条错误信息，除非使用了-Z 选项, as不会生成目标文
件。 可以在条件编译代码中使用它来发出错误信息。


7.24 .exitm
Exit early from the current macro definition. See Section 7.50 [Macro], page 4
7.

7.24 .exitm
从当前宏定义体中提前退出。见7.50 [Macro],第47页。

7.25 .extern
.extern is accepted in the source program—for compatibility with other assemb
lers—but it is ignored. as treats all undefined symbols as external.

7.25 .extern
.extern可以在源程序中使用--以便兼容其他的汇编器—但会被忽略。as将所有未定义的符
号都当作外部符号处理。


7.26 .fail expression
Generates an error or a warning. If the value of the expression is 500 or more
, as will print a warning message. If the value is less than 500, as will prin
t an error message. The message will include the value of expression. This can
occasionally be useful inside complex nested macros or conditional assembly.


7.26 .fail expression
生成一个错误(error)或警告(warning)。如果expression的值大于或等于500，as会打印一
条“警告”消息。如果expression的值小于500,as会打印一条“错误”消息。消息中包含
了expression的值。这在复杂的宏嵌套或条件汇编时偶尔用到。


7.27 .file string
.file tells as that we are about to start a new logical file. string is the ne
w file name.
In general, the filename is recognized whether or not it is surrounded by quot
es ‘"’; but if you wish to specify an empty file name, you must give the quo
tes–"". This statement may go away in future: it is only recognized to be com
patible with old as programs. In some configurations of as, .file has already
been removed to avoid conflicts with other assemblers. See Chapter 8 [Machine
Dependencies], page 61.

7.27 .file string
.file 通告as我们准备开启一个新的逻辑文件。 string 是新文件名。总的来说，文件名
是否使用引号‘"’都可以；但如果您希望规定一个空文件名时，必须使用引号-""。本语
句将来可能不再使用—允许使用它只是为了与旧版本的as程序兼容。在as的一些配置中，
已经删除了.file以避免与其它的汇编器冲突。见第8章 [Machine Dependencies], 第61页
。


7.28 .fill repeat , size , value
repeat, size and value are absolute expressions. This emits repeat copies of s
ize bytes. Repeat may be zero or more. Size may be zero or more, but if it is
more than 8, then it is deemed to have the value 8, compatible with other peop
le’s assemblers. The contents of each repeat bytes are taken from an 8-byte n
umber. The highest order 4 bytes are zero. The lowest order 4 bytes are value
rendered in the byte-order of an integer on the computer as is assembling for.
Each size bytes in a repetition is taken from the lowest order size bytes of
this number. Again, this bizarre behavior is compatible with other people’s a
ssemblers.
size and value are optional. If the second comma and value are absent, value i
s assumed zero. If the first comma and following tokens are absent, size is as
sumed to be 1.

7.28 .fill repeat , size , value
repeat, size 和value都必须是纯粹的表达式。本命令生成size个字节的repeat个副本。
Repeat可以是0或更大的值。Size 可以是0或更大的值, 但即使size大于8,也被视作8，以
兼容其它的汇编器。各个副本中的内容取自一个8字节长的数。最高4个字节为零，最低的
4个字节是value，它以as正在汇编的目标计算机的整数字节顺序排列。每个副本中的size
个字节都取值于这个数最低的size个字节。再次说明，这个古怪的动作只是为了兼容其他
的汇编器。
size参数和value参数是可选的。如果不存在第2个逗号和value参数，则假定value为零。
如果不存在第1个逗号和其后的参数，则假定size为1。


7.29 .float flonums
This directive assembles zero or more flonums, separated by commas. It has the
same effect as .single. The exact kind of floating point numbers emitted depe
nds on how as is configured. See Chapter 8 [Machine Dependencies], page 61.


7.29 .float flonums
本命令汇编0个或多个浮点数，浮点数之间由逗号分隔。它和.single的汇编效果相同。生
成的浮点数的确切类型视as的配置而定。见第8章 [Machine Dependencies], 61页。


7.30 .func name[,label]
.func emits debugging information to denote function name, and is ignored unle
ss the file is assembled with debugging enabled. Only ‘--gstabs’ is currentl
y supported. Label is the entry point of the function and if omitted name prep
ended with the ‘leading char’ is used. ‘leading char’ is usually _ or noth
ing, depending on the target. All functions are currently defined to have void
return type. The function must be terminated with .endfunc.

7.30 .func name[,label]
.func发出一个调试信息用以指示函数name，这个信息将被忽略，除非文件使用debugging
enabled方式的汇编。目前只支持‘--gstabs’。label是函数的入口点，如果name被省略
则使用预定的‘引导符’。‘引导符’通常可以是 _ 或者什么也没有，视目标机型而定。
所有函数现时被定义为void返回类型，函数体必须使用.endfunc来结束


7.31 .global symbol, .globl symbol
.global makes the symbol visible to ld. If you define symbol in your partial p
rogram, its value is made available to other partial programs that are linked
with it. Otherwise, symbol takes its attributes from a symbol of the same name
from another file linked into the same program.
Both spellings (‘.globl’ and ‘.global’) are accepted, for compatibility wi
th other assemblers.
On the HPPA, .global is not always enough to make it accessible to other parti
al programs. You may need the HPPA-only .EXPORT directive as well. See Section
8.8.5 [HPPA Assembler Directives], page 84.

7.31 .global symbol, .globl symbol
.global 使符号symbol对连接器ld可见。如果您在局部过程中定义符号symbol，其它和此
的局部过程都可以访问它的值。另外，symbol从连接到本过程的另一个文件中的同名符号
获取自己的属性。
两种写法都可以(‘.globl’ 和‘.global’)，以便兼容多种汇编器。

在HPPA上, .global未必总能够使符号被其它局部过程访问。可能同时需要使用HPPA-only
.EXPORT命令。见8.8.5[HPPA Assembler Directives],84页。


7.32 .hidden names
This one of the ELF visibility directives. The other two are .internal (see Se
ction 7.39 [.internal], page 44) and .protected (see Section 7.58 [.protected]
, page 50).
This directive overrides the named symbols default visibility (which is set by
their binding: local, global or weak). The directive sets the visibility to h
idden which means that the symbols are not visible to other components. Such s
ymbols are always considered to be protected as well.

7.32 .hidden names
这是一条关于ELF可见度的命令。其它两条是.internal(见7.39[.internal],44页) 和 .p
rotected (见7.58 [.protected], 50页)。本命令取消指定符号的缺省可见度(可见度由其
他命令捆绑设定：local,global,weak)。本命令把可见度设置为hidden,这意味着本符号对
其他部分不可见。这最好是一些需要长期保护的符号。


7.33 .hword expressions
This expects zero or more expressions, and emits a 16 bit number for each.
This directive is a synonym for ‘.short’; depending on the target architectu
re, it may also be a synonym for ‘.word’.

7.33 .hword expressions
本命令后可以不带或带多个expressions,并且为每个参数生成一个16位数。
本命令等同与'.short'命令。在某些架构上，也可能等同与'.word'。


7.34 .ident
This directive is used by some assemblers to place tags in object files. as si
mply accepts the directive for source-file compatibility with such assemblers,
but does not actually emit anything for it.

7.34 .ident
本命令被某些汇编器用来在目标文件中加入标饰。为了使汇编源码文件兼容上述的汇编器
，as简单地接受本命令，但实际上不产生东西。


7.35 .if absolute expression
.if marks the beginning of a section of code which is only considered part of
the source program being assembled if the argument (which must be an absolute
expression) is nonzero. The end of the conditional section of code must be mar
ked by .endif (see Section 7.20 [.endif], page 40); optionally, you may includ
e code for the alternative condition, flagged by .else (see Section 7.15 [.els
e], page 40). If you have several conditions to check, .elseif may be used to
avoid nesting blocks if/else within each subsequent .else block.
The following variants of .if are also supported:
.ifdef symbol
Assembles the following section of code if the specified symbol has been defin
ed.
.ifc string1,string2
Assembles the following section of code if the two strings are the same. The s
trings may be optionally quoted with single quotes. If they are not quoted, th
e first string stops at the first comma, and the second string stops at the en
d of the line. Strings which contain whitespace should be quoted. The string c
omparison is case sensitive.
.ifeq absolute expression
Assembles the following section of code if the argument is zero.
.ifeqs string1,string2
Another form of .ifc. The strings must be quoted using double quotes.
.ifge absolute expression
Assembles the following section of code if the argument is greater than or equ
al to zero.
.ifgt absolute expression
Assembles the following section of code if the argument is greater than zero.

.ifle absolute expression
Assembles the following section of code if the argument is less than or equal
to zero.
.iflt absolute expression
Assembles the following section of code if the argument is less than zero.
.ifnc string1,string2.
Like .ifc, but the sense of the test is reversed: this assembles the following
section of code if the two strings are not the same.
.ifndef symbol
.ifnotdef symbol
Assembles the following section of code if the specified symbol has not been d
efined. Both spelling variants are equivalent.
.ifne absolute expression
Assembles the following section of code if the argument is not equal to zero (
in other words, this is equivalent to .if).
.ifnes string1,string2
Like .ifeqs, but the sense of the test is reversed: this assembles the followi
ng section of code if the two strings are not the same.

7.35 .if absolute expression
.if 标志着一段代码的开始，这段代码只有在参数absolute experession(必须是一个独立
的表达式)不为0时才进行汇编。这段条件汇编代码必须使用.endif标志结束。(见7.20[.e
ndif], 40页);另外，可以使用.esle来标记一个代码块(见7.15 [.else],40页)，这个代码
块与前面那段代码只有一个会进行汇编。 如果您需要检查数个汇编条件，可以在使用.el
seif命令，以避免在.else代码块中进行if/else语句块的嵌套。
同样可以使用下面.if的变体：
.ifdef symbol
如果指定的符号symbol已经定义过，汇编下面那段代码。
.ifc string1,string2
如果两个字符串相同的话，汇编下面那段代码。 字符串可以可选地使用单引号。如果不使
用引号则第1个字符串在逗号处结束。第2个字符串在本行末结束。包含空白的字符串应该
使用引号标注。字符串比较时是区分大小写的。

.ifeq absolute expression
如果参数的值为0，汇编下面那段代码。

.ifeqs string1,string2
这是.ifc的另一种形式，字符串必须使用双引号标注。

.ifge absolute expression
如果参数的值大于等于0，汇编下面那段代码。

.ifgt absolute expression
如果参数的值大于0，汇编下面那段代码。

.ifle absolute expression
如果参数的值小于等于0，汇编下面那段代码。

.iflt absolute expression
如果参数的值小于0，汇编下面那段代码。

.ifnc string1,string2.
类似与.ifc，不过使用反向的测试： 如果两个字符串不相等的话，汇编下面那段代码。

.ifndef symbol
.ifnotdef symbol
如果指定的符号symbol不曾被定义过，汇编下面那段代码。 上面两种写法是等效的。


.ifne absolute expression
如果参数的值为不等于0，汇编下面那段代码。 (换句话说, 这是.if的另一种写法).

.ifnes string1,string2
类似与.ifeqs，不过使用反向的测试： 如果两个字符串不相等的话，汇编下面那段代码。



7.36 .incbin "file"[,skip[,count]]
The incbin directive includes file verbatim at the current location. You can c
ontrol the search paths used with the ‘-I’ command-line option (see Chapter
2 [Command-Line Options], page 11). Quotation marks are required around file.

The skip argument skips a number of bytes from the start of the file. The coun
t argument indicates the maximum number of bytes to read. Note that the data i
s not aligned in any way, so it is the user’s responsibility to make sure tha
t proper alignment is provided both before and after the incbin directive.

7.36 .incbin "file"[,skip[,count]]
这条incbin命令在当前位置逐字地引入file文件的内容。您可以使用命令行选项参数“-I
”来控制搜索路径。(见第2章[Command-Line Options], 11页)。文件名必须使用引号。

参数skip表示需要从文件头跳过的字节数目。参数count表示读入的最大字节数目。注意，
数据没有进行任何方式的对齐操作，所以用户需要在 .incbin命令的前后进行必要的边界
对齐。


7.37 .include "file"
This directive provides a way to include supporting files at specified points
in your source program. The code from file is assembled as if it followed the
point of the .include; when the end of the included file is reached, assembly
of the original file continues. You can control the search paths used with the
‘-I’ command-line option (see Chapter 2 [Command-Line Options], page 11). Q
uotation marks are required around file.

7.37 .include "file"
本命令提供在源程序中指定点引入支撑文件的手段。file中的代码如同紧跟.include后一
样被汇编。当引入文件汇编结束，继续汇编原来的文件。您可以使用命令行选项参数“-I
”来控制搜索路径(见第2章[Command-Line Options], 11页)。文件名必须使用引号来标注
。


7.38 .int expressions
Expect zero or more expressions, of any section, separated by commas. For each
expression, emit a number that, at run time, is the value of that expression.
The byte order and bit size of the number depends on what kind of target the
assembly is for.

7.38 .int expressions
可以不带参数或带多个expressions,参数之间由逗号分隔。每个expressions都生成一个数
字,这个数字等于表达式在目标机器运行时的值。字节顺序和数字的位数视汇编的目标机器
而定。


7.39 .internal names
This one of the ELF visibility directives. The other two are .hidden (see Sect
ion 7.32 [.hidden], page 42) and .protected (see Section 7.58 [.protected], pa
ge 50).
This directive overrides the named symbols default visibility (which is set by
their binding: local, global or weak). The directive sets the visibility to i
nternal which means that the symbols are considered to be hidden (ie not visib
le to other components), and that some extra, processor specific processing mu
st also be performed upon the symbols as well.

7.39 .internal names
这是一条与ELF可见度相关的命令。另外的两条是.hidden(见7.32[.hidden],42页) 和 .p
rotected (见7.58 [.protected],50页)。
本命令取消指定符号的缺省可见度(可见度由其他命令捆绑设定：local,global,weak)。本
命令把指定符号可见度设置为internal,这意味着此符号需要被隐藏（即对其他部分不可见
），另外，符号还必须经过处理器的特别的处理。




\# 回复：linux下汇编的Directive Operands 2004-09-08 3:24 PM n9871009
定语：发现简单的把英文直译成中文有时产生会极大的混乱。向前和向后就是一例，我在
5.3节符号名发现这个问题，当时另选了两个词替代了向前和向后。看起来现在必须说明一
下。
向前（移动）：向文件头的方向（移动）。
向后（移动）：向文件尾的方向（移动）。
===========================================================
7.40 .irp symbol, values . . .
Evaluate a sequence of statements assigning different values to symbol. The se
quence of statements starts at the .irp directive, and is terminated by an .en
dr directive. For each value, symbol is set to value, and the sequence of stat
ements is assembled. If no value is listed, the sequence of statements is asse
mbled once, with symbol set to the null string. To refer to symbol within the
sequence of statements, use \symbol.
For example, assembling
.irp param,1,2,3
move d\param,sp@-
.endr
is equivalent to assembling
move d1,sp@-
move d2,sp@-
move d3,sp@-

7.40 .irp symbol,values . . .
加工一个需要用values替代symbol的语句序列。语句序列从.irp命令开始，在.endr命令前
结束。对于每个value都进行如下加工：用value替代Symbol，并对此语句序列进行汇编。
如果没有给出value，则用空字符串(null sting)替代symbol，并将此语句序列汇编一次。
使用\symbol, 把参数symbol提交给语句序列。
例如下列代码
.irp param,1,2,3
move d\param,sp@-
.endr
等同与
move d1,sp@-
move d2,sp@-
move d3,sp@-


7.41 .irpc symbol,values . . .
Evaluate a sequence of statements assigning different values to symbol. The se
quence of statements starts at the .irpc directive, and is terminated by an .e
ndr directive. For each character in value, symbol is set to the character, an
d the sequence of statements is assembled. If no value is listed, the sequence
of statements is assembled once, with symbol set to the null string. To refer
to symbol within the sequence of statements, use \symbol.
For example, assembling
.irpc param,123
move d\param,sp@-
.endr
is equivalent to assembling
move d1,sp@-
move d2,sp@-
move d3,sp@-

7.41 .irpc symbol,values. . .
加工一个需要用values替代symbol的语句序列。语句序列从.irpc命令开始，在.endr命令
前结束。对于value中的每个字符，都进行如下加工；用此字符替代symbol，并对此语句序
列进行汇编。如果没有给出value参数，则用空字符串(null sting)替代symbol，并将此语
句序列汇编一次。使用\symbol, 把参数symbol提交给语句序列。
例如下列代码
.irpc param,123
move d\param,sp@-
.endr
等同与
move d1,sp@-
move d2,sp@-
move d3,sp@-


7.42 .lcomm symbol , length
Reserve length (an absolute expression) bytes for a local common denoted by sy
mbol. The section and value of symbol are those of the new local common. The a
ddresses are allocated in the bss section, so that at run-time the bytes start
off zeroed. Symbol is not declared global (see Section 7.31 [.global], page 4
2), so is normally not visible to ld.
Some targets permit a third argument to be used with .lcomm. This argument spe
cifies the desired alignment of the symbol in the bss section.
The syntax for .lcomm differs slightly on the HPPA. The syntax is ‘symbol .lc
omm, length’; symbol is optional.

7.42 .lcomm symbol , length
为一个本地通用符号symbol预留length个字节的内存。symbol 的段(属性)和值(属性)被设
置为一个新的本地通用符号应有的属性：内存是在bss段中分配的，所以在运行时,这些字
节开始都是零。因为symbol没有被声明为全局性的符号，所以symbol对ld通常不可见。

某些目标格式允许在.lcomm命令中使用第3个参数。这个参数指出这个bss段中的符号对齐
操作所需要的边界基准。
.lcomm的语法在HPPA上稍有不同。表示为‘symbol .lcomm, length’; symbol 是可选的
。


7.43 .lflags
as accepts this directive, for compatibility with other assemblers, but ignore
s it.

7.43 .lflags
as接受本命令，以兼容其他的汇编器，但忽略之。


7.44 .line line-number
Change the logical line number. line-number must be an absolute expression. Th
e next line has that logical line number. Therefore any other statements on th
e current line (after a statement separator character) are reported as on logi
cal line number line-number - 1. One day as will no longer support this direct
ive: it is recognized only for compatibility with existing assembler programs.

Warning: In the AMD29K configuration of as, this command is not available; use
the synonym .ln in that context.
Even though this is a directive associated with the a.out or b.out object-code
formats, as still recognizes it when producing COFF output, and treats ‘.lin
e’ as though it were the COFF ‘.ln’ if it is found outside a .def/.endef pa
ir.
Inside a .def, ‘.line’ is, instead, one of the directives used by compilers
to generate auxiliary symbol information for debugging.

7.44 .line line-number
更改逻辑行号，参数line-number必须是个纯粹的表达式。本命令后的下一行将被赋予此逻
辑行号。因此在当前行之前任何其他的语句（在语句分隔符后）的逻辑行号将被视作line
-number - 1。以后 as将不在支持这条命令：只是为了兼容现存的汇编器而接受本命令。

Warning: 在为AMD29K目标机器配置的as中,不能使用本指令。在这种场合可以使用.ln命令
。
尽管这是与a. out或b. out目标代码格式相关的命令，在生成COFF输出时as仍然接受它，
并且如果‘.line’出现在.def/endef之外的话，就把它视为‘.ln’命令。
如果‘.line’在.def语句块中的话，.line命令则是一条编译器使用的命令，用来为调式
生成辅助符号信息。


7.45 .linkonce [type]
Mark the current section so that the linker only includes a single copy of it.
This may be used to include the same section in several different object file
s, but ensure that the linker will only include it once in the final output fi
le. The .linkonce pseudo-op must be used for each instance of the section. Dup
licate sections are detected based on the section name, so it should be unique
.
This directive is only supported by a few object file formats; as of this writ
ing, the only object file format that supports it is the Portable Executable f
ormat used on Windows NT.
The type argument is optional. If specified, it must be one of the following s
trings. For example:
.linkonce same_size
Not all types may be supported on all object file formats.
discard Silently discard duplicate sections. This is the default.
one_only Warn if there are duplicate sections, but still keep only one copy.

same_size Warn if any of the duplicates have different sizes.
same_contents
Warn if any of the duplicates do not have exactly the same contents.

7.45 .linkonce [type]
给当前段做一个标志,以便连接器只包含它的一个拷贝。这个命令可以用于几个不同的目标
文件中包含同样的段，但需要连接器在最终的输出文件中只包含一个这样的段。. linkou
ce伪操作必须在每个段的实例都中使用。对重复段的探测基于段名来进行，因此这个段将
是唯一的。
本命令只在少数目标格式文件中有效,到写本文为止，只有基于Windows NT的PE （Portab
le Executable）格式的目标文件支持本命令，
参数type是可选的，如果指定了此参数，它必须是下列字符串之一。例如
. Linkonce same_size
不是在所有的格式目标文件都可以使用所有类型的参数。
discard 静静地舍弃重复的段，这也是默认值。
one_only 如果存在重复的段则发出警告，但只保存一个拷贝。
same_size 如果重复的段有不同的大小则发出警告。
same_contents 如果重复段的内容不是精确的相符则发出警告。


7.46 .ln line-number
‘.ln’ is a synonym for ‘.line’.

7.46 .ln line-number
‘.ln’命令等同与‘.line’.


7.47 .mri val
If val is non-zero, this tells as to enter MRI mode. If val is zero, this tell
s as to exit MRI mode. This change affects code assembled until the next .mri
directive, or until the end of the file. See Section 2.8 [MRI mode], page 13.


7.47 .mri val
如果参数val是非零值，这将通知as进入MRI模式。如果参数val的值是零，这通知as退出M
RI模式。这个变化会影响汇编的结果，直到下个.mri命令，或者直到文件尾。见2.8 [MRI
mode], 13页。


7.48 .list
Control (in conjunction with the .nolist directive) whether or not assembly li
stings are generated. These two directives maintain an internal counter (which
is zero initially). .list increments the counter, and .nolist decrements it.
Assembly listings are generated whenever the counter is greater than zero.
By default, listings are disabled. When you enable them (with the ‘-a’ comma
nd line option; see Chapter 2 [Command-Line Options], page 11), the initial va
lue of the listing counter is one.

7.48 .list
控制（和.nolist命令配合）是否生成汇编清单。这两个命令维护一个内部的计数器（计数
器初始值为0）.list命令增加计数器的值，.nolist减少计数器的值。当计数器的值大与0
时将汇编列表。
缺省状态汇编列表的生成是关闭的。当您打开它的时候（使用带-a选项的命令行）第2章
[Command-Line Options], 11页)， 内部计数器的初始值为1。


7.49 .long expressions
.long is the same as ‘.int’, see Section 7.38 [.int], page 44.

7.49 .long expressions
.long是.int的等价命令，见7.38 [.int], 44页.

7.50 .macro
The commands .macro and .endm allow you to define macros that generate assembl
y output. For example, this definition specifies a macro sum that puts a seque
nce of numbers into memory:
.macro sum from=0, to=5
.long \from
.if \to-\from
sum "(\from+1)",\to
.endif
.endm
With that definition, ‘SUM 0,5’ is equivalent to this assembly input:
.long 0
.long 1
.long 2
.long 3
.long 4
.long 5
.macro macname
.macro macname macargs ...
Begin the definition of a macro called macname. If your macro definition requi
res arguments, specify their names after the macro name, separated by commas o
r spaces. You can supply a default value for any macro argument by following t
he name with ‘=deflt’. For example, these are all valid .macro statements:


.macro comm
Begin the definition of a macro called comm, which takes no arguments.
.macro plus1 p, p1
.macro plus1 p p1
Either statement begins the definition of a macro called plus1,which takes two
arguments; within the macro definition, write ‘\p’ or ‘\p1’ to evaluate t
he arguments.
.macro reserve_str p1=0 p2
Begin the definition of a macro called reserve_str, with two arguments. The fi
rst argument has a default value, but not the second. After the definition is
complete, you can call the macro either as ‘reserve_str a, b’ (with ‘\p1’
evaluating to a and ‘\p2’ evaluating to b), or as ‘reserve_str ,b’ (with ‘
\p1’ evaluating as the default, in this case ‘0’, and ‘\p2’ evaluating to
b).
When you call a macro, you can specify the argument values either by position,
or by keyword. For example, ‘sum 9,17’ is equivalent to ‘sum to=17, from=9
’.
.endm Mark the end of a macro definition.
.exitm Exit early from the current macro definition.
\@ as maintains a counter of how many macros it has executed in this pseudov-a
riable; you can copy that number to your output with ‘\@’, but only within a
macro definition.


7.50 .macro
本命令.macro和.endm命令允许您定义宏来生成汇编输出。例如，下面的语句定义了一个宏
sum，这个宏把一个数字序列放入内存。

.macro sum from=0, to=5
.long \from
.if \to-\from
sum "(\from+1)",\to
.endif
.endm
使用上述定义，'SUM 0,5'语句就等于输入下面的汇编语句：
.long 0
.long 1
.long 2
.long 3
.long 4
.long 5

.macro macname
.macro macname macargs ...
开始定义一个名为macname的宏。如果您的宏需要使用参数，则在宏的名字后指定他们的名
字，参数之间用逗号或空格分隔。您可以为任意的参数提供参数的缺省值，只需要在参数
后使用“=deflt”，。例如，下列都是合法的宏定义语句：
.macro comm
定义一个名为comm宏,不使用参数。
.macro plus1 p, p1
.macro plus1 p p1
两个语句都声明要定义一个名为plus1的宏，这个宏需要两个参数，在宏定义体内，使用'
\p'或'\p1'来引用参数的值。
.macro reserve_str p1=0 p2
声明要定义一个名为reserve_str的宏，使用两个参数。第一个参数有缺省值，第二个没有
缺省值。宏定义完成后，您可以通过‘reserve_str a, b’(宏体中‘\p1’引用a的值，‘
\p2’引用b值)或通过‘reserve_str ,b’(‘\p1’使用缺省值，在此为‘0’，‘\p2’引
用b的值)来调用这个宏。

当调用一个宏时，您既可以通过位置指定参数值，也可以通过关键字指定参数值。例如，
‘sum 9,17’和‘sum to=17, from=9’是等价的。
.endm 标志宏定义体的结束。
.exitm 提前从当前宏定义体中退出。
\@ 这个伪变量其实是as维护的一个计数器，用来统计执行了多少个宏。您可以通过使用\
@把这个数字复制到您的输出中，但仅限于在宏定义体中使用。


7.51 .nolist
Control (in conjunction with the .list directive) whether or not assembly list
ings are generated. These two directives maintain an internal counter (which i
s zero initially). .list increments the counter, and .nolist decrements it. As
sembly listings are generated whenever the counter is greater than zero.

7.51 .nolist
控制（和.list命令配合）是否生成汇编列表。这两个命令维护一个内部的计数器（计数器
初始值为0）.list命令增加计数器的值，.nolist减少计数器的值。当计数器的值大与0时
将汇编列表。


7.52 .octa bignums
This directive expects zero or more bignums, separated by commas. For each big
num, it emits a 16-byte integer.
The term “octa” comes from contexts in which a “word” is two bytes; hence
octa-word for 16 bytes.

7.52 .octa bignums
本命令可以不带参数或多个由逗号分隔开的巨数bignum，针对每个巨数bignum,它生成一个
16个字节的整数。
术语"octa"来源：word为2个字节，故此octa-word为16个字节。


7.53 .org new-lc , fill
Advance the location counter of the current section to new-lc. new-lc is eithe
r an absolute expression or an expression with the same section as the current
subsection. That is, you can’t use .org to cross sections: if new-lc has the
wrong section, the .org directive is ignored. To be compatible with former as
semblers, if the section of new-lc is absolute, as issues a warning, then pret
ends the section of new-lc is the same as the current subsection.
.org may only increase the location counter, or leave it unchanged; you cannot
use .org to move the location counter backwards.
Because as tries to assemble programs in one pass, new-lc may not be undefined
. If you really detest this restriction we eagerly await a chance to share you
r improved assembler.
Beware that the origin is relative to the start of the section, not to the sta
rt of the subsection. This is compatible with other people’s assemblers.
When the location counter (of the current subsection) is advanced, the interve
ning bytes are filled with fill which should be an absolute expression. If the
comma and fill are omitted, fill defaults to zero.

7.53 .org new-lc , fill
向后移动当前段的位置计数器至new-lc。new-lc要么是一个纯粹的表达式，要么这个表达
式与当前子段在同一个段中。换句话说，就是您不能使用.org进行段超越。如果new-lc指
向错误的段，则忽略.org命令。为了兼容以前的汇编器，如果new-lc指向一个地址独立的
段，as发出一个警告，并假定new-lc指向当前子段。
.org 仅仅可以增大位置计数器，或者保持位置计数器不变；您不能使用.org命令把位置计
数器向回移动。
因为as尽量一次完成程序汇编，所以不能使用未定义的new-lc。如果您厌恶这个限制，我
们急切期待有机会分享经过您改进的汇编器。
注意起点相对于段的首地址，而不是子段的首地址。这与其他的汇编器相兼容。
当（当前语句块）位置计数器到达指定位置，用fill填充该字节，fill必须是纯粹的表达
式。如果没有给出逗号和fill，fill值缺省为0。


7.54 .p2align[wl] abs-expr, abs-expr, abs-expr
Pad the location counter (in the current subsection) to a particular storage b
oundary. The first expression (which must be absolute) is the number of low-or
der zero bits the location counter must have after advancement. For example ‘
.p2align 3’ advances the location counter until it a multiple of 8. If the lo
cation counter is already a multiple of 8, no change is needed.
The second expression (also absolute) gives the fill value to be stored in the
padding bytes. It (and the comma) may be omitted. If it is omitted, the paddi
ng bytes are normally zero. However, on some systems, if the section is marked
as containing code and the fill value is omitted, the space is filled with no
-op instructions.
The third expression is also absolute, and is also optional. If it is present,
it is the maximum number of bytes that should be skipped by this alignment di
rective. If doing the alignment would require skipping more bytes than the spe
cified maximum, then the alignment is not done at all. You can omit the fill v
alue (the second argument) entirely by simply using two commas after the requi
red alignment; this can be useful if you want the alignment to be filled with
no-op instructions when appropriate.
The .p2alignw and .p2alignl directives are variants of the .p2align directive.
The .p2alignw directive treats the fill pattern as a two byte word value. The
.p2alignl directives treats the fill pattern as a four byte longword value. F
or example, .p2alignw 2,0x368d will align to a multiple of 4. If it skips two
bytes, they will be filled in with the value 0x368d (the exact placement of th
e bytes depends upon the endianness of the processor). If it skips 1 or 3 byte
s, the fill value is undefined.

7.54 .p2align[wl] abs-expr, abs-expr, abs-expr
增加位置计数器(在当前的子段)使它指向规定的存储边界。第一个表达式参数(结果必须是
纯粹的数字) 代表位置计数器移动后，计数器中连续为0的低序位数量。例如‘.align 3’
向后移动位置指针直至8的倍数（指针的最低的3位为0）。如果地址已经是8倍数，则无需
移动。
第二个表达式参数(结果必须是纯粹的数字)给出填充字节的值。用这个值填充位置计数器
越过的地方。这个参数(和逗点)可以省略。如果省略它，填充字节的值通常默认为0。但在
某些系统上，如果本段标识为包含代码，而填充值被省略,则使用no-op指令填充填充区。

第3个参数表达式的结果也必须是纯粹的数字，这个参数是可选的。如果存在第3个参数，
它代表本对齐命令允许越过字节数的最大值。如果完成这个对齐需要跳过的字节比指定的
最大值还多,则根本无法完成对齐。您可以在边界基准后简单地使用两个逗号，以省略填充
值参数(第二参数)；如果您想在适当的时候，对齐操作自动使用no-op指令填充，这个方法
将非常奏效。
.p2alignw和.p2alignl是.p2align命令的变化形式。.p2alignw 使用2个字节来填充填充区
。.p2alignl使用4字节来填充。例如,. .p2alignw 2,0x368d将地址对齐到4的倍数，如果
它跳过2个字节，GAS将使用0x368d填充这2个字节(字节的准确的位置视处理器的存储方式
而定)。如果它跳过1或3个字节,填充值则不明确。


7.55 .previous
This is one of the ELF section stack manipulation directives. The others are .
section (see Section 7.66 [Section], page 52), .subsection (see Section 7.79 [
SubSection], page 56), .pushsection (see Section 7.61 [PushSection], page 50),
and .popsection (see Section 7.56 [PopSection], page 50).
This directive swaps the current section (and subsection) with most recently r
eferenced section (and subsection) prior to this one. Multiple .previous direc
tives in a row will flip between two sections (and their subsections).
In terms of the section stack, this directive swaps the current section with t
he top section on the section stack.

7.55 .previous
这是一个ELF段堆栈操作命令。其他的段堆栈操作命令还有.section (见 7.66 [Section]
, 52页), .subsection (见 7.79 [SubSection], 56页),.pushsection (见 7.61 [PushS
ection], 50页), 和 .popsection (见 7.56 [PopSection], 50页)。
本命令交换当前段（及其子段）和最近访问过的段（及其子段）。多个连续的.previous命
令将使当前位置两个段（及其子段）之间反复切换。
用段堆栈的术语来说，本命令使当前段和堆顶段交换位置。


7.56 .popsection
This is one of the ELF section stack manipulation directives. The others are .
section (see Section 7.66 [Section], page 52), .subsection (see Section 7.79 [
SubSection], page 56), .pushsection (see Section 7.61 [PushSection], page 50),
and .previous (see Section 7.55 [Previous], page 49).
This directive replaces the current section (and subsection) with the top sect
ion (and subsection) on the section stack. This section is popped off the stac
k.

7.56 .popsection
这是一个ELF段堆栈操作命令。其他的段堆栈操作命令还有.section(见 7.66 [Section],
52页), .subsection (见 7.79 [SubSection], 56页),.pushsection (见 7.61 [PushSe
ction], 50页), 和 .previous (见 7.55 [Previous], 49页).
本命令用堆栈顶段（及其子段）替代当前段（及其子段）。堆栈顶段出栈。

7.57 .print string
as will print string on the standard output during assembly. You must put stri
ng in double quotes.

7.57 .print string
as会在标准输出上打印string字符串。String必须使用双引号。


7.58 .protected names
This one of the ELF visibility directives. The other two are .hidden (see Sect
ion 7.32 [Hidden], page 42) and .internal (see Section 7.39 [Internal], page 4
4).
This directive overrides the named symbols default visibility (which is set by
their binding: local, global or weak). The directive sets the visibility to p
rotected which means that any references to the symbols from within the compon
ents that defines them must be resolved to the definition in that component, e
ven if a definition in another component would normally preempt this.

7.58 .protected names
这是一条ELF可见度的相关命令。其它两条是.hidden (参见 7.32 [Hidden], 42页)和 .i
nternal (参见 7.39 [Internal], 44页)。
本命令将取消指定符号的可见度缺省值（可见度由其他命令捆绑设定：local, global, w
eak）本命令将可见度设置为protected,这个可见度意味着：在定义此符号的部件内对此符
号的任何访问，都必须解析到这个部件内的定义体。即使其他部件中存在一个正常情况下
比此优先的定义体。

7.59 .psize lines, columns
Use this directive to declare the number of lines—and, optionally, the number
of columns—to use for each page, when generating listings.
If you do not use .psize, listings use a default line-count of 60. You may omi
t the comma and columns specification; the default width is 200 columns.
as generates formfeeds whenever the specified number of lines is exceeded (or
whenever you explicitly request one, using .eject).
If you specify lines as 0, no formfeeds are generated save those explicitly sp
ecified with .eject.

7.59 .psize lines , columns
当生成清单列表时，使用本命令声明每页的行数—还可以可选地声明列数。
如果您不使用本命令，清单列表的行数为默认的60行。可以省略逗号和列参数：默认值为
200列。
当指定的行数过多的话，as会产生进纸操作。（如果您确实需要一个进纸动作，可以使用
.eject命令）
如果您指定行数为0，则不产生进纸操作，除非您明确地使用了.eject命令。


7.60 .purgem name
Undefine the macro name, so that later uses of the string will not be expanded
. See Section 7.50 [Macro], page 47.

7.60 .purgem name
取消name的宏定义，后面使用字符串name不会被宏扩展。参见 7.50 [Macro], 47页。


7.61 .pushsection name , subsection
This is one of the ELF section stack manipulation directives. The others are .
section (see Section 7.66 [Section], page 52), .subsection (see Section 7.79 [
SubSection], page 56), .popsection (see Section 7.56 [PopSection], page 50), a
nd .previous (see Section 7.55 [Previous], page 49).
This directive is a synonym for .section. It pushes the current section (and s
ubsection) onto the top of the section stack, and then replaces the current se
ction and subsection with name and subsection.

7.61 .pushsection name , subsection
本命令是一个ELF段堆栈操作命令。其余的几个是.section (参见 7.66 [Section], 52页
) , .subsection (参见7.79 [SubSection], 56页),.popsection (参见 7.56 [PopSecti
on], 50页), 和 .previous (参见 7.55 [Previous], 49页)。
本命令与.section命令是等价的。它将当前段（及子段）推入段堆栈的顶部。并使用name
和subsection来替代当前段和子段。

7.62 .quad bignums
.quad expects zero or more bignums, separated by commas. For each bignum, it e
mits an 8-byte integer. If the bignum won’t fit in 8 bytes, it prints a warni
ng message; and just takes the lowest order 8 bytes of the bignum.
The term “quad” comes from contexts in which a “word” is two bytes; hence
quad-word for 8 bytes.

7.62 .quad bignums
.quad 可带0或多个bignum参数，每个参数由逗号分隔。对于每个bignum都汇编成一个8字
节的整数。如果某个bignum用8字节无法表示，则给出警告信息；只汇编这个bignum的最低
8字节。
术语“quad”源于一个“word”代表2个字节，所以quad-word代表8个字节。

7.63 .rept count
Repeat the sequence of lines between the .rept directive and the next .endr di
rective count times.
For example, assembling
.rept 3
.long 0
.endr
is equivalent to assembling
.long 0
.long 0
.long 0

7.63 .rept count
汇编.rept和.endr之间的语句count次。
如, 汇编下列语句：
.rept 3
.long 0
.endr
与下列语句是等价的：
.long 0
.long 0
.long 0

7.64 sbttl "subheading"
Use subheading as the title (third line, immediately after the title line) whe
n generating assembly listings.
This directive affects subsequent pages, as well as the current page if it app
ears within ten lines of the top of a page.

7.64 sbttl "subheading"
当生成汇编清单时，使用subheading作为标题（第3行，紧跟在标题行之后）。
本命令对清单的后续页起作用，如果它位于当前页的前10行内，则对当前页也起作用。



7.65 .scl class
Set the storage-class value for a symbol. This directive may only be used insi
de a .def/.endef pair. Storage class may flag whether a symbol is static or ex
ternal, or it may record further symbolic debugging information.
The ‘.scl’ directive is primarily associated with COFF output; when configur
ed to generate b.out output format, as accepts this directive but ignores it.


7.65 .scl class
设置一个符号的存储类型值（storage-class value）。本命令只能在.def/.endef之间使
用。符号的存储类型可以表明符号是static类型或是external类型，或者进一步记录符号
的调试信息。
‘.scl’命令主要与在COFF输出有关，当生成b.out输出格式时，as接受本命令，但忽略本
命令。




7.66 .section name (COFF version)
Use the .section directive to assemble the following code into a section named
name.
This directive is only supported for targets that actually support arbitrarily
named sections; on a.out targets, for example, it is not accepted, even with
a standard a.out section name.
For COFF targets, the .section directive is used in one of the following ways:

.section name [, "flags"]
.section name [, subsegment]
If the optional argument is quoted, it is taken as flags to use for the sectio
n. Each flag is a single character. The following flags are recognized:
b bss section (uninitialized data)
n section is not loaded
w writable section
d data section
r read-only section
x executable section
s shared section (meaningful for PE targets)
If no flags are specified, the default flags depend upon the section name. If
the section name is not recognized, the default will be for the section to be
loaded and writable. Note the n and w flags remove attributes from the section
, rather than adding them, so if they are used on their own it will be as if n
o flags had been specified at all.
If the optional argument to the .section directive is not quoted, it is taken
as a subsegment number (see Section 4.4 [Sub-Sections], page 25).

7.66 .section name (COFF 版本)
使用.section命令将后续的代码汇编进一个定名为name的段。
本命令只能在目标格式真正支持任意命名段时使用；例如，汇编一个a.out目标格式时，即
使name是一个标准的a.out段名，本命令也不被接受。
当目标格式为COFF时，.section命令的使用为下面某一种格式：
.section name[, "flags"]
.section name[, subsegment]
如可选参数使用了引号，它将被视为该段的标志(flags)。每个标记是单个的字符。下列是
认可的标志。
b bss 段 (未初始化的数据)
n 未装入内存的段
w 可写的段
d 数据段
r 只读段
x 代码段 （executable section）
s 共享段 （目标为PE格式有意义）
如果本命令没有指定标志，则依靠段名来确定标志缺省值。如果该段名没有使用标准段名
，则默认该段已装入内存并且可写。注意在使用n和w标志组合时，不是增加这组属性，而
是删除该段的属性。所以如果只存在这两个标志，就代表该段没有指定任何标志。
如果本命令的可选参数没有使用引号，参数将被视为子段的编号。(参见 4.4 [Sub-Secti
ons], 25页)。



7.67 .section name (ELF 版本)
This is one of the ELF section stack manipulation directives. The others are .
subsection (see Section 7.79 [SubSection], page 56), .pushsection (see Section
7.61 [PushSection], page 50), .popsection (see Section 7.56 [PopSection], pag
e 50), and .previous (see Section 7.55 [Previous], page 49).
For ELF targets, the .section directive is used like this:
.section name [, "flags"[, @type]]
The optional flags argument is a quoted string which may contain any combinati
on of the following characters:
a section is allocatable
w section is writable
x section is executable
The optional type argument may contain one of the following constants:
@progbits section contains data
@nobits section does not contain data (i.e., section only occupies space)

If no flags are specified, the default flags depend upon the section name. If
the section name is not recognized, the default will be for the section to hav
e none of the above flags: it will not be allocated in memory, nor writable, n
or executable. The section will contain data.
For ELF targets, the assembler supports another type of .section directive for
compatibility with the Solaris assembler:
.section "name"[, flags...]
Note that the section name is quoted. There may be a sequence of comma separat
ed flags:
\#alloc section is allocatable
\#write section is writable
\#execinstr section is executable
This directive replaces the current section and subsection. The replaced secti
on and subsection are pushed onto the section stack. See the contents of the g
as testsuite directory gas/testsuite/gas/elf for some examples of how this dir
ective and the other section stack directives work.

7.67 .section name (ELF 版本)
本命令是ELF的段堆栈操作命令之一，其他的段堆栈命令为.subsection (见 Section 7.7
9 [SubSection], page 56), .pushsection (见Section 7.61 [PushSection], page 50)
, .popsection (见 Section 7.56 [PopSection], page 50), and .previous (见 Secti
on 7.55 [Previous], page 49).
当目标格式为ELF时，.section命令应如下使用：
.section name [, "flags"[, @type]]
可选参数flags是被引号包围的字符串，可以由下列字符的任意组合：
a 可分配的段（allocatable）
w 可写段
x 代码段
可选的参数type可以包含下列的任一常量：
@progbits 包含数据的段
@nobits 不包含数据的段(只占用空间的段)
如果本命令没有指定标志，则依靠段名来确定标志缺省值。如果段名不是标准的段名，则
默认的该段不包含上述标志：该段不可分配内存，不可写，不可执行。该段是包含数据的
段。
当目标格式为ELF时,as还支持另一种形式的.section命令，以便兼容Solaris的汇编器：

.section "name"[, flags...]
注意段名是使用引号包围的，可能存在一系列由逗号分隔分隔的标志：
\#alloc 可分配的段（section is allocatable）
\#write 可写的段
\#execinstr 可执行的段
本命令将（用段名为name的段）替代当前段和子段。被替换的段将被推入段堆栈。参见ga
s的测试套件目录gas/testsuite/gas/elf，可以找到一些本命令和其他段堆栈操作命令的
例子。

7.68 .set symbol, expression
Set the value of symbol to expression. This changes symbol’s value and type t
o conform to expression. If symbol was flagged as external, it remains flagged
(see Section 5.5 [Symbol Attributes], page 30).
You may .set a symbol many times in the same assembly.
If you .set a global symbol, the value stored in the object file is the last v
alue stored into it.
The syntax for set on the HPPA is ‘symbol .set expression’.

7.68 .set symbol, expression
设置symbol为expression。这将改变symbol的值域和类型领域以符合expression参数。如
果symbol已被标志为external，则symbol保持它的标志。(见 5.5 [Symbol Attributes],
30页)。
您可以在同一个汇编程序中多次使用.set命令来设置同一个符号。
如果设置一个全局符号，该符号在目标文件中值为最后设定的值。
在HPPA上的语法是‘symbol .set expression’。

7.69 .short expressions
.short is normally the same as ‘.word’. See Section 7.92 [.word], page 59.

In some configurations, however, .short and .word generate numbers of differen
t lengths; see Chapter 8 [Machine Dependencies], page 61.

7.69 .short expressions
本命令通常和’.word’命令一样，见7.92 [.word], 59页.
然而在某些配置中，.short和.word命令生成的数字长度却不相同；见第8章 [Machine De
pendencies], 61页.



7.70 .single flonums
This directive assembles zero or more flonums, separated by commas. It has the
same effect as .float. The exact kind of floating point numbers emitted depen
ds on how as is configured. See Chapter 8 [Machine Dependencies], page 61.

7.70 .single flonums
本命令可以汇编0个或多个浮点参数，各个参数之间使用逗号分隔。它的作用和.float相同
。生成浮点数的具体类型视as的配置而定。见第8章 [Machine Dependencies], 61页。






\--------------------
一切有为法 如梦幻泡影




\# 回复：linux下汇编的Directive Operands 2004-09-08 3:25 PM n9871009
Re: 7 汇编器命令(下) [re: amtb]



位组合:bit pattern，想不出有什么特别的意义，大概指的是有限个数的0和1所有的组合
吧。Fix me.
sleb128/uleb128: 基于128位的低地址结尾带/无符号的数。您有什么好建议？
==========================下==================================
7.71 .size (COFF 版本)
This directive is generated by compilers to include auxiliary debugging inform
ation in the symbol table. It is only permitted inside .def/.endef pairs.
‘.size’ is only meaningful when generating COFF format output; when as is ge
nerating b.out, it accepts this directive but ignores it.

7.71 .size (COFF 版本)
本命令一般由编译器生成，以在符号表中加入辅助调试信息。本命令只能在.def/.endef命
令对之间使用。
本命令只在生成COFF格式的输出文件有意义。当as生成b.out时，as接受本命令但忽略之。




7.72 .size name , expression (ELF 版本)
This directive is used to set the size associated with a symbol name. The size
in bytes is computed from expression which can make use of label arithmetic.
This directive is typically used to set the size of function symbols.
本命令经常用来设置符号name的内存大小。内存大小的单位是字节, 通过计算参数expres
sion得到，参数expression中可以使用标签进行计算。本命令常用来设置函数符号的长度
。

7.73 .sleb128 expressions
sleb128 stands for “signed little endian base 128.” This is a compact, varia
ble length representation of numbers used by the DWARF symbolic debugging form
at. See Section 7.86 [Uleb128], page 58.

7.73 .sleb128 expressions
sleb128代表“signed little endian base 128”(低地址结尾的带符号128位基数)。这是
一个紧凑的，变长的数字表示方法，当使用DWARF符号调试格式时使用。参见7.86 [Uleb1
28], 58页。



7.74 .skip size , fill
This directive emits size bytes, each of value fill. Both size and fill are ab
solute expressions. If the comma and fill are omitted, fill is assumed to be z
ero. This is the same as ‘.space’.

7.74 .skip size , fill
本命令生成size个字节，每个字节的值都是fill。参数size和fill都必须是纯粹的表达式
。如果省略逗号和fill,则默认fill的值为0。这与’.space’相同。



7.75 .space size , fill
This directive emits size bytes, each of value fill. Both size and fill are ab
solute expressions. If the comma and fill are omitted, fill is assumed to be z
ero. This is the same as ‘.skip’.
Warning: .space has a completely different meaning for HPPA targets; use .bloc
k as a substitute. See HP9000 Series 800 Assembly Language Reference Manual (H
P 92432-90001) for the meaning of the .space directive. See Section 8.8.5 [HPP
A Assembler Directives], page 84, for a summary.
On the AMD 29K, this directive is ignored; it is accepted for compatibility wi
th other AMD 29K assemblers.
Warning: In most versions of the gnu assembler, the directive .space has the e
ffect of .block See Chapter 8 [Machine Dependencies], page 61.

7.75 .space size , fill
本命令生成size个字节，每个字节的值都是fill。参数size和fill都必须是纯粹的表达式
。如果省略了逗号和fill,则默认fill的值为0。这与’.skip’相同。
警告：在生成HPPA目标格式时，.space的意义完全不同。应该使用.block命令替代本命令
。在HP9000系列800汇编语言参考手册(HP 92432-90001)，可以找到.space命令的用法。参
见 8.8.5 [HPPA Assembler Directives],84页, 可以找到使用摘要。
在AMD 29K上，本命令将被忽略。出于兼容其它一些AMD 29K汇编器的目的，as接受本命令
。
警告：在gnu汇编器大多数版本中，这个.space命令和.block命令等效。见第8章 [Machin
e Dependencies], 61页。

7.76 .stabd, .stabn, .stabs
There are three directives that begin ‘.stab’. All emit symbols (see Chapter
5 [Symbols], page 29), for use by symbolic debuggers. The symbols are not ent
ered in the as hash table:they cannot be referenced elsewhere in the source fi
le. Up to five fields are required:
string This is the symbol’s name. It may contain any character except ‘\000’
, so is more general than ordinary symbol names. Some debuggers used to code a
rbitrarily complex structures into symbol names using this field.
type An absolute expression. The symbol’s type is set to the low 8 bits of th
is expression. Any bit pattern is permitted, but ld and debuggers choke on sil
ly bit patterns.
other An absolute expression. The symbol’s “other” attribute is set to the
low 8 bits of this expression.
desc An absolute expression. The symbol’s descriptor is set to the low 16 bit
s of this expression.
Value An absolute expression that becomes the symbol’s value.
If a warning is detected while reading a .stabd, .stabn, or .stabs statement,
the symbol has probably already been created; you get a half-formed symbol in
your object file. This is compatible with earlier assemblers!
.stabd type , other , desc
The “name” of the symbol generated is not even an empty string. It is a null
pointer, for compatibility. Older assemblers used a null pointer so they didn
’t waste space in object files with empty strings.
The symbol’s value is set to the location counter, relocatably. When your pro
gram is linked, the value of this symbol is the address of the location counte
r when the .stabd was assembled.
.stabn type , other , desc , value
The name of the symbol is set to the empty string "".
.stabs string , type , other , desc , value
All five fields are specified.

7.76 .stabd, .stabn, .stabs
有3个以.stab开头的命令。它们都用来产生符号，(参见第5章 [Symbols], 29页),供符号
调试器使用。这些符号没有收入as的散列表中：这些符号不能被源文件其他地方所访问。
它们至少需要5个属性域：
string 这是符号的名字。它可以包含除‘\000’之外的任何字符，故此可用名比普通符号
名更广泛。很多调试器经常利用这个空间，把任意复杂的结构编码为符号名。
type 这是一个纯粹的表达式。符号的类型属性由这个表达式的低8位设定。任何的位组合
（bit pattern）都可以，但连接器和调试器会被没有义的位组合所中断。
other 这是一个纯粹的表达式。由这个表达式的低8位设定此符号的“其它”属性。
desc 这是一个纯粹的表达式。由这个表达式的低16位设定此符号的描述符。
Value 这个纯粹的表达式将作为符号的值。

如果汇编.stabd, .stabn, 或 .stabs语句时引发了一个警告，该符号有可能已经被创建；
在目标文件中存在一个半成品的符号。这样做兼容于早期的汇编器！

.stabd type , other , desc
生成符号的“名字”甚至不是空字符串，而是一个空指针（null），这样安排是出于对兼
容性要求。早期的汇编器经常使用空指针，以避免空字符串在目标文件中浪费空间。
这个符号的值（值域）在重定位时设置为位置计数器的值。当程序连接之后，这个符号的
值是.stabd命令汇编时位置计数器的地址。
.stabn type , other , desc , value
这个符号的名字被设置为空字符串“”。
.stabs string , type , other , desc , value
5个属性域全部指定好。



7.77 .string "str"
Copy the characters in str to the object file. You may specify more than one s
tring to copy, separated by commas. Unless otherwise specified for a particula
r machine, the assembler marks the end of each string with a 0 byte. You can u
se any of the escape sequences described in Section 3.6.1.1 [Strings], page 19
.

7.77 .string "str"
将参数str中的字符复制到目标文件中去。您可以指定多个字符串进行复制，之间使用逗号
分隔。除非另外指定了具体的机器，汇编器将在每个字符串后追加一个0字节作为标记。您
可以使用任意的逃逸序列，参见19页中3.6.1.1 [Strings]的描述。



7.78 .struct expression
Switch to the absolute section, and set the section offset to expression, whic
h must be an absolute expression. You might use this as follows:
.struct 0
field1:
.struct field1 + 4
field2:
.struct field2 + 4
field3:
This would define the symbol field1 to have the value 0, the symbol field2 to
have the value 4, and the symbol field3 to have the value 8. Assembly would be
left in the absolute section, and you would need to use a .section directive
of some sort to change to some other section before further assembly.

7.78 .struct expression
切换到独立地址段，并用expression设定段的偏移量，expression必须是个纯粹的表达式
。您可以如下使用：
.struct 0
field1:
.struct field1 + 4
field2:
.struct field2 + 4
field3:

定义符号field1的值为0，符号field2的值为4，符号field3的值为8。这段汇编程序将保存
在独立地址段中，在进行下一步汇编前，您需要使用一个某种类型的.section命令，以切
换到相应的段。



7.79 .subsection name
This is one of the ELF section stack manipulation directives. The others are .
section (see Section 7.66 [Section], page 52),.pushsection (see Section 7.61 [
PushSection], page 50), .popsection (see Section 7.56 [PopSection], page 50),
and .previous (see Section 7.55 [Previous], page 49).
This directive replaces the current subsection with name. The current section
is not changed. The replaced subsection is put onto the section stack in place
of the then current top of stack subsection.

7.79 .subsection name
本命令是一个ELF段堆栈操作命令。其它的几个命令是（参见 7.66 [Section], 52页）,
.pushsection (参见 7.61 [PushSection],50页), .popsection (参见 7.56 [PopSectio
n], 50页), and .previous (参见7.55 [Previous], 49页)。
本命令用name子段替换当前子段。当前段并不改变。被替换的子段入段堆栈，成为段堆栈
的新栈顶。



7.80 .symver
Use the .symver directive to bind symbols to specific version nodes within a s
ource file. This is only supported on ELF platforms, and is typically used whe
n assembling files to be linked into a shared library. There are cases where i
t may make sense to use this in objects to be bound into an application itself
so as to override a versioned symbol from a shared library.
For ELF targets, the .symver directive can be used like this:
.symver name, name2@nodename
If the symbol name is defined within the file being assembled, the .symver dir
ective effectively creates a symbol alias with the name name2@nodename, and in
fact the main reason that we just don’t try and create a regular alias is th
at the @ character isn’t permitted in symbol names. The name2 part of the nam
e is the actual name of the symbol by which it will be externally referenced.
The name name itself is merely a name of convenience that is used so that it i
s possible to have definitions for multiple versions of a function within a si
ngle source file, and so that the compiler can unambiguously know which versio
n of a function is being mentioned. The nodename portion of the alias should b
e the name of a node specified in the version script supplied to the linker wh
en building a shared library. If you are attempting to override a versioned sy
mbol from a shared library, then nodename should correspond to the nodename of
the symbol you are trying to override.
If the symbol name is not defined within the file being assembled, all referen
ces to name will be changed to name2@nodename. If no reference to name is made
, name2@nodename will be removed from the symbol table.
Another usage of the .symver directive is:
.symver name, name2@@nodename
In this case, the symbol name must exist and be defined within the file being
assembled. It is similar to name2@nodename. The difference is name2@@nodename
will also be used to resolve references to name2 by the linker.
The third usage of the .symver directive is:
.symver name, name2@@@nodename
When name is not defined within the file being assembled, it is treated as nam
e2@nodename. When name is defined within the file being assembled, the symbol
name, name, will be changed to name2@@nodename.

7.80 .symver
使用.symver命令把符号装订到在源文件里指定的节点。本命令只在ELF平台上可用，如果
当前汇编的文件被连接到一个共享库中时常常用到。有些情况下应该在目标文件中使用本
命令，把目标文件自我装订进某个应用软件中，从而取代共享库中旧版本符号。
对于ELF目标，.symver命令可以这样使用：
.symver name, name2@nodename
如果符号name的定义在当前正在汇编的文件中，这个.symver命令实际用name2@nodename创
建一个符号别名，而且我们不打算创建一个正规的别名，因为在符号名中是不允许存在‘
@’这个字符的。别名中name2才是符号的真正名字，外部访问是通过这个名字进行的。符
号自己的名字name仅仅为了使用上的方便，这样在同一个源文件中的一个函数才可能有多
个定义体；编译器才能够清楚当前使用的函数是哪个具体的定义。别名中的nodename部分
应是某个节点的名字，这个节点的名字是在建立共享库时，提供给连接器的版本脚本中指
定的。如果您想覆盖共享库中的旧版本符号，则nodename应该是将被取代符号的节点名。

如果符号name的定义不在当前正在汇编的文件中，则所有对name的访问都变为对name2@no
dename的访问。如果根本没有对name的访问，将会把name2@nodename从符号表中删除。

.symver命令的另一种用法：
.symver name, name2@@nodename
在这种情况下，符号name必须存在，并且它必须在当前正在汇编的文件中被定义。这类似
与name2@nodename。区别是name2@@nodename还被连接器用来解析对name2的访问。//注：
对name2的访问被转向到nodename
.symver命令的第3种用法：
.symver name, name2@@@nodename
如果name不是在当前正在汇编的文件中被定义的时候，对符号的处理就如同name2@nodena
me。如果name是当前正在汇编的文件中定义的，符号的名字name，会被转换为name2@@nod
ename。



7.81 .tag structname
This directive is generated by compilers to include auxiliary debugging inform
ation in the symbol table. It is only permitted inside .def/.endef pairs. Tags
are used to link structure definitions in the symbol table with instances of
those structures.
‘.tag’ is only used when generating COFF format output; when as is generatin
g b.out, it accepts this directive but ignores it.

7.81 .tag structname
本命令由编译器生成，用来在符号表中增加调试辅助的信息。本命令只允许在.def/.ende
f语句对内使用。标饰（tags）常用来连接符号表中的结构定义和该结构实例。
‘.tag’只能在生成COFF格式的输出文件时使用。当as生成b.out格式的输出文件时，接受
本命令但忽略之。



7.82 .text subsection
Tells as to assemble the following statements onto the end of the text subsect
ion numbered subsection, which is an absolute expression. If subsection is omi
tted, subsection number zero is used.

7.82 .text subsection
通知as把后续语句汇编到编号为subsection的正文子段的末尾，subsection是一个纯粹的
表达式。如果省略了参数subsection，则使用编号为0的子段。


7.83 .title "heading"
Use heading as the title (second line, immediately after the source file name
and page number) when generating assembly listings.
This directive affects subsequent pages, as well as the current page if it app
ears within ten lines of the top of a page.

7.83 .title "heading"
当生成汇编清单时，把heading作为标题使用（标题在第2行，紧跟在源文件名和页号后）
。
如果这个命令出现在某页的前10行中，它不但作用影响到后续的页，也同样影响到当前页
。


7.84 .type int (COFF version)
This directive, permitted only within .def/.endef pairs, records the integer i
nt as the type attribute of a symbol table entry.
‘.type’ is associated only with COFF format output; when as is configured fo
r b.out output, it accepts this directive but ignores it.

7.84 .type int (COFF 版本)
本命令紧允许在.def/.endef 命令对之间使用，把整数int作为类型属性记录进符号表表项
。
‘.type’只和COFF格式的输出有关，当as配置生成b.out输出格式时，as接受本命令但忽
略之。

7.85 .type name , type description (ELF version)
This directive is used to set the type of symbol name to be either a function
symbol or an object symbol. There are five different syntaxes supported for th
e type description field, in order to provide compatibility with various other
assemblers. The syntaxes supported are:

.type <name>,#function
.type <name>,#object

.type <name>,@function
.type <name>,@object

.type <name>,%function
.type <name>,%object

.type <name>,"function"
.type <name>,"object"

.type <name> STT_FUNCTION
.type <name> STT_OBJECT

7.85 .type name , type description (ELF 版本)
本命令经常用来设置符号name的类型（属性）为函数符号或是目标符号两者之一。type d
escription部分允许使用5种不同的语法，以兼容众多的汇编器。这些语法是：

.type <name>,#function
.type <name>,#object

.type <name>,@function
.type <name>,@object

.type <name>,%function
.type <name>,%object

.type <name>,"function"
.type <name>,"object"

.type <name> STT_FUNCTION
.type <name> STT_OBJECT


7.86 .uleb128 expressions
uleb128 stands for “unsigned little endian base 128.” This is a compact, var
iable length representation of numbers used by the DWARF symbolic debugging fo
rmat. See Section 7.73 [Sleb128], page 54.

7.86 .uleb128 expressions
uleb128代表“unsigned little endian base 128”(低地址结尾的无符号128位基数)。这
是一个紧凑的，变长的数字表示方法，当使用DWARF符号调试格式时使用。参见7.83 [Sle
b128], 54页。



7.87 .val addr
This directive, permitted only within .def/.endef pairs, records the address a
ddr as the value attribute of a symbol table entry.
‘.val’ is used only for COFF output; when as is configured for b.out, it acc
epts this directive but ignores it.

7.87 .val addr
本命令只能在.def/.endef命令对之间使用，把addr的地址作为值属性存入符号表的表项中
。
‘.val’命令只能在COFF输出时使用；当as被配置成生成b.out输出时，接受本命令但忽略
之。



7.88 .version "string"
This directive creates a .note section and places into it an ELF formatted not
e of type NT VERSION. The note’s name is set to string.

7.88 .version "string"
本命令创建一个.note段，并把一个NT VERSION类型ELF格式的note放入该.note段。Note的
名字被设置为string。



7.89 .vtable_entry table, offset
This directive finds or creates a symbol table and creates a VTABLE_ENTRY relo
cation for it with an addend of offset.

7.89 .vtable_entry table, offset
本命令寻找或创建一个符号表，并用offset作偏移量的增量，为此符号表产生一个VTABLE
_ENTRY重定位。



7.90 .vtable_inherit child, parent
This directive finds the symbol child and finds or creates the symbol parent a
nd then creates a VTABLE_INHERIT relocation for the parent whose addend is the
value of the child symbol. As a special case the parent name of 0 is treated
as refering the *ABS* section.

7.90 .vtable_inherit child, parent
本命令寻找符号child, 并寻找或创建符号parent，为符号parent产生一个VTABLE_INHERI
T重定位，parent的偏移量增量为符号child的值。一个特例，如果parent的名字为0，则将
它交给*ABS*段处理。



7.91 .weak names
This directive sets the weak attribute on the comma separated list of symbol n
ames. If the symbols do not already exist, they will be created.

7.91 .weak names
本命令设置names中每个符号（由逗号分隔）的weak属性。如果这些符号尚不存在，则创建
这些符号。


7.92 .word expressions
This directive expects zero or more expressions, of any section, separated by
commas.
The size of the number emitted, and its byte order, depend on what target comp
uter the assembly is for.
Warning: Special Treatment to support Compilers
Machines with a 32-bit address space, but that do less than 32-bit addressing,
require the following special treatment. If the machine of interest to you do
es 32-bit addressing (or doesn’t require it; see Chapter 8 [Machine Dependenc
ies], page 61), you can ignore this issue.
In order to assemble compiler output into something that works, as occasionall
y does strange things to ‘.word’ directives. Directives of the form ‘.word
sym1-sym2’ are often emitted by compilers as part of jump tables. Therefore,
when as assembles a directive of the form ‘.word sym1-sym2’, and the differe
nce between sym1 and sym2 does not fit in 16 bits, as creates a secondary jump
table, immediately before the next label. This secondary jump table is preced
ed by a short-jump to the first byte after the secondary table. This short-jum
p prevents the flow of control from accidentally falling into the new table. I
nside the table is a long-jump to sym2. The original ‘.word’ contains sym1 m
inus the address of the long-jump to sym2.
If there were several occurrences of ‘.word sym1-sym2’ before the secondary
jump table, all of them are adjusted. If there was a ‘.word sym3-sym4’, that
also did not fit in sixteen bits, a long-jump to sym4 is included in the seco
ndary jump table, and the .word directives are adjusted to contain sym3 minus
the address of the long-jump to sym4; and so on, for as many entries in the or
iginal jump table as necessary.

7.92 .word expressions
本命令可不带表达式或带多个表达式，这些表达式可以属于任意段，每个表达式由逗号分
隔。
汇编生成的数字的大小，字节顺序视生成程序运行的目标机器而定。
警告：支持编译器的特殊处理
有些机器具有32位地址空间，但不能完全进行32位寻址，需要下列的特殊处理。如果您关
心的机器能够进行32位寻址，（或者根本不需要32位寻址；见第8章[机器相关性]，61页）
则可以忽略这个问题。
为了使由编译器产生源码的汇编结果能够正确地运行，as偶尔会对'.word'命令进行些奇怪
的操作。编译器在跳转表部分经常生成类似'.word sym1-sym2'形式的命令。所以，当as汇
编一条形如'.word sym1-sym2'的命令，且sym1和sym2之间的偏移量大于16位时，as会在下
个标签前创建一个'次级跳转表'，在'次级跳转表'前面加插上一个短-跳转指令,这个短-跳
转指令的目的地址是'次级跳转表'之后的第一个字节。 这个短跳转防止控制流程意外地落
入新的跳转表（次级跳转表）。在'次级跳转表'内是个目的地址为sym2的长-跳转指令。原
来的'.word'命令调整为sym1减去到sym2的长-跳转指令地址，。
如果在次级跳转表前出现了几个'.word sym1-sym2'，这些命令都要进行调整。如果存在一
个'.word sym3-sym4'，且地址差也大与16位，次级跳转表中将包含一个至sym4的长-跳转
指令，且.word命令将被调整为包含sym3减去到sym4长-跳转指令的地址； 如是类推，处理
原始跳转表中的需要处理的各个表项。



7.93 Deprecated Directives
One day these directives won’t work. They are included for compatibility with
older assemblers.
.abort
.line

7.93 不赞成使用的命令
将来下列命令可能不再被支持，它们的存在只是为了与老版本的汇编器相兼容。
.abort
.line