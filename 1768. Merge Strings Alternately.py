class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Declare pointers and result array with 0
        point1=0
        point2=0
        result=[0] * (len(word1) + len(word2))
        index=0

        # iterate till one the pointers reach end
        while point1 < len(word1) and point2 < len(word2):
            if index % 2==0:
                result[index]=word1[point1]
                point1 +=1
            else:
                result[index]=word2[point2]
                point2 +=1
            index += 1

        # if pointer 1 ends first
        if point1 == len(word1):
            while point2<len(word2):
                result[index] = word2[point2]
                point2 +=1
                index +=1

        # if pointer 2 ends first
        else:
            while point1<len(word1):
                result[index] = word1[point1]
                point1 +=1
                index +=1
        #return result

        # join the array of strings 
        return "".join(result)







