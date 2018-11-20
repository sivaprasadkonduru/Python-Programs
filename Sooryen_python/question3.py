'''
Write a function that takes an array of strings and string length (L) as input. Filter out all the string string in the array which has length ‘L’

eg.
wordsWithoutList({"a", "bb", "b", "ccc"}, 1) → {"bb", "ccc"}
wordsWithoutList({"a", "bb", "b", "ccc"}, 3) → {"a", "bb", "b"}
wordsWithoutList({"a", "bb", "b", "ccc"}, 4) → {"a", "bb", "b", "ccc”}

'''


def words_without_list(words, target):

    return {i for i in words if not len(i) == target}


words_without_list({"a", "bb", "b", "ccc"}, 1)
words_without_list({"a", "bb", "b", "ccc"}, 3)
words_without_list({"a", "bb", "b", "ccc"}, 4)
