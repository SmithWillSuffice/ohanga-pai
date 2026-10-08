---
title: "Macromodels — Mosler I"
weight: 19
date: 2026-10-06
toc: true
katex: true
---

I have prepared a first implementation of `mmm_0_4.toml`, below is 
some documentaiton for mulling over. How to convince a Neoclassical this 
is better than thars?

## Initial $\sout{\text{\textbf{\textsf{Owleries}}}}$ Worries

I was worried about closing the ODE system, since we introduce the JG, but 
also the Mosler Price Setter aspect of government spending. I thought maybe 
needing to introduce a dopey target for employment, but you cannot choose the 
labour rate by policy, hence dopey. But I think we can still close the ODE 
system without introducing a target percentage for public employment. However, 
doing so requires some explicit assumptions about government staffing, 
household spending, and firms' wage-setting behaviour. 

Maybe this is ok, since "government staffing" can certainly be a policy 
choice: you tell departments to stop hiring.

## 1. File Check

The new model is designed to work with our existing TOML-to-Julia 
generator.  The code generator successfully processed the specification 
without modification.

## 2. The central economic design

The model distinguishes three employment sectors:
$$
N = L_F + L_G + L_{JG} + U_{\mathrm{open}}.
$$
Here $L_F$ is firm employment, $L_G$ is ordinary government employment, and $L_{JG}$ is Job Guarantee employment.

The government announces nominal wage offers. Its ordinary public-sector wage is
$$
w_G = w_{JG} + \delta_Gw_0,
$$
where $w_0>0$ is an independent government nominal wage reference.

Firms offer
$$
w_F = (1 + \delta_F)w_G.
$$
Consequently, when $w_{JG}>0$,
$$
w_F > w_G > w_{JG}.
$$
This implements a proposed wage hierarchy. Obviously we can reverse the 
first inequality or set it stochastic $w_F \approx w_G$.  (It is an 
interesting question whether government needs to outbid the private sector 
for comparable skilled labour, or if people prefer to work in the public 
sector?  I guess it is culturally variable?)

You can thus change the $\delta_F$ premium toml spec say to,
```toml
premium_F = -0.2
# or premium_F = 0.0
```

The positive reference wage $w_0$ also resolves an important problem: 
setting $w_{JG}=0$ does not eliminate the government's nominal 
price anchor.

Government wages and procurement prices remain defined.

The Job Guarantee is activated precisely when $w_{JG}>0$.

**TODO:** Need to enforce some model quantity limits I think, since 
here we obviously have a natural constraint,
$$
\delta_F > -1
$$
which is a design issue, since _who is to say so?!_ 
I guess the model-developer, so it should go in the TOML. The end 
user who enters a parameter outside the limits is then warned before 
compile time, before any Julia ODE solver is generated.





## 3. Price-level determination

Here I have drawn particularly on three papers.

[Tcherneva’s 2002](https://www.epicoalition.org/docs/Pavlina_2007.pdf) paper explicitly discusses the Employer of Last Resort 
as a government purchase at a fixed price, with other prices determined 
by market conditions. 

[Levey’s 2021](https://www.levyinstitute.org/pubs/wp_992.pdf) paper distinguishes the MMT explanation of the price level 
from a theory explaining subsequent inflation dynamics.

Mosler and Armstrong similarly distinguish government spending prices 
from the relative prices subsequently determined through market activity.

My proposed implementation combines a government nominal wage anchor 
with the existing firm's monopoly markup mechanism.

Define the firm's unit labour cost:
$$
P_{\mathrm{cost}}=\frac{w_F}{A_F}.
$$
Let $m$ be the monopoly markup, and $e$ measure excess demand relative 
to firm production capacity. We have a new parameter to fit, $\eta_p$ 
which is markup pressure from goods-market excess demand.

Then the firm's desired price is
$$
P_{\mathrm{target}} = (1+m)\frac{w_F}{A_F} \exp(\eta_p e).
$$
The price ODE becomes
$$
\dot P = \tau_P(P_{\mathrm{target}}-P).
$$
Inflation is as usual
$$
\pi(t) = \frac{\dot P}{P}.
$$

This provides two mechanisms: a nominal price reference transmitted 
through government wage policy, and an endogenous private-sector 
price response.

Importantly, government wage policy does not mechanically determine 
every private price. Private prices can still change because of 
productivity, markup behaviour, and excess demand.

This distinction could become central to our experiments, maybe worth 
a Dirtbag MMT preprint.

### Parameters

We cna guess a few for software development, but for $eta_p$, $e$, $m$, 
it could be a serious problem fitting them, since they are not quantities 
government statistics provide. I do not see much hope other than running 
Monte Carlo simulations, maybe combined with some LSTM/CNN models for some 
tuning, using something like [pdefinder](https://pypi.org/project/pdefinder/) , 
[DoLQ](https://github.com/topics/ode-discovery) or [pySINDy](https://pysindy.readthedocs.io/en/latest/).

## 4. Closing the labour-market equations

I had concerns over using a government employment-share target.

Instead, I introduced an ordinary public-sector *nominal payroll budget* 
$B_G$.

I mean ... it is a tricky thing, I woudl prefer figuring out some sort of 
mental model for how Parliament determens the **Size of the public sector**.
I naively woudl think it is staff numbers, given the public sector is not 
enormous, and so there is a lot of job moment slack. But it is not a 
modelling issue I have put enough thought into.

In future I might try to see if is is empirical input! (Just read the 
numbers off `foo.govt.nz`.)

Proceeding under the budget size then ...

Government employment is then
$$
L_G=\frac{B_G}{w_G}.
$$
This avoids specifying the percentage of the workforce government 
should employ.

The firm employment variable is $\lambda_F$, defined over the workforce 
remaining after ordinary government employment:
$$
L_F=\lambda_F(N-L_G).
$$
Its dynamics respond to excess demand:
$$
\dot\lambda_F = \kappa_L\lambda_F(1-\lambda_F)e.
$$

The JG subsequently absorbs the residual:
$$
L_{JG} = 
\begin{cases}
N-L_F-L_G,&w_{JG}>0,\\\\
0,&w_{JG}=0.
\end{cases}
$$

The factor $\lambda_F(1-\lambda_F)$ helps preserve the admissible 
employment interval.
We then hopefully have the mechanism I wanted: the JG is a 
passive labour buffer, rather than another employment target.

One terminology distinction: My proposed $U3=N - L_F - L_G$ is 
useful as a measure of _non-JG labour-market slack_. It is not the 
conventional [published U-3 unemployment](https://www.bls.gov/charts/employment-situation/alternative-measures-of-labor-underutilization.htm) 
statistic when those workers are employed by the JG. But I am ok calling 
it U3 since there is no US BLS statistic for a JG provision yet!


## 5. Stock-flow consistency

I added seven Godley transactions covering firm wages, public wages, 
JG wages, government procurement, household consumption, 
household taxation, and firm taxation.

There are three financial accounts:
$$
F_D,\qquad W_D,\qquad G_N.
$$
The first two are firm and household deposits. The third is the 
consolidated government's signed financial position, rather than a 
conventional government bank deposit.

The accounting equations satisfy
$$
\dot F_D+\dot W_D+\dot G_N=0.
$$
Equivalently,
$$
\frac{d(F_D+W_D)}{dt}=G-T.
$$
This gives us a useful fiscal accounting invariant.

It is not yet a complete banking-sector stock-flow-consistent model: 
bank loans, reserves, capital and several other balance-sheet items 
remain outside this model's boundary. Nevertheless, the seven included 
transactions are balanced.

## 6. The ODE's

You will see the TOMl onyl has two explicit ODE's,
```toml

[equations.ode]
# Anchored private price adjustment; not an exogenous CPI inflation process.
f_P = "tau_P*(P_target - P)"
# Within (0,1), lambda_F remains within (0,1) under this logistic adjustment.
# Employment responds to real effective demand relative to firms' output.
f_lambda_F = "kappa_L*lambda_F*(1 - lambda_F)*excess"
# f_F_D, f_W_D, f_G_N supplied entirely by the [godley] transactions above.

```
It has these two explicitly written ODEs _plus three more generated from the Godley transactions_, so the actual dynamical state is five-dimensional.

The TOML says

```toml
names = ["P", "lambda_F", "F_D", "W_D", "G_N"]
```
and then explicitly gives only

```toml
f_P
f_lambda_F
```
because `f_F_D`, `f_W_D`, and `f_G_N` are synthesized from the `[godley]` 
flows before Julia generation. So the complete system is
$$
\dot P,\qquad
\dot\lambda_F,\qquad
\dot F_D,\qquad
\dot W_D,\qquad
\dot G_N.
$$

### 6.1 ODE System: qualitative assessment

Although we did not reduce the dimensionality too much (`mmm_0_3` had 12 
dynamical variables I think) `mmm_0_4` does shift some behaviour from 
dynamical degrees of freedom into algebraic closure relations and policy rules.

In `mmm_0_3`, the intended state was roughly
$$
(P,D,\lambda,u),
$$
so price, debt, employment, and wage share all had independent 
dynamical evolution.

In `mmm_0_4`, several of those objects have instead been made algebraic:
$$
\begin{align*}
w_G &= w_{JG}+\delta_G w_{\rm base}, \\\\
w_F &= (1+\delta_F)w_G, \\\\
L_G &= \frac{B_G}{w_G}, \\\\
L_{JG} &= N-L_F-L_G
\end{align*}
$$
when the JG is active.

So yeah, government policy has constrained away some degrees of freedom. 
That is not necessarily intrinsically a regression to a lesser model 
than `mmm0_3`. Afterall, the JG is not what we have in the real world, 
but what we want to explore.

For a primitive price-anchor model `mmm_0_4` is useful because it 
lets us ask a particular question:

> _What happens to private prices and employment when the government 
fixes particular nominal terms of exchange?_

That is close to the conceptual purpose of the monopoly-money literature. 
Tcherneva's simple model explicitly treats the government price of labour 
as exogenous, rather than assigning it its own market-clearing dynamic.

But there is a genuine cost: we have currently eliminated endogenous 
wage dynamics.
And I think that this is probably one step too far constrained for the 
model we ultimately want? Although, you might think you want government to 
impose such stability?

At present `w_F` is not a state variable. It is
$$
w_F=(1+\delta_F)w_G,
$$
and because `w_G`, `w_JG`, `w_base`, `premium_G`, and `premium_F` are 
presently fixed parameters, `w_F` is constant in nominal terms.

So although we can certainly compute and plot
$w_F$
and the real wage
$$
w_F^{\rm real}=\frac{w_F}{P}
$$
the nominal firm wage itself would just plot as a horizontal line.

The real wage would still be dynamic because $P(t)$ is dynamic:
$$
\frac{w_F}{P(t)}.
$$
That already gives a meaningful time series. In fact I would definitely 
add both:
```toml
real_wage_F = "w_F/P"
```
and perhaps the public/JG counterparts:
```toml
real_wage_G = "w_G/P"
real_wage_JG = "w_JG/P"
```
Then
```toml
time_series = [
    "P",
    "lambda_F",
    "F_D",
    "W_D",
    "G_N",
    "w_F",
    "real_wage_F",
    "U3",
    "U_open",
    "L_JG",
    "pi_rate"
]
```

would work conceptually, assuming `plots4model.py` already permits 
auxiliary variables in `time_series`, which appears to be the intent of 
that machinery.

But I think there is a more important design question: should `u(t)` 
return as an actual dynamical wage variable?

I think eventually yes? Not sure. The separation would be:
$w_{JG}$ 
is the fixed policy anchor,
$w_G$
may be fixed or policy-determined, while
$$
u(t)\equiv w_F(t)
$$
is a private-sector wage that evolves dynamically.

Then the government fixes the nominal floor but does not dictate the 
entire private wage structure.

A natural first version would be something like
$$
\dot u = \tau_u \left( u_{\rm target} - u \right), 
$$
with
$$
u_{\rm target} = w_G\, R(\lambda_F,\text{labour tightness},\ldots),
$$

where $R$ is the desired private/public wage ratio.

Or, closer to your older model, one could retain a Phillips-type 
wage adjustment while imposing the JG/public wage as a lower reference:
$$
\frac{\dot u}{u} = \Phi(\lambda_F) + \text{other terms}.
$$
Then impose economically
$$
u_{\rm target}\ge w_{JG},
$$
or more realistically allow firms that offer below the JG package simply 
to fail to recruit workers.

That latter construction is better than mechanically clipping the wage 
with a `max()`, because it turns the JG wage into an actual labour-market 
constraint rather than an arbitrary numerical bound.

So I might distinguish two stages.

For `mmm_0_4a`, keep the present small model and add
$$
w_F,\qquad \frac{w_F}{P}
$$

as diagnostics. This lets us study the government price-anchor 
mechanism cleanly.

For `mmm_0_4b`, promote the private nominal wage $u(t)$ to a state variable:
$$
\mathbf{x} = (P,u,\lambda_F,F_D,W_D,G_N)
$$

so the system becomes six-dimensional, with
$$
\dot P,\quad \dot u,\quad \dot\lambda_F,\quad
\dot F_D,\quad \dot W_D,\quad \dot G_N.
$$
Then the key relative-price observable becomes
$$
\omega_F(t) = \frac{u(t)}{P(t)}
$$
which is the real firm wage.

That, I think, is closer to where you originally expected the model to 
go. The government/JG wage supplies a nominal anchor, but private wages and 
prices remain endogenous dynamical variables rather than being entirely 
algebraically chained to government policy.

So I think `mmm_0_4` is useful as the primitive benchmark. But before 
doing serious inflation simulation experiments, I would think about 
adding an endogenous private wage ODE as the next model refinement?

 
**TODO** what I really wanted to check was whether setting $w_{JG}=0$ 
recovers something like our current system, with that wasted labour, less 
output. But I worried we might then need to model an unemployment benefit 
(basic income guarantee).

### 6.2 Input Checks

I have been a bit slack about type checks and whatnot, but that's fair 
for an amature project. Life is short. But this model raises some 
immediate issues that should be part of the design of the model, and 
in the toml.

Parameter validation is hopefully only a small and worthwhile refactor. 
I will not put the limits into Python source, because the model developer 
should specify admissibility. The natural design is to add a TOML 
validation section, for example:

```toml
[parameter_limits]

[parameter_limits.premium_F]
min = -1.0
min_inclusive = false

[parameter_limits.w_JG]
min = 0.0

[parameter_limits.lambda_F]
min = 0.0
max = 1.0
```

although `lambda_F` is an initial condition rather than a parameter, so 
I should probably distinguish parameter limits from initial-condition 
limits:

```toml
[parameter_limits.premium_F]
min = -1.0
min_inclusive = false

[parameter_limits.w_JG]
min = 0.0

[initial_condition_limits.lambda_F]
min = 0.0
max = 1.0
```

Then `generate_julia_odesolver.py` should call something like

```python
validate_model_config(config)
```
immediately after

```python
config = tomllib.load(f)
```
and before either template is rendered.

The failure should be explicit, e.g.

```text
Model validation failed: mmm_0_4.toml

  parameter: premium_F
  value:     -1.2
  required:  premium_F > -1.0

No Julia solver was generated.
```
and exit with nonzero status.

We could go slightly further and make the syntax generic enough 
that it later drives the GUI as well:

```toml
[parameter_limits.premium_F]
min = -1.0
min_inclusive = false
max = 2.0
max_inclusive = true
description = "Firm/public wage differential"
```

Then the CLI validator and DearPyGui can consume exactly the same 
metadata. That avoids maintaining two separate definitions of 
admissibility.

This is probably on the order of one new validation function plus a 
call in the generator, not a redesign. I would also validate some 
structural things at the same time: every state variable has an 
initial condition, every state variable eventually acquires 
an `f_...` equation either explicitly or through Godley flows, 
unknown keys in limit sections are flagged, and perhaps basic 
time-span conditions such as `t1 > t0`, `dt > 0`. That would eliminate 
several of the failure modes we identified earlier.

## 7. Preliminary numerical checks

I tested three values of the JG wage:

| JG wage | JG active | Open unemployment | Accounting |
|---|---|---|---|
| $0.0$ | No | Nonzero | Conserved |
| $0.6$ | Yes | Zero | Conserved |
| $2.0$ | Yes | Zero | Conserved |

All three cases integrated successfully over the specified 50-year 
interval.

The maximum numerical drift in the consolidated accounting identity 
was approximately $2\times10^{-12}$ or less.

These checks demonstrate numerical closure for the tested cases, not 
macromodel validation. I am a bit behind on doing any real-world data 
validations. Where are my grad students?


## 8. Three modelling decisions

Before we develop this further, I would particularly like to nuance 
my judgement on three or four issues:

**First: ordinary government employment.** I used a nominal public 
payroll budget rather than a workforce-share target. This seems compatible 
with our objectives for this model, but it still represents an independent 
fiscal spending decision. Alternatively, we could derive government hiring 
from a demand for public services?

I'd use whichever has better empirical data we can grab and input.

**Second: firm wages.** For this first model, firms offer a fixed 
premium above ordinary government wages. This establishes a particularly 
transparent nominal anchor, but it suppresses endogenous private wage 
bargaining. We could later introduce a wage ODE responding to employment, 
productivity, or profitability.

**Third: government goods procurement.** Government purchases goods at 
its posted procurement price $P_G$, which can differ from the firm's 
private-market price $P$. Currently, the model assumes firms fulfil 
those purchases. A more complete treatment would allow firms to reject 
government bids, resulting in procurement rationing. That distinction 
may prove particularly important when studying the limits of government 
price-setting power.

There is also a productivity notation issue: I distinguish productivity 
levels $A_F,A_G,A_{JG}$ from their growth rates 
$\alpha_F,\alpha_G,\alpha_{JG}$. I have not assumed that JG labour 
has higher physical productivity than ordinary public or private employment.


### First Attempts

Keep `mmm_0_4` as a deliberately minimal model of government price 
anchoring and the JG labour buffer.

The initial system has five ODE state variables:
$$
\mathbf{x} = (P,\lambda_F,F_D,W_D,G_N).
$$
This is considerably simpler than introducing a complete capital 
accumulation and banking system immediately.

Here is a nerdy question?:

> Can we decide whether the proposed **government payroll closure and fixed firm wage premium** adequately express my macroeconomic assumptions or intuitions?

Dunno.

---

Next chapter will some some grungy stuff, a few model validations and 
unit tests. Developer issues.

But in the chapters after next we should be back to Job Guarantee models, 
and seeing some plots and all that nice end-user stuff.

I am still trying to figure out what preprint to write-up with this? 
But that "nerdy question" above 👆🏼 seems like a good use-case. 

My frame of mind is models for macroeconomics are only good for 
comparisons. But in our case we may have an exception if we can get a 
decent NZ-MMT Model with decent empirical data for fitting the parameters, 
since it could be used predictively ... is my guess. 
Still, the aim will be to compare to DGSE. I am not yet up for making 
a DGSE model, so will need to find someone sympathetic at the RBNZ to 
collaborate with who runs a DGSE or knows one, or knows someone who 
knows one. 

In the `mmm_0_4` case we are flying solo, since it is real world 
counterfactual, so we'd have to use a non-JG similar model to fit 
parameters.  Which makes me worry about needing a Basic Income Guarantee 
(unemployment benefit) model, and a pension/retirement sector! Can we 
avoid that by just reparametrization of the average wage? It would mean 
our 

> model wage  = real-world-wage + pension?

We  can eventually get the needed data for the dynamical variables, 
but the unemployment rate is only monthly frequency, and is published 
late. So we will always be using slightly out-of-date parameters.
Or predicting the near past, rather than the near future. Good 
for "would have told ya so" but not for "can NZX trade on this."




<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_00_macromodels_mosler">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../341_02_macromodels_mosler">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_00_macromodels_mosler">Macromodels — Mosler 0</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../341_02_macromodels_mosler">Macromodels — Mosler II</a></td>
</tr>
</table>


