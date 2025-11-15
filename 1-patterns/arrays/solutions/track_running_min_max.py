def buy_and_sell_stock_once(prices: list[float]) -> float:
    """
    Pattern: Track Running Min/Max

    Goal: Maintain best value seen so far while iterating

    When to use: Finding optimal subarray, max difference, best transaction
    Problems that use it: Stock profit, max difference, longest subarray
    Key insight: Update running extremum and result independently each iteration
    """
    min_price_so_far = float('inf')
    max_profit = 0.0

    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit
