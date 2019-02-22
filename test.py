import re
def isLegalIP(IP):
    if not IP or IP == "":
        return False
    pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    match = pattern.match(IP)
    if not match:
        return False
    nums = IP.split(".")
    for num in nums:
        n = int(num)
        if n < 0 or n > 255:
            return False
    return True


def catrgoryIP(IP):
    if not IP or IP == "":
        return False
    nums = IP.split(".")
    if 1 <= int(nums[0]) <= 126:
        return "A"
    elif 128 <= int(nums[0]) <= 191:
        return "B"
    elif 192 <= int(nums[0]) <= 223:
        return "C"
    elif 224 <= int(nums[0]) <= 239:
        return "D"
    elif 240 <= int(nums[0]) <= 255:
        return "E"
    return False


def isPrivateIP(IP):
    if not IP or IP == "":
        return False
    nums = IP.split(".")
    if int(nums[0]) == 10:
        return True
    elif int(nums[0]) == 172:
        if 16 <= int(nums[1]) <= 31:
            return True
    elif int(nums[0]) == 192 and int(nums[1]) == 168:
        return True
    return False


def isLegalMask(MASK):
    if not MASK or MASK == "":
        return False
    if not isLegalIP(MASK):
        return False
    binaryMask = "".join(map(lambda x: bin(int(x))[2:].zfill(8), MASK.split(".")))
    firstZero = binaryMask.find("0")
    lastOne = binaryMask.find("1")
    if lastOne > firstZero:
        return False
    return True


while True:
    A, B, C, D, E, Err, P = [0, 0, 0, 0, 0, 0, 0]
    try:
        # s = input()
        s = "10.70.44.68~255.254.255.0"
        IP, MASK = s.split("~")
        if not isLegalIP(IP) or not isLegalMask(MASK):
            Err+=1
        else:
            if isPrivateIP(IP):
                P += 1
            cat = catrgoryIP(IP)
            if cat == "A":
                A += 1
            elif cat == "B":
                B += 1
            elif cat == "C":
                C += 1
            elif cat == "D":
                D += 1
            elif cat == "E":
                E += 1


    except:
        print(A + " " + B + " " + C + " " + D + " " + E + " " + Err + " " + P)
        pass