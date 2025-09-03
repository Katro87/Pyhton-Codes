def reverse(s):
    return s[::-1]

print(reverse("Hello my name is sufyan"))
def reverse(s):
    reversed_word = []
    for word in s.split():
        reversed_word.append(word[::-1])
    return reversed_word


print(reverse("Hello my name is sufyan"))

