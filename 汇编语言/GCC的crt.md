/usr/lib/x86_64-linux-gnu/Scrt1.o

```
0000000000000000 <_start>:
   0:   f3 0f 1e fa             endbr64
   4:   31 ed                   xor    ebp,ebp
   6:   49 89 d1                mov    r9,rdx
   9:   5e                      pop    rsi
   a:   48 89 e2                mov    rdx,rsp
   d:   48 83 e4 f0             and    rsp,0xfffffffffffffff0
  11:   50                      push   rax
  12:   54                      push   rsp
  13:   4c 8b 05 00 00 00 00    mov    r8,QWORD PTR [rip+0x0]        # 1a <_start+0x1a>
  1a:   48 8b 0d 00 00 00 00    mov    rcx,QWORD PTR [rip+0x0]        # 21 <_start+0x21>
  21:   48 8b 3d 00 00 00 00    mov    rdi,QWORD PTR [rip+0x0]        # 28 <_start+0x28>
  28:   ff 15 00 00 00 00       call   QWORD PTR [rip+0x0]        # 2e <_start+0x2e>
  2e:   f4                      hlt
```

/usr/lib/x86_64-linux-gnu/crti.o

```
Disassembly of section .init:

0000000000000000 <_init>:
   0:   f3 0f 1e fa             endbr64
   4:   48 83 ec 08             sub    rsp,0x8
   8:   48 8b 05 00 00 00 00    mov    rax,QWORD PTR [rip+0x0]        # f <_init+0xf>
   f:   48 85 c0                test   rax,rax
  12:   74 02                   je     16 <_init+0x16>
  14:   ff d0                   call   rax

Disassembly of section .fini:

0000000000000000 <_fini>:
   0:   f3 0f 1e fa             endbr64
   4:   48 83 ec 08             sub    rsp,0x8
```

/usr/lib/x86_64-linux-gnu/crtn.o

```
Disassembly of section .init:

0000000000000000 <.init>:
   0:   48 83 c4 08             add    rsp,0x8
   4:   c3                      ret

Disassembly of section .fini:

0000000000000000 <.fini>:
   0:   48 83 c4 08             add    rsp,0x8
   4:   c3                      ret
```

main函数

```
Disassembly of section .text:

0000000000000000 <main>:
   0:   f3 0f 1e fa             endbr64
   4:   55                      push   rbp
   5:   48 89 e5                mov    rbp,rsp
...
  21:   b8 00 00 00 00          mov    eax,0x0
  26:   5d                      pop    rbp
  27:   c3                      ret
```

