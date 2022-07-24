def inverse(x,y):
    numbers_x = []
    numbers_y = []
    
    for k in range(1,60):
        numbers_x.append(k*x)
        numbers_y.append(k*y)
        
    found = False # To see if inverse was found
    multiplicator_x = 0
    multiplicator_y = 0
    
    for every_x in numbers_x:
        multiplicator_x += 1
        multiplicator_y = 0
        for every_y in numbers_y:
            multiplicator_y += 1
            if every_y == every_x + 1:
                found = True
                print(f"Found: {x}*{multiplicator_x} = {every_x} - {y}*{multiplicator_y} = {every_y}")
                break
                
    if found == False:
        print("No inverse found, otherwise, extend the range of multiplcators in the first for loop :) ")
        return 0
    else:
        return 1
