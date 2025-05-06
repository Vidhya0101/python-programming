def reverse_number(number):
    original_number = number
    reverse = 0

    for _ in str(number):
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    print(f&quot;Original Number: {original_number}&quot;)
    print(f&quot;Reversed Number: {reverse}&quot;)

reverse = 6789
reverse_number(reverse)
