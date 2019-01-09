#! /bin/bash/env python3
'''
This is a quick function to use low level encoding. Base64 is not too
complicated on its own; however coupled with Hashing creates a secure
data structure.

Created By Lynton Brown 01/09/2019
'''
import base64

def Encode(data):
    encodedData=base64.b64encode(data.encode())
    print("Encoded Data:\n\t%s"%(encodedData.decode('ascii')))
    return(encodedData)

def Decode(data):
    decodedData=(base64.b64decode(data))
    print("Decoded Data:\n\t%s"%(decodedData.decode('ascii')))
    return(decodedData)

data=(input("Data to be encoded:\n\t"))
Decode(Encode(data))
