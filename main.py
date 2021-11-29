f = open('result_prove.txt', 'w')

def calclulate():
    number_base = 2
    result = []
    # base = []
    next_base = None 
    txt_beginning = "Result of "
    while True:
        result.append(txt_beginning + str(number_base))
        number_result = number_base
        
        while(number_result > 1):
            base = number_result
            if number_result % 2 == 0 :
                
                (number_result) = number_result / 2
                result.append(str(number_base)+" use "+"(" +str(base)+" / 2)"+ " => " + str(number_result))
            elif number_result < 1:
                print(number_base)
                break
            else:
                (number_result) = (number_result * 3) + 1
                result.append(str(number_base)+" use "+"("+str(base)+" * 3 + 1)"+  " => " + str(number_result))
                
        # print(str(number_base)+" => "+ str(number_result))

        next_base = number_base + 1
        
        if next_base != number_base + 1 :
            break
        
        if number_result != 1:
            print(number_result)
            break

        number_base += 1
        
        if number_base == 6:
            break
    
    for i in result:
        print(i)

calclulate()
