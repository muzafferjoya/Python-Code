def sort_nums(items):
    nums=iter(sorted([num for num in items if str(num).isdigit()]))
    res=[]
    for item in items:
        res.append(item) if str(item).isalpha() else res.append(next(nums))
    return res
