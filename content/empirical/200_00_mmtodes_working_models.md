---
title: "MMT-ODES Working Models — I"
weight: 18
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

## Methodology

The ODES is completely specified by a toml file.  My software system 
automatically generates Julia sovlers for the toml. We get a cmdl version 
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

## Model-0

Description: The stupidest model I could think of, without any serious 
literature research.









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
