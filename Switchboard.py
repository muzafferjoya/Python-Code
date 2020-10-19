from collections import defaultdict
def switchboard(switch):
	board=defaultdict(lambda :0)
	board[switch]=1
	return ''.join([str(board[num]) for num in range(1,7)])
