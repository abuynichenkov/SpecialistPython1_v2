# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    if len(ticket_str) != 6:
        return False
    first_half = ticket_str[:3]
    second_half = ticket_str[3:]
    return sum(map(int, first_half)) == sum(map(int, second_half))


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
