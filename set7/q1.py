#1a)
def find_palindromes(sentence):
    words = sentence.split()
    palindromes = [word for word in words if word == word[::-1]]
    return palindromes

# Input from user
sentence = input("Enter a sentence: ")
palindrome_words = find_palindromes(sentence)

print("Palindrome words in the sentence are:", palindrome_words)

#1b)
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in sentence if char in vowels)

# Input from user
vowel_count = count_vowels(sentence)

print("Total number of vowels in the sentence:", vowel_count)
