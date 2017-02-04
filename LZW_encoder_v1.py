#Karuna Ramkumar, 800906857, k@uncc.edu
import sys,getopt,struct
abc=sys.argv[1] #import file name
source=open('%s.txt' %abc,'r') #open a file by the given name
data=source.read() #store the contents of the file in data
source.close()

done=open('%s.lzw' %abc,'wb') #create an lzw file for storing encoded string

bitlength=int(sys.argv[2]) #bitlength specified in command line
if bitlength <9 or bitlength >16:
       bitlength = input("Enter bit length within range of 9-16: ")
x=len(data) #size of string
MAX_TABLE_SIZE = 2 ** bitlength #max table size
string=['a']*MAX_TABLE_SIZE # size of string
count = 0 #initializations
ss=""
code = [0]*MAX_TABLE_SIZE
a = 0
for i in range(0,256): # originial ascii table
	string[i]=chr(i)
while (count < x): #while data is still present
       symbol=data[count]
       if ss+symbol in string:
              ss += symbol
       else:
              code[a]=string.index(ss)
              
              if a < (MAX_TABLE_SIZE-256):
                     string[256+a]=ss+symbol
                     print(string[256+a])
              
                     print(string.index(ss))
              else:
                     print("Sorry. Max table size reached. Please increase the bit length if possible")
                     exit()
              a += 1
              ss=symbol
       count += 1
if count is x:
       code[a]=string.index(ss)       
for i in range(MAX_TABLE_SIZE):
       done.write(struct.pack('>H',code[i])) #struct pack the output code to hex format
print(code)
print(string)

done.close()
