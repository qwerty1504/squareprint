def squareprint(lst):
    Y = len(lst) ** 0.5
    Y = round(Y)
    B = 0
    for i in range(Y):
        for x in range(Y):
            print(lst[B], " ", end ='')
            B += 1
        
        print(' ')       
 
