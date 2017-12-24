#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 21:40:28 2017

@author: kratisaxena
"""

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    list_of_argv = []
    for i, v in enumerate(argv):
        print("argv[{0}]: {1}".format(i, v))
        list_of_argv.append(v)
    print(list_of_argv)
        
    # Store input and output file names
    ifile=''
    ofile=''
    
    #find index of "-i" and "-o" to find the input and output file
    i_index = list_of_argv.index("-i")
    o_index = list_of_argv.index("-o")
    ifile = list_of_argv[i_index+1]
    ofile = list_of_argv[o_index+1]
    
    # Display input and output file name passed as the args
    print ("Input file : %s and output file: %s" % (ifile,ofile) )
    
    if ("-d" in list_of_argv and "-e" not in list_of_argv):
        #decoding
        w = open(ofile, "wb") 
        with open(ifile, "r") as f:
            byte = f.read(77)
            while byte:
                w.write(base64Decode(byte))
                byte = f.read(77)
            w.close()
        f.close()
    else:
        #encoding
        w = open(ofile, "w") 
        with open(ifile, "rb") as f:
            byte = f.read() #57
            while byte:
                w.write(base64Encode(byte))
                w.write("\n")
                byte = f.read() #57
            w.close()
        f.close()

    
def base64Encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", 
                "H", "I", "J", "K", "L", "M", "N", 
                "O", "P","Q","R","S","T","U","V",
                "W","X","Y","Z","a","b","c","d",
                "e","f","g","h","i","j","k","l",
                "m","n","o","p","q","r","s","t",
                "u","v","w","x","y","z","0","1",
                "2","3","4","5","6","7","8","9","+","/"]
    bit_str = ""      
    base64_str = ""

    for char in data:
        bin_char = bin(char).lstrip("0b")
        bin_char = bin_char.zfill(8)
        bit_str += bin_char 

    brackets = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]

    for bracket in brackets:
        if(len(bracket) < 6):
            bracket = bracket + (6-len(bracket))*"0" 
        base64_str += alphabet[int(bracket,2)]

    return base64_str

def base64Decode(text):
        alphabet = ["A","B","C","D","E","F","G",
                    "H","I","J","K","L","M","N",
                    "O","P","Q","R","S","T","U",
                    "V","W","X","Y","Z","a","b",
                    "c","d","e","f","g","h","i",
                    "j","k","l","m","n","o","p",
                    "q","r","s","t","u","v","w",
                    "x","y","z","0","1","2","3",
                    "4","5","6","7","8","9","+","/"]
        bit_str = ""
        text_str = ""

        for char in text:
            if char in alphabet:
                bin_char = bin(alphabet.index(char)).lstrip("0b")
                bin_char = bin_char.zfill(6)
                bit_str += bin_char

        brackets = [bit_str[x:x+8] for x in range(0,len(bit_str),8)]

        for bracket in brackets:
            text_str += chr(int(bracket,2))

        return text_str.encode("UTF-8")
