def check_rhythm(poem):
    lines = poem.split()
    syllables = []

    for line in lines:
        words = line.split('-')
        count = 0
        for word in words:
            count += count_syllables(word)
        syllables.append(count)

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(word):
    vowels = "УуЕеЫыАаООоЭэЯяИиЮю"
    count = 0

    if word[0] in vowels: 
        count += 1

    for i in range(1, len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            count += 1

    return count

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)