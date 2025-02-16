from collections import Counter
import re
from syllapy import count as syllapy_count

def word_analysis(word1, word2):
    # Function to count common letters
    def common_letter_percentage(w1, w2):
        w1_letters = Counter(w1.lower())
        w2_letters = Counter(w2.lower())
        common = sum((w1_letters & w2_letters).values())
        max_possible = max(len(w1), len(w2))  # Use the length of the longer word
        return (common / max_possible) * 100 if max_possible > 0 else 0

    # Function to count syllables
    def count_syllables(word):
        try:
            return syllapy_count(word.lower())
        except Exception:
            # Fallback heuristic if syllapy fails
            return len(re.findall(r'[aeiouyåäöøœéèêáàâíìîóòôúùû]+', word.lower()))

    percentage = common_letter_percentage(word1, word2)
    syllables_word1 = count_syllables(word1)
    syllables_word2 = count_syllables(word2)
    
    return round(percentage, 2), syllables_word1, syllables_word2

# # Example usage
# word1 = "circumstancia"
# word2 = "circumstances"
# result = word_analysis(word1, word2)
# print(f"w1: {word1}, w2: {word2} >> res: {result}")



def word_analysis2(word1, word2):
    # Function to count common letters
    def common_letter_percentage(w1, w2):
        w1_letters = Counter(w1.lower())
        w2_letters = Counter(w2.lower())
        common = sum((w1_letters & w2_letters).values())
        max_possible = max(len(w1), len(w2))  # Use the length of the longer word
        return (common / max_possible) * 100 if max_possible > 0 else 0

    # Function to count syllables
    def count_syllables(word):
        try:
            return syllapy_count(word.lower())
        except Exception:
            # Fallback heuristic if syllapy fails
            return len(re.findall(r'[aeiouyåäöøœéèêáàâíìîóòôúùû]+', word.lower()))
    
    # Function to check if common letters appear in the same order
    def common_letters_in_order(word1, word2):
        # Extract unique common letters from both words
        unique_common1 = []
        for letter in word1:
            if letter in word2 and letter not in unique_common1:
                unique_common1.append(letter)
        
        unique_common2 = []
        for letter in word2:
            if letter in word1 and letter not in unique_common2:
                unique_common2.append(letter)
        
        # Check if the order of unique common letters is the same
        return unique_common1 == unique_common2


    percentage = common_letter_percentage(word1, word2)
    syllables_word1 = count_syllables(word1)
    syllables_word2 = count_syllables(word2)
    order_match = common_letters_in_order(word1, word2)
    
    return round(percentage, 2), syllables_word1, syllables_word2, order_match

# Example usage
# word1 = "Star"
# word2 = "Setare"
# result = word_analysis2(word1, word2)
# print(f"w1: {word1}, w2: {word2} >> res: {result}")  # Expected True for order

word1 = "caravan"
word2 = "karevan"
result = word_analysis2(word1, word2)
print(f"w1: {word1}, w2: {word2} >> res: {result}")  # Expected False for order



def outer_func(n1, n2):
    def inner_one(n1, n2):
        return(n1 + n2)
    
    def inner_two(n1, n2):
        return(n1 * n2)
    
    def inner_three(n1, n2):
        return(n1 - n2)
    

    addition = inner_one(n1, n2)
    multip = inner_two(n1, n2)
    subtrac = inner_three(n1, n2)

    return(addition, multip, subtrac)


print(outer_func(12, 6))


def test_lambda():
    addr = [
        {"street": "Delta Rd", "postcode": "KT4 7HP", "doornum": 9},
        {"street": "Contsford Avenue", "postcode": "KT3 7EU", "doornum": 3},
        {"street": "Delta Rd", "postcode": "KT4 7HP", "doornum": 11},
        {"street": "Earls Court", "postcode": "SW5 0AU", "doornum": 24},
        {"street": "Allan Close", "postcode": "KT3 5ET", "doornum": 3}
    ]

    addr.sort(key=lambda addr_sorted: addr_sorted['street'])

    for addr_sorted in addr:
        print(f"{addr_sorted['street']}, {addr_sorted['postcode']}, {addr_sorted['doornum']}")


test_lambda()