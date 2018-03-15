#Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".

def translate(text):
    V = ['a','e','i','o','u','A','E','I','O','U']
    t = ""
    for c in text:
        if (c not in V) and (c != " "):
            t+=c+'o'+c
        else:
            t+=c
    return t

print (translate("this is fun"))
