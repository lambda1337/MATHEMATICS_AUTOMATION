def inverse(x,y):
    numbers_x = []
    numbers_y = []
    
    for k in range(1,60):
        numbers_x.append(k*x)
        numbers_y.append(k*y)
        
    multiplicator_x = 0
    multiplicator_y = 0
    for every_x in numbers_x:
        multiplicator_x += 1
        multiplicator_y = 0
        for every_y in numbers_y:
            multiplicator_y += 1
            if every_y == every_x + 1:
                print(f"Found: {x}*{multiplicator_x} = {every_x} - {y}*{multiplicator_y} = {every_y}")
                break
    return 0
