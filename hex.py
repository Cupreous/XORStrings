#Test Variables
key1 ="A"
key2 ="FISH"
message1="hello"
message2=")$--."
message3="this is a test"
message4="f=;!5i:;f(s<#:'"

#Given Template:
import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]

key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

#My Code:
def xor(inp, key, mode):
    output = ""
    length = len(inp)

    if mode == "human":
        for i in range(length):
            output = output + chr(ord(inp[i]) ^ ord(key))
    
    if mode == "numOut":
        for i in range(length):
            output = output + (str(hex(ord(inp[i]) ^ ord(key)))[-2:] + " ")
    return output

print(xor(inp,key,mode))