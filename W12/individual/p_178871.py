def solution(players, callings):
    position = {player: i for i, player in enumerate(players)}

    for calling in callings:
        index = position[calling]

        players[index], players[index - 1] = players[index - 1], players[index]

        position[players[index]] = index
        position[players[index - 1]] = index - 1

    return players
