"""
Example illustrating basic data input and output in python
The file datafile.out is opened, read through line-by-line and 
numbers corresponding to "k-cactus" values are extracted. These numbers
are then written to "cactus.out"
"""

infile = open("datafile.out","r")
num = []
for line in infile:
    if "cactus" in line:
        words = line.split()
        print words
        num = num + [words[-1]] #add the last word in line to num
        
print "num=",num        
infile.close()


#output numbers to cactus.out
outfile = open('cactus.out','w')

for a in num:
    outfile.write(a+"\n") #the \n creates a new line in the output file

outfile.close()