a = "hello"
b = "Gauri"

print(f"{a}{(' '+b)*10}")

c = []
c.append("Khushboo")
c.append("Gauri")

d = ["Yogita","Wifey"]
c.append(d[0])
c.append(d[1])

c.extend(d)
print(c)

print(b[2:4])

for i in range(len(c)):
    print(c[i])
for x in c:
    print(x)


