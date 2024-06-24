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

#28. Find the Index of the First Occurrence in a String
def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

#58. Length of Last Word
def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        # print("$",s,"$")
        res = ' ' in s
        if res==False:
            return len(s)
        #s.rindex gave error when there were no spaces in s
        lastIndex =s.rindex(' ')
        # print(lastIndex)
        subs=s[lastIndex+1:]
        # print(subs)
        return len(subs)

#125. Valid Palindrome
def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        st=""
        for i in range(len(s)):
            if s[i].isalnum():
                st=st+s[i]
        print(st)

        for i in range(len(st)):
            if st[i]!=st[len(st)-i-1]:
                return False
                
        return True 
#344. Reverse String
def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

#345. Reverse Vowels of a String
def reverseVowels(self, s: str) -> str:
        lowerVowels ="aeiou"
        upperVowels ="AEIOU"
        vowel =[]
        for characters in s:
            if characters in lowerVowels or characters in upperVowels:
                vowel.append(characters)
        ans = ""
        vowel.reverse()
        i=0
        for characters in s:
            if characters in lowerVowels or characters in upperVowels:
                ans=ans+vowel[i]
                i+=1
            else:
                ans=ans+characters
        return ans
# 1773. Count Items Matching a Rule
 def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans=0
        rule = {'type':0, 'color':1, 'name':2}
        for i in items:
            if i[rule[ruleKey]]==ruleValue:
                ans+=1
        return ans

