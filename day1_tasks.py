
print("Hello World")

#1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.

mylist=[1,2,2,3,3,4,5,6,6,7]

for x in range(len(mylist)):
	if((mylist.count(x))>1):
		print(x,'is duplicate')


#2.Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random
list=['a','e','i','o','u']
random.shuffle(list)
print(' '.join(list))


#3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

sample=[1,2,3,4,5,6,7,8,9]
while len(sample)>2:
	print(sample[2])
	sample.remove(sample[2])
	if(len(sample)>2):
		print(sample)

#4.Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.

input_list= [1,2,4,-3,5,6,7,8,0,0,0]

def unique_triplets_sum_zero(x):
    triplets = set()
    x.sort()

    for i in range(len(x) - 2):
        if i > 0 and x[i] == x[i-1]:
            continue

        n2, n3 = i+1, len(x) - 1

        while n2 < n3:
            total = x[i] + x[n2] + x[n3]

            if total == 0:
                triplet = (x[i], x[n2], x[n3])
                triplets.add(triplet)
                n2 += 1
                n3 -= 1

                while n2 < n3 and x[n2] == x[n2-1]:
                    n2 += 1
                while n2 < n3 and x[n3] == x[n3+1]:
                    n3 -= 1
            elif total < 0:
                    n2 += 1
            else:
                    n3 -= 1

    return triplets

result = unique_triplets_sum_zero(input_list)
print(result) 



#5.Write a Python program to ask user a long text, convert the string to a list and print all the words and their frequencies.

string_words=input("enter strings")
word_list = string_words.split()
word_freq = [word_list.count(n)for n in word_list]

print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
#print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))


 
#6. Write a Python program to count the number of each character of a given text of a text file. 

fname = input("Enter the name of the file:")
file = open(fname, 'r')
lines = 0
words = 0
characters = 0
for line in file:
    wlist = line.split()
    lines = lines + 1
    words = words + len(wlist)
    characters = characters + len(line)
print(lines)
print(words)
print(characters)

 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 





 







