def read_write():
    f = open('input.txt', 'r')
    lines = f.readlines()
    f.close()
    o = open('output.txt', 'w')
    o.writelines(lines)
    o.close()
    return

read_write()