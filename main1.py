file = open ('codingal.txt','r')
print("read first line")
print(file.readline())
file.close()

file = open ('codingal.txt','r')
print("read three line")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open ('codingal.txt','r')
print("looping through the lines")
for line in file:
    
    print(line)
file.close()