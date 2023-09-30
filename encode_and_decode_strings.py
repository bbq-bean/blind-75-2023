class Codec:
    @staticmethod
    def encode(strs):
        # at the beginning of every string, put directions for how long the
        # word is like 1# or 4#
        encoded_str = ''
        for word in strs:
            # dog becomes 3#dog
            encoded_str += str(len(word)) + '#' + word

        return encoded_str

    @staticmethod
    def decode(s):
        res = []

        i = 0
        while i < len(s):
            j = i
            # Part 1, extract directions added by encode method
            # advance j to element before next #
            while s[j] != '#':
                j += 1
            # slice out digits before next #, convert to int
            length = int(s[i:j])

            # Part 2, use directions to extract work
            # skip past #
            i = j + 1
            # this must be the end of the word
            j = i + length
            # slice word out finally
            res.append(s[i:j])

            # advance i to char after end of word
            i = j

        return res


print(Codec.decode(Codec.encode(["a", "bb", "ccc"])))
