class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp =[]
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        clean = ''.join(temp)
        reverse = temp[::-1]
        if(reverse == temp):
            return True
        return False
        