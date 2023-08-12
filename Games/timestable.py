table=[]
inside=[]
added=0
for x in range(0,8):
    for y in range(0,8):
        added+=x
        inside.append(added)
    table.append(inside)
    inside=[]
    added=0
print(table)