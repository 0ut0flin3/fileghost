'''
MIT License

Copyright (c) 2022 0ut0flin3

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import secrets
import json
import sys
import os
global SEP
SEP='__FIL3GH0ST__'
global SEPARATOR
SEPARATOR=list(bytes(SEP.encode()))

def keystore_validity_test(keys:dict):
    def valid_values():
        flag=True
        for v in keys.values():
            if v>255:
               flag=False
               return flag
               break
        return flag
    print("Checking for keystore validity...")
    assert isinstance(keys,dict), "Keystore must be a dictionary"
    assert len(keys)==256, "Keystore keys count must be 256, but "+str(len(keys))+" instead"
    assert sum(keys.keys())==32640, "Sum of keystore keys should be 32640, but "+str(sum(keys.keys()))+" instead"
    assert len(keys.values())==len(set(keys.values())), "Keystore values must be unique and must not repeat, but duplicates found"
    assert valid_values()==True, "Any keystore values must be less than 256"
    
    return True
class keygen():
    def __init__(self):
        global l
        l=[]
        while len(l) != 256:
              r=secrets.randbelow(256)
              if r not in l:
                 l.append(r)
    def to_keystore(self):#needed for file encryption/decryption
        s = set(range(256))
        keystore=dict.fromkeys(s)
        for x in keystore:
            keystore[x]=l[x]
        return keystore
        return hl

    def to_byte_array(self):
        return l    
    def to_hex(self):
        return bytes(l).hex()
    def to_int(self):
        return int(bytes(l).hex(),16)
#KEYS FOR ENCRYPTION AND DECRYPTION MUST BE IN KEYSTORE \ DICTIONARY FORMAT , OTHERWISE YOU NEED TO CONVERT THEM#
def encrypt(inp, keys, disable_input_max_length=False):
    print('\n')

    inp=list(inp)
    if disable_input_max_length==False:
        if len(inp)>256:
           print("error: input cannot exceed 256 bytes")
           sys.exit()
    if len(inp)<256:
        inp.extend(SEPARATOR)
        while len(inp)<256:
                 inp.append(secrets.randbelow(256))
    inp=bytes(inp)


    already_encrypted=0
    enc_bytes=[]
    for n in inp:
        enc_bytes.append(keys[n])
    for p in range(0,len(enc_bytes)):
        enc_bytes[p]=enc_bytes[p] ^ keys[p%len(keys)]
        already_encrypted+=1
        print("Encrypted "+str(already_encrypted)+ " bytes of "+str(len(inp))+" total [ "+str((already_encrypted/len(inp))*100)[:4]+"% ]", end='\r')
    print('\n\nDone.\n')
    return enc_bytes

def decrypt(inp, keys:dict):
    
    already_decrypted=0
    decr_bytes=[]
    for p in range(0,len(inp)):
        inp[p]=inp[p] ^ keys[p%len(keys)]
    

    for b in inp:
        if b in keys.values():
           decr_bytes.append(int(list(keys.keys())[list(keys.values()).index(b)]))
           already_decrypted+=1
           print("Decrypted "+str(already_decrypted)+ " bytes of "+str(len(inp))+" total [ "+str((already_decrypted/len(inp))*100)[:4]+"% ]", end='\r')
    print('\n\nDone.\n')
    decr_bytes=bytes(decr_bytes)
    decr_bytes=decr_bytes[:decr_bytes.find(SEP.encode())]
    return decr_bytes


def savekeys(priv,path):
    if os.path.isfile(path):
       q=inp('''This file already exists on specified path. Do you want to replace it? \n Be careful, if you replace it , all the files encrypted with that keystore will be lost forever.\nContinue? [\033[1mY\033[0m/\033[1mN\033[0m]\n''')
       if q=='y' or q== 'Y':
          k=priv
          j=json.dumps(k)
          f=open(path,"w")
          f.write(j)
          f.close()
          print("Generated new keystore:", path)
       else:
            print("Aborted.")
            sys.exit()
    else:
          k=priv
          j=json.dumps(k)
          f=open(path,"w")
          f.write(j)
          f.close()
          print("Generated new keystore:",path)
