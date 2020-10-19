import random

def five_even_randoms(start,end):
    return [num for num in random.sample(range(start,end+1),5) if num%2==0]
