def string_to_bits(words):
    vowel = {'a', 'e', 'o', 'ü', 'u', 'ö', 'ı', 'i'}
    bits = ''
    for i in words:
        bits += '1' if i in vowel else '0'
    return bits


def syllable_word(word):
    syllable_list = []
    syllable = ""
    bits = string_to_bits(word)
    continue_count = 0
    for i, char in enumerate(bits):
        if continue_count > 0:
            continue_count -= 1
            continue
        if char == '0':
            syllable = syllable + char
        elif char == '1':
            # Ünlüden sonraki kısım önemli, ayırılacak olan hecelere karar verilecek.
            syllable = syllable + char
            x = len(syllable)
            if bits[x: x+3] == '001':  # Yan yana gelen 2 ünsüz
                syllable_list.append(word[:x+1])
                word = word[x + 1:]
                bits = bits[x + 1:]
                syllable = ''
                continue_count += 1
            elif bits[x:x+3] == '000':  # 3 tane ünsüz yan yana
                syllable_list.append((word[:x+2]))
                word = word[x+2:]
                syllable = ''
                bits = bits[x + 2:]
                continue_count += 2
            elif bits[x:x + 2] == '01':  # 2 ünlü arasında ki ünsüz
                syllable_list.append(word[:x])
                bits = bits[x:]
                word = word[x:]
                syllable = ''
            elif bits[x:x+1] == '1':  # 2 ünlü arka arkaya
                syllable_list.append(word[:x])
                bits = bits[x:]
                word = word[x:]
                syllable = ''
            elif bits[x:x+1] == '0':  # kelime sonu ünsüz
                syllable_list.append(word[:x+1])
                bits = bits[x:]
                word = word[x:]
                syllable = ''
            else:  # bütün elifleri gezip patern yoksa o elimizde ki kendi bir hece
                syllable_list.append(word[:])
                bits = bits[x:]
                word = word[x:]
                syllable = ''
    print(syllable_list)


entered_input = "kaan"
syllable_word(entered_input)

