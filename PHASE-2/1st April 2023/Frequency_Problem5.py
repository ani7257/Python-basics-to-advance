#Problem5
text = input("Enter the text: ")
text = text.lower()
words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_freq = 0
max_word = ""

for word in freq:
    if freq[word] > max_freq:
        max_freq = freq[word]
        max_word = word
    elif freq[word] == max_freq:
        if len(word) > len(max_word):
            max_word = word
print(max_word, max_freq)
