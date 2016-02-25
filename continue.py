i=0
while 1:
    i +=1
    while 1:
        print "inner 1",i
        if i==2:
            print "inner"
            continue
        else:
            i +=1
    if i ==23:
        print i
        break
    print "i:",i
    
