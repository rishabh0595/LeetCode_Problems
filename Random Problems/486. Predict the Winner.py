def predictTheWinner(nums):
        score_1 = 0
        score_2 = 0

        low = 0
        high = len(nums)-1

        turn = 1

        while low <= high :
            if turn % 2 != 0:
                if nums[low] < nums[high]:
                    score_1 += nums[high]
                    high = high - 1
                else:
                    score_1 += nums[low]
                    low = low+score_1
            else:
                if nums[low] < nums[high]:
                    score_2 += nums[high]
                    high = high - 1
                else:
                    score_2 += nums[low]
                    low = low+score_1
            turn +=1
        print(f'')
        if score_2 > score_1:
            return False
        else:
            return True

nums =[1,5,233,7]
print(predictTheWinner(nums))