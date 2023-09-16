import wordfreq
import sys
import urllib.request

def main():
    is_file = False
    if sys.argv[2].startswith("http://") or sys.argv[2].startswith("https://"):
        response = urllib.request.urlopen(sys.argv[2])
        inp_file = response.read().decode("utf8").splitlines()
    else:
        is_file = True
        inp_file = open(sys.argv[2])

    stop_word_file = open(sys.argv[1])
    amount = int(sys.argv[3])

    stop_words = []

    for line in stop_word_file:
        stripped_line = line.strip()
        stop_words.append(stripped_line)

    words = wordfreq.tokenize(inp_file)
    frequencies = wordfreq.countWords(words, stop_words)
    wordfreq.printTopMost(frequencies, amount)

    if is_file:
        inp_file.close()
    stop_word_file.close()

if __name__ == "__main__":
    main()