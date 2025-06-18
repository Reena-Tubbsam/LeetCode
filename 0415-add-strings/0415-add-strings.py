class Solution(object):
    def addStrings(self, num1, num2):
        i = len(num1) - 1  # start from the end of num1
        j = len(num2) - 1  # start from the end of num2
        carry = 0          # carry starts at 0
        result = []        # empty list to store answer digits

    # keep adding until both numbers are done and no carry left
        while i >= 0 or j >= 0 or carry:
        # get current digits, or 0 if string is finished
            if i >= 0:
                digit1 = ord(num1[i]) - ord('0')
            else:
                digit1 = 0

            if j >= 0:
                digit2 = ord(num2[j]) - ord('0')
            else:
                digit2 = 0

        # add digits and carry
            total = digit1 + digit2 + carry
            carry = total // 10         # update carry
            result.append(str(total % 10))  # store current digit

        # move to the left in both numbers
            i -= 1
            j -= 1
    # reverse result to get correct order
        return ''.join(result[::-1])