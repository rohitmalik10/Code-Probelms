# Input abcd10jk
# Approach 1 Brute force run 2 loops with two variables i and j compare str[i]and str[j] if they become equal at any point return false
def uniquechar(str):
	for i in range(len(str)):
		for j in range (i+1,len(str)):
			if(str[i]==str[j]):
				return False
	return True

str="Rohit"

if(uniquechar(str)):
	print("unique")
else:
 	print("Duplicate")