def compress_words(word, K):
    for index, c in enumerate(word):
        substr = word[index:index + K]

        if len(set(substr)) == 1:
            word = word.replace(substr, "")

        # breaking condition
        if len(set(word)) == len(word):
            return word


print(compress_words('bvsadddaa', 3))
