#string is immutable
name ='nehal'
print(name.upper())
print(type(name))

# Take input
# num = input("Enter a number:")
# print("Number entered = ", num)

#Lists
l1 =[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
print(l1[2:8])
l1.sort()
print(l1)

#Tuple = immutable
t1= (3,5,1,3,5)
print(t1.count(5))
print(t1.index(1))

#Sets

s1= {1,2,3,3,3,2,1}
s2 = {4,5,6,3}
print(s1)
print(s1.union(s2))
print(s1.intersection(s2))

#Type of an empty set is dictionary
d={}
print(type(d))
d={"nehal":1,"rashi":2, "bhanu":3}
print(d["nehal"])
#ASCII
name="NEHAL"
for i in name:
    print(ord(i))

#3110. Score of a String

def scoreOfString(self, s: str) -> int:
    ans=0
    for i in range(len(s)-1):
        val1=ord(s[i])
        val2=ord(s[i+1])
        ans+=abs(val2-val1)
    return ans

