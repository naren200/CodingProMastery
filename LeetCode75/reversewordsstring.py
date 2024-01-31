class Solution:
    def reverseWords(self, s: str) -> str:
        # Things Learnt -> return ' '.join(s.split()[::-1])

        size = len(s)-1
        return_word = ""
        record = False
        save_word = ""
        for i in range(size,-1,-1):
            # print(i)

            if(record == True and (s[i] != " " or i == 0 )):
                print(s[i])
                save_word = save_word + s[i]

            if((s[i] == " " or i == 0 ) and record == True ):
                print("record is false")
                record = False
                save_word = save_word[::-1]
                if(save_word[0]== " "):
                    save_word = save_word[1:]
                return_word += save_word
                if(i!=0):
                    return_word += " "

            if(s[i] == " " and s[i-1] != " " or (i == size and s[i] != " ") and record != True):
                print("I am gonna start recording")
                record = True
                if(i==size and s[i]!=" "):
                    save_word = s[i]
                else:
                    save_word = ""
                print(save_word)
                continue

        if(len(s)==1):
            return s
        if(return_word[-1]== " "):
            return_word = return_word[:len(return_word)-1]

        return return_word