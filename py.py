if __name__ == "__main__":
    """
      skadkasndkasn
    """
    if len(sys.argv) != 2:
        print("Invalid input. Try typing 'python main.py <filename>.py'\n")
        sys.exit(1)
    """
      skadkasndkasn"""
    parser = argparse.ArgumentParser()
    parser.add_argument("pythonfile")
    args = parser.parse_args()

    filename = args.pythonfile

    # CFG TO CNF
    convertCFG("CFG.txt") 
    cnfInput = "CNF.txt"
'''
dasdasdas
'''