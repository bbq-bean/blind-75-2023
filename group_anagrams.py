class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input is list of strings
        # return is a list of lists with the anagrams grouped together

        # default dict will return empty list if key is not found
        res = defaultdict(list)

        for s in strs:  # O(n)
            count = [0] * 26

            for c in s:  # O(n)
                # print(c, ord(c), ord("a"), ord(c) - ord("a"))
                # e 101 97 4
                # a 97 97 0
                # t 116 97 19
                count[ord(c) - ord("a")] += 1

            # there is a neat "builtin" matching login here with the dictionary
            # the count dictionary we created for each word is the key
            # words that are anagrams will have the same count dict created
            # so the current word gets appended to the matching entry in the res
            res[tuple(count)].append(s)

        # O(m * n)
        # * we got 2 loops
        # m number of string, n average length of string
        return res.values()
    