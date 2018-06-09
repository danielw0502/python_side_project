print"Please input the file name:"

file_name = raw_input()

file_read = open(file_name)

times = 0
def word_statistics(cnt,word,centence):
    if len(word) > len(centence):
        return cnt
    elif word == centence:
        return cnt+1
    else:
        for i in range(0,len(centence)-len(word)+1):
            if word == centence[i:i+len(word)]:
                if i == 0 and centence[i+len(word)] == ' ':
                    cnt += 1
                elif i >= 1 and centence[i-1] == ' ' and i+len(word) < len(centence) and centence[i+len(word)] == ' ':
                    cnt += 1
                elif i+len(word) == len(centence) and centence[i-1] == ' ':
                    cnt += 1
    #print centence
    return cnt

while 1:

    if times != 0:
        file_read = open(file_name)
    
    times += 1
    word = raw_input("Please input the word:(if exit please input /exit )")
    

    cnt = 0

    if word == '/exit':
        break
    
    while 1:
        line = file_read.readline().strip()
        print line
        if not line:
            file_read.close()
            break
        cnt = word_statistics(cnt,word,line)

    print ("The number of %s in %s is %d" % (word,file_read,cnt))

