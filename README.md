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

<img src="https://github.com/MatthewBoyce/alGO/blob/main/images/v1.gif?raw=true"/>



