# Steps First we will Sort the string And 
# Then traverse the string to find the occurence of each character And 
# Return the maximum occuring character
# Here technique used is "Hashing" in this we will traverse through string and hash each character into array os ASCII characters
#EX input here
# count['h']=1
# count['e']=2
#count['r']=1
# CODE
ASCII_SIZE=256 #Or 0 to 127
def MaxOccur(string):
	count=[0]*ASCII_SIZE
	max=-1
	c=''
	for i in string:
		count[ord(i)]+=1;
	for i in string:
		if max<count[ord(i)]:
			max=count[ord(i)]
			c=i
	return c

string="ramboo"#input string to check max occurence
print(MaxOccur(string))