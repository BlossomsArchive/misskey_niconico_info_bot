f = open("test.txt", "r")
test_content = f.read()
f.close()

print(test_content)

g = open("test.txt", "w")
g.write("It has changed")
g.close

print("echo \"Hello, World\" > test.txt")
