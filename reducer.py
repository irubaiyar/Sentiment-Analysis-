from operator import itemgetter
import sys
count=[]
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# parse the input we got from mapper.py
	word = line.split(",")
	#only extract the second element of the list i.e. the integers
	c=int(word[1])
	#store all elements in a list
	count.append(c)
		
index=sum(count)

index_s=str(index)

print index

f=open('2018-04-09.txt','w')
f.write(index_s)
f.close()
