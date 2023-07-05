f = open("test.txt", "r")
test_content = f.read()
f.close()

print(test_content)

print("echo \"Hello, World\" > test.txt")
