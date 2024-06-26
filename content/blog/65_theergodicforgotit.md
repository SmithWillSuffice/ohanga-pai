---
title: "The Ergodic Forgot-it"
weight: 66
date: 2024-04-25
draft: false
katex: true
disableTitleSeparator : true
toc: true
---

I found a nice lunch-break series on youtube from some economics nerds 
[here](https://www.youtube.com/playlist?list=UULFJG8N5P1RFX29JTKt_6R21A)
on [ergodicity in economics](https://www.youtube.com/playlist?list=UULFJG8N5P1RFX29JTKt_6R21A).
It is worth a few comments.

These are econophysics bros, but among the finance bro nerds, these guys 
seem to be of the decent variety. There is a trace of a hint of some level of 
concern for the plight of the poor in their work.

## Wealth Reallocation Models

There are many simple models for how financial wealth gets distributed. 
Unfortunately most are politically neutral or politically agnostic. So all 
are unrealistic. However, they are empirically accurate. How can that be?

Firstly, modelling macroeconomics is a lot like some aspects of statistical 
mechanics, where there can be phenomena akin to multiple realization: meaning 
more than one underlying dynamics or set of governing rules could determine 
the same qualitative macroscopic behaviour.

Secondly, in the real world governments do not behave as if they have a 
monopoly control of their own tax credits (aka. the currency) and so a lot of 
economic injustices occur due to plain ignorance --- massively tragic form of 
banal evil. If governments cause unemployment in the first place (as MMT shows) 
then a morally agnostic government operating according to quasi free market 
ideology --- welfare for the rich, rugged individualism for the poor --- 
will practically guarantee end results that are Pareto tailed --- the rich 
get richer.

The econophysics bros models capture such politically "agnostic" dynamics. 
Only the problem is they fail to realize this is political mismanagement on an 
epic and tragic scale. It is not agnosticism at all.

Sure, you might be justified in claiming absent a currency monopoly there 
would be some kind of free market, then those models become applicable. The 
result is a free market always evolves to extreme injustice --- highly 
unequal distribution of financial wealth. (Hence real wealth too, since 
financial wealth equates to real purchasing power. The more money (scorepoints) 
you can rake in from rentier activity, the more you can purchase without 
reduction in your hoard of financial scorepoints.

I am not claiming any particular reason the econophysics models seem to 
accurately account for real world wealth distribution, just pointing out some 
possible explanations.  But*one thing is for certain*: the real world data 
is drawn from nations that run MMT systems. So it is clear that governments 
in these nations have the operational ability to eliminate the Pareto tails 
and ensure fair & just wealth distributions. Meaning if politics were good, 
serving the public purpose, then the econophysics bro's 'models would be 
wrong.

That is really my main point today.

> The econophysics models might be correctly capturing some aspects of 
macroeconomic real-world dynamics, but the main point to make is that this 
does not mean the real world *should* be as it is: we could do much better.


### Negative $\tau$

The simple stochastic geometric Brownian motion model for wealth reallocation 
is definitely a politically agnostic model, so pretty disgusting. But that is 
because our political economy is pretty disgusting. Yes, for sure, all you 
Enlightenment nerds: human civilization has progressed for the good, in so 
many ways, but that does not imply we are at a stage of decent political 
economy. It just means all past human history where power elites have been 
found, it has been diabolically nasty and brutal.

In [Yonatan Berman’s model](https://www.youtube.com/watch?v=V7j4eO4Kbls&list=UULFJG8N5P1RFX29JTKt_6R21A&index=2&pp=iAQB) 
the main control parameter $\tau$ allows for interactions between individuals, 
and this is what allows the dynamics to become non-ergodic.

It is seriously important in the econophysics, because ergodicity is 
thought to be characteristic of the real-world under typical circumstances. 
The long time average of a distribution of wealth is the same as the average 
over all infinite possible ensembles.

((Why so seriously important? It is because these econophysics models are all 
about the statistical mechanics, so the statistical characteristics are the 
only thing they need to get right, so they need to get (non)ergodicity --- and 
other statistical characterizations --- right, if nothing else.))

Models where the time average does *not* equal the ensemble average are 
non-ergodic, and this is the real-world situation when there are increasing 
returns to wealth and decreasing returns to the poor. The Gilded Age, the 
Great Depression, and the Neoliberal era, are possible non-ergodic periods 
in our recent history, times when the rich got not only richer, but 
obscenely richer --- in relative terms.

The base model is *random multiplicative growth* --- which means the growth 
in wealth over a distribution is dominated completely by random exchange.
This is non-ergodic.

The first adjustment for reality is a reallocation term, with parameter $\tau$, 
which governs how one individual contribute aa fraction of their wealth every 
time period to a common pool, this pool is then split evenly between 
everyone.  The model is very simple,
$$
dx\_i = x\_i \left(\mu \\, dt + \sigma\\, dW\_i (t)\right) - \tau\left(x\_i - \braket{x}\_N\right)\\, dt
$$
The first term in  parentheses is the geometric Brownian random exchange 
effect, the second is the reallocation.


For simple analysis $\tau$ is taken to be the same for everyone, which means 
the amount of wealth put into the common pool is the same proportion of an 
individual's current wealth. The rich contribute more than the poor, but in 
equal percentages.

For $\tau>0$ people with wealth greater than the population mean 
$\braket{x}_N$ is a net contributor, while the poorer are net receivers.
This is the ergodic regime.

(Technically, the reallocation model is ergodic if $\tau > tau\_c$ for some 
threshold $\tau\_c$, but for a large enough population $\tau\_c \approx 0$.)

In the ergodic regime rescaled wealth converges in time. Although it still 
has a "disgusting" Pareto tail (technically an inverse $\Gamma$ distribution), 
it is at least telling us that government have a role to play in fairly 
redistributing nominal wealth. Why? Because in the real world everyone knows 
redistribution does not occur. The rich can afford tax evasion, and the poor 
not only have a tax burden but also tend to need to borrow from banks just to 
not starve --- through no fault of their own (why the hell are they being 
taxed? There is no good reason.)

In particular, the models show that in times when in the real world the 
effective $\tau <0$ are times of increasing return to the rich, when 
inequality soars. These are non-ergodic periods. It is pretty revealing to 
see the data estimates showing the periods in recent history where such 
instability occurs, the following screenshot is Barman's data.

{{< nonergodic_wealth_reallocation >}}

The light grey bands are the regions where $\tau <0$ for the USA, the 
non-ergodic regimes where wealth inequality grows and people with negative 
wealth arise.

For $\tau < 0$ the dynamics are non-ergodic. One interesting thing is that 
Berman characterizes this regime by the effect on the poorest:
> In this regime some individuals end up with *negative* wealth, even if all 
start with positive wealth.

The long neoliberal era period from 1980 to today where $\tau < 0$ is  as 
story of a new gilded age. Crushing for the poor and the working middle 
class. Boom times for the rentiers and grifters.

Currently then, under present government policy, pretty much across the world, 
we are in a terrible era of non-ergodic wealth allocation effects, $\tau < )$, 
and *_the reallocations are from the poor to the rich._*

What it also shows is that the default assumptions in mainstream economics: 
that reallocation is ergodic, are unjustified, and often downright invalid.
But that is the most mild criticism of mainstream economics. I mean... 
hells bells... everyone *knows* the political economy is unjust, we did not 
need a model to tells us this is due to non-ergodicity. Without incredible 
unheard of charity and altruism on a global scale, it'd be unjust even in the 
ergodic regimes, given present neoliberal policy dominance.


What more can be said?

Well I know: a helluva lot more. People need to know MMT. Governments need to 
know what the full policy space available to a monopoly currency issuer is, 
if only so they know their policy is designed to benefit the rich and crush 
the poor. The first step to denouncing neoliberalism is to know what the 
policy does and why the policy is stupid, at best, horrific class warfare 
at worst, tantamount to murder by government design or ignorance.

You cannot claim moral righteousness if you think there is no 
alternative.


## Interest Rate Effects

Although MMT scholarship is pretty clear in interest rate effects, it is 
not crystal clear, because the macroeconomics is highly non-linear and 
dynamical and non-linear. Interest rate have "perverse" effects, meaning they 
can be pro-inflationary (most oftne) but under some conditions can stifle 
effective demand.

The LSE EgodicityEcon group have a write-up where they advocate low interest 
rates, but I thought they offer an incorrect analysis, so I wrote this comment 
to them:

> Hey, in your write-up 
<https://ergodicityeconomics.com/2017/08/14/wealth-redistribution-and-interest-rates/> 
you get interest rates slightly wrong. Most loans are fixed rate, so lowering 
the interest rate does not help the poor too much, except to slow down 
inflation. High rates are one-to-one pro-inflationary through interest-income 
and forward price effects, given propensities of savers to spend and borrowers 
to save are empirically about equal. But in fact moderate inflation helps with 
a bit with fixed rate debt, since it means higher nominal income servicing a 
fixed rate debt. It still sucks that most lower income families in debt have 
to also pay higher CPI prices, but nevertheless, if they stay afloat a moderate 
rate of inflation helps them pay off fixed rate debts faster. Which means a 
higher interest rate tomorrow helps them to pay off past lower fixed rate debt.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The more serious inequality issue is with debts that cannot be repaid out of income flow.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Debts that cannot be paid should be 
forgiven, since in the macro they are a drag on effective demand or 
currency circulation, and we all know healthy effective demand is a healthy 
economy. Debts that can be repaid can be serviced out of income flow. That 
suggests decent wages buttressed by a Job Guarantee wage floor is the superior 
policy to ineffective monetary policy.  It is called fiscal dominance.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Yeah, central bank interest rates should 
be permanent zero (ZIRP) and this is non-inflationary, once you understand the 
source of the price level. Chartered banks can always operate for a profit 
from the spread rate, and they always do, they can make loans regardless of 
the CB rate. The constraint on bank credit is the number of credit-worthy 
borrowers. Banks do not lend reserves or deposits, they issue credit simply 
by marking-up the customer's bank account, the currency is created *ex nihilo*, 
in receipt of a promissory note to repay (also in the form of a credit card 
agreement). The licensed software operationally does not permit a bank to 
lends reserves or deposits.  Moving around deposits is what non-bank trusts 
need to do, since they do not have access to the legal means to create the 
currency *ex nihilo*, if they tried they'd be jailed for counterfeit. Chartered 
banks do not operate like this, they have a license to create the currency 
*ex nihilo* by computer account entries (albeit with severe penalties for 
fraudulent issuance --- they do need to find or "generate" a 
credit-worthy borrower).   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Guess what helps create more 
credit-worthy customers? --- a higher CB rate, since the CB/Treasury rate is 
essentially a basic income scheme: 
*_basic income but only for people who already have money in proportion to how much money they already have._*".

Follow-up:  
> As for folks who fear forgiving debts can lead to instability and rampant 
inflation, let me just say they are ignoramuses. Effective demand has never 
been a *_cause_*  of hyperinflation (the causation goes the other way, with 
usually war reparations, massive corruption, or severe natural disasters the 
cause), and moderate inflation is a good thing --- it erodes the purchasing 
power of hoarded wealth, encourages more circulation and reduces the burden of 
past debt, provided wages go with. The way to get wages "going with" is via 
Job Guarantee wage floor. The CB sets the interest rate floor by votes, the 
Parliament must set the wage floor, also by a vote. There is no market force 
obstacle at play for a monopoly currency issuer, unless the politicians 
falsely act as if there is market pressure. They can tell the bond traders 
to pi55 off. The government does not need to borrow it's own fiat currency.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tax returns and bonds do not finance the 
government. Taxes help resource the government in *_real terms_* --- the 
tax liability generates demand for the otherwise worthless currency. Tsy Bonds 
are an interest rate maintenance operation, an asset swap, not a borrowing 
operation.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;And the discipline on banks has to be 
understood. It never works out if the liability side is chosen as the place 
for discipline. For starters no customers know the risk, to think they do is 
laughable. The proper place for discipline is on the asset side. The proper 
policy is to give banks unlimited overdraft at the CB, to ensure payments 
clearing, and discipline the banks on the asset side. You tell banks only 
what they can do, and that is to (1) run the payments clearing, (2) assess 
credit worthiness. Do not allow them anything else. Bankers are dangerous 
animals and need to be kept in cages.

Quite a bit of channelling Mosler the GOAT there, which I will always do 
given half a chance.



### All We Need is a Warp Drive

I want to return to my main point:  
_The econophysics models might be correctly capturing some aspects of 
macroeconomic real-world dynamics, but the main point to make is that this 
does not mean the real world *should* be as it is: we could do much better._

And we can do better without any heavy-handed social engineering or forced 
communism or the like. We can do better simply if, **(a)** governments 
understand they have at least tow unique and powerful monopoly instruments 
(the legal and the monetary system, the former includes military and police 
power). And **(b)** we have real serious democratic control of our 
governments, meaning they bend to "the people's" will, not to the will of 
the oligarchs.

When I write, "simply if" please know that I realize this does not mean 
politically or sociologically simple. It means operationally simple. The 
politics messes you up. "All we need is the correct moral and ethical 
political will to do good...", is a phrase a lot like interstellar travel 
plans: "All we need is a Warp drive...".

However, I am not a pessimist nor nihilist. We can find this macroeconomics 
"warp drive". It is not a scifi fantasy. That is because the macroeconomics 
warp drive is not a physical thing, it does not have to be materially 
engineered. It is a spiritual reality, it is love for other people, compassion, trustworthiness, humility, compassion, justice, mercy, forgiveness, wisdom.
That is our political economy warp drive.

It costs nothing material to get it. It costs suppression of ego and greed.
Which is why it seems incredibly hard to get. No one can legislate better 
morality. Moral and ethical transformation has to be learned, nurtured, grown, 
and fostered with the metaphorical water of wisdom and kindness.


## Power

This is something everyone who learns MMT eventually comes to appreciate. 
MMT is a necessary step in the battle, but it is only a first step. Yeah, it 
can be taken in parallel with other steps.

But once you realize a government has amazing monopoly powers, you realize the 
magnitude of the task ahead. Those wielding that power fail to acknowledge MMT, 
and hide their wilful or innocent ignorance behind veils of "let the markets 
do their magic" parables. Such market ideology is in fact anti-democratic.
But it gets endlessly paraded as a manifestation of democracy and freedom.

The task for pursuit of greater justice is thus truly immense.

We are talking biblical in scale, lest it be not obvious!
 
<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../64_electric_cars">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../66_newsworthy">Next post</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../64_electric_cars">Noeoelectric Cars</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../66_newsworthy">Newsworthy</a></td>
</tr>
</table>
