from collections import defaultdict

# training text
text = "The quick brown fox jumps over the lazy dog"

text = "".join([i for i in text.lower()])

frequencies = defaultdict(int)
symbols = set({})

for w in text.split(" "):
    frequencies[w] = frequencies.get(w, 0) + 1

    for char in w:
        symbols.add(char)

training_iters = 10

# turn the quick brown fox jumps over the lazy dog into a list of characters like
# (t, h, e, 10)
text_as_chars = []

merges = {}

# frequencies
for word in text.split(" "):
    chars = list(word)
    text_as_chars.append((chars, frequencies[word]))

for i in range(0, training_iters):
    pair_count = {}

    for word, freq in text_as_chars:
        for i in range(0, len(word) - 1):
            pair = (word[i], word[i + 1])
            pair_count[pair] = pair_count.get(pair, 0) + freq

    # merge the most frequent pair
    if len(pair_count) == 0:
        break

    most_frequent_pair = max(pair_count, key=pair_count.get)

    merges[most_frequent_pair] = pair_count[most_frequent_pair]

    new_text_as_chars = []

    for item in text_as_chars:
        word, freq = item
        
        # replace the most frequent pair with a new symbol
        new_word = []

        # don't remove the last char

        i = 0

        while i < len(word):
            if i == len(word) - 1:
                new_word.append(word[i])
                i += 1
                break

            if word[i] == most_frequent_pair[0] and word[i + 1] == most_frequent_pair[1]:
                new_word.append(most_frequent_pair[0] + most_frequent_pair[1])

                # skip the next char
                i += 2
            else:
                new_word.append(word[i])
                i += 1

        new_text_as_chars.append((new_word, freq))

    text_as_chars = new_text_as_chars

    vocab = {}

    for word, freq in text_as_chars:
        for char in word:
            vocab[char] = vocab.get(char, 0) + freq

    text_as_chars = sorted(text_as_chars, key=lambda x: x[1], reverse=True)

    print(vocab)

input_seq = "there"

encoded = []

def encode(input_seq):
    encoded = []

    while len(input_seq) > 0:
        for i in range(0, len(input_seq)):
            if input_seq[0:i + 1] in vocab:
                encoded.append(input_seq[0:i + 1])
                input_seq = input_seq[i + 1:]
                break

    return encoded

result = encode(input_seq)

print(result)