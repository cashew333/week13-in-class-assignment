def findMaxInList(numbers): 
    maxValue = numbers[0]
    for num in numbers:
      if num > maxValue:
         maxValue = num
    return maxValue

numbers = [200, 5, 80 ,20]

print(findMaxInList(numbers))
