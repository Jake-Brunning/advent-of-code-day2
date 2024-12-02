
#read the file input
def readFile(fileName: str):
    # This opens a handle to your file, in 'r' read mode
    file_handle = open(fileName, 'r')
    # Read in all the lines of your file into a list of lines
    lines_list = file_handle.readlines()
    # Do a double-nested list comprehension to get the rest of the data into your matrix
    my_data = [[int(val) for val in line.split()] for line in lines_list[0:]]

    return my_data

    
    

def main():
    input = readFile("input.txt")
    print(countSafe(input))

#count the amount of safe levels
def countSafe(input):
    totalSafe = 0

    for x in input:
        totalSafe += checkSafetyOfRecord(x)

    return totalSafe

def checkSafetyOfRecord(input: list[int]) -> int:
    ifBounds, remBoundIndex = checkInBounds(input, -1)
    ifIncrDecr, remIncrDecrIndex = checkAllIncrDecr(input, remBoundIndex)

    if((ifBounds and ifIncrDecr) and (remBoundIndex == remIncrDecrIndex)):
        return 1
    
    return 0

    
def checkInBounds(input: list[int], removedYet: int):
    LB = 1 #inclusive
    UP = 3 #inclusive

    for i in range(1, len(input)):
        difference = abs(input[i-1] - input[i])
        if (difference < LB or difference > UP and removedYet == -1):
            
            del input[i]
            return checkInBounds(input, i)
        
        elif(difference < LB or difference > UP):
            return False, -1
        
    return True, removedYet

def checkAllIncrDecr(input: list[int], removedYet: int) -> bool:
    asc = input[0] < input[1] #if we are ascending or not

    for i in range(2, len(input)):
        goUp = input[i - 1] < input[i]
        if(goUp and not asc):
            if(removedYet == -1):
                del input[i]
                return checkAllIncrDecr(input, i)
            else:
                return False, -1
        if(not goUp and asc):
            if(removedYet == -1):
                del input[i]
                return checkAllIncrDecr(input, i)
            else:
                return False, -1

    return True, removedYet
    


if __name__ == '__main__':
    main()