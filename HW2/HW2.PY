# User-defined function to get frequency of characters
def char_frequency(text):
    freq = {}
    for ch in text:
        ch_lower = ch.lower()  # count ignoring case
        freq[ch_lower] = freq.get(ch_lower, 0) + 1
    return freq

# Main Program
user_input = input("Enter string: ")
parts = user_input.split(",")

for word in parts:
    word = word.strip()
    result = char_frequency(word)

    output = []
    seen = []
    for ch in word:  # preserve order
        ch_lower = ch.lower()
        if ch_lower not in seen:
            output.append(f"{ch}={result[ch_lower]}")
            seen.append(ch_lower)
    print(", ".join(output))
