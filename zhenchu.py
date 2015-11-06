count = 0
i = 0
def is_ok(a):
   if a % 2 == 0:
       return True
   if a % 3 == 0:
       return True
   return False
while True:
    i +=1
    if is_ok(i):
        count += 1
    if count ==2333:
        print i
        break
