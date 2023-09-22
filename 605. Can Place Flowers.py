def canPlaceFlowers(flowerbed, n) :
    count = 0

    # Base Case
    if len(flowerbed)==1:
        if flowerbed[0]==0 and (n ==1 or n==0):
            return True
        elif (n==0):
            return True
        else:
            return False

    # First and Last Element Check
    if flowerbed[0]==0 and flowerbed[1]==0:
        flowerbed[0]=1
        count +=1
    if flowerbed[-1]==0 and flowerbed[-2]==0:
        flowerbed[-1]=1
        count +=1
    
    # Check rest of the array 
    for i in range(1,len(flowerbed)-1):
        # Check if the current plot is empty.
        if flowerbed[i] == 0:
            # Check if the left and right plots are empty.
            empty_left_plot = (flowerbed[i - 1] == 0)
            empty_right_lot = (flowerbed[i + 1] == 0)
            
        # If both plots are empty, we can plant a flower here.
        if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                
    return count >= n

flowerbed =[1,0,0,0,1,0,0]
n=2
print(canPlaceFlowers(flowerbed,n))

