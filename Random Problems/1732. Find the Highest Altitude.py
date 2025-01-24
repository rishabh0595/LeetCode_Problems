def largestAltitude(gain):
        #gain.insert(0, 0)
        maxAltitude = 0
        maxAltitude=max(maxAltitude,gain[0])
        for i in range(1,len(gain)-1):
            gain[i]=gain[i]+gain[i-1]
            maxAltitude=max(maxAltitude,gain[i])
        return maxAltitude

gain =[52,-91,72]
print(largestAltitude(gain))