class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""

        for word in strs:
            length = len(word)

            encoded_word = str(length) + "#" + word

            encode_str = encode_str + encoded_word

        return encode_str

    def decode(self, s: str) -> List[str]:
        final_list = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            word = s[word_start:word_end]

            final_list.append(word)

            i = word_end




        return final_list
