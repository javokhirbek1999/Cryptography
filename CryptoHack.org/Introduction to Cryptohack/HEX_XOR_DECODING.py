inp = input()

d = {
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}


res = ""

for i in range(0,len(inp),2):
    res += str(int(inp[i:i+2],16))

print(res)
