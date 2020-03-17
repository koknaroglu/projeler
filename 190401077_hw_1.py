def get_hist(liste): #dosyadaki kelimelerin her birinden kaç tane olduğunu buluyor
    my_hist={}
    for w in liste:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist[w]=1
    return my_hist


def get_words(my_file): #dosyadaki her kelimeyi listeye topluyor
    my_list=[]
    f = open(my_file,"r+")
    contents = f.readlines()
    for line in contents:
        words=(line.split(" ")).split(",")
        for word in words:
            my_list.append(word)
    f.close()
    return my_list


print(get_hist(get_words("C:\\Users\\batuh\\Desktop\\Yeni klasör\\1.txt")))
