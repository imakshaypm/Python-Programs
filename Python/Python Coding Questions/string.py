def caesarCipher(s, k):
    # Write your code here#
    st = ''
    g = k % 26
    for i in s:
        if 97 <= ord(i) <= 122:
            if ord(i) + g >= 123:
                st = st + chr((ord(i) + g) - 26)
            else:
                st = st + chr(ord(i) + g)
        elif 65 <= ord(i) <= 90:
            if ord(i) + g >= 91:
                st = st + chr((ord(i) + g) - 26)
            else:
                st = st + chr(ord(i) + g)
        else:
            st = st + i
        
    return st

s = "www.abc.xy"
print(caesarCipher(s, 87))
#print(ord("d") + (98 % 26))
#print(chr(120))