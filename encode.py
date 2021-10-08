# coded by wolkan @ 2021

import hashlib

print("""
ALGORITHMS
1- MD-5
2- SHA-1
3- SHA-256
""")

secim = input("Algorithm Type: ")

if (secim == "1"):
    word = input("Word: ")
    crypt = hashlib.md5(word.encode('utf-8')).hexdigest()
    print("MD5:",crypt)

elif (secim == "2"):
    word = input("Word: ")
    crypt = hashlib.sha1(word.encode('utf-8')).hexdigest()
    print("SHA-1:",crypt)

elif (secim == "3"):
    word = input("Word: ")
    crypt = hashlib.sha256(word.encode('utf-8')).hexdigest()
    print("SHA-256:",crypt)

else:
    print("Wrong keystroke!")