def draw_stars(a):
    for i in a:
        if type(i)==str:
            print(i[0].lower()*len(i))
        else:
            print("*"*i)

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
