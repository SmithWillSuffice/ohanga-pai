---
title: "Ōhanga Pai Projects Overview"
description: ""
date: 2019-10-31
lastmod: 2019-10-31
cover: ""
coverAlt: ""
toc: true
katex: true
tags: []
---

## Overview of the Projects

### Asset Exchange Models

These are pretty simple models in the class of "[econophysics](https://en.wikipedia.org/wiki/Econophysics)".
They are agent-based models, and show the basic wealth distributions that occur generically given some rules for how entities (individuals or units like small firms) exchange assets.

These models are great for thinking about fair distribution policies, which at a government regulatory level means fiscal policy. 
The models show that highly unfair wealth distributions naturally occur even when asset exchanges are uniform and random. 
This illustrates Pareto dynamics, or more colloquially *the rich get richer* and the poor get poorer (in relative terms).

The interest in these models is that they show that even before accounting for political and social power relations, just raw asset exchange can ruin people's lives, through no fault of their own and no fault of the super rich. 
The existence of wealthy powerful people in the real world can only make things worse than these ideologically neutral asset exchange dynamics.
"Worse," that is, absent some sort of supernatural altruism and charity from the super rich. 
(When has human civilization ever witnessed such sociology?)

They are *not* good models for real economic analysis which concerns production, energy, employment and price stability.

### Minksy Models

These are ordinary differential equation (ODE) models of realistic monetary economic systems. 
They chunk an economy into separate sectors, and use behavioural models to model the microeconomics of individuals and firms. 
Because they are macroeconomic models (chunked sectors) they accurately account for sectoral balances, and hence provide a brilliant analysis of economic class and distribution, but sacrificing *microeconomics of firms* details.

We use time series ODE simulations, which is the proper way to model an economy as a dynamical system. 
There is thus no assumption of equilibrium in markets.

We model money, asset and labour markets, as roughly three homogenous types of market. However, for some analysis more sophistication is required, for example, three basic generalizations are,

* **Two price** models --- financial assets (stocks, bonds, forex trading, non-owner occupied real estate) are in the modern world only very loosely coupled to pricing for real commodities (water, food, electricity,...). A decent macroeconomic model should thus account for at least two general price levels. (A third price is labour, the nominal wage rate, but Keen-Goodwin models already have separate governing equations for wages.)
* **Four interest rate** models --- private banks offer a spread on top of central bank rates. So at a minimum a proper monetary model should use four interest parameters, two for the commercial bank rates (governing credit money and term deposits) and two for government bonds (governing fiat currency operations).
* **Capitalism** models --- these are models where the Private sector is split into three sectors, Banks, Firms and Household, or if you prefer, Bankers, Capitalists and Workers. This is the proper way to conduct a modern Marxist analysis of the class struggle.

If you have enough computing power then of course defining further class structure can also be valuable for more nuanced class analysis. 
We all know there is a big difference between households who are in credit to their bank and households who are in debt. 
If left alone (laissez faire policy) the wealthy household will get wealthier and the indebted households will get poorer --- through no fault of their own!

#### What about DSGE? 

Note that we have absolutely no interest in neoclassical and New Keynesian [DSGE models](https://arxiv.org/pdf/2210.16224) (dynamic general stochastic equilibrium) --- because those are garbage. 
GIGO applies. 
You cannot realistically model a complex dynamical system like a whole economy using assumptions of equilibrium, or pretending equilibrium attains and just gets perturbed by some stochastic processes. 
Such thinking is retarded, and unnecessary. 

Historically the reasons mathematical economics made assumptions of equilibrium supply and demand was because no one had the computer power to model non-equilibrium dynamics. 
In the 1970's that all changed, and while physicists learned to use non-linear dynamical system models, the classical economists did not, for the most part, hence the continued futile and vain work on the utterly bogus DSGE models.

As evidence, which our [philosophy pages](/questions/) might discuss, the [DSGE models](https://arxiv.org/pdf/2210.16224) have no way to predict debt-deflation crashes, like the 2008 GFC, or the Great Depression crash of 1929. 
Proper time evolution dynamical models by contrast can predict financial crashes, or anticipate their onset. 
Any decent macroeconomic model must be capable of predicting such financial crashes, this is why DSGE has to be completely rejected, it is a failed paradigm, and we know why it fails. 
So why do mainstream economists and central bankers still use them? (This is a bit of a mystery, because they're not stupid people, the answer for resolving this mystery is sociological and ideological.)


## System Dynamics Models

The Minksy models are a class of non-linear dynamical system, or System Dynamics (SD) models. 
They can exhibit chaotic dynamics, or what is known in popular cultures as [The Butterfly Effect.](https://en.wikipedia.org/wiki/Butterfly_effect)

### Why Macro Matters

These SD models are what policy people should study, because the microeconomics of firms and households are only loosely coupled to large scale macroeconomics due to failures of composition. 

**Failure of composition** means *the whole is more than the sum of it's parts*.

The reason microeconomics agents do not compose or scale up to macroeconomics is due to several critical factors:

1. most national (single legislature) economies use a single currency (at least outside the eurozone),
2. those single currency regions are regulated by a currency monopolist (otherwise known as "the government")
3. the existence of a currency and legislative monopoly, which are the same institution, means endogenous money analysis fails, and so microeconomics cannot be scaled up to macro.

I place "the government" in scare quotes above because this phrase is prone to being misunderstood. The Government means the entire government system, which for a monetary economy means the legislature (Parliament), the Executive (Ministries, Prime Ministers and Presidents), the Treasury and the Central Bank. 
No matter who owns the Central Bank furniture, it is still a branch of the consolidated government, it is required by law (in every country on Earth today) to do the bidding of the Parliament and to cooperate daily with the Treasury.

The Treasury make the instructions for all payments authorized by Parliament, and the Central Bank runs the banking and payments clearing system which makes those payments. 
All commercial bank reserves are spreadsheets owned by the Central Bank.
(In the days before computers they were ledger books.)

As with any agency of government, the Parliaments may grant their agents some autonomy and independence, but this is not granted freely. 
The mythical independence of central bankers is precisely that, a myth. 
If the Parliament desires a zero interest rate bound, then it can always instruct Its central bank to make it so. 
This is true even for the UK and USA where central bank independence is supposedly a sacred mantra.  It is a false mantra. 
How do we know so? *Government cheques never bounce.*

If the central bank refuses to issue payments on behalf of a Parliament desiring to provision the public service, those central bankers will soon be fired. 
(But of course we do not know this for a fact, because the central banks have never refused to make the payments${}^\ast$, and they always can, because they are the monopoly issuers of the state's currency unit --- they cannot run out of money, they issue it by fiat).

${}^\ast$ There was that time the Russian central bank turned off their lights. That was a default. However, as soon as they realized they issued rouble by keystroke the lights came back on. So this can be filed under "the exception proves the rule."
The Argentina and Mexican debt defaults were in foreign currencies, not their own currency, so not the same thing either. 
MMT Short Lesson: no government *needs* to borrow a foreign currency, not ever. 
They might borrow in order to manipulate their exchange rate, but all that does is change domestic distribution (who gets to mow lawns, who gets to play golf).

#### Summary

A simpler way to say all that is that the existence of a single currency monopoly power means a single currency region is inherently macroeconomic, the macro dictates the micro in several ways, so it is inherently a top-down system (with some elements of bottom-up, if there is a semblance of a democracy). 
For more of this sort of theory of micro versus macro in economics see the [philosophy section](/ohanga-pai/questions/) or [Professor Steve Keen\'s work](https://doi.org/10.1080/09538259.2020.1810887) and [here](https://ssrn.com/abstract=3466606), and [here.](https://www.rrojasdatabank.info/Keen49.pdf)



[Next chapter (TBD)](./)  
[Previous chapter (Projects Introduction)](../0_introduction_to_projects)  
[Back to Empirical Pages](../)
