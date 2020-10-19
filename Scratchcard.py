from collections import defaultdict
from random import choice
def scratchcard():
	tickets=[*range(1,11)]
	results=defaultdict(lambda :'$1')
	results[choice(tickets)]='$1000'
	for num in range(1,11): print(num,results[num])
