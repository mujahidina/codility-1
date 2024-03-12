
def solution(A, D):
    balance = 0
    fees = 5
    cards = {}

    for amount, date in zip(A, D):
        month = int(date.split('-')[1])
        if amount >= 0:
            balance += amount
        else:
            balance += amount
            if month in cards:
                cards[month].append(amount)
            else:
                cards[month] = [amount]

    for month in range(1, 13):
        if month in cards and len(cards[month]) >= 3 and sum(cards[month]) >= -100:
            balance += fees * (len(cards[month]) - 3)
        else:
            balance -= fees

    return balance

print(solution([100, 100, 100, -10], ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']))
print(solution([180, -50, -25, -25], ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-31']))

