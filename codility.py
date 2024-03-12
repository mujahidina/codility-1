def solution(A, D):
    # Initialize balance and fees
    balance = 0
    fees = 5
    # Dictionary to keep track of cards by month
    cards = {}

    # Iterate through transactions
    for amount, date in zip(A, D):
        # Extract month from date
        month = int(date.split('-')[1])
        # If amount is positive, add it to balance
        if amount >= 0:
            balance += amount
        else:
            # If amount is negative, add it to balance and track it in cards dictionary
            balance += amount
            if month in cards:
                cards[month].append(amount)
            else:
                cards[month] = [amount]

    # Iterate through each month
    for month in range(1, 13):
        # Check if there are at least 3 transactions in the month and total amount is greater than or equal to -100
        if month in cards and len(cards[month]) >= 3 and sum(cards[month]) >= -100:
            # If conditions met, apply fees for transactions beyond the first 3
            balance += fees * (len(cards[month]) - 3)
        else:
            # If conditions not met, apply fees for the month
            balance -= fees 

    return balance


#TEST CASES


print(solution([100, 100, 100, -10], ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']))
print(solution([180, -50, -25, -25], ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-31']))
print(solution( [1, -1, 0, -105, 1],  ['2020-12-31', '2020-04-04', '2020-04-04', '2020-04-14', '2020-07-12']))

