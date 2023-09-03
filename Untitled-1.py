
sentence_length = 0
word_count = 0
vowel_count = 0


sentence = input("Enter a sentence (end with a period '.'): ")


for char in sentence:
    
    sentence_length += 1

    if char.isalpha():
        
        if char.lower() in "aeiou":
            vowel_count += 1

        
        if sentence_length > 1 and sentence[sentence_length - 2] == ' ':
            word_count += 1


if sentence[-1] == '.':
    
    sentence_length -= 1


print("Length of the sentence:", sentence_length)
print("Number of words in the sentence:", word_count + 1)  
print("Number of vowels in the sentence:", vowel_count)
