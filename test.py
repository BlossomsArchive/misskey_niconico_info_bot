import datetime

f = open("test.txt", "r")
test_content = f.read()
f.close()

print(test_content)

g = open("test.txt", "w")
g.write(datetime.datetime.now())
g.close

print("It has changed")
