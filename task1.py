def encrypt(text, n=1):
    if n <= 0 or text is None or text == '':
        print(text)
    else:
        text = text.lower()
        t = 1
        while t <= n:
            bits = len(text)
            even_bits = ''
            odd_bits = ''
            for i in range(0, bits):
                if i % 2 == 0:
                    even_bits += text[i]
                else:
                    odd_bits += text[i]
            t += 1
            text = odd_bits + even_bits
        return odd_bits + even_bits


word = encrypt("Abcdefghij", 2)
print(word)


def decrypt(encrypted_text, n=1):
    if n <= 0 or encrypted_text is None or encrypted_text == '':
        print(text)
    else:
        text = encrypted_text.lower()
        bits = len(text)
        t = 1
        while t <= n:
            if bits % 2 == 0:
                firs_half = text[int(bits / 2):]
                second_half = text[: int(bits / 2)]
            else:
                firs_half = text[int(round(bits / 2)):]
                second_half = text[: int(round(bits / 2))]
            result = ''
            i = 0
            while len(result) < bits:
                result += firs_half[i]
                try:
                    result += second_half[i]
                except:
                    pass
                i += 1
            text = result
            t += 1
        print(result)

decrypt(word, 2)
