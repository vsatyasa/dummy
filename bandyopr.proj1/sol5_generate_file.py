with open('my_file', 'wb') as f:
    f.seek(7)
    f.write(b'0')
