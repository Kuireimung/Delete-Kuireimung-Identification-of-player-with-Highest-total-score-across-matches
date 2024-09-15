
scores_dict = {
    'match1': {'player1': 57, 'player2': 38},
    'match2': {'player3': 9, 'player1': 42},
    'match3': {'player2': 41, 'player4': 63, 'player3': 91}
}
def orangecap(d):
    player_scores = {}


    for match_scores in d.values():
        for player, score in match_scores.items():
            player_scores[player] = player_scores.get(player, 0) + score


    top_player = max(player_scores, key=player_scores.get)
    top_score = player_scores[top_player]

    return (top_player, top_score)



result = orangecap(scores_dict)


print(f"The player with the highest total score is {result[0]} with the score of {result[1]}.")
