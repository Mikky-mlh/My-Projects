def word_to_num(word):
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    teens = {
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19
    }
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    word = word.lower()
    if word in units:
        return units[word]
    elif word in teens:
        return teens[word]
    elif word in tens:
        return tens[word]
    else:
        # Handle complex numbers like "twenty one" or "one hundred twenty three"
        parts = word.split()
        num = 0
        for part in parts:
            if part in units:
                num += units[part]
            elif part in tens:
                num += tens[part]
            elif part == "hundred":
                num *= 100
            elif part == "thousand":
                num *= 1000
            elif part == "million":
                num *= 1000000
            elif part == "billion":
                num *= 1000000000
        return num

num = input("Enter a number in words: ")
print(word_to_num(num))
