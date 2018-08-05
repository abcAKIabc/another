team = ["1", "2", "3", "4", "5"]
for t1 in team:
    for t2 in team:
        print(t1, "vs", t2)


team = [ "1", "2", "3", "4", "5" ]
for t1 in team:
    for t2 in team:
        if t1 != t2:
            print(t1, "vs", t2)



team = [ "1", "2", "3", "4", "5" ]
for t1 in team:
    for t2 in team:
        if t1 == t2:
            continue
        print(t1, "vs", t2)



team = [ "1", "2", "3", "4", "5",]
opps = [ "1", "2", "3", "4", "5",]
for t1 in team:
    opps.remove(t1)
    for t2 in opps:
        print(t1, "vs", t2)