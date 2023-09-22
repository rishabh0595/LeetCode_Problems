def canPlaceFlowers(flowerbed, n) :
    count=0
    i=0
    if len(flowerbed)==1:
        if flowerbed[i]==0:
            n=n-1
    else:
        if i == 0 and flowerbed[i]==0 and len(flowerbed)>0:
            if flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n=n-1
        i=i+1

        while i < len(flowerbed)-1:
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                n=n-1
            i=i+1



        if i == len(flowerbed)-1 and flowerbed[i]==0:
            ("Last Element")
            if flowerbed[i-1]==0:
                n=n-1
            
    if n==0:
        return True
    else:
        return False
        

flowerbed =[1,0,0,0,1,0,0]
n=2
print(canPlaceFlowers(flowerbed,n))

