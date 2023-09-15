def tokenize (lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            
            if line[start].isspace():
                start = start+1
                continue
            if line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end+1
                words.append((line[start:end]).lower())
                start = end
                continue
            elif line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end+1
                words.append((line[start:end]).lower())
                start = end
                continue
            else:
                words.append(line[start])
            start = start+1
    return words

def countWords (words, stopWords):
    dictionary = {}
    for word in words:
        if word in stopWords:
            continue
        if word in dictionary:
            dictionary[word] = dictionary[word]+1
        else:
            dictionary[word] = 1
    return dictionary

def printTopMost (frequencies, n):
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_frequencies) < n:
        n = len(sorted_frequencies)

    for i in range(n):
        word = sorted_frequencies[i][0]
        count = sorted_frequencies[i][1]
        output = str(word).ljust(20) + str(count).rjust(5)
        print(output)