print(*(lambda x: (sum(x)//5, sorted(x)[2]))([int(input()) for _ in range(5)]))
