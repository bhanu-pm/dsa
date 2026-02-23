# array of strings given
# group all the anagrams in a list, return list(list(all groups))


########## Naive solution
# we can make a list of dictionaries
    # each dict has counts of chars of a word
# OrderedDict{word = dict{letter = count}}
# final = []
# while len(od.keys()) >= 0:
    # od.keys()[0]
    # group.append(word)
    # del od[word]
    # for newword in od.keys():
        # if od[newword] == od[word]
            # group.append(newword)
            # del od[newword]
    # final.append(group)
# return final


############ Group elements by property
# dict(anagram = [list of words])
# return list(dict.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = dict()
        for i in strs:
            keyl = sorted(i)
            key = ''.join(keyl)
            if key not in final:
                final[key] = []
            final[key].append(i)
        return list(final.values())