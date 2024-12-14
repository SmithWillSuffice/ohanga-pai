---
title: "Macromodels I --- IS-LM"
weight: 6
date: 2024-12-10
toc: true
katex: true
---

This is a new chapter series on macroeconomic modelling. I set my task to go 
through all the crud before getting to the good stuff of MMT and 
Minsky/Godley Table models.  The desire would be to do as much justice to 
the lamestream models, and then test them against empirical data. 

The two mainstream models will be,
* IS-LM
* DSGE. 

That's the curd.

Then we will try to increase sophistication:

* CNN/LSTM fit models (to provide a base case for prevailing policy conditions).
* Dirk Ehnts AD model.
* Sam Levey Price Models (minimal MMT, aimed at modelling the source of the 
price level).
* Keen-Minsky models (state of the Art MMT).

## Caveats

It is hard to claim DSGE is "wrong" because there are too many free 
parameters, so one can simply curve fit and claim a DSGE model "just works". 
That is disingenuous of course, so we will want a long term forecast form 
all the models, at least 6 months ahead. No one should expect a macroeconomic 
model to forecast accurately that far ahead, just as no one should expect the 
meteorological office to predict the weather six months ahead. But that is 
not our purpose. We only desire a fair comparison for assessing parsimony of 
the various models. 

We _want_ all the models to eventually fail. The idea is to see which 
models are more robust.

If a macroeconomic model never failed than that'd only be because it's buttons 
were constantly being tweaked. Cheating! Like a CNN/LSTM.  There is Zero 
knowledge in such epicyclic type modelling.

## IS-LM History

This is the original bastardization of Keynes' General Theory. It was 
invented by John Hicks. It was always a stupid toy model. The fact 
professional academic economists still teach this model is weird. It is not 
like teaching Newtonian Gravity for physics classes, it is far worse. That is 
because there is Zero Knowledge in the IS-LM model. IT does noty begin with 
correct assumptions. Newtonian Gravity at least begins with a very good 
approximation to GR.

However, unlike gravity, macroeconomics does not have a General Relativity 
analogue. Perhaps the closest is the Keen--Minsky model, but we would 
classify that MMT model as more like the analogue of Newtonian Gravity. 
There really is no fundamental MMT macroeconomic model, because MMT 
recognizes government policy (human brains) dictate a large amount of 
structure in the real world dynamics of a macroeconomy.
It is like... good luck modelling _that!_

In other words, if it is a pure mathematical model you desire, then the 
state-of-the-art will probably always be a neural network model that 
brute-forces the forecasting, subject to accurate policy input parameters.

Why being with a bastard model then? The answer is that MMT also 
recognizes political and institutional inertia. Because government 
economics advisors will tend to operate with a Loanable Funds or IS-LM model 
in their head or in their spreadsheets, we want to at least understand why 
they consistently get forecasts and policy backwards, promoting 
unemployment to "fight inflation", instead of promoting full employment
and not having to worry about inflation.

John Hicks later repudiated his IS-LM model entirely, he became embarrassed 
by it, and overtly in his later publications admitted it left out the one 
key ingredient of Keynes' General Theory, which was that there is no tendency 
to equilibrium, and that uncertainty plays a fundamental role in 
macroeconomics. It is thus admittedly painful to bother taking the time to 
explore IS-LM, but if we desire to be politically engaged and combat the 
lunatics in professional economics, it is probably a good idea to 
understand the source of their idiocy.

### Relation to DSGE

Both IS-LM are equilibrium assumption models, IS-LM is the baby version, 
so-to-speak. Fewer adjustable parameters, so perhaps more parsimonious, 
but less useful in forecasting. Completely useless for informing 
government policy.

### Assumptions

The IS-LM curves are hypothetical relations presumed to be an idealization 
of some equilibrium between, (1) markets for goods --- supply and demand 
of real output, and (2) the money market (demand for currency, aka. liquidity).

The presumed equilibria are, 
1. (Real goods market) --- investment = savings.
2. (Money market) demand for money = supply of money.

**Assumption of interest rate effect:** the model further assumes the interest 
rate is endogenous (not determined by policy, but rather by markets forces 
so that the money market equilibrium became a tautology:

> The interest rate is whatever rate it needs to be so that there is 
equality of money demand and supply in the money market. 

It was further treated as a _given_ (unquestioned assumption) that
goods market equilibrium could be established.

The IS-LM model then postulates an interdependence of the two markets.

Since real output is roughly proportional to employment, the IS-LM model 
seeks to show how an equilibrium solution exists for some given level of 
output (hence employment) and simultaneously an interest rate, where the 
two markets are in equilibrium.

**Note:** we do not even need MMT understanding that the labour market is 
controlled by a monopolist (government) so there is no natural interest 
rate other than zero, to appreciate that the IS-LM model is already false, 
because just from empirical data we can see there is no equilibrium 
condition in real life markets. Thus from the outset we have to treat 
the IS-LM model as nothing but a toy.

**Consequence:** If the IS-LM model produces favourable forecasts then it 
would be by accident.

However, let's persist.

### Analytics

Stated more mathematically, unknowns are (i) real output, 
(ii) the interest rate. IS-LM needs two equations so these can be 
computed. Or minimally two _linear_ equations. Non-linear models could be 
admitted but then might not yield unique solutions.


### Definitions

The Money Supply we will use is "M1" = notes, coins and bank deposits 
(CD = "current deposits").

## Beyond IS-LM

We already mentioned the DSGE model, which we will discuss in a later 
chapter.

There is another more minimal extension of IS-LM, the AD-AS model 
(Aggregate Demand--Aggregate Supply) but it does not significantly patch 
any of the flaws in IS-LM, so is still a Zero Informative model.
We will instead, after briefly looking at DSGE, jump to a more MMT-like 
model due to the economist Dirk Ehnts --- the so-called ISMY model.
This model was developed for analyzing the EMU (European Monetary Union) 
system of interlinked state economies, so is not a complete MMT model. 
MMT models would apply to single currency regions where there is a 
monopoly fiscal authority called "the government". No such institution 
exists for the EMU.

Collectively the EU governments plus the ECB act _as if_ there were a 
monopoly government, but the fiscal space is so constrained that using 
such an "effective government" frame is probably unwise. It obscures the 
full fiscal space that is available to a monopoly currency issuer with 
full legislative power and control over the central bank and all 
commercial banks.  More importantly, for political purposes, it is just 
a bad idea to say the EMU "has a government," since that tends to insert 
in the mind the notion of some kind of democracy, but this is entirely 
lacking in the EU/EMU. Where there is no democracy is is a bad thing to 
pretend there is one, since a democracy is probably not a bad system of 
government to have in part. So if a corrupt elite-power driven government 
is falsely though of as having democratic elements, and the result is 
austerity and poverty, and evisceration of the working class, then it 
is betetr to call that institution The Oligarchy, not "the government".
Placing fault where fault belongs.







<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_1_macro_trader">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../999_1_quantopian_phacks">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_1_macro_trader">Macrotrader I</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../301_2_macromodels_ii">MM—II, DSGE</a></td>
</tr>
</table>


