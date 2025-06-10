sentence = input("Sentence: ").lower()
words = sentence.split()
freq_dict = {}

for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

for _ in range(3):
    max_freq = -1
    max_word = None
    
    for word, count in freq_dict.items():
        if count > max_freq:
            max_freq = count
            max_word = word
    
    if max_word is None:
        break  # no words left
    
    print("Word:", max_word, ", Frequency:", max_freq)
    del freq_dict[max_word]  # remove this word for next iteration
