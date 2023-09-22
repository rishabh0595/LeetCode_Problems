def kidsWithCandies(candies, extraCandies):

        maxCandies=max(candies)
        result=[False]*len(candies)
        for i in range (len(candies)):
            print(f'candies[i] + extraCandies is {candies[i] + extraCandies} and {maxCandies}')
            
            if (candies[i] + extraCandies) >= maxCandies:
                result[i]=True
            if candies[i] >= maxCandies:
                 maxCandies=candies[i]
            
        return result
        

candies =[7,2,5,6,9,9,4,5]
extraCandies=3
print(kidsWithCandies(candies,extraCandies))