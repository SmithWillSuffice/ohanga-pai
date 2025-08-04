---
title: "Macromodels I.3 — IS-LM"
weight: 12
date: 2024-12-09
toc: true
katex: true
---

I will try to use '**ISLM**' for the general idea of ISLM modelling, I will use 
lowercase '**islm**' for our particular python model, which I've also 
named _OpenEconomyISLMModel()_.


## ISLM Scenario Testing

Basically we want to know for what the model can predict, how good is it?
An AIC score might be nice too. 

The problem with ISLM is that it is not fit for forecasting. What it portends
to accomplish is take an existing set of macroeconomic variables, suppose some
of them change in the future, and then output $Y$ and interest rate $r$ are
predicted for a new equilibrium.

When you think about this from a dynamical system perspective the model is
really just entirely unworkable. It is the dumbest most clunky thing you could
do. No systems engineer would even think of using  a moving static equilibrium
to analyse a dynamical system. It would not be a model that is even "on the
table".

But as the soldiers we are, fighting incompetence (including our own) we might
want to persist just to show how ISLM does not work.

### Methodology for Testing the Model

We aim to compare the model's predictions of output ($Y_{eq}$) and interest 
rates ($r_{eq}$) with observed real-world data for $Y$ and $r$ from FRED.

However, we also should have in mind all the other models we also want to test.
The other models should also output at least $Y$ maybe also other indicators
like inflation, unemployment, and is an MEA and MSE error analysis the only
thing to compare?

### Addressing Bias

We are using $Y$ and $r$ as input data to estimate some of the islm 
parameters, this creates circularity bias (the model assumes what it is 
pretending to predict). To avoid this bias some things to consider might be,

* Use Proxy Variables:  
    Replace $Y$ with leading indicators such as retail sales, industrial 
    production, or other proxies for GDP.   
    Replace $r$ with instruments like the Federal Funds rate, LIBOR, or 
    policy rates.
* Validation with Out-of-Sample Data:  
    Train the model on data excluding $Y$ and $r$.  
    Validate predictions using $Y$ and $r$ from a separate time period.  
    (This begs the question what is the "correct" lag?)
*  Counterfactual Simulations:  
    Set scenarios where you modify only one input (e.g., increase $G-T$) 
    and observe how well the model matches the directional trends in 
    real-world data.
* Granger Causality Testing:   
    Use statistical methods to determine if the model's inputs 
    Granger-cause $Y$ and $r$.  
* Impulse Response Analysis:  
    Assess how shocks to certain inputs (e.g., $G-T$ or $M$) affect 
    $Y$ and $r$ over time, compared to real-world responses.

This multi-faceted approach will help validate the islm model's usefulness 
in explaining real-world macroeconomic behavior. But I am not sure I have 
the time and inclination to try all of these approaches.

I think it is worthwhile running two methodologies,

**Method-A.** Mean square errors on $(Y, r)$ for various lags.

**Method-B.** Granger cause: do the inputs Granger cause $(Y, r)$?

Method-B is good because it is model independent, we do not need the 
islm model to run a Granger Case test. However we can compare Granger Cause
statistics for _both_ the real world $(Y, r)$ and the model 
output $(Y_{eq}, r_{eq})$.  This will not be any test of the islm model 
directly, but what we want  is to **_compare_** the Granger causality of 
the islm model against the granger-causality of the other models we will 
study later, like Minsky and ISMY.

### Methodology A

**1. Input Scenarios.**  
We've already used historical data from our FRED fetches
to generate islm model inputs saved in `islm_series.csv`. This includes all 
the parameters needed by `OpenEconomyISLMModel()` for each month.

**2. Generate Predictions.**  
For each row in the CSV file:  
    Use observed values for model parameters as inputs (excluding $Y$ and $r$).

    Use the islm model to predict $Y$ and $r$.
    Repeat for months 1, 2,..., 12 ahead in time.

**3. Evaluate Predictions**  
Calculate prediction errors (e.g., Mean Absolute Error (MAE) or Mean Squared Error (MSE)) for $(Y_{eq}, r_{eq})$ compared to their actual values $(Y, r)$.

**4. Estimate the Lag**  
From year to year the lag to get to the presumed islm equilibrium could vary,
there is nothing in the ISLM framework to suggest what the lag is, nor if there
is any well-defined concept! (Since the real economy is not ever in equilibrium.)
However, we can examine perhaps a decade of data and estimate the optimal 
lag that gives the best fit for the islm outputs.

We then want to highlight this "best predictor" lag in the visualizations of our
analysis.

**5. Visualize the Results**  
We will think of something nice using Plotly.





















## Last Word

You might notice the inordinate amount of work we had to do to fetch empirical
data to get the parameters for our IS and LM curves. But the ISLM model only
spits out a static equilibrium analysis, and only gives us two outputs, Income
and Interest rate. But (we will see later) we can use plain old econometric
forecasts or modern neural networks to better predict output $Y$ changes in
response to policy variable changes within reason. Is the ISLM model going to
really give us a good estimate for how $Y$ might respond to money supply or
investment variables? Let alone changes to public employment and welfare policy?
Impossible! 

This places into serious question whether there is _any_ use for an ISLM model
in informing good policy? 

The case seems extremely weak, or weak to completely backwards!

Our conclusion is that ISLM is hazardous to use as a predictive tool. It should
not even be taught in schools. 

Every ISLM model, or anything like it, should come with an obligatory warning
from the Surgeon General:

> **Caution:** This is a bullshit equilibria macroeconomic model, if
persistently used in policy it can damage the health of all of society. 
Possibly leading to extinction of your species.





<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../302_02_macromodels_islm_2">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../310_00_macromodels_dsge">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../302_02_macromodels_islm_2">MM—II, ISLM</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../310_00_macromodels_dsge">MM—X.0, DSGE</a></td>
</tr>
</table>


