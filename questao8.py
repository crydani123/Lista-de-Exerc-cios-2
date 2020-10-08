def recl(l, i=0):
    try:
        elmnt = l[i]
        i+=1
        return elmnt + recl(l,i)
    except:
        return 0

print (recl([5,8]))