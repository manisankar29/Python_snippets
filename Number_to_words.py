from inflect import engine

def num_to_words(num):
    p = engine()
    return p.number_to_words(num)

number = int(input("Enter the number:"))
print(num_to_words(number))