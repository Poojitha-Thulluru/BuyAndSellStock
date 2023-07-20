def max_profit(prices: list) -> int:
    if not prices or len(prices) == 1:
        return 0
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The maximum possible profit is : ", max_profit(num_array))
except ValueError:
    print("Invalid Input, Please enter only integer")
