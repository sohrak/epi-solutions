from typing import List

def buy_and_sell_stock_once(prices: List[float]) -> float:
    profit = 0.0

    # First cut solution, but is O(N^2).
    # for i in range(len(prices) - 1):
    #     delta = max(prices[i + 1:]) - prices[i]
    #     if delta > profit:
    #         profit = delta

    # Track min price instead of finding max price, which is O(N).
    min_price = prices[0]
    for i in range(1, len(prices)):
        # Check profit with previous minimum price
        profit = max(profit, prices[i] - min_price)

        # Check if current price is the new minimum
        min_price = min(min_price, prices[i])
        
    return profit
