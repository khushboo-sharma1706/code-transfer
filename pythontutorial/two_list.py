#Write a function that takes two lists and returns True if they have at least one common member.

def two_list(l1,l2):
    n1 = []
    n2 = []
    for x in l1:
        if x in l2:
            return True
    return False

m = (input(" Enter first List elements: ") )
n = (input(" Enter Second List elements: ") )
print(two_list(m,n))
