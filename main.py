file = open('codingal.txt','r')
print(file.read())
file.close()
file = open('codingal.txt','r')
print("\n raed in parts \n")
print(file.read(8))
file.close()
file = open('codingal.txt','a')
file.write("Hi iam ragav")
file.close()