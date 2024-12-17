---
title: "Macromodels II --- IS-LM"
weight: 7
date: 2024-12-06
toc: true
katex: true
---


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

Those are the basics. But to build a "nice" analytical model we need 
a few equations. It turns out not to be too complicated to have an 
open economy, so we might as well start with this most realistic 
minimal case. A lot of undergrad textbooks might begin with a 
closed economy, just to get the student mental balls rolling, but 
here we do not want to retard the mind with an unideal base case, 
not when we can go straight to an open economy form the start.

# Open Economy IS-LM Model: Theoretical Foundation and Implementation

You can find the python code for this model soon on the Ohanga-Pai website. 

This documentation provides a detailed explanation of the IS-LM
model, describing its theoretical underpinnings, mathematical formulation, 
and computational implementation.

## Theoretical Framework

### Model Objectives

The Open Economy IS-LM model aims to:
- Analyze the interactions between real economic activity and monetary 
conditions
- Explore how changes in key macroeconomic parameters affect economic 
equilibrium
- Provide insights into the effects of monetary and fiscal policies 
in an open economy context

**Caveat and WARNING:** All this is based upon a flawed overly simplistic 
set of assumptions. 


### 2.2 Key Model Components

The model comprises three primary equations:

1. **Consumption Function**
   
   The consumption equation describes how aggregate expenditure 
   depends on national income:

   $C = C_0 + c_y \cdot Y$

   Where:
   - $C$ is total consumption
   - $C_0$ is autonomous consumption
   - $c_y$ is the marginal propensity to consume
   - $Y$ is national income

2. **Investment-Saving (IS) Curve**

   The IS curve relates national income to the interest rate, incorporating net exports in an open economy:

   $Y = C_0 + I_0 - b(r - r^*) + NX(Y, e)$

   Where:
   - $I_0$ is autonomous investment
   - $b$ is investment sensitivity to interest rates
   - $r$ is domestic interest rate
   - $r^*$ is foreign interest rate
   - $NX$ represents net exports (function of income and exchange rate)

3. **Liquidity Preference-Money Supply (LM) Curve**

   The LM curve describes the relationship between money demand, income, and interest rates:

   $M = L(r, Y)$

   Where:
   - $M$ is money supply
   - $L$ is money demand function
   - $r$ is interest rate
   - $Y$ is national income

## 3. Model Assumptions

The implemented model makes several simplifying assumptions:

- Balanced trade (net exports set to zero)
- Linear relationships between variables
- Fixed exchange rate
- Closed economy approximation with limited foreign sector interactions

## 4. Computational Implementation

### 4.1 Equilibrium Determination

The model finds equilibrium through an iterative process:
- Initial guesses for income and interest rate
- Successive approximations using IS and LM curve equations
- Convergence to a point where both curves intersect

### 4.2 Scenario Analysis

The implementation supports:
- Monetary policy simulation (money supply changes)
- Fiscal policy exploration (autonomous consumption variations)
- International economic condition analysis (foreign interest rate modifications)

## 5. Limitations and Extensions

### Potential Improvements
- Incorporate more complex net export functions
- Add exchange rate dynamics
- Implement non-linear relationships
- Enhance numerical solving methods

## 6. Mathematical Notation

| Symbol | Description |
|--------|-------------|
| $Y$ | National Income/GDP |
| $r$ | Domestic Interest Rate |
| $r^*$ | Foreign Interest Rate |
| $C_0$ | Autonomous Consumption |
| $c_y$ | Marginal Propensity to Consume |
| $M$ | Money Supply |
| $NX$ | Net Exports |

## 7. References

1. Mundell-Fleming Model
2. IS-LM Model Extensions
3. Open Economy Macroeconomics Textbooks

**Note**: This is a simplified representation intended for educational and analytical purposes.







<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../300_1_macromodels_intro">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../302_3_macromodels_iii">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../300_1_macromodels_intro">MM—I, Intro</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../302_3_macromodels_iii">MM—III, DSGE</a></td>
</tr>
</table>


