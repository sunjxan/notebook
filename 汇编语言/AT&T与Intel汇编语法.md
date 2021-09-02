[原网页](https://www.cnblogs.com/guochaoxxl/p/7083173.html)

　　由于绝大多数的国内程序员以前只接触过Intel格式的汇编语言，很少或几乎没有接触过AT&T汇编语言，虽然这些汇编代码都是Intel风格的。但在Unix和Linux系统中，更多采用的还是AT&T格式，两者在语法格式上有着很大的不同，其实完全可以使用原来汇编的思路解决问题，只要掌握下面两者的不同：

　　一、在AT&T汇编格式中，寄存器名要加上' %'作为前缀；而在Intel汇编格式中，寄存器名不需要加前缀。例如：

| AT&T格式   | Intel格式 |
| ---------- | --------- |
| pushl %eax | push eax  |

　　二、在AT&T汇编格式中，用'$'前缀表示一个立即操作数；而在Intel汇编格式中，立即数的表示不用带任何前缀。例如：

| AT&T格式 | Intel格式 |
| -------- | --------- |
| pushl $1 | push 1    |

　　三、AT&T和Intel格式中的源操作数和目标操作数的位置正好相反。在Intel汇编格式中，目标操作数在源操作数的左边；而在AT&T汇编格式中，目标操作数在源操作数的右边。例如：

| AT&T格式      | Intel格式  |
| ------------- | ---------- |
| addl $1, %eax | add eax, 1 |

　　四、在AT&T汇编格式中，操作数的字长由操作符的最后一个字母决定，后缀'b'、'w'、'l'分别表示操作数为字节（byte，8比特）、字（word，16比特）、长字（long，32比特）和四字（quadruple，64比特）；而在Intel汇编格式中，操作数的字长是用"byte ptr"和"word ptr"等前缀来表示的。例如：

| AT&T格式      | Intel格式            |
| ------------- | -------------------- |
| movb val, %al | mov al, byte ptr val |

　　五、在AT&T汇编格式中，绝对转移和调用指令（jump/call）的操作数前要加上'*'作为前缀，而在Intel格式中则不需要。

远程转移指令和远程子调用指令的操作码，在AT&T汇编格式中为"ljump"和"lcall"，而在Intel汇编格式中则为"jmp far"和"call far"，即：

| AT&T格式                     | Intel格式               |
| ---------------------------- | ----------------------- |
| ljump section,section,offset | jmp far section:offset  |
| lcall section,section,offset | call far section:offset |

　　与之相应的远程返回指令则为：

| AT&T格式           | Intel格式            |
| ------------------ | -------------------- |
| lret $stack_adjust | ret far stack_adjust |

　　六、在AT&T汇编格式中，内存操作数的寻址方式是
```
section:disp(base, index, scale)
```
 　而在Intel汇编格式中，内存操作数的寻址方式为：
```
section:[base + index*scale + disp]
```
 　无论形式如何，都是实现如下的地址计算：（其中base和index必须是寄存器，disp和scale可以是常数）
```
disp + base + index * scale
```
 　下面请看内存操作数的例子：

| AT&T格式                       | Intel格式                     |
| ------------------------------ | ----------------------------- |
| movl -4(%ebp), %eax            | mov eax, [ebp - 4]            |
| movl array(, %eax, 4), %eax    | mov eax, [eax*4 + array]      |
| movw array(%ebx, %eax, 4), %cx | mov cx, [ebx + 4*eax + array] |
| movb $4, %fs:(%eax)            | mov fs:eax, 4                 |

　　**七、不同语法格式的Hello World!程序**

　　所有程序设计语言的第一个例子都是在屏幕上打印一个字符串"Hello World!"，那我们也以这种方式来开始介绍Linux下的汇编语言程序设计。在Linux操作系统中，你有很多办法可以实现在屏幕上显示一个字符串，但最简洁的方式是使用Linux内核提供的系统调用。使用这种方法最大的好处是可以直接和操作系统的内核进行通讯，不需要链接诸如libc这样的函数库，也不需要使用ELF解释器，因而代码尺寸小且执行速度快。Linux是一个运行在保护模式下的32位操作系统，采用flat memory模式，目前最常用到的是ELF格式的二进制代码。一个ELF格式的可执行程序通常划分为如下几个部分：.text、.data和.bss，其中.text是只读的代码区，.data是可读可写的数据区，而.bss则是可读可写且没有初始化的数据区。代码区和数据区在ELF中统称为section，根据实际需要你可以使用其它标准的section，也可以添加自定义section，但一个ELF可执行程序至少应该有一个.text部分。下面给出我们的第一个汇编程序，用的是AT&T汇编语言格式：

　　**例1.**AT&T格式

```assembly
# hello.s

.data  # 数据段声明
msg: 
    .string "Hello, world!\n"  # 要输出的字符串
    len = . - msg  # 字符串长度

.text  # 代码段声明
.global _start  # 指定入口函数
_start:  # 在屏幕上显示一个字符串
    movl $len, %edx  # 参数三：字符串长度
    movl $msg, %ecx  # 参数二：要显示的字符串
    movl $1, %ebx  # 参数一：文件描述符(stdout)
    movl $4, %eax  # 系统调用号(sys_write)
    int $0x80  # 调用内核功能

    # 退出程序
    movl $0, %ebx  # 参数一：退出代码
    movl $1, %eax  # 系统调用号(sys_exit)
    int $0x80  # 调用内核功能
```

　　初次接触到AT&T格式的汇编代码时，很多程序员都认为太晦涩难懂了，没有关系，在Linux平台上你同样可以使用Intel格式来编写汇编程序，建议还是坚持一下，毕竟在linux下at&t才是主流的语言格式：

　　**例2.**Intel格式

```assembly
; hello.asm

section .data  ; 数据段声明
msg:
    db "Hello, world!", 0xA  ; 要输出的字符串
    len equ $ - msg  ; 字串长度

section .text  ; 代码段声明
global _start  ; 指定入口函数
_start:  ; 在屏幕上显示一个字符串
    mov edx, len  ; 参数三：字符串长度
    mov ecx, msg  ; 参数二：要显示的字符串
    mov ebx, 1  ; 参数一：文件描述符(stdout)
    mov eax, 4  ; 系统调用号(sys_write)
    int 0x80  ; 调用内核功能

    ; 退出程序
    mov ebx, 0  ; 参数一：退出代码
    mov eax, 1  ; 系统调用号(sys_exit)
    int 0x80  ; 调用内核功能
```

　　上面两个汇编程序采用的语法虽然完全不同。

　　相同的是：　1、功能却都是调用Linux内核提供的sys_write来显示一个字符串；

　　　　　　　　2、调用sys_exit退出程序。在Linux内核源文件/usr/include/asm/unistd.h中，可以找到所有系统调用的定义。

　　不同的是：　1、程序注释AT&T使用#开始注释，Intel使用;开始注释；

　　　　　　　　2、AT&T段的声明直接使用.data和.text即可，Inter使用section .data和section .text；