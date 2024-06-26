# 8) Palindrome. Is string a palindrome? A palindrome is a word which reads the same backward as forwards.
# Two Pointers, String
# “ololo” ⇒ Yes
# “cafe” ⇒ No


def is_palindrome(word: str) -> bool:
    word = [c.lower() for c in word if c.isalnum()]
    return word == word[::-1]


def is_palindrome2(word: str) -> bool:
    word = [c.lower() for c in word if c.isalnum()]
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True


def main():
    print('ololo', is_palindrome2('ololo'))
    print('cafe', is_palindrome2('cafe'))


main()
