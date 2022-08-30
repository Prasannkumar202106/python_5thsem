#a function that returns all the permutation of the given string  
def permutate(str, solution):
	if (len(str) == 0):
		print(solution, end = " ")
		return
	#using  binary search method
	for i in range(len(str)):
		ch = str[i]
		left_substr = str[0:i]
		right_substr = str[i + 1:]
		result = left_substr + right_substr
		permutate(result, solution + ch)

# pass the value to check the function
solution = ""

str = input("Enter the string : ")

print(f"All the possible permutation of {str} are : ")
permutate(str, solution)