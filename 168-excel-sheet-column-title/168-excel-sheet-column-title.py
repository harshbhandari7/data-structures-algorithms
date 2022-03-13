class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chr_key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N',             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        
        output = ''
        while(columnNumber > 0):
            output += chr_key[(columnNumber-1)%26]
            columnNumber = (columnNumber-1) // 26
        return output[::-1]
        