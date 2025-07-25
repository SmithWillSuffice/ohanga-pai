---
title: "Macromodels I.1 — IS-LM"
weight: 10
date: 2024-12-06
toc: true
katex: true
---

## IS-LM History

This is the original bastardization of Keynes' General Theory. It was 
invented by John Hicks. It was always a stupid toy model. The fact 
professional academic economists still teach this model is weird. It is not 
like teaching Newtonian Gravity for physics classes, it is far worse. That is 
because there is Zero Knowledge in the IS-LM model. It does not begin with 
correct assumptions. Newtonian Gravity at least begins (albeit only in hindsight) 
with a very good approximation to GR.

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

Why begin with a bastard model then? The answer is that MMT also 
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

# Open Economy IS-LM Model

## Theoretical Foundation and Implementation

You can find the python code for this model soon on the Ohanga-Pai website. 

This documentation provides a detailed explanation of the IS-LM
model, describing its theoretical underpinnings, mathematical formulation, 
and computational implementation.

### Model Objectives

The Open Economy IS-LM model aims to:
- Analyze the interactions between real economic activity and monetary 
conditions.
- Explore how changes in key macroeconomic parameters affect economic 
equilibrium.
- Provide insights into the effects of monetary and fiscal policies 
in an open economy context.

**Caveat and WARNING:** All this is based upon a flawed overly simplistic set of
assumptions. Thus, for heavens sake, do not use this model for policy analysis
if you are in a government position, in fact, if you use the IS-LM model at all,
you might consider doing the exact opposite of what the model suggests.

### Mathematical Notation

| Symbol | Description |
|--------|-------------|
| $Y$ | National Income (GDP) |
| $G-T$ | Net government spending |
| $r$ | Domestic Interest Rate |
| $r^\ast$ | Foreign Interest Rate |
| $C_0$ | Autonomous Consumption |
| $c_y$ | Marginal Propensity to Consume |
| $M$ | Money Supply |
| $\ell$ | Money demand sensitivity |
| $NX$ | Net Exports |


### Key Model Components

The model comprises three primary equations:

**1. Consumption Function**
   
The consumption equation describes how aggregate expenditure 
depends on national income:
$$
   C = C_0 + c_y \cdot Y
$$
Where:
   - $C$ is total consumption
   - $C_0$ is autonomous consumption
   - $c_y$ is the marginal propensity to consume
   - $Y$ is national income

**2. Investment-Saving (IS) Curve**

The IS curve relates national income to the interest rate, incorporating net
exports in an open economy: 
$$ 
Y = (G-T) + C_0 + I_0 - b(r - r^*) + NX(Y, e) 
$$
   Where:
   - $G-T$ = government net expenditure (could be negative = "surplus"). 
   - $I_0$ is autonomous investment
   - $b$ is investment sensitivity to interest rates
   - $r$ is domestic interest rate
   - $r^*$ is foreign interest rate
   - $NX$ represents net exports (function of income and exchange rate)
and here also the investment function is assumed linear:
$$
I = I_0 - b(r - r^\ast)
$$

**3. Liquidity Preference-Money Supply (LM) Curve**

The LM curve describes the relationship between money demand, income, and interest rates:
$$
   M = L(r, Y, \ell)
$$
Where:
   - $M$ is money supply
   - $L$ is money demand function
   - $r$ is interest rate
   - $Y$ is national income
   - $\ell$ is the liquidity preference parameter, or 'money demand sensitivity'

## Model Assumptions

The implemented model makes several simplifying assumptions:

- Balanced trade (net exports set to zero)
- Linear relationships between variables
- Fixed exchange rate
- Closed economy approximation with limited foreign sector interactions

In addition we will need to cook up some response functions. For the 
money supply (LM curve) we will use a linear function,
$$
M = \ell(r_{eq} + Y)
$$

For the IS curve I stuck in a balanced trade assumption somewhat 
egregiously!  Then the IS curve simplifies to,
$$
Y_{eq} = (G - T + C_0 + NX + 
                b * (r^\ast - r)) / (1 - c_y)
$$

## Computational Implementation

### Equilibrium Determination

The model finds equilibrium through an iterative process:
- Initial guesses for income and interest rate
- Successive approximations using IS and LM curve equations
- Convergence to a point where both curves intersect

### Scenario Analysis

The implementation pretends to support:
- Monetary policy simulation (money supply changes)
- Fiscal policy exploration (autonomous consumption variations)
- International economic condition analysis (foreign interest rate
  modifications)

### Limitations and Extensions

Some things you could explore, should you care (you should not care) might be:

- Incorporate more complex net export functions
- Add exchange rate dynamics
- Implement non-linear relationships
- Enhance numerical solving methods

**Note**: This is a simplified representation intended for educational 
and analytical purposes.



# Example --- Income and IR

Our OpenISLM model has 8 inputs and two outputs (not much bang for 
the bucks!)

**Inputs:**
1. `gov_expenditure`: Government spending
2. `autonomous_consumption`: Baseline spending level 
3. `consumption_sensitivity`: How spending changes with income
4. `investment_sensitivity`: Investment response to interest rates
5. `money_demand_sensitivity`: Money demand's income responsiveness
6. `money_supply`: Total money in circulation
7. `foreign_interest_rate`: International interest benchmark
8. `exchange_rate`: Currency valuation (simplified)


**Outputs:**
- `equilibrium_income`: Predicted economic activity level.
- `equilibrium_interest_rate`: Market-clearing interest rate.

## Usage Example

To test your copy of the python module is working try running this example.
```python
# Define base economic parameters
base_params = {
    'gov_expenditure': 100,
    'autonomous_consumption': 500,
    'consumption_sensitivity': 0.6,
    'investment_sensitivity': 0.2,
    'money_demand_sensitivity': 0.1,
    'money_supply': 1000,
    'foreign_interest_rate': 0.04,
    'exchange_rate': 1.0
}

# Create model instance
model = OpenEconomyISLMModel(base_params)

# Define policy scenarios to test
scenarios = [
    {'money_supply': 1200},     # Expansionary monetary policy
    {'autonomous_consumption': 600}  # Increased consumer confidence
]

# Simulate scenarios
results = model.simulate_scenarios(scenarios)

# Display results
for scenario, data in results.items():
    print(f"\nScenario: {scenario}")
    print(f"Equilibrium Income: {data['equilibrium_income']:.2f}")
    print(f"Equilibrium Interest Rate: {data['equilibrium_interest_rate']:.4f}")
```

## A Critical Model Assessment -- Prior to Testing

Here are some things for really excessive nerds to consider.

Our proposed IS curve model:
$$
Y=(G−T) + C_0 + I_0 - b(r-r∗) + NX(Y,e)
$$
has a structure which is consistent with standard IS curve formulations, balancing
consumption, investment, government spending, and trade flows. Incorporating
$NX(Y, e)$ as a function of income and the exchange rate makes it 
quasi-dynamic and accounts for open-economy effects.

Comments on Parameters:

**(a) Net Exports $NX(Y, e)$:**  
— $Y$ dependency: Higher domestic income ($Y$) can increase imports, reducing $NX$.   
— $e$ dependency: A weaker currency (higher $e$ in a USD/foreign currency sense) can boost exports and reduce imports, improving $NX$.

**(b) Functional form of $NX$:**  For example, we could define,   
$
NX(Y,e) = a_1 - a_2 Y + a_3 e
$  
where:  
— $a_1$ captures autonomous net exports,  
— $a_2$ reflects the income elasticity of imports,  
— $a_3$ measures exchange rate sensitivity.

However, I prefer to just use data for NX, not a model fit, since most of the
input data is readily available in monthly frequency. This means we can instead
fit the parameters $a_1$, $a_2$, $a_3$ to the fetched FRED data, however this is
_not_ and ISLM prediction, bemuse neon of the inputs $Y$, $e$ are ISLM
predictions, so this is a pointless exercise unless you cannot find decent $NX$
data for your country of study.

Actually, I realise all the data for the USA will probably not be available for
any country you choose. Or it might be a pain-in-the-neck to gather, if so, then
using fits for $a_1$, $a_2$, $a_3$ from available data for a similar country can
be an option. But the USa will not be a "similar country" in all likelihood.
However, OECD countries ted to have sufficient published econometric data, so
all is probably not lost.

These comments apply to *_all_** macroeconomic modelling, not just ISLM. So we
should bookmarks these tips!


**(c) Investment Sensitivity to Interest Rates ($b$):**

— Parameter $b$ captures the sensitivity of investment to interest rate 
spreads $(r - r^*)$. If $b$ is too low, it implies weak monetary policy 
transmission.

— Autonomous Terms ($C_0$, $I_0$):   
    $C_0$ (autonomous consumption) and $I_0$ (autonomous investment) should be calibrated or estimated empirically. Time series data on consumption and investment are necessary to extract these constants.

— Open Economy Effects:   
    Including $r^\ast$ makes the model more robust to international capital 
    flow effects. However, if trade flows are small relative to GDP, the 
    $r^\ast$ term may have limited influence.

#### Suggestions for Improvement:

**Option:** You could consider explicitly incorporating expectations for $r$ or $r^*$. 
For example: 
$$
Y = (G-T) + C_0 + I_0 - b(E\[r\] - E\[r^\ast\]) + NX(Y,e),
$$
where $E\[r\]$ represents the expected domestic rate.

**Option:** We could add a sensitivity parameter, $d$, for $NX$: 
$$
Y = (G-T) + C_0 + I_0 - b(r -r^\ast) + d⋅NX(Y,e).
$$
which is admittedly nob-twiddling, but with a lemon you try to 
make lemonade?

**Option:** Test with alternative formulations of $NX$. For instance:

* Export-Led Approach: Exports depend on $Y_\text{foreign}$ and $e$, while 
imports depend on $Y$ and $e$.
* Income Effects Only: Simplify $NX$ to $NX = f(Y)$ if $e$ is stable or irrelevant.



## Towards a Working Example

Because the IS-LM is an equilibrium model, it cannot make any forecasts 
_per se_. However, we can use it (dangerously) as a tool for quasi-predicting the
model effect of changes in the inputs. This is called scenario modelling. We
think of some scenario, like an increase in the money supply, then run the model
to observe the "predicted" change in income and interest rates.

A "quasi-prediction" is a fairly hairy concept, even a government never has full
control of the inputs, especially not the behaviour of the foreign sector, 
but our cunning purpose is not to make forecasts, it is to make post-dictions. 
This is partly because our only aim in this course is to establish IS-LM is 
a bad model.

The methodology is to use macroeconomic time series up to say 12 months past,
then use the data series available from the FRED to observe the changes in the
inputs to ISLM over periods of 1, 2 to 12 months, to date. We will then run our
ISLM model with these new inputs to see what change in Income and Interest Rate
the model predicts. We then know the data for the 12 month period and so can
compare the real world data against the model post-dictions.

We will have to assume some time period for "equilibration" and for that we can
simply allow any time period from 1 to 11 months. Thus we will have eleven 
different post-dictions. If the ISLM model has any credence, then one of the 
time periods should show up as a best predictor. It might be 3 months. To 
determine which is best will just be a matter of repeating running the model for 
various historical data windows of recent years. A bit tedious, but we have 
computers to automate the task.

A full year is considered sufficient time for equilibrium. But if someone ever
wanted to assume it takes longer, then they could just use FRED data from two
years hence. This would of course be very hazardous for your mental health if
you took it seriously, since who can honestly say that an economy only gets to
equilibrium after two years, and no shocks or policy changes have every occurred
in between! This alone should raise your suspicions about whether macroeconomic
models based on concepts of equilibrium are ever valid.

Income is of course a rough proxy for economic output, which is what a society
generally wants to increase or at least improve in quality. Crudely speaking any
increase in Income is some worth of improvement in either quantity or quality of
output or both. 

This is basically the intended usefulness of the IS-LM model. Note that there is
no Unemployment input or output, so the model is pretty useless. But remember,
we persist because we desire to know the model is bad and should never be used
for informing policy. 

## Policy Recommendation Framework

Here we consider what some idiots in government policy might do if we handed
them the grenade of our ISLM model. What they might do is:

1. Compare different scenario equilibrium points (vary the inputs).
2. Note which sets of input changes result in higher Income and low interest rates.
3. Figure out the government policy options for making the input parameter
   changes if possible.
4. Advise government to change policy in the indicated direction, maybe 
increase money supply, or intervene to manipulate the exchange rate.

**Example Policy "Insight":**  
If increasing money supply from 1000 to 1200 results in:
- higher equilibrium income,
- lower equilibrium interest rate,

then tell government to spend more currency, or loosen prudential 
requirements for banks on credit-worthiness.

**Hypothetical recommendation:**  
Third Monkey Policy Wonk says: "Moderate monetary expansion could 
stimulate economic activity with minimal interest rate disruption."

Some real monkey works of policy wonkery might even suggest lowering the central
bank interest rate to "stimulate credit" hence stimulate consumption if the 
ISLM model tells them more consumption is good. But ISLM has the monetary operations
backwards, since it has the interest rate as a model output, not input! So it would
be a bit weird if the ISLM modeller gave such advice to the central bank! That
might not stop them, but it would simply be admitting the Interest Rate should
not be an output of the model, so it would just be admitting their advice is
confused and not worth listening to.

In the real world the interest rate is a policy choice, not an
equilibrium market output.  So again, we've already seen how ISLM is simply a
false model, even before empirical assessment. But like good soldiers, we will
persist in the fight, since the ISLM enemy are on little Islands in little
bunkers thinking they are still going to win the war.

Note that it might not be bad policy to lower the interest rate! So the ISLM
analysis will not always yield bad policy, but if it yields good policy it would
be largely by accident. A proper analysis using the MMT lens would just
recommend permanent Zero interest rate policy and floating exchange rate, since
this gives the government the maximum policy space for achieving full employment
with minimal inflation bias.  Whereas there are scenarios where an ISLM analysis
might recommend raising the interest rate. MMT would say this would be
unnecessary if the exchange rate is on a float.

## Last Word

Every ISLM model, or anything like it, should come with an obligatory warning
from the Surgeon General:

> **Caution:** This is a bullshit equilibria macroeconomic model, if
persistently used it can damage the health of all of society. Possibly leading
to extinction of your species.

<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../300_00_macromodels_intro">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../302_03_macromodels_islm_2">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../300_00_macromodels_intro">MM—0, Intro</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../302_03_macromodels_islm_2">MM—III, ISLM</a></td>
</tr>
</table>


