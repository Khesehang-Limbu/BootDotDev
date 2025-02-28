"""
Even Teams
Fantasy Quest is having a problem where Battleground teams are uneven when the match begins. We need a function that will correctly split the two teams evenly.

Assignment
Complete the split_players_into_teams function. Use a slice with a "step" to create two new lists from the players list:

even_team should have the players with even-numbered indexes.
odd_team should have the players with odd-numbered indexes.
Return even_team and odd_team in that order. Be careful not to assign the wrong values to these variables!
"""

def split_players_into_teams(players):
    return players[::2], players[1::2]
