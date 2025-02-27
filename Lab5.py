def menu():
    print("Decoding Menu\n"
          "-------------\n"
          "1. Decode hexadecimal\n"
          "2. Decode binary\n"
          "3. Convert binary to hexadecimal\n"
          "4. Quit\n")

def hex_char_decode(digit): # Decodes a single hexadecimal digit and returns its decimal value.
    digit = str(digit) #Start Process: Upper Single Digit
    tempList = []
    tempList.append(digit)
    bigTempList = tempList[0].upper() #End of Process: Upper Single Digit

    upperDigit = bigTempList[0]

    if upperDigit == "A":
        return 10
    elif upperDigit == "B":
        return 11
    elif upperDigit == "C":
        return 12
    elif upperDigit == "D":
        return 13
    elif upperDigit == "E":
        return 14
    elif upperDigit == "F":
        return 15


def hex_string_decode(hex): #Decodes an entire hexadecimal string and returns its decimal value.
    tempList = [0]
    tempList[0] = list(str(hex))

    if tempList[0][0:2] == ['0', 'x']:
        del tempList[0][0:2]

    revHexList = tempList[0][::-1]

    result = 0

    for i in range(len(revHexList)): #touches every item in reversed list
            currentItemBin = revHexList[i]

            if str(currentItemBin) == "A":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)
            elif str(currentItemBin) == "a":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)

            elif str(currentItemBin) == "B":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)
            elif str(currentItemBin) == "b":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)

            elif str(currentItemBin) == "C":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)
            elif str(currentItemBin) == "c":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)

            elif str(currentItemBin) == "D":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)
            elif str(currentItemBin) == "d":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)

            elif str(currentItemBin) == "E":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)
            elif str(currentItemBin) == "e":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)

            elif str(currentItemBin) == "F":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)
            elif str(currentItemBin) == "f":
                currentHexDigit = hex_char_decode(currentItemBin)
                result += int(currentHexDigit) * (16 ** i)

            elif 0 <= int(currentItemBin) <= 9:
                result += int(currentItemBin) * (16**i)

    return result


def binary_string_decode(binary): #Decodes a binary string and returns its decimal value.
    rawBinList = [0]
    rawBinList[0] = list(str(binary)) #Store the numeric input


    if rawBinList[0][0:2] == ['0', 'b']:
        del rawBinList[0][0:2]

    revBinList = rawBinList[0][::-1] #Store the reversed numeric input

    basePowerList = 0

    for i in range(len(revBinList)): #touches every item in reversed list
        currentItemBin = revBinList[i]

        if currentItemBin == "0":
            basePowerList += 0

        elif currentItemBin == "1":
            basePowerList += (2**i)

    return basePowerList



def binary_to_hex(binary):  # Decodes a binary string, re-encodes it as hexadecimal, and returns the hexadecimal string.
    decimal = binary_string_decode(binary) #Binary to Decimal

    quotient = decimal
    remList = []

    while quotient > 0:
        tempQuotient = quotient // 16
        rem = quotient % 16
        remList.append(rem)
        quotient = tempQuotient

    result = ""

    for i in range(len(remList)):
        if 0 <= remList[i] <= 9:
            result += str(remList[i])
        elif 10 <= remList[i] <= 15:
            if remList[i] == 10:
                result += "A"
            elif remList[i] == 11:
                result += "B"
            elif remList[i] == 12:
                result += "C"
            elif remList[i] == 13:
                result += "D"
            elif remList[i] == 14:
                result += "E"
            elif remList[i] == 15:
                result += "F"

    resultList = list(result)
    revResultList = resultList[::-1]

    resultFinal = ""

    for i in range(len(revResultList)):
        resultFinal += revResultList[i]

    return resultFinal


menu()
i = 1

while i == 1:
    menuInput = int(input("Please enter an option: "))

    if menuInput == 4:
        print("Goodbye!")
        break

    numInput = input("Please enter the numeric string to convert: ")

    if not(1 <= menuInput <= 4):
        print("Error: Invalid selection!")

    elif 0 <= menuInput <= 4:

        if menuInput == 1:
            numInput = str(numInput)
            result = hex_string_decode(numInput)
            print(f"Result:", result, "\n")

        elif menuInput == 2:
            numInput = str(numInput)
            result = binary_string_decode(numInput)
            print(f"Result:", result, "\n")

        elif menuInput == 3:
            numInput = str(numInput)
            result = binary_to_hex(numInput)
            print(f"Result:", result, "\n")

    menu()
