#Karuna Ramkumar, 800906857, k@uncc.edu
import sys,getopt,struct
abc=sys.argv[1] #file name
source=open("%s.lzw" %abc,"rb")
packedcode=source.read()#read codes

bitlength=int(sys.argv[2])
MAX_TABLE_SIZE = 2 ** bitlength
if bitlength <9 or bitlength >12:
      bitlength = input("Enter bit length within range of 9-12: ")
h='>'
for i in range(MAX_TABLE_SIZE/2):
    h += 'H'
tupcode=struct.unpack(h,packedcode[0:MAX_TABLE_SIZE])#input codes in tuple format. Converting to int
code=[0]*MAX_TABLE_SIZE
code_i=0
for i in range(0,MAX_TABLE_SIZE/2):
    if tupcode[i] is not 0:
        code[code_i]=int(tupcode[i])
        code_i += 1
source.close()

string=[' ']*MAX_TABLE_SIZE # size of string

for i in range(0,256): #ascii table
	string[i]=chr(i)
x=0
for i in range(0,MAX_TABLE_SIZE):#calculating number of code strings
    if (code[i] > 0):
        x += 1
        if (x != i+1):
            x = i+1
count=0
a=0
current_code=code[count]
count += 1
ss=string[current_code]
output=ss
while (count < x): #running the loop code number of times
    current_code = code[count]
    count += 1
    if current_code > (255+a):#if current code index not in the table yet
        newstring=newstring + ss[0]
        print('greater')
    else:
        newstring = string[current_code]
    output += newstring
    if (a<MAX_TABLE_SIZE):
        string[256+a]=ss+newstring[0]
        a += 1
    ss=newstring

print(string)
print(output)
abc += '_decoded'    
done=open('%s.txt' %abc,'w') #output file
done.write(output)
done.close()
