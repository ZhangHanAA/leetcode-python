class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not numRows > 1: return s

        if numRows == 2:
            s1 = s[::2]
            s2 = s[1::2]
            s3 = s1 + s2
            return s3

        s_Initialize = [''] * numRows
        i = 0
        n = len(s)
        while i < n:
            for count_columns in range(numRows):
                if i < n:
                    s_Initialize[count_columns] += s[i]
                    i += 1
            for count_rows in range(numRows - 2, 0, -1):
                if i < n:
                    s_Initialize[count_rows] += s[i]
                    i += 1

        return ''.join(s_Initialize)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    res = sol.convert(s, numRows)
    print(res)
