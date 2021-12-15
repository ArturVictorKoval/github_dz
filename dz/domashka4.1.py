#[12, 3, 4, 10] => [10, 12, 3, 4]
lst = [12, 3, 4, 10]
print(lst)
a = lst.pop(-1)
lst.insert(0,a)
print(lst)
