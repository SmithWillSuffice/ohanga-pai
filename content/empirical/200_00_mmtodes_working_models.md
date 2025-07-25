---
title: "MMT-ODES Working Models — I"
weight: 7
date: 2025-07-24
toc: true
draft: false
katex: true
---

In this series I am going to indulge in some pedagogy. We will show all 
the mistakes and bugs (or at least one high-level view of them) --- the 
purpose being educational. I make no claim to be an expert on macroeconomics 
modelling, so the models we develop should be in every case regarded as Toys.
(But see [notes at the end](#getting-to-pro-models) for what you might 
do to build a serious model kit.)

## Assumptions

Will will build up in complexity from a Sectoral Balance  Model to eventually 
a full Credit--Debt monetary model.

* Government is the currency monopolist.
* No geopolitics considerations.
* Treat the **MMT** models as like a Weather system --- nonlinear, so only 
short run simulations have any predictive meaning. Long-run simulations are 
"not even _Economic Climate_" since the government policy parameters will 
likely change.

## Methodology

The ODE System is completely specified by a toml file.  My software system 
automatically generates Julia solvers from the toml. We get a cmdl version 
and a version that should work with a GUI (I use dearpygui for speed and 
the cool retro look). 

Here is an example for a damped pendulum**:
```tomlrm 
model_name = "pendulum"

[parameters]
mass = 1.0
length = 1.0
damping = 0.1
g = 9.81

[variables]
names = ["theta", "omega"]

[initial_conditions]
theta = 0.785398
omega = 0.0

[equations.auxiliary]
# none for this model

[equations.ode]
# dy/dt = f(y, t)
# Use Julia-like syntax here
f_theta = "omega"
f_omega = "-damping * omega - (g / length) * sin(theta)"

[tspan]
t0 = 0.0
t1 = 100.0

[solver]
dt = 0.01
method = "Tsit5"  # or "DP5", "RK4", "Rodas5", etc.

[plots]

# Optional: restrict which time series to show (omit to show all)
time_series = ["theta", "omega"]

# Optional: phase plots, list of variable pairs or triples
# Each entry is a list of 2 or 3 variable names
[[plots.phase]]
vars = ["theta", "omega"]      # 2D plot
aspect = [1.0, 1.0]        # Optional: scaling for x:y
```

You can ignore the plotting, I use a plotly script to post-process the 
results, but will not be teaching that today.


## Model-0

**Description:** The stupidest model I could think of, without any serious 
literature research.


For our first Model we will start with a pretty crappy ODES, it is 
nothing more than a crude attempt to put some words into the form of ODE's.
I literally did next to no thinking for this. 

**MMM** refers to Monetary Minsky Model. Although this one for starters 
does not have much money, we have no Godley Tables. 

The toml spec. is:
```toml
model_name = "mmm_model_0"

[parameters]
K = 100.0              # Total capital
nu = 2.5               # Capital-output ratio (Y = K / nu)
alpha = 0.02           # Productivity growth (A = A0 * exp(alpha * t))
N = 100.0              # Total labor force
J = 0.5                # JG share of buffer policy (0 = BI-only, 1 = JG-only)
J_u = 0.7              # JG wage as share of normal wage (u)
gamma = 0.05           # Phillips-like inflation responsiveness
i_G = 0.0              # Policy interest rate (govt)
i_S = 0.03             # Bank spread above govt rate
monopoly = 0.2         # Markup percentage on firm costs
theta = 0.1            # Sensitivity of inflation to utilization (Y / Y_max)
r_T = 0.25             # Effective tax rate

[variables]
names = ["Pi", "Y", "u", "lambda"]

[initial_conditions]
Pi = 1.0
Y = 50.0
u = 0.6
lambda = 0.9

[equations.auxiliary]
A = "exp(alpha * t)"
K_r = "K * lambda"                  # Capital used in regular sector
K_j = "K * (1 - lambda)"            # JG sector gets remaining capital
Y_r = "K_r / nu"                    # Regular sector output
Y_j = "J * (1 - lambda) * N * J_u * u * A"  # JG sector output, scaled by JG wage
Y_total = "Y_r + Y_j"

capacity_utilization = "Y / Y_total"  # For inflation term
interest_rate = "i_G + i_S"

[equations.ode]
# Price pressure from demand + monopoly power.
f_Pi = "gamma * (Y - Y_total) / Y_total + monopoly * u * A * lambda + theta * capacity_utilization + 0.5 * (1 - J) * (1 - lambda)"
# Nominal output expands with productivity and labor
f_Y = "alpha * Y + u * A * lambda * N"
 # Wage increases if labor market tight
f_u = "gamma * (lambda - 0.95) * u"
# Adjust employment rate toward output-labor ratio
f_lambda = "0.1 * ((Y / (A * N)) - lambda)" 

[tspan]
t0 = 0.0
t1 = 50.0

[solver]
dt = 0.1
method = "Tsit5"
```

**Notes:**  
The model is structurally similar to a simple Goodwin model. We have, $\dot{u}$ (which is `f_u` in the spec. file), and $\dot{\lambda}$ (which is `f_lambda`) 
written in the Goodwin forms:
$$
\begin{align*}
\dot{u} \& = -c u + u f(\lambda) \\\\
\dot{\lambda} \& = a \lambda - \lambda g(u)
\end{align*}
$$

**Exercise: (Sanity Check)** For a start, examine this model and check it 
makes sense. I do not even recall if I had all $\pm$ signs correct, so you 
can really treat this specification as total raw and ready for pounding.


**Exercise: (Asymptotics):**  Now check that appropriate asymptotic 
dependence is being modelled. Nothing should be "blowing up". Note: the 
exponential grow for $A(t)$ is blowing up, but at a slow rate. You could 
replace the exponential with a sigmoidal function. Try this and see if the 
short run output significantly differs.

### Refinement---0.1

As an exercises, create your own model that adds an Investment 
function $I(t)$. From this we can use the price model which gives $\Pi$, 
so derive Savings and Investment in nominal terms. With no Foreign Sector 
yet (to come much later). Then in turn we will have a way to enforce 
Sectoral Balance.

In my Goodwin model from about a decade ago, I saw that I wrote an 
investment function. It used a depreciation parameter $\delta$, but this was 
not automatically guaranteeing sectoral balance consistent. So today I am 
trying a different way to get an investment function. Since $I$ is in the 
Sectoral Balance, we can simply make it a dependent variable. Drop the 
depreciation parameters $\delta$, and instead us a savings desires 
parameter $s$ (same thing, from a different point of view... well, roughly).
I think this is advantageous, since savings desires are measurable, while 
depreciation is a dodgy parameter (possibly reasonably constant, but hard 
to quantify).

You recall what this is? _Sectoral balances always sum to zero._ 

<span id=two_sector_balance>
$$
\text{(Two Sector Balance)} \quad (G-T) + (I - S) = 0.
$$
</span>
Go ahead and wite a toml spec for this revised model.


```
TODO
Investment function, and Savings.
```
One option which increases to code complexity is to run a loop inside 
the solver to enforce Sector Balance. But a cleaner solution, I think, 
is to make one of the terms a dependent variable:
```toml
[parameters]
s = 0.2    # Savings desires
# ... other parameters as before


[auxiliary]
I = "s * Y - (G - T)"
# ... other auxiary functions as before
```
We're not finished, because we need to get $I$ into the ODE system. 
How would _you_ do this?















I think that's it, I think, for MMM.0.1. Try and see if it compiles and runs.

---


**Exercise:** Have a think about the need for a Foreign Sector? Is there 
a need?

Hint: The MMT lens is perfectly good for "highly macro", meaning we can 
have Two Sector Balance, just Government and Non-Government. What is the 
loss in using a Two Sector model?

**Reflections:** In MMT unemployment is _defined_ by:

> **(Unemployment)** _People seeking to exchange their labour or goods 
for tax credits._

But wat... that means we do not need a Foreign Sector. Foreigners needing our government scorepoints are unemployed in our currency, which is a waste 
of human lives (or at least some sort of dopiness needing elimination --- 
maybe the Aussies borrowed some NZD off us, for whatever silly reason). 

Unemployment of NZ dollars is pointless, so we can really regard foreigners 
as part of our economy, they are "Kiwis who do not live in NZ and do 
not own NZ things." You can add,  "... and who do not pay NZ taxes." 
Big deal, whoop-dee-doo.

What's the downside then?

Obviously we will not have any iodea about international fincial flows, 
and FOREX and sop forth can be a source of parasitic wasteful human 
activity, so it might be nice to use  a Three Sector model. But if we are 
not too worried about those flows, then we should not care.


### Remarks on MMM-0

### Running the Simulation



## MMM-1 --- Slightly Monetary

The next job is the modify MMM-0 to at least have some stock--flow 
consistency. We will do this by merely ensuring Sectoral balance.
No banking needs to be developed.

This should actually be ok. The bankig system in part plays a vitalrole 
in clearing payments, but if we are not too concerned with household debt crises, then a simpel Sectoral Balance model shoul be ok for short run simualtions.
























## Getting to Pro Models

Just a quick note on what to do if you are a salaried professional, but 
have no experience in building ODES models.

1. Take the Toy model and add whatever features you think necessary for 
more realism, which will not be computational no-gos; and remove bits of 
the model you think are superfluous.
2. Fetch relevant real world data for the government of interest. My minimum 
set currently is: (1) Unemployment (U6); (2) wage share; (3) output, 
(4) price level (CPI is only a rough approximant). Then we need the policy 
parameters: (5) interest rates (at least two); (6) tax rate (effective average).
3. Use parameter fitting tools, like Monte Carlo nonlinear regressions to 
get fits to your other model parameters and structural constants.
4. Needless to say, if you fitting was for 2023-Q1 data, then your 
testing needs to be for 2024-Q1, and then your forecasting can be made 
for 2025-Q1.

### Time Periods

I have no idea yet, but I think it'd be unwise to run an MMT model for 
more than a quarter of the next year. But the idea would be the model has all 
four quarterly parameter adjustments. So we'd be able to in a single 
run integrate the ODE for 12 months. Any longer is mere **policy analysis** 
(the "what if's"), not **not forecasting**.


### Fetching Data

The USA is the best studied case, since the FRED have all the empirical data 
you would need to get a nice fit. Maybe also the EU as a whole? Maybe also 
the UK? But I have not looked into other nations.  Fetching time series 
from the OECD and BIS portals can be automated, just not as smoothly as 
with the FRED.

For NZ I could not find good Treasury Statements except form the NZ Treasury
XLS spreadsheets. StatsNZ is too cumbersome, and does not have the Treasury 
data in any convenient form I can find.

If you want to develop some neural net predictors in parallel with ODES 
models then banking sector data can be useful, but again our RBNZ does not 
have a seamless portal for fetching this data from what I can tell.

Part of the problem here is that I am only doing this as an unpaid 
volunteer, working "for the community" (I am my own boss, and I raise my 
pay by 100% every year). If some pro time were devoted to the effort then 
perhaps we could build a nice MMT data portal for NZ.




<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../100_00_nzecon">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../100_00_nzecon">NZ ECON — 0</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../">(TBD)</a></td>
</tr>
</table>
