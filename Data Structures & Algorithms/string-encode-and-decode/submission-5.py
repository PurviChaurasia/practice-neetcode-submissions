class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))
            encoded_str += "#"
            encoded_str += word
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        counter = 0
        while counter < len(s):
            j = s.find('#', counter)
            length = int(s[counter:j])
            word = s[j+1:j+1+length]
            decoded_str.append(word)
            counter = j + 1 + length

        return decoded_str