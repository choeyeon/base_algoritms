start_list = [1, 8, 6, 2, 5, 4, 8, 3, 7,]
n = 0

n2 = len(start_list) - 1
print(n2)
cuferku = []
while n != len(start_list):
    element = start_list[n]
    d = element * n2
    print("n2", n2)
    if n2 == 0:
        n += 1
        n2 = len(start_list) - 1
        print("n", n)
    
    n2 = n2 - 1
    
    cuferku.append(d)
    
print(cuferku)
