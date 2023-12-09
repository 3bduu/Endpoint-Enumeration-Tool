import requests

file = open("wordlist.txt","r").read().split('\n')
url = input("URL target: ")

def in_ou_tro(tag):    
    print(f"------------------------------------------------------------{tag}-------------------------------------------------------------")

in_ou_tro("START")
for endp in file:
    res = requests.get(url=f"{url}/{endp}")
    print(f"-> The '{endp}' Content : {res.content}") if res.status_code == 200 else print(f"-> The '{endp}' is not Working 'Status code : {res.status_code}'") 
in_ou_tro("FINISH")