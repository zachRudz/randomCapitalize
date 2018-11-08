import sys
import random

# How often will each character be capitalized?
rng = 0.5

# Since we need to iterate over the string and modify each value,
#	we need to get a mutible version of the string.
# The alternative is to continuously append to a new list, which doesn't have O(1)
#	complexity when we outgrow the array (similar to Java's ArrayLists). 
#	We could still take this approach with a final O(N) complexity, although
#	at that point we're still using the same space complexity at the end of the algo.
def fetchMutableString(original_str):
	return list(original_str)

def randomCapitalize(original_str):
	str = fetchMutableString(original_str)

	for i in range(len(str)):
		if(random.random() > rng):
			str[i] = str[i].upper()
		else:
			str[i] = str[i].lower()
	
	# Convert the list back to string format
	return ''.join(str)


if __name__ == "__main__":
	# Build the original string from command line args
	args = sys.argv[1:]
	originalString = " ".join(args)

	# Modify the string, and print it
	randomCapString = randomCapitalize(originalString)
	print(randomCapString)
	
