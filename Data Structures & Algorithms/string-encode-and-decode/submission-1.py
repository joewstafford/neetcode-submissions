class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        #Encodes hello as 5#hello, 'hello world' as 11#hello world so decoder can see spaces
        for string in strs:
            encoded += str(len(string)) + "#" + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            #Gets next number followed by a hashtag
            j = i
            while s[j] != "#":
                j+=1
            #that number is the length of the current string
            length = int(s[i:j])
            #extracts that word from the string (skipping hash with +1)
            word = s[j+1: j+1+length]
            #and adds it to decoded
            decoded.append(word)
            #sets i to be start of next word
            i = j + 1 + length
        return decoded


