def rec_coin(target, coins):

    min_coins = target

    # base case if target is in coins to change
    if target in coins:
        return 1

    else:

        for i in [c for c in coins if c <= target]:

            num_coins = 1 + rec_coin(target - i, coins)

            if num_coins < min_coins:

                min_coins = num_coins

    return min_coins

# print "Min num of coins to change: %d" % rec_coin(63, [1, 5, 10])


def rec_coin_dyn(target, coins, known_result):

    min_coins = target

    # base case if target in coins
    if target in coins:
        known_result[target] = 1
        return 1

    # check if we already now how much coins we need
    elif known_result[target] > 0:
        return known_result[target]

    # calculate amount of coins
    else:

        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_dyn(target - i, coins, known_result)

            if num_coins < min_coins:
                min_coins = num_coins
                known_result[target] = min_coins

    return min_coins

# print "Min num of coins to change dyn: %d" % rec_coin_dyn(63, [1, 5, 10, 25], [0] * 64)


def coin_dyn(target, coins, min_coins):

    for cents in range(target + 1):

        num_coins = target

        for i in [c for c in coins if c <= target]:

            if min_coins[target - i] + 1 < num_coins:

                num_coins = min_coins[target - i] + 1

        min_coins[target] = num_coins

    return min_coins[target]

print "Min num coins without rec: %d" % coin_dyn(63, [1, 5, 10, 25], [0] * 64)