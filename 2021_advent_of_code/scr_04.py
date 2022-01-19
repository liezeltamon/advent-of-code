import numpy as np


bingocrd_arr = np.genfromtxt("input_04.txt", skip_header=2)
bingocrd_arr = np.reshape(bingocrd_arr, (100, 5, 5))
print(np.sum(np.isnan(bingocrd_arr)))

num_drawn = np.genfromtxt("input_04.txt", delimiter=",", max_rows=1)

num_drawn = num_drawn + 1
bingocrd_arr = bingocrd_arr + 1

print(np.min(bingocrd_arr))

won_card_all = np.array([-1])
won_round = 0

for num in num_drawn:

    bingocrd_arr[bingocrd_arr == num] = 0

    row_sum = np.sum(bingocrd_arr, axis=2)
    col_sum = np.sum(bingocrd_arr, axis=1)
    sum_rowcol = np.array([row_sum, col_sum])

    won_card = np.where(sum_rowcol == 0)[1]
    won_card_round = np.setdiff1d(won_card, won_card_all)
    is_no_winner = won_card_round.size == 0

    won_card_all = np.union1d(won_card_all, won_card_round)

    if is_no_winner:
        next
    elif not is_no_winner:

        won_round = won_round + 1

        if won_round == 1:
            first_won_card = bingocrd_arr[won_card_round, :, :]
            first_won_drawn = num

        last_won_card = bingocrd_arr[won_card_round, :, :]
        last_won_drawn = num

    else:
        print("Unexpected case.")

ans_cards = (first_won_card, last_won_card)
ans_drawns = (first_won_drawn, last_won_drawn)

for i in range(len(ans_cards)):

    # Need to subtract appropriately cause I added one to all bingo card and drawn numbers so I can use 0 to mark bingo card

    num_non0 = np.sum(ans_cards[i] > 0)
    winner_score = (np.sum(ans_cards[i]) - num_non0)
    winner_score = winner_score * (ans_drawns[i] - 1)
    print(i + 1, " winning score: ", winner_score)
