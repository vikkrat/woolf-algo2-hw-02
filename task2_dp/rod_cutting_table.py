from typing import List, Dict

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    solution = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if j <= len(prices):
                if dp[i] < dp[i - j] + prices[j - 1]:
                    dp[i] = dp[i - j] + prices[j - 1]
                    solution[i] = solution[i - j] + [j]

    cuts = solution[length]
    return {
        "max_profit": dp[length],
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }
