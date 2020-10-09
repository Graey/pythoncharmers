
def checksum(cheknum, clen, odd_even):
    for i in range(odd_even, clen, 2):
        #test1=int(cheknum[i] * 2 /10)
        cheknum[i] = int(cheknum[i] * 2 / 10) + (cheknum[i]*2 % 10)
    return cheknum


while True:
    cardnum = input("What is your card number?: ")
    if(0 < len(cardnum)):
        try:
            temp_list = list(cardnum)
            map_object = map(int, temp_list)
            # print(map_object)
            cnum = list(map_object)
            # simply setting ctype = cnum in python instead of saving a copy of it, python will reference the ctype to point at cnums address .hence to copy we need to use cnum[:] to actually copy it!!
            ctype = cnum[:]
        except:
            print("INVALID")
            exit()
    if ((len(cardnum) != 13) and (len(cardnum) != 15) and (len(cardnum) != 16)):
        print("INVALID")
        exit()

    # variable to hold the lenght
    clen = len(cnum)
    if clen == 13:
        # the even is to take care of alternative numbers to not include the even numbers or first and last number and truly be alternatives.
        even = 1
        sumchek = checksum(cnum, clen, even)
        if(sum(sumchek) % 10 == 0 and ctype[0] == 4):
            print("VISA")
            exit()

    elif clen == 15:
        # the even is to take care of alternative numbers to not include the even numbers or first and last numbers and truly be alternative.
        even = 1
        sumchek = checksum(cnum, clen, even)
        if(sum(sumchek) % 10 == 0 and ctype[0] == 3 and(ctype[1] == 4 or ctype[1] == 7)):
            print("AMEX")
            exit()

    elif clen == 16:
        # the odd is to take care of alternative numbers.
        odd = 0
        sumchek = checksum(cnum, clen, odd)
        if(sum(sumchek) % 10 == 0 and ctype[0] == 4):
            print("VISA")
            exit()
        elif (sum(sumchek) % 10 == 0 and ctype[0] == 5 and(ctype[1] == 1 or ctype[1] == 2 or ctype[1] == 3 or ctype[1] == 4 or ctype[1] == 5)):
            print("MASTERCARD")
            exit()