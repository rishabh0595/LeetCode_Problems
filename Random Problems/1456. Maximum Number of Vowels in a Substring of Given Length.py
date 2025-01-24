def isVowel(ch):
 
    # Make the list of vowels
    str = "aeiouAEIOU"
    return (str.find(ch) != -1)

def maxVowels(s,k) :
    sum=0
    n=len(s)
    windowSum=0
    
    # Sum of window
    for i in range (k):
        if isVowel(s[i]):
            windowSum +=1

    maxSum=windowSum

    # Iterate from k to n
    for i in range (k,len(s)):
        # remove starting element and add last element
        if isVowel(s[i]):
            windowSum += 1
        if isVowel(s[i-k]):
                windowSum -=1
        #windowSum = windowSum + s[i] - s[i-k]
        maxSum= max(windowSum,maxSum) # Maximum Sum
        print(f'maxsum is {maxSum}')
    
    # Return Average
    return (maxSum)

#s="abciiidef"
s = "aeiou"
k=2
print(maxVowels(s,k))