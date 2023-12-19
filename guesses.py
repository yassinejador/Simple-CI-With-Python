def guesses(target):
    iteractions=0
    left = 0
    right = target
    while (left <= right):
        mid = left + (right-left)//2
        if (mid == target):
            return f"Number is : {mid}\nNumber of iterations is : {iteractions}"
        if (mid <target):
            left = mid+1
        else:
            right = mid-1
        iteractions+=1

target=100000000000000000
print(guesses(target))