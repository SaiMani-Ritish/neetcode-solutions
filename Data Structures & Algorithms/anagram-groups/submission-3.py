class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        hmap = defaultdict(list)
        for str in strs:
                prime_product = 1.0
                for c in str:
                        prime_product *= primes[ord(c) - ord('a')]
                hmap[prime_product].append(str)
        return list(hmap.values())

        