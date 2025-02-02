def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        # print(file_contents)

    words = file_contents.split()
    # print(len(words))
    report_word = len(words)

    lower = file_contents.lower()
    count = letter_count(lower)
    report(report_word, lower)

def letter_count(lower):
    count = [x for x in lower]
    # print(count.count("p"))
    letter_counter = {}
    for i in count:
        letter_counter[i] = letter_counter.get(i, 0 ) + 1
    return letter_counter

def report(report_word, lower):
    # print("Report of ")
    # print(f"{report_word} in book")

    count = [x for x in lower if x.isalpha()]
    # print(count.count("p"))
    letter_counter = {}
    for i in count:
        letter_counter[i] = letter_counter.get(i, 0 ) + 1
    
    y = dict(sorted(letter_counter.items()))
    # print(y)
    for letter, amount in y.items():
        print(f"Letter '{letter}' appears {amount} times")
        print("?")

if __name__ == "__main__":
    main()
