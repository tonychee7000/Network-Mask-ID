#!/usr/bin/env python3
#
# author:tonychee7000 <tonychee1989@gmail.com>
#
import sys


try:
    a = int(sys.argv[1])
    b = 32 - a
    
    if b not in range(0, 32):
        raise SyntaxError
    
    B32 = 2 ** 32 - 1
    bing = B32 - (2 ** b - 1)
    mask = []
    
    for i in [24, 16, 8, 0]:
        mask.append(bing // (2 ** i))
        bing %= 2 ** i

    sts = ""
    
    for i in range(0, 4):
        if i != 3:
            sts += str(mask[i]) + '.'
        else:
            sts += str(mask[i])
    print(sts)
except ValueError:
    try:
        a = sys.argv[1]
        b = a.split('.')
        c = 0
        
        for j in range(0, 3):
            if b[j] != '255' and b[j + 1] != '0':
                raise SyntaxError
        
        for i in range(0, 4):
            c += int(b[i]) << (8 * (3 - i))
        
        bits = bin(c)
        print(bits.count('1'))
    except (ValueError, IndexError):
        if a == "-h":
            print("usage: mask.py <num[0,32]/mask id>")
        else:
            print("Not mask bits or mask id!!")
    except SyntaxError:
        print("Invalid mask ID!!!")

except SyntaxError:
    print("Out of Range")
except IndexError:
    print("usage: mask.py <num[0,32]/mask id>")
