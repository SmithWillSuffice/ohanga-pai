---
title: "Macromodels I --- Introduction"
weight: 8
date: 2024-12-08
toc: true
katex: true
---

This is a new chapter series on macroeconomic modelling. I set my task to go 
through all the crud before getting to the good stuff of MMT and 
Minsky/GodleyTable models.  The desire would be to do as much justice to 
the lamestream models, and then test them against empirical data. 

The two mainstream models will be,
* IS-LM
* DSGE. 

That's the crud.

Then we will try to increase sophistication:

* CNN/LSTM fit models (to provide a base case for prevailing policy conditions).
* Dirk Ehnts ISMY model.
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


## Course Outline

By "Analytics" I mean running a model with parameters fit to past NZ data, and
running ahead 1, 2,..., 12 months in time. The entire aim of this course is to
compare macro models. If we can program a model, we want to use it only if it is
better than some other programmable model.

However --- also --- if we have a bunch of programmable models, and they all
suck, then we want to know that, and will not use any of them to inform
government policy. This is no great loss. With an MMT lens we do not need
predictive mathematical models, because we can always operate at the spiritual
economics level, which is to focus on sustainable resources and full employment.
Quite literally we can say "stuff the price level nonsense" since we know the
currency is a mere numeraire, and what really matters is the share of the pie,
not the nominal price of the pie. Provided the pie is produced sustainably. 

This is a radical MMT stance of course, since in politics not worrying about the
price level can get you voted out of office.Thus the price level will not be of
zero concern, we will want to know what nobs and dials need adjusting so the
price level does not rise too fast. All that means, really _all that means_ is
"it does not get you voted out of office".

The way to have a high inflation rate _not_ get you voted out of office is,
however, not exactly a thing we need to model, since it is political, and the
remedy is to make damn sure the lowest real wage is rising the fastest. This is
a political decision. That should in principle keep a government in office,
probably forever, provided none of your other policies are dick-headed,
war-mongering, colonialist or rapist. The only postulate here would be this
government, whoever they may be, seized power Once Upon a Time. That is the hard
part, and no MMT model can solve that problem for you, but it can help you
dialogue and stump electioneer your way into power.

The TODO list:

1. Finish the IS-LM analytics.
2. DSGE Example and analytics
3. ISMY Example and analytics
4. Levey Price Model example and analytics?
5. Minksy--Molser example and analytics.
6. CNN/LSTM comparative model --- this will be our basic Ptolemy 
nobs and dials model.
6. SINDy comparative model --- a second basic Ptolemy nobs 
and dials model.

This is going to take a long time to get through! It is not a one semester 
course, probably not even two semesters.

# Focus on Minksy--Mosler

This main end goal is to have a Minsky ODE base case for analysis. This will
have a price model borrowed from Levey, Godley Tables from Keen-Minksy, and a
Job Guarantee as the stabilizer.

# SINDy comparative model

Not sure we will end up using SINDy, but it is an easy model to construct so
perhaps worthwhile. A naïve starter model could just use up to quadratic
response functions, unless we can get custom functions for Investment and
Phillips curve determined, my feeling is there is some freedom in the
PK/Heterodox/MMT literature on how to model these response functions.

However, I think it is fair to say it is only up to the second derivative that
matters, given the amount of noise in macroeconomics. That is, we should never
consider a 12 month prediction to be anything but fantasy, and so all the models
are like weather forecasting. We need to data of government policy responses and
changes fed in continually, as they happen.

Every government response invalidates the current model, even if the model
continues working.






<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_2_funds_flows">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../301_2_macromodels_islm">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_2_funds_flows">Funds Flows</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../301_2_macromodels_islm">MM—II, IS-LM</a></td>
</tr>
</table>


