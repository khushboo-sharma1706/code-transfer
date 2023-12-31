animals = ["elephant", "lion", "tiger", "giraffe"]  # Create a new list
print(animals)

animals += ["monkey", "dog"]  # Add two items to the list
print(animals)

animals.append("dino")  # Add one more item to the list using append() method
print(animals)

animals[-1] = "dinosaur"
print(animals)
animals.extend([["dino", 1]])
print(animals)
animals.append(50.78)
print(animals)
