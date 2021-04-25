# alGO

Go had remained for a number of years as a final frontier of classical board games for machine learning researchers to conquer. In this repository i will apply a number of historical techniques and build up to the same models that are used today to beat world champions. Games are great because they simplify the the complexities of real life, so all the attention can be on the algorithm. 

Why is go so hard to model? In the context of tree search, the branching factor for chess is about 30, the first turn for example gives the user only 20 legal branches to consider. By comparison, go's first move branching factor is 361! A mote carlo esc approach would need to evaluate 4 billion positions just to find the optimal first four moves. As we will see with the older and less technical models; relying on raw compute wont cut it, we need to embed 'intuition' as decisions need to be made with incomplete sequences. 


### Assumptions
- Area scoring rather than territorial.
- Komi, white gets 7.5 under area scoring for going second.
- Self Capture is prohibited
- Benchmarking will be done using other go models to estimate the ranking the model would be granted in professional go setting.
- Some more naive Versions will use hardcoded rules to prevent the bot from filling its own eyes (V1)

## Version 1: Naive 

Starting with the most basic, version 1 is simply a naive bot that selects a random legal move with only a hard coded helper to prevent it from taking its own eyes. This represents our zero baseline that every future version should easily beat. Here is a gif to represent two version one algorithms playing against each other in real time. 

You can run this bot vs bot simulation yourself using version-1/bot_v_bot.py, if you want to test your skills against this bot you can use human_v_bot.py to play against it on the command line! **(Watch out this version does not have error handling so playing an illegal move will end your game)**

<img src="https://github.com/MatthewBoyce/alGO/blob/main/images/v1.gif?raw=true"/>

## Version 2: Tree Search (Mini/Maxing)

Go like chess is a deterministic perfect information game, where one move is theoretically the 'best'. Min/maxing is quite a simple concept, your trying to get the best score you can while assuming your rival is trying is trying to minimize your score. Assuming you both have the same knowledge; ie the rival can calculate their own optimum move, what is the best move for you to make?

Roughly a minmax tree search algorithm  means looping over every possible legal move and applying the following hursitics:

1. See if you can win on the next move. If so, play that move.
2. If not, see if your opponent can win on the next move. If so, block that.
3. If not, see if you can force a win in two moves. If so, play to set that up.
4.  If not, see if your opponent could set up a two-move win on their next move.

For a game like tic-tac-toe, this is easy since you can fully iterate through all the nested branches of the tree, however there are too many possibilities to compute for Go. Since running the algorithm would take several years even on on a super computer, the branches need to be pruned. This can be done both on a with and depth basis.

Width - Alpha beta pruning, evaluate and put a score against the outcome of each decision on the game state. Use this score to rule out branches early on and only search through the higher scoring outcome branches. 

Depth - Evaluate how strong your position is based on percentage of net pieces you control and use this to determine how many layers you need to travel down.



