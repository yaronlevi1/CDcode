my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def myfunc(a):
    tList = []
    for key,val in a.items():
        tList.append( (key, val ))
    print (tList)
    return tList

myfunc(my_dict)
