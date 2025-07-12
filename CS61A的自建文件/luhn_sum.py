def luhn_sum(card_number):
    if card_number < 10:
        return card_number
    else:
        new_card_number = card_number // 10
        return luhn_sum_double(new_card_number) + card_number % 10
    
def luhn_sum_double(card_number):
    if card_number < 10:
        return (card_number * 2) // 10 + (card_number * 2) % 10
    else:
        new_card_number = card_number // 10
        return luhn_sum(new_card_number) + (card_number % 10) * 2 // 10 + (card_number % 10) * 2 % 10
    
print(luhn_sum(138743))