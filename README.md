# specific-holdings

Consider a certain financial commodity. The phrase “buy low sell high” is commonplace but ambiguous. How “low“ should trigger a buy? How much to buy? How “high” triggers a sell? How much of the commodity should be sold? These are questions that can be potentially addressed by examining parameters associated with each action. 

**How can we define a rule for commodity transactions that will maximize our returns?**

Define these parameters and a measurable outcome, such as the proportion of increase in holdings after a set amount of time (or as a function of time) or the probability that the holdings have increased after a set amount of time. The problem is therefore to determine the parameters that maximize the measurable outcome as a function of the model parameters.

As a starter example to help understand the problem and get a feel for its feasibility, pick any model of a financial commodity (ARMA, etc) and choose numerical values for the model parameters and starting price. Suppose one share is held. Fix a rule for buy and sell triggers, maybe like one that you’ve already used in your simulations. At the sell trigger, ask sell a proportion $\Delta _s$ of the value. At the buy trigger, buy an amount of the commodity equal to the total of what was earned from the last consecutive sells. Set an amount of time to let the process run. Find $\Delta$ that maximizes the average holdings at the end of the set time. The average would be found by averaging the resulting holding values from a large number of simulations.