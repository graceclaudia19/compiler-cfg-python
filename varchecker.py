#FUNCTION PENGECEKAN NAMA VARIABEL
def varChecker(varName):
    # pengecekan huruf pertama dari nama variabel (hanya boleh huruf dan _ )
    if (varName[0] == '_' or (ord(varName[0])>65 and ord(varName[0])<122)):
        for i in range (1,len(varName)):
             # pengecekan sisa hurruf selain huruf pertama dari nama variabel menggunakan ascii value (hanya boleh huruf, _, dan angka )
            if not (varName[i]== "_" or (ord(varName[0])<=65) or (ord(varName[0])>=122) or (ord(varName[0])<=57) or (ord(varName[0])>=48)):
                return False
        return True
    return False

# untuk pengecekan
# while (True):
#     varName = input()
#     print(varChecker(varName))

# def varChecker(varName):
#     return varName.isidentifier()