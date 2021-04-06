
import re as regex
f = open("raw.txt", "r", encoding="utf-8").read().split("\n")
for x in f:
    search1 = regex.search("^Филиал", x)
    if search1:
        print(x.replace("Филиал ", ""))
    search2 = regex.search("^БИН", x)
    if search2:
        print(x.replace("БИН ", ""))
    search3 = regex.search("^Время: ", x)
    if search3:
        print(x.replace("Время: ", ""))
    search4 = regex.search("^г. ", x)
    if search4:
        print(x)
start = f.index("ПРОДАЖА")
end = f.index("Банковская карта:")
steps = int((end - start - 1) / 6)
data = list()
for t in range(steps):
    name = f[start + t*6 + 2]
    num = f[start + t*6 + 3].split(" x ")
    count = num[0].split(",")
    unit = num[1]
    total = f[start + t*6 + 4]
    print(str(t + 1)+")", name, "|", count[0], "|", unit, "|", total)