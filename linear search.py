def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            return i
        i = i + 1

    return False

list = [5,8,4,6,9,2]
n = 9
result = search(list, n)
if result:
   print("Found at", result)
else:
   print("Not Found")