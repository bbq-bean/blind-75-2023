class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        builder_dict = {}

        for word in strs:
            # 1. sort each word
            sorted_word = "".join(sorted(word))

            # 2. Anagram Groups are represented by their sorted form as key
            # if its already present, add current form of the word to the Anagram Group
            if sorted_word in builder_dict:
                builder_dict[sorted_word].append(word)
            # else create a new entry with our sorted key and itself as the first element of the Anagram Group
            else:
                builder_dict[sorted_word] = [word]

        # so we end up with a dict like this:
        # input strs
        # ["eat","tea","tan","ate","nat","bat"]

        # builder_dict
        # {'aet': ['eat', 'tea', 'ate'],
        #  'ant': ['tan', 'nat'],
        #  'abt': ['bat']}

        # now extract the lists of anagrams and create the list of lists to return
        output = []

        for v in builder_dict.values():
            output.append(v)

        return output
