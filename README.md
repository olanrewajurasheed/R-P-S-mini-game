[Rock-Paper-Scissors]
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.

A brief summary:

If the two players choose the same “character” it’s a tie, and the game repeats.
    {Rock beats Scissors
    Paper beats Rock
    Scissors beats Paper}
In this version, one player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player). 

NOTE:
"R" for "rock", 
"P" for "paper", 
"S" for "scissors".

When the program is run, the user is ask to pick an option between ("R", "P" or "S")
If user input is invalid (not amongst our options), an error is printed , and ask for their input again (should be a loop)
Both player's moves are in the format: `Player (Rock) : CPU (Paper)`

By checking both player's moves: 
If there is a winner, the winner is printed , and the program ends. 
If it's a tie (the computer and player pick the same move), the game will be restarted. 