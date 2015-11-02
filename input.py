again = ""
while again == "":
    name = raw_input("Hello, please enter your name?: ")
    if name:
        print "Hello %s I am soandso" % name
    again = raw_input("Do you want again ?")
