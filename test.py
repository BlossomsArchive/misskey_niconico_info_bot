import datetime

f = open("test.txt", "r")
test_content = f.read()
f.close()

print(test_content)

g = open("test.txt", "w")
now_time = datetime.datetime.now()
g.write(str(now_time))
g.close

print("It has changed")
