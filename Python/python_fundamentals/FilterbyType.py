
x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1  ]

if type(x)==int:
    if x>=100:
        print("that's a big number!")
    else:
        print("that's a small number")
elif type(x)==str:
    if len(x)>=50:
        print("long sentence")
    else:
        print("short sentence")
elif type(x)==list:        
    if len(x)>=10:
        print("long list")
    else:
        print("short list")


