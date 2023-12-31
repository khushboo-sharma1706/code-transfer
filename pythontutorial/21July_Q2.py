"""Q2: Write a Python program to check whether it follows the sequence given in the
patterns array.

Pattern example:
For color1 = ["red", "green", "green"] and patterns = ["a", "b", "b"]
the output should be samePatterns(color1, patterns) = true;
For color2 = ["red", "green", "greenn"] and patterns = ["a", "b", "b"]
the output should be samePatterns (strings, color2) = false."""
import patterns as patterns

color1 = ["red", "green", "green"]
patterns = ["a", "b", "b", "c"]
dic = {}  # {"a": "red"}
success = True
if len(color1) != len(patterns):
    print("Fail")
    exit(1)
for i in range(len(patterns)):
    if patterns[i] not in dic:
        dic[patterns[i]] = color1[i]
    else:
        if dic[patterns[i]] == color1[i]:
            continue
        else:
            print("Fail")
            success = False
            break
if success:
    print("True")

