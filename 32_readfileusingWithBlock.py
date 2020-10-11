# With block to open a file - no need to close a file

with open("gary.txt") as f:
    # content = f.read()
    # print(content)
    print(f.readline(), end='')
    print(f.readline(), end='')
    print(f.readline(), end='')
