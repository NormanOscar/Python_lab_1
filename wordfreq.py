# Splits lines of text into list of words
def tokenize (lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            # Skip whitespace
            if line[start].isspace():
                start = start+1
                continue
            # If the character is a letter, add it to the word
            if line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end+1
                words.append((line[start:end]).lower())
                start = end
                continue
            # If the character is a digit, add it to the word
            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end+1
                words.append((line[start:end]).lower())
                start = end
                continue
            # If the character is a symbol, add it to the word
            else:
                words.append(line[start])
            start = start+1
    return words

# Counts the number of times each word appears in the list of words
def countWords (words, stopWords):
    dictionary = {}
    for word in words:
        # Skip stop words
        if word in stopWords:
            continue
        # If the word is already in the dictionary, increment its count
        if word in dictionary:
            dictionary[word] = dictionary[word]+1
        # Otherwise, add it to the dictionary
        else:
            dictionary[word] = 1
    return dictionary

# Prints the top n most frequent words
def printTopMost (frequencies, n):
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    # If the number of words is less than n, set n to the number of words
    if len(sorted_frequencies) < n:
        n = len(sorted_frequencies)
    
    # Print the top n most frequent words
    for i in range(n):
        word = sorted_frequencies[i][0]
        count = sorted_frequencies[i][1]
        output = str(word).ljust(20) + str(count).rjust(5)
        print(output)