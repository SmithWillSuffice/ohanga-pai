---
title: "Accelerators and Repellers -1"
weight: 8
description: ""
date: 2022-12-31
lastmod: 2022-12-31
cover: ""
coverAlt: ""
katex: true
tags: []
---

This is one in possibly a series of posts for the general audience on some of the 
dynamical systems ideas underlying macroeconomics. Our focus is on macro and 
mesoeconomics. So we are **_not_** interested in particular stock prices, or even 
sectors, we are interested in the main aggregated market indices 
(in the USA the SPX, NASDAQ and whatever). This is partly pragmatic. 
If you liken the economic system to the weather and climate, the climate is very 
predictable (highly macro) the weather is not (too micro).

Whenever you see such qualitative level distinctions, you know you are dealing with a 
dynamical system with so-called *emergent* properties, and top-down causations. A 
purely bottom-up system that admits a reductionistic description can always be 
modelled using micro-casual analysis --- with enough compute power. A genuine 
top-down controlled system does not admit such analysis. But most dynamical systems 
are not entirely top-down. And the economy of a large nation is such a hybrid system, 
it has micro-causal and macro-causal responses and feedbacks, so also involves 
potential for useful mesoscopic analysis.

((For the philosophers: genuine top-down causation is impossible in classical physics, and so is considered impossible in economics, because the economic system is considered to not be sensitive to quantum mechanics. But this is incredibly naïve and foolish. There is a stupid dumb way you can see it is foolish at a very basic level, because all the computers running the modern fintec systems and nanosecond trading algorithms absolutely must rely upon quantum mechanics, because their transistors cannot function otherwise. But this is stupid because the transistors are a mere means to a classical end. The computation on the trader's desktop is a Turing machine process, even sub-Turing because it lacks an infinite memory tape. So all *that* is totally classical physics input into the economic system.))

((So where is the top-down in economics? You do not have to believe Roger Penrose to 
think quantum mechanics pays a role in human thinking processes, but you should 
understand human consciousness is not explained by physics (the inner subjective 
phenomenal qualia). So no matter what the source of human consciousness is (we do not 
really care for present purposes) whatever it is, it is not physics. So human 
psychology is not driven by bottom-up blind physical events. You will need to read my 
other website ([T4G theory](https://t4gu.gitlab.io/t4gu/)) to see one set of reasons 
why, or just trust me. Human beings making good and bad, lame and chad, decisions are 
top-down influences on economics, with bottom-up signals as other inputs.))


## Generalized Forces

One question one might naïvely ask is "What are the generalized forces in an economic 
system that *move* prices?"

The six billion dollar question. Most analysts give up, and use brute raw statistical 
probability theory analysis, which is admitting you have no idea about the forces.
You only know distributions of outcomes. Which I think is a fair approach, even with 
state-of-the-art dynamical systems models and ANN (artificial neural networks).

The thing is, no dynamical system model can do a better prediction or modelling job 
than the accuracy of your modelling assumptions permits. And no ANN can do a better 
prediction or modelling job than the data it gets trained on can admit. This is 
because all real ANN's are finite state machines. So they lack conscious thought and so 
lack genuine creative insight capacity, and so cannot generate more than what 
information theory à la Shannon can be found in their inputs. (This is all so 
unless you subscribe to radical panpsychism.)

Anyhow, this is a big issue for our effort over at the 
[DougBot project](https://www.patreon.com/mmtmacrotrader), because what I argue (with 
Douglas) is that we are automating his canniness, not creating a new thinking being 
that can oracle the stock prices. In pragmatic terms this does not really effect our 
research, because in research a team needs push and pull. But for you philosophers of 
finance this might be of interest, also if you are an investor who has come across 
some wild good claims about how a genius has found a way to beat the markets and earn 
you insane returns. Did someone just say "Carlo Pietro Giovanni Guglielmo Tebaldo 
Ponzi"? 

Rather than looking for oracle powers, the idea and method for DougBot is to use 
hybrid techniques. The simplest is to use a dynamical system model, of the Steve Keen 
Goodwin-Minsky variety, to get the very high level macro dynamics correct. A dude in 
Portugal did this for the Portuguese economy, Pedro Sousa, you can get 
[his PhD paper here.](https://repositorio.iscte-iul.pt/bitstream/10071/11199/1/TESEcorrigida.pdf)
Being in the EU this thesis was not trivial, the bank flows had to be carefully 
analysed. Sousa did an excellent job.

Such models are not going to say squat about stock prices, but they might have useful 
information for informing us about macro aggregates, like the S&P500 or NASDAQ, or in 
New Zealand the NPX.

The trouble is, macroeconomic models deal with fiscal flow or [Godley Tables,](https://www.youtube.com/watch?v=CoglF8_z7lk) 
and there is no real generalized force in them for seeing how relative prices move, 
because with the complexity available currently in these Minsky models, there is only 
one price level, or two if you are clever (asset prices (I call them fictional goods) 
can be partially de-coupled from goods prices, real goods being physical things 
people consume, not numbers on bits of paper).

All the forces in most of the Keen-Minsky models I can currently build are 
behavioural equations, such as the Phillips curve. The rest is just stock-flow 
consistency (the "mere accounting".)

Your nation does have to have a fair justice system to have the accounting rules 
satisfied in reality though, it is not trivial. Imagine rampant counterfeit. Imagine 
rampant bank fraud. Such deviant (and illegal) behaviour would invalidate a 
Minksy-Keen model, unless we accounted for it --- black market ops and counterfeit 
rows in the Godley Tables?  For the most part we hope to be able to ignore such 
factors.

((Here I have a conjecture: to get wild insane returns, like one particular fund 
claims, you need to be dealing in the black market, or something illegal. Drug dealers 
and traffickers will be prepared to make insane losses, due to the nature of their
business, they can still eat caviar, but their loss is someone else's gain, so a 
black ops "hedge fund" I bet, an investor who is "extremely diversified."))

This leaves us with the generalized forces driving relative and absolute price 
movements that will need to be empirically determined. That is a hard task. 
But some physics principles can help us.


### How can you measure a force?

If something is moving, you can measure the force by measuring acceleration. 
But that's only provided there is a single force. Which is not the case in general. Multiple forces can cancel, whenever there are pushes and pulls, then this manifests 
as a type of stress. However, it is still always true that any *net* force will be manifested as an acceleration, and that's what one worries about for price movements, 
the net force.

We can do this for a lot of the fiscal flow data published by the FRED and BIS.
The good early news is that we can see hints of causal relations from looking at the 
accelerations in lagged margin debt and the SPX. This is promising, because although 
there is still a lot of noise, we can see a generalized force acting.

The conceptual idea of movements in incomes and wages and other macroeconomics variables can be illustrated in a diagram:

{{< attractors_and_repellers >}}

Here the physics concept of "energy" needs to be replaced in economics by something 
like an optimal output, such as "productivity" or "real output". So on one side there's 
too little (starvation) on the other side too much (resource depletion). 

The illustration is only showing one-dimension, in the real world there will be 
multiple dimensions, so instead of a curve we'd actually have the "ball" (the system 
of interest, a firm, a household sector, a commodity, or any sub-system of the 
economy you are interested in that causes changes in the $y$ objective function). 
The general point is that viewed this way, only as a metaphor, there are "forces" at 
work in macroeconomics.

On the right diagram the interest rate is shown as a repeller force. If you are 
middle income at the top of the "energy" curve you are maybe safe but unstable to 
getting poor or rich, since the interest rate hikes hurt the poor and reward the 
rich, it is a force that creates a growing wealth divide. 

The deceptive thing about simple diagrams (like IS-LM models) is that they are not 
showing the full manifold of all effective objective functions (happiness, social 
unrest/peace, optimal food output, optimal savings, &c.)  On the right diagram I drew 
the curve going back upwards at higher wealth levels, which for instance might be due 
to a third dimension an the manifold not visible that effects $y$ when too many rich 
people exist. You can imagine several such factors from too many idle people 
(lowering optimal useful output) to social unrest (lowering unit worker 
productivity).

I will maybe re-use these metaphors in further discussion, because although they're 
not quantitative, they are useful for illustrating conceptual idea that are very 
important in macroeconomics. I'd summarize this as going beyond the stupid 
"equilibrium" supply--demand curves.

### It's a high-dimensional Manifold

The problem is the economic system has many people with their feet on gas peddles and 
brakes, all over the place. And we are looking at the superposition of them all in the 
aggregate. So it is always going to be noisy. 

The conjecture our research is based upon is that some of this will be gaussian 
noise. If it is, then we are not dealing with power law dynamics, and not with fat 
tails in signals.  This is vital for getting well-trained neural nets. ANN's do not 
"like" noise. It is best to think of an ANN as merely canning your reasoning capacity 
when comatose or dead drunk. It is going to be feeble. But you can make out numbers 
and letters, and maybe stop versus go signs.

What if the forces are static (in stress)? I am not sure economics has this concept, 
but "consumer sentiment" is possibly a qualitative form of data we might be able to 
use, but at this stage it would be sketchy. (It is something stock brokers and finance 
journalist use.) Debt-to-GDP is a stock divided by flow, and stocks are a lot like 
static forces. You can measure their velocity and acceleration to get a flow variable, 
but if you can also find a "force" signal in the stock, then that is acting like 
a stress.

A good example of this is a major example! The Great Crash of 1929 and the GFC of 
2007-8. Both had private debt in excess of 150% of GDP. This was the stress variable. 
It's rate of change was over 10%, and that was a velocity measure, so the rate of change 
of *the* was the acceleration, indicating an underlying force. Both the stress and the 
velocity seem to be triggers, neither separately, this is from empirical work by 
Richard Vague (see, 
[A Brief History of Doom](https://www.upenn.edu/pennpress/book/15996.html).
Although, if I am right, there should have been an impulse the triggered the 
great crash, that would be s short burst in the accelerator. If I recall from reading 
J K Galbraith 
[The Great Crash, 1929](https://www.goodreads.com/book/show/41591.The_Great_Crash_of_1929) the force was mostly psychological: 
"boundless hope and optimism". In 2007-8 the force was the emergence of just a few short 
traders. They pushed the subprime mortgage market off the knife-edge balance of wild 
optimism in real estate CDO's and MBS's. But it is always more complicated, rumour, 
gossip, wild optimism yields to neurosis, &c.

It is hard to gauge these forces. But in the time series the accelerations the 
forces produce are always visible.

I should have more to write about this in coming months. We are trying to find the 
dominant accelerators. I guess it is also worth mentioning Wall Street Quants 
probably know the accelerators, they just do not make that knowledge public.
So we have to do this work for our community of followers.


### Forces from Ledger Books?

The Godley Tables [explained here by Ty Keynes](https://www.youtube.com/watch?v=CoglF8_z7lk) do not model generalized economic forces *per se*. 
They model the accounting rules. The flows are determined by behavioural equations 
that relate the stock variables in Minsky-Keen models. For example, a Phillips Curve 
for the wage rate as a function of employment and price level.

The behavioral function, here $f(t)$,
$$
\frac{dx_i}{dt} = f(t, x_1, x_2, \ldots)
$$
is like a generalized force. But if the dependent variable $x_i$ here is not a price, 
then it is not so useful for DougBot. The price might however be sensitive to $x_i$, 
which would be useful to know.
Also, we'd need $x_i$ itself to be a flow, not a stock. That is because a rate of 
change, $dx/dt$ is a velocity, not an acceleration. If $x_i$ were a stock then $f(t)$ 
would be a velocity (e.g., how fast cash is turning over).

If we were to only look at velocities we would not have a causal model. To get cause, 
we need force. Forces are the drivers. Velocities are the effects of the drivers, and 
stocks are the lowest downstream effects (where things end up after a given time 
period).

I need to write a caveat: all this is largely metaphorical. Outside Steve Keen's 
work, no one really understands the financial system in force-like terms, it is all 
"energy-like" --- in thermodynamic equilibrium --- if you wanted a physics analogy, 
which is all wrong-headed neoclassical thinking.

BTW: The reason Steve Keen says his Minksy DynSys models 
"prove MMT" is because he says "MMT is just accounting." (This is pretty awful of 
Steve, but he can be forgiven.)

We, MMT enthusiasts, would say MMT is a lot more than accounting. It is about 
societies legal and financial institutional arrangements, and much more than just 
accounting rules. However, in part, Steve Keen is right about the use of Godley 
tables because of these legal rules. In the old days it used to be ledger books.
Money was created by fountain pen.

You'd have a hard time back then doing real-time forecasting! With the financial 
time series published these days an amateur computer programmer can probably see 
near to real time the velocities and accelerators in the financial data.


## The Interest Rate repeller


```
TODO: went on the rant below before finishing the notes on attractors and repellers.
```

### Other Social Forces

There is of course a lot more to the MMT analysis and its implications for system 
dynamics. Stock prices move by one type of set of forces, but wages by others. And 
often activists are more interested in wage and consumer price goods price movements, 
and could give a fig about the stock price movements. 

These cannot all be completely de-coupled, because of the fiscal 
constraints embedded in the banking system. The government has "freedom" to set the 
absolute price level (what appears in a Keen-Goodwin-Minsky model) but not all the 
relative prices (unless they are a totalitarian government, which we have never 
really perfectly seen on Earth, just approximations).

One reason Steve Keen tarnishes his reputation by abusing the MMT community as 
"nothing but accountants" is because it matters politically whether people understand 
the MMT system, and use it wisely, and that has been the point of the MMT social 
movement for over 30 years as of to date, from the founding by Warren Mosler, Bill 
Mitchell and Randall Wray, joined by Stephanie Kelton and Pavlina Tcherneva, 
Matt Forstadter, Scott Fulwiler, and now legions of others.

In particular, what Steve Keen has never acknowledged correctly afaik is the insight 
of Bill Mitchell on buffer stocks, and that the MMT system which is currently an 
operational reality in most nations in the world, uses a labour buffer. This is vital 
to MMT understanding. Without it you get idiots like Steve Keen (I can say this, 
since he is a good Internet friend, and an Aussie, so he knows I am just blowing hot 
air, but only half-joking) claiming MMT is nothing but accounting. I say to Steve that a labour buffer is not accounting, it is a matter of grave social justice (or injustice, depending on how people understand the buffer). 

I also think Steve Keen is very old school on the Treasury bonds story. 
Warren Mosler 
[had the insight](http://moslereconomics.com/wp-content/uploads/2019/10/35432615-Soft-Currency-Economics.pdf) 
(no one else agreed with him at the time) that when the FED sells Treasury bonds for 
"monetary operations" it was functionally the same as Treasury selling bonds for 
"fiscal operations". He realized you cannot call them different functions. Still to 
this day most post-Keynesians disagree, and this is not a mere accounting squabble. 
People agree about the software operations, I think. It is a government function 
insight. The FED cannot be thought of as a private entity independent of US 
government. If you still think otherwise, you are not MMT aware.

The thing is, it makes a huge difference in political economy, so is far, *far* 
beyond the impact of "just accounting." It can ruin people's lives, and always those 
who lives are already the most miserable, by pushing an austerity politics using the 
interest rate repeller, among other injustices.

I would also claim that warren Mosler best understood the impact of moving to a 
floating exchange rate, and the fiscal space this freed up for a government. 
Post-Keynesians (generally, not all) still do not comprehend this, and Steve Keen 
seems to still be one of them. Most post-Keynesian think the exchange rate is an 
exogenous constraint. MMT says it is not, not if you understand the correct actual 
software-driven, legally instituted monetary operations available to governments. But 
this includes *legal*.  Let me say it again **legal arrangements.** MMT says these 
matter, over and above the accounting principles. This is vital for understanding why 
no fit currency issuing government has any foreign exchange constraint (they do if 
they make up one). Only Mosler in 1995 understood this. Most post-Keynesians still 
do not, hence we have stupid debates about trade policy and exports as a cost, 
imports as a benefit (the MMT story, which is correct). The exports are the price you 
pay for your imports. This is not "neoclassical" thinking as Steve Keen slurs the MMT 
community with, it is just logic.

But the logic can cause suffering for poorer nations if people do not understand it. 
Like the logic of what happens when you ignore momentum and walk into street lamp 
poles.

Lastly for today, I will mention two key **_conditional fundamentals_** that 
post-Keynesians do not seem to understand or know:

1. Deposit holders know crap all about their bank. So the liability side of banking is not the place for market discipline.
2. The central bank policy levers are about prices (interest rates) and not quantities.

Why are these *conditional* fundamentals? It is because they apply when a nation uses a 
tax credit which is a non-convertible currency on a floating exchange rate. Without 
those conditions the central bank has to employ methods like bond issuance to control 
interest rates to control (weakly) exchange rates. They furthermore will want to 
deliberately cause mass unemployment to limit inflation, like psychopaths who have 
broad public approval for their ax murdering.  With floating exchange rates there 
is no need for those functions, and the above two fundamentals apply.

On fundamental **1** Mosler writes, "...even Wall Street analysts can't reliably 
do this" (assess bank insolvency risk). I also thought it worth quoting the rest 
of Warren's paragraph on banking proposals for helping the smaller banks:

> "Regulation and supervision on the asset side then became the imperative. And while 
we have seen periodic failures due to lax regulation and supervision of the asset 
side of the US banking system, and it's a work in progress, the alternative of using 
the liability side of banking for market discipline exposes the real economy to far 
more disruptions and far more destructive systemic risk."

You cannot get more MMT than this. If you do not understand monetary operations, you will introduce instability and inequality.

What ticked me off about Steve's flippant comments was that it is not only Warren who has been preaching the truth for years, Steve Keen's acquaintance Charles Goodhart has too, as Warren relates (fairly blisteringly true I might add):

> Those who understand reserve accounting and monetary operations, including those 
directly involved in monetary operations at the world's central banks, have known for 
decades that in banking, causation runs from loans to deposits, with reserve 
requirements, if any, being merely a 'residual overdraft' at the central bank and not 
a control variable. This includes Professor Charles Goodhart at the Bank of England, 
who has written extensively on this subject for roughly half a century, endlessly 
debating the 'monetarist' academic economists who spew gold standard and fixed 
exchange rate rhetoric, and who are unaware of how monetary operations are altered 
when there is no legal convertibility of a currency.

Once Steve acknowledges all this, and the other generalized forces in the MMT social 
movement, he will apologise to us!  He is a good guy. I mean a *really* good and nice 
guy. Salt of the Earth, with a bit of a fire cracker in his hand too though. Also, I 
am pretty sure he is trolling us when he says "MMT is just accounting." So I took the 
bait. Also, he said that 
[at an MMT Conference](https://www.youtube.com/watch?v=DoMPlG5kgNE), 
so of course he was having an Aussie lark, but he can also be damaging to the MMT 
movement when he says such things more publicly, because they are wrong. This matters because Steve is a very influential economist and activist.

((**Note to self:** need to write a theory section on trade. When we write about trade, the important thing is to not be too simplistic and naïve (a word I seem to need to use a lot). Fadhel Kaboub and Jan Kregel are MMT aware and have a decent body of work on international trade, and the exchange rate is not their problem, the biggest problems by far are imperial power abuses, neocolonialism, and just broadly war and injustice and dysfunctional justice systems in the weaker nations. Fixing up their exchange rate is pretty much negligible help with all that, but they need the MMT lens to know what to do about it when they restore civil society. Australia will never have a foreign exchange constraint because their government know how to tell foreign buyers of their land and politicians to piss off --- at least if they want too, if they do not want to, well,...  then their civilized BBQ's with shrimp could turn into charcoaled gruel purchased at 
a Tesco Lotus shop.))

Even *more generally* we are, in the DougBot project, using an MMT understanding, a 
lens, to do finer grain price analysis. It is not merely accounting, and although we 
could call it post-Keynesian, or Institutionalist, MMT is a superset of these 
schools, not a subset. Anyone thinking otherwise is just being very nasty to the 
founders of the movement like Mosler and Mitchell. Randall Wray is a better arbiter, 
since he was a post-Keynesian, and still is! He considers himself now MMT in thought. 
Not that any of these labels and names matter, but funnily in the economics 
profession they seem to, like they do not in physics or mathematics where I come 
from.


<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 15%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../07_cashless">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">Back to Blog</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../09_mmt_semantics">Next post</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../07_cashless">Is a Cashless Society Good?</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;"><a href="../">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../09_mmt_semantics">Semantics of MMT</a></td>
</tr>
</table>
