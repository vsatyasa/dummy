import sys

count = 0
for byte in range(int(sys.argv[1])):
    for word in range(4):
        print('w,%d,41'%(count))
        count += 1
print('q')
