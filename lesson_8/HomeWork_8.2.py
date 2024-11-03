def is_palindrome(s):

    text_without_punctuation = ''.join(char.lower() for char in s if char.isalnum())

    return text_without_punctuation == text_without_punctuation[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
