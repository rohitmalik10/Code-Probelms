# First step 1) sort both string 
# Second step 2) compare te sorted strings
# input 1) abcd 2) dabc 
#output permutation of each other 
# Permutation of a string is another string that contains same characters only order of characters can be different
# def permutations(str1,str2):
# 	n1=len(str1)
# 	n2=len(str2)

# 	if(n1!=n2):
# 		return False
# 	a=sorted(str1)
# 	str1=" ".join(a)
# 	b=sorted(str2)
# 	str2=" ".join(b)
# 	for i in range(0, n1, 1):
#           if (str1[i]!=str2[i]): 
#                  return False
#   return True 
# str1="Rohit"
# str2="Malik"
# if(permutations(str1,str2)):
# 	print("Permutation Yes")
# else:
# 	print("Permutation no")
