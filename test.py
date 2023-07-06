import pathlib

f = open("test.txt", "r")
test_content = f.read()
f.close()

print(test_content)

root = pathlib.Path(__file__).parent.resolve()
text = root / "test.txt"
with open(text,"w") as f:
  f.write("It has changed")

print("It has changed")
