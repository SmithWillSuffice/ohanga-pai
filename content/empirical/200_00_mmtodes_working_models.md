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


**Exercise (a bad model):** First have a look at 
<a href="../../files/bad_mmm_0.toml" download>this toml file here</a>, 
and see if you can figure out why it is a bit dopey. Hint: the dynamical 
variables should be independent.


**Solution:** Well, I did write that file, but I knew it was bad, because 
I did not think about it, and there might even be some dimensional 
inconsistencies. However, the thing which struck me next was that Price $P$ 
labour $\lambda$, and wages $u$, determine output $Y$. So we can turn that 
ODES into a $(P, u, \lambda)$ model, I reckon. Just using a few definitions.


**Modifications:** for pedagogical purposes I am going to display some 
toml files I've not generated code for, you can bother about code 
generation, but I'd counsel not to waste your time. This first chapter 
is just theory. We will get to some models we trust in theory enough to 
bother generating and running the code later on. 'and for this first fix 
we need some definitions.

The new toml spec. is:
```toml
TODO
```

**Notes:**  
The model is structurally similar to a simple Goodwin model. We have, $\dot{u}$ (which is `f_u` in the spec. file), and $\dot{\lambda}$ (which is `f_lambda`) 
written in the Goodwin forms:
<span id=eq_GoodwinDesai_model>
$$
\begin{align*}
\dot{u} \& = -c u + u f(\lambda) \\\\
\dot{\lambda} \& = a \lambda - \lambda g(u)
\end{align*}
$$
</span>

**Exercise: (Sanity Check)** For a start, examine this model and check it 
makes sense. I do not even recall if I had all $\pm$ signs correct, so you 
can really treat this specification as total raw and ready for pounding.


**Exercise: (Asymptotics):**  Now check that appropriate asymptotic 
dependence is being modelled. Nothing should be "blowing up". Note: the 
exponential grow for $A(t)$ is blowing up, but at a slow rate. You could 
replace the exponential with a sigmoidal function. Try this and see if the 
short run output significantly differs.



---

In pedagogical spirit I thought we could proceed as follows:

* mmm-0.1 Add an investment function $\mathcal{I}(u)$, but using 
"primitive debt" (no accounting variables) but with a price level.
* mmm-0.2 Try to enforce sectoral balance some way.
* mmm-0.3 Add the banking sector and accounts, so we can model 
sectoral balances correctly, and debt \&\ credit will be treated 
monetarily, instead of primitively.


What do I mean by "primitive credit/debt"? I do not really know, it 
is just a model choice before we get the proper Godley tables. But I 
guess you can think of it in monetary terms, just without accounting 
records?



### Refinement--0.1

As an exercises, create your own model that adds an Investment 
function $I(t)$. From this we can use the price model which gives $P$, 
so derive Savings and Investment in nominal terms. With no Foreign Sector 
yet (to come much later). Then in turn we will have a way to enforce 
Sectoral Balance.  But what is sectoral balance with just a closed economy? 
What two sectors are there?

(Well, you can see where this must lead: in the later refinement we will 
need to include government variables, $(G, T, \tau_r, i_G)$ --- for 
spending, tax return, tax rate, policy interest rate.  Or some similar 
minimum set.)

In the one I develop next I will us _primitive debt._ And the model 
dynamic variables will be $(P, D, u, \lambda)$.

Or $(P, D, u, \lambda, A, N)$ for longer runs when productivity and 
population, $A(t)$, $N(t)$, advance.


Crucially, "debt" will be private debt (we're ignoring government for 
now, recall! ... while we remove our toddlers wheels). This is bad of us. 
We will not have `mmm-1.0` until we get a government. 


_Rate of change of Debt_ (flow) is Investment 
less Profits from sales,
$$
\frac{dD}{dt} = I - \Pi 
$$

**Profit equation:** What about this? It will depend on sales less 
interest on debt and labour costs,
$$
\Pi = Y - w\cdot L - i_d\cdot D
$$
To avoid the pedants piling upon us, at this stage "Labour" means 
workers plus energy. But we're not going to worry for now about where 
energy comes from! It's "free", maybe from the Sun. This is of course 
terrible modelling, since oil prices for starters are a huge source 
of price instability (not so much production, since the lights will 
still go on, you just increase the price, but maybe an add to 
unemployment if import energy prices go up). We'll say domestic energy,
like food, is just part of output $Y$.

You can suppose there are primitive banks charging the interest 
$i_d$ fee.


#### Investment Curve ($\mathcal{I}$)

This is getting into some deep Keynes! But we can keep it simple.
To model an upwards (Minsky) instability we want Debt to grow with 
investment if investment gets too wild, but we have that already. What 
we need next is an investment response function that depends on profit 
to the capitalist/investor class.  


**Power Law Model:**   
A prototype model is,
<span id=eq_investment_func>
$$
\begin{equation}
\mathcal{I}(\pi) = \frac{I}{Y} = \frac{a_i}{(b_i + c_i\cdot\pi)^{\gamma_i}}  - d_i.
\end{equation}
$$
</span>
This defines the _reduced investment function_ $\mathcal{I}$. In our simple 
model it is a function of a single variable, the _reduced profit rate_, 
$\pi$, defined by,
<span id=eq_profit_reducedrate>
$$
\begin{equation}
\pi = \frac{I}{Y} = \frac{\Pi}{\nu Y} = \frac{\Pi}{K}
\end{equation}
$$

That's a lot of new free parameters above in $\mathcal{I}$! But I have 
not found ways to 
derive investment--profit relations theoretically yet, so I will suck 
this up.

We probably should not regard the exponent $\gamma_i$ as a parameter, 
since the power law is a structural constant, which likely could be 
theoretically fixed by macroeconomics theory, no modelling or data 
fitting required, a lot like a critical exponent for phase transitions. 
But to my knowledge no one has ever done this, and probably no one ever 
needs to, since empirical uncertainty swamps most such nuances. We can 
take the exponent to be $\gamma_i = 2$, without too much debate. 

But if you have any objection do let me know.

**General Exponential Model:**  
As an alternative to the power law, we can use tamer asymptotics 
by using a General Exponential response function:
<span id=eq_investment_genexp_func>
$$
\begin{equation}
\text{GenExp}(x) \quad =
(b - m) \exp\left\[ \frac{s(x - a)}{b - m}\right]  + m
\end{equation}
$$
</span>
I sometimes write this $\text{GenExp}(x; a,b,s,m)$ to emphasize the 
independent vaiable $x$ and the four parameters. The _function definition_ 
(not the function itself) is a function of the parameters and $x$. 
What values of the constant four parameters you choose is a model decision.
Both can be fit to empirical data.

You select the constants $(a,b,s,m)$ then you have yourself a particular 
function $\text{MyGenExp}(x)$.

We can use this general form for both Phillips curve and Investment 
function responses, since both are upwards curving monotonic functions 
of their single argument.


Even at this early stage you thus might wonder if we are not building 
a Ptolemaic Epicycles ODE system?

My defences is that we are not, provided the relations we model are 
based on real world institutional arrangements. It is not out fault in this 
regard that we are unaware of all the structural constants. But think about 
it! Political economy is not like the Weather or Celestial Mechanics, or even 
the carbon atom. It is far more complex, and human beings have socially 
constructed our economic systems with oodles of these parameters!  All the 
multitude of parameters are in fact real. You can see how many there are by 
browsing the legal Statutes. 

So we are in fact building a highly parsimonious model, becuas ee we 
will use far fewer arbitrary constants than there are in the real world 
macroeconomy. To a physicists, this is just one of the annoying things 
about macroeconomics. It's a hot mess of Rube--Goldberg knobs and dials.


**Capital Growth Function ($\Gamma$):**  
Sometimes it is nicer to think of investment in terms of capital growth, 
$\Gamma$, which is _defined_ as,
<span id="eq_capital_growth_rate">
$$
\Gamma = \frac{\dot K}{K}
$$
</span>
Introducing capital depreciation, $\delta$, a linear response function 
for this is,
$$
\Gamma = \frac{1-u}{\nu} - \delta
$$
You can also try a different nonlinear parameterization using two 
different constants, $\omega_K $ and $\bar{u}$, as follows
$$
\Gamma(u) = \omega_K  \ln\left\[ \frac{\bar{u} - u}{1 - u} \right\] - \delta
$$
I got this one off [Desai et al (2006)](https://www.sciencedirect.com/science/article/abs/pii/S0165188905001818) or try [pdf (here)](https://discovery.ucl.ac.uk/id/eprint/2575/1/2575.pdf).

#### Price function

The price level is determined by government, but 
before we try to get government into the model we can begin with a 
simpler mode of "cost + markup". The markup uses a monopoly parameter,
but expressed instead as a _monopolists share_ parameter $\sigma$. 
The more the monopoly power, the more the markup, the less the wage 
share, the worker share being $(1-\sigma)$.  For the 
rate of change we use a time constant, $\tau_P$.

How to use it? Well, wages $w$, and wage share is $u = w/A$. Equilibrium 
is when worker share equals wage share,
$$
(1-\sigma) P - u = 0
$$ 
so that will be proportional to $(1-\sigma) \dot{P}$ for deviations away 
from equilibrium. But what is the proportionality factor? Well, since $u$ 
and $P$ are currency units, or at least implied to be so, we need to divide 
by a time period. This will be the out-of-equilibrium time constant, which 
is typically a year to six months adjustment, though it can be empirically 
fitted later if need be, so that's our parameter, $0.5 \le \tau_P \lt 1$. 
Putting this together,
<span id=eq_price_markup_func>
$$
\begin{equation}
\frac{dP}{dt} = \frac{1}{\tau_P}\left(\frac{u}{ 1- \sigma } - P\right)
\end{equation}
$$
</span>
Empirical studies might suggest $\sigma \approx 0.2$.


**Exercise ($\Delta P$ sign):** You might wish to check the sign is 
correct. What happens if the capitalist takes everything? 

**Capitalist takes all:** $\Rightarrow$ $\sigma = 1$, and $\dot P \to +\infty$. 
Correct. That's easier to understand in reverse cause: if the price is 
set to $\infty$ the workers gets zilch.  Of course this never happens 
because capitalists want to sell at least something.

**Worker takes all:** $\Rightarrow$ $\sigma = 0$, implies the price was 
so low the workers could afford it all (this is all "in the macro" you 
appreciate, not a single firm or anything).  Then what happens?   
**When $u < P$ :** then there is downwards price pressure, due to workers 
unable to buy all the goods. Correct.   
**When $u > P$ :** the sales $P$ is a upwards price pressure, $\dot P > 0$, 
due to high effective demand from $u$. Correct again.


In a market economy with government the currency monopoly, the 
sectoral balance will be needed to get a proper price function. That's 
because it is government spending $G$ which sets the price level.
We will leave this as a TODO later. (Especially because I've never come 
across dynamical models where this has been taken into considerations, and 
I'm still thinking about how best to model this.)


#### Phillips Curve ($\Phi$)

Without explicit accounting systems, a Phillips Curve 
is practically necessary in the model because we need some way to enforce 
the constraint $0 \gt \lambda < 1$. One way is to have a Phillips Curve 
$\Phi(u)$ which diverges at $\lambda = 1$. The conventional form is,

<span id=eq_phillips_curve>
$$
\Phi(\lambda) = \frac{d}{(1 - \lambda)^\gamma} - c
$$
</span>
A numerical problem with this form is that unlike an exponential, it 
requires careful tuning of the constants, since they have dimensions, so 
if you use arbitrary constants you risk ODE instability. That just means it 
can be a little painful trial and error to get good constants.

How does this asymptotics work? Well, we need one of the derivatives to 
also diverge at $\lambda = 1$. Which one? It is not going to be Debt or 
Output ($Y$) right?  A finite $L=N$ number of workers cannot generate 
diverging output or debt for investors. Thus (in the present modelling) it 
has to be in $\dot u$, in the wage share.

**Warning!** One thing computationally you need to worry about is if you choose 
a fractional $\gamma_p$, say $\gamam_p = 1.3$ and you do not have good 
asymptotics for $\lambda$, since of $\lambda > 1$ you will get a root of 
a negative number for the power law Phillips curve. While python can 
handle that, the usual solvers from numpy, scipy or gnuScienceLib probably 
do not work with complex functions, Julia would need a complex package, 
but in both languages this is unlikely to play well with your ODE solver.
This is why $]\gamma_p = 2.0$ is "numerically safe" even if not perfectly 
empirically accurate.

If you scroll back, you see we already had this correct 
functional response in the wage share ODE $\dot u$, 
([see above](#eq_GoodwinDesai_model)) we just re-write it now using the 
more suggestive symbol $\Phi$ for $f$ (they're the same thing):
$$
\dot{u} = u \cdot\bigl( c - \Phi(\lambda) \bigr)
$$


**Exercise:** No need to write toml for this just yet, but have a think 
about what you need to change to introduce a Job Guarantee labour 
buffer?, hence full employment $\lambda = 1$ permanently. Hint: we still 
need to use the Phillips curve with that divergence, otherwise we have 
no buffer mechanics.


#### Employment and Output

Recall(?) these are not independent, so our model dynamical variables are 
either $(\lambda, u, P, D)$ or $(Y, u, P, D)$.  I usually go for $\lambda$ 
and think of output $Y$ as dependent on labour.  But what is the substitution?

It is easiest for me to begin with a reasonable definition of output:
$$
Y = \lambda A N
$$
For _macroeconomics_ that is a pretty hard & fast definition. Differentiating 
using the product and quotient rules, we see,
$$
\begin{align*}
\frac{\dot Y}{Y} \& = \frac{\dot \lambda}{\lambda} + \frac{\dot A}{A} + \frac{\dot N}{N} \\\\
\& = \frac{\dot \lambda}{\lambda} + \alpha + \beta\\\\
\therefore\qquad \frac{\dot \lambda}{\lambda}\& = 
\frac{\dot Y}{Y}  - \alpha - \beta
\end{align*}
$$
The second line there is a short run model $A(t)$and $N(t)$ where can be 
regarded as slow exponentials, 
so basically linear. We really want them sigmoidal, but in all honesty who 
knows where the inflexion point is?  Even a linear function will suffice 
from an empirical fit 0--- which is because we never inted to run our MMT 
models for more than a year or two. Why? I told you earlier: because it 
would be silly to do so, every bit as silly as using a two week weather 
forecast to extrapolate out to a year.

Anyhow, exponentials make it easier in this case since then 
$\dot{A}/A = \alpha$, the productivity growth rate. Same for 
$\dot N/N = \beta$, the population growth rate. Heck dude! You just manually 
tweak these year-to-year as census data comes in. What else are you going 
to do? Predict female birth propensity? Predict scientific innovation? 
(No, and No.)

Now looking back at the 
[capital growth rate](#eq_capital_growth_rate), $\Gamma$, and noting 
$Y = K/\nu$, we have $\dot Y/Y = \dot K/K$, hence can write,
<span id="eq_goodwin_lambda_ode">
$$
\begin{align*}
\frac{\dot \lambda}{\lambda} \&= \Gamma(u) - \alpha - \beta \\\\
\therefore\qquad \frac{d\lambda}{dt} \&= \lambda\cdot\left(\Gamma(u) - \alpha - \beta\right)
\end{align*}
$$
</span>
Because we've already defined $\Gamma(u)$ this is all, for now, for 
the $\lambda$ equation. Later refinements will come when we consider 
more complicated models.

### The Production Function $Y(K, L)$

The Leontief function is widely regarded as the simplest of the physically 
well-justified models, assuming $L$ is labour + energy. This beggars 
belief a bit, since energy adds to costs, hence price, but we're going to 
ignore that for now. Note that presently our ODES does not incorporate 
the Price ODE, even though we have one. It is autonomous, purely dependent 
on the mechanics of the Cycle. This is because we have not incorporate 
Government into the model yet, despite this being our grand ultimate 
objective!

Anyhow, 
$$
\text{Leontief:}\quad Y = \text{min} \left\\{\frac{K(t)}{\nu}, A(t)L(t)\right\\}
$$ 
but we've been assuming $Y = K\nu$. This is justified as the 
assumption of full utilization of capital: $K\/\nu \approx L N$.

**Exercise:** What can you do if empirically you know this is not the case?
Say $K\/\nu < L N$? Doesn't that just mean you can redefine $\nu$?

In which case, you aught not lie about it, and you say we have a _structurally 
effective_ $\nu\_\text{eff} < \nu$, such that $LN=K/\nu_\text{eff}$. If you 
are a policy person you might then 
wish to research into why this is so, if you think the Leonteif model is ok.
But seriously, are you going to put research resources into this? The 
macroeconomy is far too messy and gnarly to worry with this, I would say. 

> What matters is full employment and decent livelihoods for all people.

The MMT dynamics, and especially what the Price level is doing, are nothing 
compared to this objective. And no ODE solver analysis is going to help you 
achieve this objective. Hence, no, I don't care if the Leontief model is a 
bit unrealistic.

That all said, I am going to save this Goodwin Model and run it to check 
the software system is working.

### A Puzzle --- Closing the ODE

While writing the first draft I had got to this point:
$$
\begin{align*}
\dot u \&= u \cdot(c - \Phi(\lambda)) \\\\
\dot \lambda \& = \lambda \cdot ( \Gamma(u) - \alpha - \beta ) \\\\
\dot D \&= I - \Pi \\\\
\dot P \&= \frac{1}{\tau_P} \cdot \left(\frac{u}{1 - \sigma} - P\right).
\end{align*}
$$
The price equation is nicely _in your face_ there in large fractions! Sort 
of perversely fitting, since it is the odd one out, it can be dropped and 
we'd still have a valid ODES. But I've left it alone since maybe it is 
nice to track "inflation" in simulation real-time.

Is this a well-defined ODES?
This is a nice student exercise.

**Exercise:** Close the ODE system, that is, find the substitutions needed 
to get all dynamical variables on the left in terms of known functions 
of time $t$ or the current variables at time $t$, $\lambda(t), u(t)$ etc.
Hint: $\Gamma(u)$ is fine, that's a response function we have defined.

**Solution?:** The difficulty I had was an apparent inconsistency, since 
in back-tracking to compute investment $I$ and profit $\Pi$ for the $\dot D$ 
response, I had two different solutions. So I had to do some algebra 
detective work to avoid a circularity or over-determination.

We had, I believe,
$$
I(\pi) = Y \cdot \mathcal{I}(\pi)
$$
which seems ok, since $\mathcal{I}(\pi)$ was that power law, or the GenExp 
response function, it just depends on $\pi$. OK, but what is $\pi$?
We had,
$$
\pi = \frac{\Pi}{Y} = \frac{\Pi}{\lambda A N}
$$
that's ok. But I've dropped the independent variables, since I forgot what 
$\Pi$ depends upon. All we see there is $\pi = \pi(\lambda)$ which would be ok. 
So what is $\Pi$? We had a practical definition,
$$
\begin{align*}
\Pi \&= Y - uAL - i_d D \\\\
\&= Y - uA^2 \lambda - i_d D
\end{align*}
$$
I think that's all, the end of the line. All three terms are now 
consistently determined by $(u, \lambda, P, D)$, or really in this 
simple model by $(u, \lambda, D)$.


**Exercise:** Check this is so. If it is not then fix it! 

I myself will quit at this point and declare victory since life is too short.
Plus, my feelings for full employment do not care about my mathematics.

#### Productivity Squared

This was the first time I noticed this modified Goodwin system depends 
on $A^2$. A little nonlinearity.  Where''s the turning point I wondered? 
Since $A(t)$ is growing slowly it is not too important, but I did wonder 
if I'd got the dimensions correct? That's hard to check without some Typing 
(_data types_, not keyboard bashing). 

**Exercise:** Is the $A^2$ dependence correct there?

Should we spell out the $\dot D$ equation? Well, we now understand,
$$
\pi = \pi (\lambda, D)
$$
so we have got,
$$
\begin{align*}
\frac{dD}{dt} \& = \lambda A N \mathcal{I}(\lambda, D) -\Bigl( \lambda A N - u A^2 \lambda - i_d D \Bigr)\\\\
\& = \lambda A N \cdot\bigl( \mathcal{I}(\lambda, D) - 1\bigr) + u A^2 \lambda + i_d D
\end{align*}
$$
where,
$$
\mathcal{I}(\pi) = \frac{a\_i}{(b_i + c_i \pi(\lambda, D))} - d_i.
$$
Is the full stop for real now?

Well, I doubt there are any cancellations to be made or anything, so yeah, I 
think that's it for now.


#### Simulation Game-0.1

This model `mmm-0.1` is worth running through the software package.























### Refinement--0.2


**Issue 1.**
The clear issue I have with the above model is no clear sectoral balance, 
since it is a One Sector model (a closed PK circuit). 

**Issue 2.** I want the government as currency monopolist to get a proper 
MMT system. So we need to change the Price equation, and put the price level 
into the dynamics somehow, at a minimum as a policy response pressure.

**Issue 3.** In my Goodwin model from about a decade ago, I saw that I wrote an 
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

[equations.auxiliary]
I = "s * Y - (G - T)"
# ... other auxiary functions as before
```
We're not finished, because we need to get $I$ into the ODE system. 
How would _you_ do this?


### Refinement--0.3

We'd rather not write an arbitrary Investment function, right? The level 
of investment should be determined by the interest rates. But in a 
government centred economy --- like every nation today- --- the interest 
rate is a policy parameter. So we can just look-it-up from the FRED or 
wherever. The banker only needs a credit-worthy customer. This is good 
for us, it means we do not need to solve some awful market equilibrium 
problem.


```
TODO
Use my PDFLaTeX notes.
```










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
