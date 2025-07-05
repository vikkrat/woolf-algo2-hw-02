from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def dp(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = 0
        best_cut = []
        for i in range(1, n + 1):
            if i <= len(prices):
                profit, cuts = dp(n - i)
                profit += prices[i - 1]
                if profit > max_profit:
                    max_profit = profit
                    best_cut = cuts + [i]
        memo[n] = (max_profit, best_cut)
        return memo[n]

    profit, cuts = dp(length)
    return {
        "max_profit": profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }
