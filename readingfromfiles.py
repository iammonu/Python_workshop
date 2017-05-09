import sys
inputFilename=input("enter name of input file")
inputFile=open(inputFilename,"r")
print("Opening file ",inputFilename,"for reading.")
for line in inputFile:
    sys.stdout.write(line)
    inputFile.close()
    print("completed reading of file",inputFilename)
    
