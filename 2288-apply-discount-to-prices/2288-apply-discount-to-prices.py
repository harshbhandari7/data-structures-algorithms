class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sen_lst = sentence.split()
        leng = len(sen_lst)
        
        for i in range(leng):
            char = sen_lst[i]
            if char[0] == '$' and char[-1].isdigit():
                num = char[1:]
                
                if (num.isnumeric()):
                    if discount == 100:
                        new_char = '$0.00'
                    else:
                        disc = (int(num) * discount) / 100
                        disc_price = int(num) - disc
                        new_char = '$' + str(format(disc_price, '.2f'))
                    sen_lst[i] = new_char
                
        return ' '.join(sen_lst)