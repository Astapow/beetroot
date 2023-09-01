user_input = input("Enter text: ")

words = user_input.split()

word_count = {word: words.count(word) for word in words}

print("Your dict: ", word_count)
