"""
Написать функцию, которая будет принимать список и находить уникальное число.
Пример:
find_unique_value([1, 2, 1, 1]) -> 2
find_unique_value([2, 3, 3, 3]) -> 2
find_unique_value([5, 5, 5, 0.5]) -> 0.5
"""

from collections import Counter
MyList = [1, 2, 1, 1]
ListCount = Counter(MyList)
def Unique(MyList):
    for item in ListCount.items():
        if item [1]==1:
            return (item[0])
print(Unique(MyList))
