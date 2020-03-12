str = 'How are you John'
print(len(str))

def count_letter(str):
    count = 0
    for i in range(len(str)):
        if str[i].isalpha():
            count += 1
    return count
print(count_letter('How are you John?'))
