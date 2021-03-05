import re 
mytxt=open("input.txt", "r", encoding="utf-8")

for x in mytxt:
    search1 = re.search("^Филиал", x)
    if search1:
        print(x.replace("Филиал ", ""))
    search2 = re.search("^БИН", x)
    if search2:
        print(x.replace("БИН ", ""))
    search3 = re.search("^Время: ", x)
    if search3:
        print(x.replace("Время: ", ""))
    search4 = re.search("^г. ", x)
    if search4:
        print(x)