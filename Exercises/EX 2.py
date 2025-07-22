def add_dots(string):
   return ".".join(string)
def remove_dots(string):
  return string.replace(".", "")

print(add_dots("Test"))
print(remove_dots("t.e.s.t"))
