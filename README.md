# Fileghost by 0ut0flin3
Open-source File Encryption

**UPDATE: You can now generate a key directly in your browser here: https://fileghost.github.io/ ( pull requests and suggestions on how to improve this and on a possible Fileghost frontend implementation are welcome )**


```

                                             ,cccc,
                                            ,$$$$$$$b
      | FILEGHOST v0.1.4 by 0ut0flin3 |    ,$$$$$$$$$$,
                                           d$$$$$$$$$$$c        ,c,
                                           $$$$$$$$$$$$$b     ,d$$$L
                                        ,c$$$$$$$$$$$$$$$b ,,d$$$$$$,
                                     ,d$$$$$$$$$$$$?$$$$$$$J$$$$$$$$b    .
                                  ,cF',,$$$$?$$$$$$`$$$$$$$$$$$$b"$$$bcc$P
                                ,d3$$$$$$$$$$c`?$$$ ?$$$$$$$$$$$"  "????"
                              ,dP"""$$$$$$$$$$$;$$$  `?$$$$$$$$"
                             ,$",zc$$$$$$P"""?$$$$P     "?$$$F
                            J$$d$$$$$$$$$$b. ,$$$$F
                           d$P""$$$$$$$$$$$>d$$$$$
               .,,,cccccccd$$c$cJ$$5$$$$$$$$$$$$$$
             c$$$$$$$$$$$$$$$$"""P'$$c ?$$$$$$$$$F
            $$$$$$")$$$$$$$$$$d$c`$$$$$z$$$$$$$dC
            $$$$$$,c?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b,
            "$$$$$$$b,?$$$$$$$$$$$$$$$cF"$$$$$$$$$$$$$c
              "$$$$$$$bc,"?$$$$$$$$$$$" cc"$$$$$$$$$$$$$c
                `"?$$$$$$$c  """??"".,c$$$b$$$$$$$$$$$$$$,
                   "$c$$$$$         J$$$$$$$$$$$$$$$$$$$$$
            .,cc$$cc`$b?$$$F....:: ,$$$$$$$$$$$$$$$$$$$$$$
          cd$$$$$$$$,?$b`$$$,`:::',$$$$$$$$P".,.`"$$$$$P"
       ,c$$$$$$$$$$P$ $$b`$$$c,``,$$$$3$$$",$$$$$c`""
      c$$$$$$$$$$$$L?,?$$b ?$$$$$$$$F,$$$",$$$$$$$c
    ,$$$$$$$$$$$$$$$?$ $$$$,"$$$$$P"d$$$ J$$$$$$$$$,
  ,$$$$$$$$$?$$$$$$$ $ ?$$$$$c,,,,c$$$$FJ$$$$$$$$$$$
,d$$$$$$$$$"d$$$$$$$ $L`$$$$$$$$$$$$$$$Fd$$$$$$$$$$$L
$$$$$$$$$$F.$$$$$$$$ $$ ?$$$$$$$$$$$$$$;$$$$$$$$$$$$$
$$$$$$$$$$ d$$$$$$$$ $$,`$$$$$$$$$$$$$$$$$$$$$$$$$$$$L
$$$$$$$$$"4$$$$$$$$$ $$$ $$$$$$$$$$$?$$$$$$$$$$$$$$$$$
$$$$$$"$$.$$$$$$$$$$ $$$,`$$$$$$$$$'d$$$$$$$$$$$$$$$$$h
$$$$$$<$F,$$$$$$$$$$ $$$$,`$$$$$$$'d$$$$$$$$$$$$$$$$$$$
$$$$$$<$ $$$$$$$$$$$ $$$$$,`$$$$",$$$$3$$$$$$$$$$$$$$$$h
$$$$$$'F<$$$$$$$$$$$ ?$$$$$c,"",d$$$$'$$$$$$$$$$$$$$$$$$
```
this is a project created by a computer nerd, not an engineer, but he is really believes in privacy and thinks that everyone has the right to be able to use the internet without being monitored or controlled ,if they wish. That said, I always count on user feedback and support for any vulnerabilities so that we can make this "method" stronger . Pull requests are welcome. 

# INTRO:
Fileghost allows to encrypt any file (or sequence of bytes, like a message) using an unique, random generated sequence of 256 bytes. Each of these keys is unique and unrepeatable and can have almost infinite combinations. You can create as many keys as you like but the file encrypted with a certain key can only be recovered using the same key used for encryption.
You can use the same key to encrypt multiple files, or you can create a new key for each file, but for greater security *it is highly recommended to use one for each file or message.*

Starting from this version (0.1.4), by default, the maximum size of the input cannot exceed 256 bytes. It is still possible to disable this limit (if you go down below you will see how to do it),but you have to do it explicitly, and bearing in mind that it could make your key and your original input file/message more vulnerable to attacks. At this moment, for maximum security *the input size should never exceed 256 bytes.*


The same key can be reproduced in different formats:

1) JSON format (or dictionary) and this is the main format that is needed to encrypt/decrypt files
2) hexadecimal format
3) as an integer 
4) as a byte array.

Python is the best way to use Fileghost
The Python version allows great control and, moreover, allows you to encrypt even just a simple message like `b'hello'` instead of a file, however, some ligthweight , portable binary versions will soon be available for Windows and Linux 64bits and can be used without the need to have Python installed but they will just work with files.


That said, below are some examples for the use with Python, and if you go further, you will find an explanation of how keys are generated and how they are used for encryption.



## How to use Fileghost with Python:
Install using PIP: `pip install fileghost`

---------------
Generate keys:
---------------
```
import fileghost.fileghost as fg
key = fg.keygen()

key.to_keystore() # {0: 215, 1: 125, 2: 114, 3: 75...}
key.to_hex() # d77d724bc1f99a5fa63c3f0bb1808653b2b78d6...
key.to_int() # 27203095526857900917255529156...
key.to_byte_array() # [215, 125, 114, 75, 193, 249, 154...]
```

-------------------------------------------------------------------------
PS: You can use `savekeys()` function to save your key as a JSON file:
-------------------------------------------------------------------------
```
import fileghost.fileghost as fg
key = fg.keygen()
fg.savekeys(key.to_keystore(), "./mykeys.json")
```
---------------
Encrypt a file:
---------------
```
import fileghost.fileghost as fg

key = fg.keygen().to_keystore()
inputfile = open("cat.jpg","rb").read()
encrypted_file = fg.encrypt(inputfile, key)
#if the input size exceeds 256 bytes will cause an error, if you want to disable it set 'disable_input_max_length=True'
#wait for completion,it can take some time depending on file size and your hardware resources
#then, if you want, you can write the encrypted file to disk
encr_file=open("encrypted_cat.jpg","wb")
encr_file.write(bytes(encrypted_file))
encr_file.close()
```
---------------
Decrypt a file :
---------------
```
import fileghost.fileghost as fg
encrypted_file=open("encrypted_cat.jpg","rb").read()
key=key #must be the same used for encryption
decrypted_file=fg.decrypt(encrypted_file, key)
#wait for completion,it can take some time depending on file size and your hardware resources
#then, if you want, you can write the decrypted file to disk
decr_file=open("cat.jpg","wb")
decr_file.write(bytes(decrypted_file))
decr_file.close()

```
---------------
Encrypt a message:
---------------
```
import fileghost.fileghost as fg

key = fg.keygen().to_keystore()
message = b'hello'
encrypted_message = fg.encrypt(message, key)
#if the message size exceeds 256 bytes will cause an error, if you want to disable it set 'disable_input_max_length=True'
```

---------------
Decrypt a message :
---------------
```
import fileghost.fileghost as fg
key=key #must be the same used for encryption
decrypted_message=fg.decrypt(encrypted_message, key)

```


## How keys are generated and how they are used:
An example of the same key represented in the 4 different formats (dictionary, hexadecimal,integer and bytearray) :

### dictionary format:
```
{0: 215, 1: 125, 2: 114, 3: 75, 4: 193, 5: 249, 6: 154, 7: 95, 8: 166, 9: 60, 10: 63, 11: 11, 12: 177, 13: 128, 14: 134, 15: 83, 16: 178, 17: 183, 18: 141, 19: 99, 20: 246, 21: 209, 22: 150, 23: 235, 24: 47, 25: 55, 26: 17, 27: 163, 28: 221, 29: 94, 30: 36, 31: 237, 32: 142, 33: 160, 34: 102, 35: 196, 36: 5, 37: 165, 38: 73, 39: 156, 40: 146, 41: 233, 42: 253, 43: 13, 44: 56, 45: 81, 46: 59, 47: 172, 48: 2, 49: 133, 50: 241, 51: 106, 52: 88, 53: 158, 54: 104, 55: 74, 56: 18, 57: 135, 58: 239, 59: 84, 60: 66, 61: 140, 62: 25, 63: 199, 64: 86, 65: 222, 66: 46, 67: 10, 68: 105, 69: 51, 70: 200, 71: 89, 72: 92, 73: 85, 74: 14, 75: 240, 76: 12, 77: 182, 78: 65, 79: 168, 80: 204, 81: 157, 82: 245, 83: 224, 84: 206, 85: 223, 86: 216, 87: 143, 88: 76, 89: 4, 90: 231, 91: 212, 92: 124, 93: 30, 94: 230, 95: 138, 96: 180, 97: 192, 98: 130, 99: 205, 100: 54, 101: 103, 102: 15, 103: 61, 104: 67, 105: 213, 106: 144, 107: 62, 108: 78, 109: 7, 110: 108, 111: 164, 112: 90, 113: 131, 114: 197, 115: 69, 116: 96, 117: 22, 118: 176, 119: 190, 120: 137, 121: 80, 122: 244, 123: 195, 124: 26, 125: 16, 126: 179, 127: 107, 128: 185, 129: 252, 130: 24, 131: 152, 132: 132, 133: 186, 134: 115, 135: 20, 136: 174, 137: 6, 138: 255, 139: 248, 140: 232, 141: 71, 142: 127, 143: 49, 144: 48, 145: 187, 146: 79, 147: 236, 148: 188, 149: 220, 150: 198, 151: 243, 152: 101, 153: 32, 154: 147, 155: 171, 156: 8, 157: 173, 158: 254, 159: 153, 160: 139, 161: 226, 162: 52, 163: 228, 164: 129, 165: 148, 166: 162, 167: 68, 168: 151, 169: 77, 170: 225, 171: 218, 172: 113, 173: 37, 174: 126, 175: 112, 176: 43, 177: 201, 178: 64, 179: 41, 180: 184, 181: 93, 182: 118, 183: 100, 184: 98, 185: 159, 186: 110, 187: 44, 188: 50, 189: 116, 190: 234, 191: 122, 192: 87, 193: 27, 194: 161, 195: 33, 196: 194, 197: 203, 198: 229, 199: 149, 200: 207, 201: 119, 202: 0, 203: 250, 204: 82, 205: 120, 206: 136, 207: 219, 208: 121, 209: 35, 210: 58, 211: 40, 212: 28, 213: 251, 214: 227, 215: 111, 216: 45, 217: 211, 218: 97, 219: 123, 220: 57, 221: 19, 222: 109, 223: 181, 224: 42, 225: 38, 226: 175, 227: 167, 228: 191, 229: 189, 230: 170, 231: 214, 232: 242, 233: 70, 234: 210, 235: 217, 236: 34, 237: 91, 238: 247, 239: 23, 240: 31, 241: 29, 242: 208, 243: 117, 244: 155, 245: 1, 246: 202, 247: 145, 248: 9, 249: 238, 250: 169, 251: 53, 252: 72, 253: 3, 254: 21, 255: 39}
```
### hexadecimal format
```
d77d724bc1f99a5fa63c3f0bb1808653b2b78d63f6d196eb2f3711a3dd5e24ed8ea066c405a5499c92e9fd0d38513bac0285f16a589e684a1287ef54428c19c756de2e0a6933c8595c550ef00cb641a8cc9df5e0cedfd88f4c04e7d47c1ee68ab4c082cd36670f3d43d5903e4e076ca45a83c5456016b0be8950f4c31a10b36bb9fc189884ba7314ae06fff8e8477f3130bb4fecbcdcc6f3652093ab08adfe998be234e48194a244974de1da71257e702bc94029b85d7664629f6e2c3274ea7a571ba121c2cbe595cf7700fa527888db79233a281cfbe36f2dd3617b39136db52a26afa7bfbdaad6f246d2d9225bf7171f1dd0759b01ca9109eea93548031527
```
### integer format
```
27203095526857900917255529156459248426224426932033896257926343250383493871417109019061130428222729535719618635855899468507450979641537364389947635497713841705363731238830042636157479268887290660070358963521994345338213320059740709074193728549799001397413746543822089507292541795388324737499457547792913781979892950639593326968826748948872830505251821386023880723659100217767976386794346297991142285518890720411935495244382284994311783782375573793042070116815581561696308429384581208783779411980392274018305147581730938367082604124684848789380944923813592344089198004389338553847180782222388978180699267725560174023975
```
### bytearray format
```
[215, 125, 114, 75, 193, 249, 154, 95, 166, 60, 63, 11, 177, 128, 134, 83, 178, 183, 141, 99, 246, 209, 150, 235, 47, 55, 17, 163, 221, 94, 36, 237, 142, 160, 102, 196, 5, 165, 73, 156, 146, 233, 253, 13, 56, 81, 59, 172, 2, 133, 241, 106, 88, 158, 104, 74, 18, 135, 239, 84, 66, 140, 25, 199, 86, 222, 46, 10, 105, 51, 200, 89, 92, 85, 14, 240, 12, 182, 65, 168, 204, 157, 245, 224, 206, 223, 216, 143, 76, 4, 231, 212, 124, 30, 230, 138, 180, 192, 130, 205, 54, 103, 15, 61, 67, 213, 144, 62, 78, 7, 108, 164, 90, 131, 197, 69, 96, 22, 176, 190, 137, 80, 244, 195, 26, 16, 179, 107, 185, 252, 24, 152, 132, 186, 115, 20, 174, 6, 255, 248, 232, 71, 127, 49, 48, 187, 79, 236, 188, 220, 198, 243, 101, 32, 147, 171, 8, 173, 254, 153, 139, 226, 52, 228, 129, 148, 162, 68, 151, 77, 225, 218, 113, 37, 126, 112, 43, 201, 64, 41, 184, 93, 118, 100, 98, 159, 110, 44, 50, 116, 234, 122, 87, 27, 161, 33, 194, 203, 229, 149, 207, 119, 0, 250, 82, 120, 136, 219, 121, 35, 58, 40, 28, 251, 227, 111, 45, 211, 97, 123, 57, 19, 109, 181, 42, 38, 175, 167, 191, 189, 170, 214, 242, 70, 210, 217, 34, 91, 247, 23, 31, 29, 208, 117, 155, 1, 202, 145, 9, 238, 169, 53, 72, 3, 21, 39]
```
The keys generated are nothing but random sequences of 256 bytes. Each of these 256 bytes can range from 0 to 255 and does not repeat, so each  key always contains all numbers from 0 to 255, but each time the sequence is different. There are therefore 256! (256*254*253*252...*1) possible combinations.

Currently the encryption function performs two transformations on input:

1) When you feed Fileghost with a file to be encrypted, every byte of the file is taken and replaced with that of the key at that precise index. For example if the first number of the key is equal to 23 then all the bytes corresponding to the number 0 in the file will be replaced with 23, if the second number of the key is equal to 132 then all the bytes in the file array corresponding to the number 1 will be replaced with 132. This makes it already very difficult to access the original input or key, but it is still possible with some effort and dedication. Then, another function is performed in addition which we will see now. This first "function" can be described simply like this (keeping in mind that the `keys` variable is a *dictionary* like the one above):
```
output=[]
for n in input:
    output.append(keys[n])
```
2) Then, for each byte encrypted with the first function , it will already execute a bitwise XOR operation on that byte with an item from the keys, based on the byte's position in the previous output:
```

for p in range(0,len(output)):
    output[p]=output[p] ^ keys[p%len(keys)]
```
This last function does a little magic but its strength is based on the fact that the input remains 256 bytes (as the key length), this doesn't mean that it's simple and immediate to crack an input longer than 256 bytes, but it could be possible if someone takes the time to do it commitment and good will, although the chances of doing so are very low indeed.
For the generation of random numbers the `secrets` module present in Python from version 3.6 is principally used, which provides a strong and acceptable level of security, furthermore the generation of randomness could be enchanted in future.
