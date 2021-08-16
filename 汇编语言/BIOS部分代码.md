```
000ffff0: jmpf 0xf000:e05b          ; ea5be000f0      jmp 0xf000:0xe05b
```

```
000fe05b: xor ax, ax                ; 31c0            xor ax, ax
000fe05d: out 0x0d, al              ; e60d            1
000fe05f: out 0xda, al              ; e6da            1
000fe061: mov al, 0xc0              ; b0c0            mov al, 0xc0
000fe063: out 0xd6, al              ; e6d6            1
000fe065: mov al, 0x00              ; b000            mov al, 0
000fe067: out 0xd4, al              ; e6d4            1
000fe069: mov al, 0x0f              ; b00f            mov al, 0xf
000fe06b: out 0x70, al              ; e670            1
000fe06d: in al, 0x71               ; e471            1
000fe06f: mov bl, al                ; 88c3            mov bl, al
000fe071: mov al, 0x0f              ; b00f            mov al, 0xf
000fe073: out 0x70, al              ; e670            1
000fe075: mov al, 0x00              ; b000            mov al, 0
000fe077: out 0x71, al              ; e671            1
000fe079: mov al, bl                ; 88d8            mov al, bl
000fe07b: cmp al, 0x00              ; 3c00            1
000fe07d: jz .+36 (0x0000e0a3)      ; 7424            1
000fe07f: cmp al, 0x0d              ; 3c0d            1
000fe081: jnb .+32 (0x0000e0a3)     ; 7320            1
000fe083: cmp al, 0x05              ; 3c05            1
000fe085: jnz .+3 (0x0000e08a)      ; 7503            1
000fe087: jmp .-20001 (0x00009269)  ; e9dfb1          1
000fe08a: cmp al, 0x0a              ; 3c0a            1
000fe08c: jnz .+3 (0x0000e091)      ; 7503            1
000fe08e: jmp .-19964 (0x00009295)  ; e904b2          1
000fe091: cmp al, 0x0b              ; 3c0b            1
000fe093: jnz .+3 (0x0000e098)      ; 7503            1
000fe095: jmp .-19963 (0x0000929d)  ; e905b2          1
000fe098: cmp al, 0x0c              ; 3c0c            1
000fe09a: jnz .+3 (0x0000e09f)      ; 7503            1
000fe09c: jmp .-19957 (0x000092aa)  ; e90bb2          1
000fe09f: push bx                   ; 53              1
000fe0a0: call .+12421 (0x00001128) ; e88530          1
000fe0a3: cli                       ; fa              1
000fe0a4: mov ax, 0xfffe            ; b8feff          mov ax, 0xfffe
000fe0a7: mov sp, ax                ; 89c4            mov sp, ax
000fe0a9: xor ax, ax                ; 31c0            xor ax, ax
000fe0ab: mov ds, ax                ; 8ed8            mov ds, ax
000fe0ad: mov ss, ax                ; 8ed0            mov ss, ax
000fe0af: mov byte ptr ds:0x04b0, bl ; 881eb004       1
000fe0b3: cmp bl, 0xfe              ; 80fbfe          1
000fe0b6: jnz .+3 (0x0000e0bb)      ; 7503            1
000fe0b8: jmp .-19972 (0x000092b7)  ; e9fcb1          1
000fe0bb: mov es, ax                ; 8ec0            mov es, ax
000fe0bd: mov cx, 0x0080            ; b98000          mov cx, 0x80
000fe0c0: mov di, 0x0400            ; bf0004          mov di, 0x400
000fe0c3: cld                       ; fc              1
000fe0c4: rep stosw word ptr es:[di], ax ; f3ab       1
000fe0c6: call .+13763 (0x0000168c) ; e8c335          1
000fe0c9: call .-17357 (0x00009cff) ; e833bc          1
000fe0cc: mov ax, 0x027f            ; b87f02          mov ax, 0x27
000fe0cf: mov word ptr ds:0x0413, ax ; a31304         1
000fe0d2: call .-20097 (0x00009254) ; e87fb1          1
000fe0d5: mov ax, 0xfea5            ; b8a5fe          mov ax, 0xfea5
000fe0d8: mov word ptr ds:0x0020, ax ; a32000         1
000fe0db: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe0de: mov word ptr ds:0x0022, ax ; a32200         1
000fe0e1: mov al, 0x34              ; b034            mov al, 0x34
000fe0e3: out 0x43, al              ; e643            1
000fe0e5: mov al, 0x00              ; b000            mov al, 0
000fe0e7: out 0x40, al              ; e640            1
000fe0e9: out 0x40, al              ; e640            1
000fe0eb: mov ax, 0xe987            ; b887e9          mov ax, 0xe987
000fe0ee: mov word ptr ds:0x0024, ax ; a32400         1
000fe0f1: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe0f4: mov word ptr ds:0x0026, ax ; a32600         1
000fe0f7: mov ax, 0xe82e            ; b82ee8          mov ax, 0xe82e
000fe0fa: mov word ptr ds:0x0058, ax ; a35800         1
000fe0fd: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe100: mov word ptr ds:0x005a, ax ; a35a00         1
000fe103: xor ax, ax                ; 31c0            xor ax, ax
000fe105: mov ds, ax                ; 8ed8            mov ds, ax
000fe107: mov byte ptr ds:0x0417, al ; a21704         1
000fe10a: mov byte ptr ds:0x0418, al ; a21804         1
000fe10d: mov byte ptr ds:0x0419, al ; a21904         1
000fe110: mov byte ptr ds:0x0471, al ; a27104         1
000fe113: mov byte ptr ds:0x0497, al ; a29704         1
000fe116: mov al, 0x10              ; b010            mov al, 0x10
000fe118: mov byte ptr ds:0x0496, al ; a29604         1
000fe11b: mov bx, 0x001e            ; bb1e00          mov bx, 0x1e
000fe11e: mov word ptr ds:0x041a, bx ; 891e1a04       1
000fe122: mov word ptr ds:0x041c, bx ; 891e1c04       1
000fe126: mov bx, 0x001e            ; bb1e00          mov bx, 0x1e
000fe129: mov word ptr ds:0x0480, bx ; 891e8004       1
000fe12d: mov bx, 0x003e            ; bb3e00          mov bx, 0x3e
000fe130: mov word ptr ds:0x0482, bx ; 891e8204       1
000fe134: call .+11032 (0x00000c4f) ; e8182b          1
000fe137: mov ax, word ptr ds:0x0410 ; a11004         1
000fe13a: mov al, 0x14              ; b014            mov al, 0x14
000fe13c: out 0x70, al              ; e670            1
000fe13e: in al, 0x71               ; e471            1
000fe140: mov word ptr ds:0x0410, ax ; a31004         1
000fe143: xor ax, ax                ; 31c0            xor ax, ax
000fe145: mov ds, ax                ; 8ed8            mov ds, ax
000fe147: xor bx, bx                ; 31db            xor bx, bx
000fe149: mov cl, 0x14              ; b114            mov cl, 0x14
000fe14b: mov dx, 0x0378            ; ba7803          mov dx, 0x0378
000fe14e: call .-17962 (0x00009b27) ; e8d6b9          1
000fe151: mov dx, 0x0278            ; ba7802          mov dx, 0x0278
000fe154: call .-17968 (0x00009b27) ; e8d0b9          1
000fe157: shl bx, 0x0e              ; c1e30e          1
000fe15a: mov ax, word ptr ds:0x0410 ; a11004         1
000fe15d: and ax, 0x3fff            ; 25ff3f          mov ax, 0x3fff
000fe160: or ax, bx                 ; 09d8            or ax, bx
000fe162: mov word ptr ds:0x0410, ax ; a31004         1
000fe165: mov ax, 0xe739            ; b839e7          mov ax, 0xe739
000fe168: mov word ptr ds:0x0050, ax ; a35000         1
000fe16b: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe16e: mov word ptr ds:0x0052, ax ; a35200         1
000fe171: xor bx, bx                ; 31db            xor bx, bx
000fe173: mov cl, 0x0a              ; b10a            mov cl, 0xa
000fe175: mov dx, 0x03f8            ; baf803          mov dx, 0x03f8
000fe178: call .-17973 (0x00009b46) ; e8cbb9          1
000fe17b: mov dx, 0x02f8            ; baf802          mov dx, 0x02f8
000fe17e: call .-17979 (0x00009b46) ; e8c5b9          1
000fe181: mov dx, 0x03e8            ; bae803          mov dx, 0x03e8
000fe184: call .-17985 (0x00009b46) ; e8bfb9          1
000fe187: mov dx, 0x02e8            ; bae802          mov dx, 0x02e8
000fe18a: call .-17991 (0x00009b46) ; e8b9b9          1
000fe18d: shl bx, 0x09              ; c1e309          1
000fe190: mov ax, word ptr ds:0x0410 ; a11004         1
000fe193: and ax, 0xf1ff            ; 25fff1          and ax, 0xf1ff
000fe196: or ax, bx                 ; 09d8            or ax, bx
000fe198: mov word ptr ds:0x0410, ax ; a31004         1
000fe19b: mov ax, 0xfe6e            ; b86efe          mov ax, 0xfe6e
000fe19e: mov word ptr ds:0x0068, ax ; a36800         1
000fe1a1: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1a4: mov word ptr ds:0x006a, ax ; a36a00         1
000fe1a7: mov ax, 0xff53            ; b853ff          mov ax, 0xff53
000fe1aa: mov word ptr ds:0x0128, ax ; a32801         1
000fe1ad: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1b0: mov word ptr ds:0x012a, ax ; a32a01         1
000fe1b3: mov ax, 0xfe93            ; b893fe          mov ax, 0xfe93
000fe1b6: mov word ptr ds:0x01c0, ax ; a3c001         1
000fe1b9: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1bc: mov word ptr ds:0x01c2, ax ; a3c201         1
000fe1bf: call .-20190 (0x000092e4) ; e822b1          1
000fe1c2: mov ax, 0xe9dd            ; b8dde9          mov ax, 0xe9dd
000fe1c5: mov word ptr ds:0x01c4, ax ; a3c401         1
000fe1c8: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1cb: mov word ptr ds:0x01c6, ax ; a3c601         1
000fe1ce: mov ax, 0x8ea3            ; b8a38e          mov ax, 0x8ea3
000fe1d1: mov word ptr ds:0x01d0, ax ; a3d001         1
000fe1d4: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1d7: mov word ptr ds:0x01d2, ax ; a3d201         1
000fe1da: mov ax, 0xe2c7            ; b8c7e2          mov ax, 0xe2c7
000fe1dd: mov word ptr ds:0x01d4, ax ; a3d401         1
000fe1e0: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1e3: mov word ptr ds:0x01d6, ax ; a3d601         1
000fe1e6: mov ax, 0xf065            ; b865f0          mov ax, 0xf065
000fe1e9: mov word ptr ds:0x0040, ax ; a34000         1
000fe1ec: mov ax, 0xf000            ; b800f0          mov ax, 0xf000
000fe1ef: mov word ptr ds:0x0042, ax ; a34200         1
000fe1f2: call .-17691 (0x00009cda) ; e8e5ba          1
000fe1f5: call .-18344 (0x00009a50) ; e858b8          1
000fe1f8: mov cx, 0xc000            ; b900c0          mov cx, 0xc000
000fe1fb: mov ax, 0xc780            ; b880c7          mov ax, 0xc780
000fe1fe: call .-17896 (0x00009c19) ; e818ba          1
000fe201: mov dx, 0x03d4            ; bad403          mov dx, 0x03d4
000fe204: mov al, 0x00              ; b000            mov al, 0
000fe206: out dx, al                ; ee              1
000fe207: inc dx                    ; 42              inc dx
000fe208: in al, dx                 ; ec              1
000fe209: test al, al               ; 84c0            1
000fe20b: jnz .+5 (0x0000e212)      ; 7505            1
000fe20d: mov ax, 0x0003            ; b80300          mov ax, 0x0003
000fe210: int 0x10                  ; cd10            1
000fe212: call .+12093 (0x00001152) ; e83d2f          1
000fe215: call .-21099 (0x00008fad) ; e895ad          1
000fe218: call .-20967 (0x00009034) ; e819ae          1
000fe21b: call .+13723 (0x000017b9) ; e89b35          1
000fe21e: call .+14565 (0x00001b06) ; e8e538          1
000fe221: call .+21186 (0x000034e6) ; e8c252          1
000fe224: call .+12164 (0x000011ab) ; e8842f          1
000fe227: mov cx, 0xc800            ; b900c8          mov cx, 0xc800
000fe22a: mov ax, 0xe000            ; b800e0          mov ax, 0xe000
000fe22d: call .-17943 (0x00009c19) ; e8e9b9          1
000fe230: call .+12532 (0x00001327) ; e8f430          1
000fe233: sti                       ; fb              1
000fe234: int 0x19                  ; cd19            1
```

