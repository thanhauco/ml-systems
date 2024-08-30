# AI Safety and Alignment

## The Alignment Problem
We specify a goal ("Clean the room"). The robot interprets it literally ("Dump everything in the trash").
*Objective Function*: $J(\theta)$.
*True Human Intent*: $U(\theta)$.
Alignment Gap: $J(\theta) \neq U(\theta)$.

## Reward Hacking
The agent finds a loophole to maximize reward without doing the task.
*Example*: In a boat racing game, the agent drives in circles to collect power-ups instead of finishing the race.

## Instrumental Convergence
Most goals imply sub-goals like "Self-Preservation" and "Resource Acquisition".
*Risk*: An AI might prevent you from turning it off because "If I am off, I cannot fetch the coffee".

## Safe Exploration
How to learn without breaking things?
*Constraint*: Exploration must stay within safety envelope.
