def candy(ratings):
    length = len(ratings)

    if length < 2:
        return length

    candies = [1 for _ in ratings]

    for i, r in sorted(enumerate(ratings), key=lambda x: x[1]):
        for n in [i-1,i+1]:
            if 0 <= n < length:
                if ratings[n] < ratings[i] and candies[n] >= candies[i]:
                    candies[i] = candies[n] + 1

    return sum(candies)
