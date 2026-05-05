class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "?" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            # Step 1: find the delimiter '?'
            while s[j] != "?":
                j += 1

            # Step 2: get the length
            length = int(s[i:j])

            # Step 3: extract the string
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Step 4: move pointer forward
            i = j + 1 + length

        return result
