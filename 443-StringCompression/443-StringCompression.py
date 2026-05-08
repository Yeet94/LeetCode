# Last updated: 5/8/2026, 4:22:47 PM
class Solution:
    def compress(self, chars: List[str]) -> int:
        writer = 0
        explorer = 0


        while explorer < len(chars):
            compressed_char = chars[explorer]
            count = 0 

            while explorer < len(chars) and chars[explorer] == compressed_char:
                explorer +=1  
                count +=1
            
            chars[writer] = compressed_char
            writer +=1

            if count > 1:
                for digit in str(count):
                    chars[writer] = digit
                    writer += 1

        
        return writer
