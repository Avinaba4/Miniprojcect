import re
from collections import Counter


def analyze_text(text, n):
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    avg_word_len = sum(len(word) for word in words) / word_count
    word_freq = Counter(words).most_common(n)

    output = f"Word count: {word_count}\n"
    output += f"Character count: {char_count}\n"
    output += f"Sentence count: {sentence_count}\n"
    output += f"Average word length: {avg_word_len:.1f}\n"
    output += f"Most frequent words: {[word for word, freq in word_freq]}"

    return output


if __name__ == '__main__':
    text = input("Enter text to analyze: ")
    n = int(input("Enter number of most frequent words to display: "))
    print(analyze_text(text, n))
