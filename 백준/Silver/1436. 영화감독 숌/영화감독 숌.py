n = int(input())
doom_cnt = 0
i=666
while(True):
    string = str(i)
    if "666" in string:
        doom_cnt+=1
        if doom_cnt == n : 
            print(i)
            break
    i+=1