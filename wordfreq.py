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