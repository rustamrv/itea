# map filter

list_of_number = [1, 2, 3, 4, 5]
list_of_number2 = [6, 7, 8, 9, 10]

res = list(map(lambda n, m: (n+m)**2, list_of_number, list_of_number2))
print(res)
res2 = list(filter(lambda n: n > 100, res))
print(res2)
                                                                                                                                                                                                                                                      # map filter

list_of_number = [1, 2, 3, 4, 5]
list_of_number2 = [6, 7, 8, 9, 10]

res = list(map(lambda n, m: (n+m)**2, list_of_number, list_of_number2))
print(res)
res2 = list(filter(lambda n: n > 100, res))
print(res2)
