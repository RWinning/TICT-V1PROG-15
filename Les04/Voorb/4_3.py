def swap (lst):
    if len(lst) > 1:
        lst[0], lst[1] = lst[1], lst[0]
        return lst
lijst= [4, 0, 1, -2]
res = swap(lijst)
print(res)
