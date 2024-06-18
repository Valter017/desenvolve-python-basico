import string

def remove_punctuation_and_whitespace(text):
    return ''.join(char for char in text if char not in string.punctuation + ' ').lower()

def is_palindrome(text):
    clean_text = remove_punctuation_and_whitespace(text)
    return clean_text == clean_text[::-1]

def main():
    while True:
        frase = input('Digite uma frase (digite "fim" para encerrar): ').strip()
        if frase.lower() == 'fim':
            break
        if is_palindrome(frase):
            print(f'"{frase}" é palíndromo')
        else:
            print(f'"{frase}" não é palíndromo')

if __name__ == "__main__":
    main()
