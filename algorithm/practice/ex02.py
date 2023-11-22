def rectangle (x, y):
    return x * y , (x+y)*2
x,y = (20, 30)

print(rectangle(x,y))


def rectangle (x, y):
    area =  x * y 
    perimeter = (x+y)*2
    return area,perimeter 

print(rectangle(20,30))