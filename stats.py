def word_count(text):
    return text.split()

def char_count(text):
    letters={}
    chars={"char":""}
    text=text.lower()
    for s in text:
        if s in letters:
            letters[s]+=1
        else:
            letters[s]=1
    return letters

def sort_on(dict):
    return dict["num"]

def create_list(dict):
    firstlist=[]
    for k in dict:
        minidict1={}
        minidict1["char"]=k
        minidict1["num"]=dict[k]
        firstlist.append(minidict1)
    firstlist.sort(reverse=True, key=sort_on)
    return firstlist
        



