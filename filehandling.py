
# data= open('demo.txt','r')
# x=data.read()
# print(x)

data = open('demo.txt','rt')

for i, line in enumerate(data,1):
    if i == 3:
        print(line)
        break 



