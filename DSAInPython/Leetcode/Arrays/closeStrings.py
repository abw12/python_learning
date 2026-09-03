class CloseStrings:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # length of two words should be same
        if len(word1) != len(word2):
            return False
        # create two 26 length array to store the english characters
        freq1 = [0] * 26
        freq2 = [0] * 26
        # populate two arrays
        for ch in word1:
            freq1[ord(ch) - ord('a')]+=1 # ord fucntion return the unicode code point ofa character(eg a=96)
        for ch in word2:
            freq2[ord(ch) - ord('a')]+=1

        # 1. Both words must share the exact same active characters
        for i in range(26):
            if ((freq1[i] == 0) != (freq2[i] == 0)):
                return False
        # 2. Frequencies must match regardless of which character has which count
        return sorted(freq1) == sorted(freq2)
