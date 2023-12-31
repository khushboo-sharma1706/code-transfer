text = 'Gauri\'s World'      # use forward slash to escape the character
print(text
      )
print("\n")
                             # multi line string
ms = """hello world is a world       
is a cartoon is a program
is a known code"""
print(ms)
print("\n")
                              # length of string
message = "Hello World"
print(len(message))
print(message[10])            # Indexing
print(message[0:6])
print(message[:5])
print(message[6:])

print(message.lower())
print(message.upper())
print(message.count("Hello"))
print(message.count("l"))
print(message.find("World"))
print(message.find("Universe"))
message = message.replace("World", "Universe")
print(message)
  # Concatination
greeting = "Hello"
name = "Manthan"
  # Formatted String
print(greeting + ", " + name + ". Welcome!")
print(f"{greeting}, {name.upper()}. Welcome!")

"""
print(dir(name))
print(help(str))
"""
