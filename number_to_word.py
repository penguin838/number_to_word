ones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teens = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
suffix = ["","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion"]

def convert_twodigit(num):
    numlist = list(str(num))
    
    numlist[0] = int(numlist[0])
    if len(numlist) > 1:
        numlist[1] = int(numlist[1])
    
    if len(numlist) == 1:
        return ones[numlist[0]]
    elif len(numlist) == 2:
        if numlist[0] < 2 and numlist[1] != 0:
            return teens[numlist[1]-1]
        else:
            if numlist[1] != 0:
                return f"{tens[numlist[0]-1]}-{ones[numlist[1]]}"
            else:
                return f"{tens[numlist[0]-1]}"

def convert_threedigit(num):
    numlist = list(str(num))
    for i in range(len(numlist)):
        numlist[i]=int(numlist[i])
    if len(numlist)<3:
        return convert_twodigit(num)
    else:
        if numlist[1] == 0 and numlist[2]==0:
            return f"{ones[numlist[0]]} hundred"
        else:
            return f"{ones[numlist[0]]} hundred and {convert_twodigit(int(str(numlist[1])+str(numlist[2])))}"

def convert_large(num):
    numlist = []
    numstring = "{:,}".format(num)
    numlistelement = 0
    for i in list(numstring):
        if i == ",":
            numlistelement +=1
        else:
            try:
                numlist[numlistelement] +=i
            except:
                numlist.append(i)

    answer = ""
    for i in range(len(numlist)):
        if "zero" not in convert_threedigit(numlist[i]):
            answer += convert_threedigit(numlist[i])+" "+suffix[len(numlist)-i-1]+" "
    return answer
    
def convert(num):
    return convert_large(num)
