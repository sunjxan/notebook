交互模式下直接回车的作用是重复上一指令，对于单步调试非常方便

- 分割窗口

    - layout：用于分割窗口，可以一边查看代码，一边测试：
    - layout src：查看源代码和命令窗口
    - layout asm：查看反汇编代码和命令窗口
    - layout split：查看源代码、反汇编代码和命令窗口
    - layout regs：查看寄存器，如果当前为layout split状态，寄存器窗口会覆盖一个窗口
    - Ctrl + L：刷新窗口

- 反汇编

  disas /sr
  
  自动反汇编后面要执行的代码，输入：`set disassemble-next-line on`

- 寄存器

  set $reg

  print /x $reg

- 内存

    set {char}0xffff = 0x8888

    print /x {char}0xffff

    x /wx 0xffff

- 源代码

  - list ：简记为 l ，其作用就是列出程序的源代码，默认每次显示10行。
  - list 行号：将显示当前文件以“行号”为中心的前后10行代码，如：list 12
  - list 函数名：将显示“函数名”所在函数的源代码，如：list main
  - list ：不带参数，将接着上一次 list 命令的，输出下边的内容。
  
- 断点

  - b[reak] FILE:NUM  在FILE文件第NUM行处设置断点
  - b fn1 if a＞b：条件断点设置
  - break func（break缩写为b）：在函数func()的入口处设置断点，如：break cb_button
  - delete 断点号n：删除第n个断点
  - disable 断点号n：暂停第n个断点
  - enable 断点号n：开启第n个断点
  - clear 行号n：清除第n行的断点
  - info b(reakpoints) ：显示当前程序的断点设置情况
  - delete breakpoints：清除所有断点


- 控制
  
  - run：简记为 r ，其作用是运行程序，当遇到断点后，程序会在断点处停止运行，等待用户输入下一步的命令。
  - continue （简写c ）：继续执行，到下一个断点处（或运行结束）
  - next：（简写 n），单步跟踪程序，当遇到函数调用时，也不进入此函数体；此命令同 step 的主要区别是，step 遇到用户自定义的函数，将步进到函数中去运行，而 next 则直接调用函数，不会进入到函数体内。
  - step （简写s）：单步调试如果有函数调用，则进入函数；与命令n不同，n是不进入调用的函数的
  - until：当你厌倦了在一个循环体内单步跟踪时，这个命令可以运行程序直到退出循环体。
  - until+行号： 运行至某行，不仅仅用来跳出循环
  - finish： 运行程序，直到当前函数完成返回，并打印函数返回时的堆栈地址和返回值及参数值等信息。
  - call 函数(参数)：调用程序中可见的函数，并传递“参数”，如：call gdb_test(55)
  - quit：简记为 q ，退出gdb

run

cont

next

step

finish

break

tbreak

delete

up

down

print

print*

display

undisplay

info display

info args

info locals

info stack

info breakpoints

quit

I/O Win

no I/0 Win