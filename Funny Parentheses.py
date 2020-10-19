class parentheses:
	def is_valid(self,str):
		stack,valid=[],{'(':')','[':']','{':'}'}
		for char in str:
			if char in valid:
				stack.append(char)
			elif len(stack)==0 or valid[stack.pop()]!=char:
				return False
		return len(stack)==0
