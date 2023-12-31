# # Read File
# file1 = open("test.txt")
# print(file1.read())
# file1.close()
#
# # Seek Cursor Position
# print("-----")
# file1 = open("test.txt")
# print(file1.read())
# file1.seek(1,0)
# print(file1.read())
# file1.close()
#
# # Read Line by Line
# print("-----")
# file1 = open("test.txt")
# print(file1.readline())
# print(file1.readline())
#
# # Read All Lines in Array
# print("-----")
# file1 = open("test.txt")
# a = file1.readlines()
# print(a)
# for l in a:
#     print(len(l), l)

# Write a File (W Mode)
# file2 = open("test21.txt", "w")
# file2.write("Gauri\n")
# file2.write("Manthan")
# file2.close()
pass
# Write a File (A Mode)
# file2 = open("test2.txt", "a")
# file2.write("Gauri\n")
# file2.write("Manthan\n")
# file2.close()

# Write a File (X Mode)
# file2 = open("test2x.txt", "x")
# file2.write("Gauri\n")
# file2.write("Manthan\n")
# file2.close()

# Write and Read a File (R+ Mode)
# (doesn't create the file if it doesn't exist, nor does it truncate the file)
# file2 = open("test2.txt", "r+")
# file2.write("Gauri\n")
# file2.write("Manthan\n")
# print(file2.readlines())
# file2.close()

# Write and Read a File (W+ Mode)
# opens the file for reading and writing and creates the file if it doesn't already exist
# file2 = open("test2.txt", "w+")
# file2.write("Gauri\n")
# file2.write("Manthan\n")
# print(file2.readlines())
# file2.close()

# Write and Read a File (a+ Mode)
# a+ mode creates the file if it doesn't already exist, but it positions the stream at the end of the file.
file2 = open("test2.txt", "a+")
file2.write("Gauri\n")
file2.write("Manthan\n")
print(file2.readlines())
file2.close()

## Easy Open and Close
with open("test2.txt", "r") as file4:
    print(file4.readlines())


