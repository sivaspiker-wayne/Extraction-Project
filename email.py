import re

def email_extractor(file):
    with open (file,"r") as fhand:
        contents=fhand.read()
    
        pattern=r"[a-z0-9.+-]+@[a-z]+\.[a-z]{2,}+(?:\.[a-z]{2})?"
        extract=re.findall(pattern,contents)

    return extract

if __name__=="__main__":
    result=email_extractor("customer_support_tickets.txt")
    print(result)