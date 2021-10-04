class Solution(object):
   def isPalindrome(self, s):
      """
      :type s: str
      :rtype: bool
      """
      x = ""
      diff = ord('a') - ord('A')
      for i in s:
         if ord(i)>=ord('a') and ord(i)<=ord('z') or ord(i)>=ord("0") and ord(i)<=ord("9"):
            x+=i
         elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            i = chr(diff+ord(i))
            x+=i
      #print(s)
      #print(x)
      return x == x[::-1]
ob1 = Solution()
print(ob1.isPalindrome("A Man, a Plan, a Canal: Panama"))