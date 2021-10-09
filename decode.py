# coded by wolkan @ 2021

import hashlib
from typing import _SpecialForm 

print("""
ALGORİTHMS
1- MD5
2- SHA-1
3- SHA-256
""")

choice = input("Algorithm Type: ")

if (choice == "1"):

    Diccionary = input("File Address: ")
    hash1 = input("HASH: ")

    listaslineas = open(Diccionary,"r").readlines()

    for i in range(0,len(listaslineas)): 
	    hash2 = hashlib.md5(listaslineas[i].replace("\n","").encode()).hexdigest()

	    if hash1 == hash2:
		    print("Password Found: "+listaslineas[i].replace("\n",""))
		    exit()

    print("HASH not found!")

elif (choice == "2"):

    Diccionary = input("File Address: ")
    hash1 = input("HASH: ")

    listaslineas = open(Diccionary,"r").readlines()

    for i in range(0,len(listaslineas)): 
	    hash2 = hashlib.sha1(listaslineas[i].replace("\n","").encode()).hexdigest()

	    if hash1 == hash2:
		    print("Password Found: "+listaslineas[i].replace("\n",""))
		    exit()

    print("HASH not found!")

elif (choice == "3"):

    Diccionary = input("File Address: ")
    hash1 = input("HASH: ")

    listaslineas = open(Diccionary,"r").readlines()

    for i in range(0,len(listaslineas)): 
	    hash2 = hashlib.sha256(listaslineas[i].replace("\n","").encode()).hexdigest()

	    if hash1 == hash2:
		    print("Password Found: "+listaslineas[i].replace("\n",""))
		    exit()

    print("HASH not found!")

else:
    print("Wrong keystroke!")
