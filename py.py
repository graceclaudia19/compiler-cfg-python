if __name__ == "__main__":
    '''
    tes comment 
    '''
    '''
    tes comment'''
    """
      skadkasndkasn
    """
    if len(sys.argv) != 2:
        print("Invalid input. Try typing 'python main.py <filename>.py'\n")
        sys.exit(1)
    """
    asdkfljadsf"""
    parser = argparse.ArgumentParser()
    parser.add_argument("pythonfile")
    args = parser.parse_args()

    filename = args.pythonfile # asdkfjhasdlkfja

    # CFG TO CNF
    convertCFG("CFG.txt")
    cnfInput = "CNF.txt"

    # CNF PARSINNG
    # terminate (returning empty list) if invalid varname or invalid use of ticks (' and "),
    # if all valid, it will return array and proceed to cyk algorithm

    valid = True
    while (valid):
        file = filename # yayoyoyoyo
        list = pyToStr(file)
        # check before parse process
        
        # print(list)
'''
dasdasdas
''' #lkasdjasdlkfh