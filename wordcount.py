filename = "pattern.py"
word_counts = {}

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

for word in word_counts:
    print(word, word_counts[word])


