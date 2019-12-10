inp = input("write:")
pi = 3141592653589793238462643383279502884197169
sum = 0
goodlist = []
if inp == pi:
    print("+")
else:
    print("-")

limp = list(str(inp))
lpi = list(str(pi))
print(limp)
print(lpi)
#print(k[sum])
for m in limp:
    if m == lpi[sum]:
        sum += 1
        print(m)
        goodlist.append(m)
        print("+")
    else:
        print("ower")
        print(goodlist)
        break
print(sum)