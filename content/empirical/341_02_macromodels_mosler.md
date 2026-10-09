---
title: "Macromodels — Mosler II"
weight: 20
date: 2026-10-07
toc: true
katex: true
---

## Basic Model Validations

To date just input parameter limits, not much else. As I wrote earlier, I 
was too lazy to implement a lot of type-checking. The rule is thus 
_model-developer responsibility_. We can be consenting adults about model 
hygiene, and you can be as dirty as you please, but today I have 
implemented a way the TOML specifier-developer can impose some purity:

* parameter limits,
* variable initial condition limits.
 
These will be useful for my hopeful GUI, dearpygui. I just love the retro 
look and the speed of dearpygui, and am almost making the GUI just to 
say be able to boast that I once used this library! I already used 
dearpygui for a high-school level pendulum simulation, but to do one 
for MMT is too good to pass up.


**Example:  Lorenz attractor**

Here is the full toml: 
<a href="../../files/lorenz_attractor.toml" download>lorenz_attractor.toml</a>

Here is just the input validation bit:
```toml
# Physical Lorenz-convection parameter domain. The mathematical ODEs can be
# extended outside this domain, but this saved model is intended to represent
# the standard convection interpretation.
[limits.parameters.sigma]
min = 0.0
min_inclusive = false
description = "Prandtl-like parameter sigma must be positive"

[limits.parameters.rho]
min = 0.0
description = "Rayleigh-control parameter rho is nonnegative in this model"

[limits.parameters.beta]
min = 0.0
min_inclusive = false
description = "Geometric dissipation parameter beta must be positive"
```

I know ... I do not like the expanded data structure of toml, it gets 
bloated quickly, and it is nicer to specify a data type all-in-one 
(name, type, value, limits) but who has the time? 

With the help of Claude.ai I can easily write unit tests for a lot of the 
new PukahaPai software. So we are able to progress faster than in the 
early 2020's. However, I have a bad habit of not reading the unit tests 
carefully, I just browse them, so this is also incurring possible technical 
debt. At this stage in life, too bad. No grandkids will have to pay it off!


## Local Stability 

I had a $\pm$ sign wrong in the Julia templates!  Hopefully this is now 
fixed. But I had to run some tests to check. 

My previosuly generated Julia templates compute the Jacobian of 
the DAE residual
$$
F(\dot{\mathbf x},\mathbf x,t) = \dot{\mathbf x}-\mathbf f(\mathbf x,t).
$$
Holding $\dot{\mathbf x}$ fixed,
$$
\frac{\partial F}{\partial \mathbf x} = -\frac{\partial\mathbf f}{\partial\mathbf x}.
$$
The old templates were taking eigenvalues of $\partial F/\partial x$ 
directly. For ODE stability we need eigenvalues of
$$
J_{\rm ODE} = \frac{\partial\mathbf f}{\partial\mathbf x}
 {} = -J_{\rm residual}.
$$

So the actual fix was to both Julia templates:

```julia
J_residual = ForwardDiff.jacobian(u_var -> begin
    tmp = similar(u_var)
    dae!(tmp, du, u_var, p, t)
    return tmp
end, u)

J_ode = -J_residual
return eigvals(J_ode)
```

`plots4model.py` did not need changing.

I did make a small revision to `stability.py`, but for a different 
reason: to centralize the local-stability criterion, add a numerical 
tolerance, improve CSV-header handling, and avoid claiming more than the 
calculation establishes. The report now says “local Jacobian stability 
criterion” rather than asserting global nonlinear stability.

There is one important correction to my expectation about the 
Lorenz ODE system. The standard Lorenz parameters you currently use,
$$
\sigma=10,\qquad \rho=28,\qquad \beta=2.6,
$
are deliberately in the familiar chaotic regime. So are perhaps not a 
stable test case --- even though the attractor is bounded.  But there 
should be no fixed points? 

In particular, the origin is an equilibrium and for $\rho>1$ it has a 
positive Jacobian eigenvalue. At the origin,
$$
J = \begin{pmatrix}
-\sigma & \sigma & 0 \\\\
\rho & -1 & 0 \\\\
  0  &  0 &-\beta
\end{pmatrix}.
$$

For my parameters one eigenvalue is positive, so the origin is 
linearly unstable.

That is actually useful. The new `lorenz_attractor_unstable.toml` I wrote
uses,
```toml
x = 0.0
y = 0.0
z = 0.0
```
with $\rho=28$. The numerical trajectory therefore remains exactly at 
the equilibrium, while the Jacobian says unambiguously “unstable.” It is 
a good regression test.

The pendulum gives the complementary stable case. At its downward 
equilibrium,
$$
\theta=0,\qquad \omega=0,
$$
the ODE Jacobian is
$$
J = 
\begin{pmatrix}
  0     & 1 \\\\
-g/\ell & -d
\end{pmatrix}.
$$
Its characteristic equation is
$$
\lambda^2 + d\lambda + \frac{g}{\ell} = 0,
$$
so for positive damping,
$$
\Re(\lambda) = -\frac d2<0.
$$
With my $d=0.1$, that gives real part $-0.05$.

This provides a nice test of the original bug: the residual Jacobian has 
the opposite eigenvalues and would report real part $+0.05$, falsely 
classifying the damped pendulum as unstable.

The new tests all passed.


The five tests cover:

```
pendulum equilibrium                    stable
old residual sign on pendulum           incorrectly unstable
corrected residual sign                 stable
standard rho=28 Lorenz origin           unstable
dedicated unstable Lorenz model         unstable
both Julia templates                    contain J_ode = -J_residual
```

I also rendered the revised template through my current julia code 
generator. The generated pendulum solver now contains:

```julia
J_residual = ForwardDiff.jacobian(...)
J_ode = -J_residual
return eigvals(J_ode)
```
and I fixed a small adjacent issue in the templates: the eigenvalue 
CSV header is now generated with exactly the correct number of 
eigenvalue columns, e.g.

```
t,e1,e2
```
for the pendulum rather than the previous placeholder

```
t,e1,e2,e3,...
```
That lets `stability.py` read the CSV normally with its header.


***A Caution:** 

One conceptual caution is worth noting. For the nonlinear Lorenz 
trajectory, “instantaneous Jacobian has a positive eigenvalue” is a 
_local linear_ statement. It is not by itself the same thing as a 
Lyapunov-exponent calculation or a theorem of global instability. 
For equilibria, however, the Jacobian eigenvalue criterion is exactly 
the standard local stability test. That is why the pendulum equilibrium 
and the Lorenz origin make good unit tests.


## Lyapunov Analysis

I never got around to Lyapunov analysis when I was doing 
magnetohydrodynamics the old way. It makes me nostalgic.  But with the 
LLM's I think we have enough power to get a Lyapunov analysis up and 
running in a few hours. Much less nostalgia, not as much fun. So I 
undertook this with a heavy heart. I just do not have time to dig up the 
old textbooks and go for it solo. Honestly, it is a bit depressing. If I 
had income security I would just go and do it all the old human way for 
the pure fun of it.

It is bad man.  It is actually the sort of point where I just want to 
give up doing this stuff.  At least we can still enjoy the theory. 
So I am here for the theory, such as I can recall it.

Lyapunov analysis is intended for nonlinear models where 
local Jacobian stability can be misleading.

The Jacobian test is at a particular state $\mathbf x(t)$, computing,
$$
J(t)=\frac{\partial f}{\partial x}\bigg|_{\mathbf x(t)},
$$
and examines the instantaneous linearized dynamics. At an equilibrium, 
this is the standard local stability test. Away from an equilibrium, 
however, it is only an instantaneous statement.

A Lyapunov exponent instead asks what happens to an infinitesimal 
perturbation after it has evolved through the entire time-dependent 
dynamics:
$$
\dot{\delta x}=J(t)\delta x.
$$
The largest Lyapunov exponent is essentially
$$
\l ambda_{\max} = \lim_{T\to\infty}
\frac1T \ln\frac{\|\delta x(T)\|}{\|\delta x(0)\|}.
$$
Its interpretation is fairly simple:
$$$
\lambda_{\max} < 0
$$
means nearby trajectories converge,
$$
\lambda_{\max} = 0
$$
means neutral separation, and
$$
\lambda_{\max} > 0
$$
means exponential sensitivity to initial conditions.

That last case is the characteristic diagnostic of deterministic chaos.

For our purposes this is useful for two reasons. First, the 
Lorenz attractor is a canonical example where an instantaneous Jacobian 
analysis is not an adequate description of long-run behaviour. Second, 
macroeconomic models may eventually have cycles, quasi-periodic solutions, 
transient instability, strange attractors, or complicated policy-regime 
dynamics. A Lyapunov diagnostic tells us whether small modelling or initial-
condition perturbations actually amplify over the simulated trajectory.

I would therefore regard the two analyses as complementary rather than alternatives:
 
> Jacobian analysis} = local linear stability

and

> Lyapunov analysis =  trajectory-level sensitivity/stability.

For the pendulum, with damping and eventual relaxation to the 
downward equilibrium, we should obtain a negative largest Lyapunov 
exponent after the transient. For the standard Lorenz parameters near
$$
\sigma=10,\qquad \rho=28,\qquad \beta\approx 8/3,
$$
we expect a positive largest exponent, because that is the chaotic regime.

The special `lorenz_attractor_unstable.toml` we just made is actually 
a different type of test. Starting exactly at the unstable origin,
$$
(0,0,0),
$$
the trajectory remains exactly there numerically, while perturbations 
grow. Both the Jacobian and Lyapunov analysis should therefore identify 
instability. That makes it a useful validation model, but it does not 
test chaos as nicely as the ordinary Lorenz attractor does.

We can initially compute the largest Lyapunov exponent, 
$\lambda_{\max}$. That gives almost everything we need for a first 
diagnostic and avoids unnecessary code.

The desired numerical output could be a CSV such as

```text
t,lambda_max
0.0,...
1.0,...
2.0,...
...
40.0,...
```
where `lambda_max(t)` is the accumulated finite-time estimate
$$
\lambda_{\max}(t) = \frac1t\sum_k
\ln\frac{\|\delta x_k^{\rm before\\,renorm}\|}
              {\|\delta x_k^{\rm after\,renorm}\|}.
$$

The main plot would then show convergence of the finite-time estimate 
toward its asymptotic value.

A useful HTML summary could say something like

```text
Largest Lyapunov exponent: +0.87 / year
Classification: chaotic / exponentially sensitive
```
or

```text
Largest Lyapunov exponent: -0.05 / year
Classification: asymptotically stable
```
with a tolerance around zero.

Later, if useful, we could calculate the complete spectrum
$$
\lambda_1\geq\lambda_2\geq\cdots\geq\lambda_n.
$$

For Lorenz, the spectrum is especially informative because a chaotic 
attractor typically has one positive exponent, one approximately zero 
exponent associated with motion along the flow, and one negative 
exponent. The sum also measures phase-space volume contraction.

For the macroeconomic models, though, I will begin with just 
$\lambda_{\max}$.

As for architecture: this can remain largely analogous 
to `stability.py`, but there is one mathematical complication ...

`stability.py` can consume eigenvalues already written by Julia. 
Lyapunov exponents cannot in general be obtained by simply averaging 
the instantaneous Jacobian eigenvalues. The Jacobians at different 
times do not generally commute:
$$
J(t_1)J(t_2)\neq J(t_2)J(t_1),
$$
so the orientation of perturbation vectors matters.

We must actually evolve the tangent equation
$$
\dot Q=J(t)Q.
$$
For the largest exponent, this can be just one perturbation vector:
$$
\dot v=J(t)v,
$$
with periodic renormalization.

For the full spectrum, one evolves a matrix of tangent vectors and 
periodically applies QR orthogonalization.

So this architecture should suffice:
```
TOML
  |
  v
generated Julia model
  |
  +--> ordinary trajectory CSV
  |
  +--> Lyapunov calculation
           |
           v
      *_lyapunov.csv
           |
           v
      lyapunov.py
           |
           v
      Plotly/report tab
```

The numerical Lyapunov calculation should probably remain in Julia, 
because Julia already has the model RHS and automatic differentiation 
available.

The new module `lyapunov.py` would then play essentially the same role 
that `stability.py` does now: read the numerical results, classify 
them, and produce plotting/report information.

That avoids reimplementing the entire TOML expression evaluator in 
Python.

I will not try to calculate the Lyapunov exponent from the existing 
simulation CSV alone. We need access to $J(t)$ or the RHS itself while 
propagating perturbations.

The minimal implementation would therefore probably require:

- one small Julia Lyapunov routine, preferably shared between the 
two templates;
- one new `lyapunov.py`;
- a very small change to `plots4model.py` to add an optional **Lyapunov** 
tab when the corresponding CSV exists;
- optionally a TOML section such as

```toml
[lyapunov]
enabled = true
method = "largest"
renormalize_dt = 0.1
transient = 5.0
```

I will make this an opt-in, just as eigenvalue diagnostics are opt-in.

Then the final HTML structure would naturally become:
```
Simulation Results
Stability
Lyapunov
```

with the Lyapunov tab containing at least:

1. a plot of finite-time $\lambda_{\max}(t)$;
2. the final estimated $\lambda_{\max}$;
3. a classification such as stable / neutral / sensitive-chaotic;
4. later, optionally, the full spectrum.

For a macroeconomic model this could become quite valuable. If a 
policy regime has
$$
\lambda_{\max} > 0,
$$
then precise long-horizon forecasting becomes intrinsically unreliable 
even though the model itself is deterministic. That is pretty useful to 
know I think.
So I think it is worth implementing all this, but I would keep it as a 
separate diagnostic layer rather than mixing it into `stability.py` since
the two analyses answer different mathematical questions.

And I did end up chucking all this into the LLM, I just cannot be bothered 
spending the time doing it all myself, and want to get on to policy 
advocacy & real world activism.


### Lyapunov Upgrades

The central design is still simple: Julia performs the trajectory-level 
tangent calculation because it already owns the dynamical system 
and Jacobian; `lyapunov.py` is purely post-processing/reporting, 
analogous to `stability.py`. `plots4model.py` then assembles Dynamics, 
Stability, and Lyapunov into the browser report.

The TOML interface is:

```toml
[lyapunov]
enabled = true
renormalize_dt = 0.1
transient = 5.0
```
When enabled, the generated Julia solver writes

```text
models/<model>_lyapunov.csv
```
with

```text
t,lambda_max
...
```

The Julia calculation evolves a tangent vector according to
$$
\dot v=J(t)v,
$$
using the correctly signed ODE Jacobian
$$
J_{\rm ODE} = -\frac{\partial F}{\partial u}
$$
from our DAE residual. Between solver steps it uses
$$
v(t+\Delta t)\simeq \exp\!\left[J(t)\Delta t\right]v(t),
$$
with periodic Benettin-style renormalization. The accumulated quantity 
is the finite-time estimate
$$
\lambda_{\max}(T) = \frac{1}{T} \sum_k\log s_k.
$$
That is better than attempting to average instantaneous Jacobian eigenvalues.

`lyapunov.py` reports the final estimate, the mean and standard deviation 
over the last 20% of estimates, and one of three deliberately cautious 
classifications: contracting, neutral/unresolved, or exponentially 
sensitive. It does not label every positive exponent “chaos,” because 
the unstable Lorenz equilibrium is the obvious counterexample: 
$\lambda_{\max}>0$ there represents an unstable equilibrium, not a 
strange attractor.

For the browser output, the default is now a three-tab layout :

```
Dynamics    Stability    Lyapunov
```
The inactive buttons are Dodger Blue `#1E90FF`, the active button is a 
soft pale green `#70C1A3`, all text is white, the page background 
remains black, and Plotly remains dark-themed.

You can combine the two analysis tabs, if you prefer, with:
```toml
[plots]
combine_stability_lyapunov_plots = true
```
The default is `false`. With it enabled, the browser becomes:
```
Dynamics    Stability & Lyapunov
```

**Caveat:** I have not checked it all works for the older models, and I 
never will! 

I also made one small compatibility update to `plot_utils.py`: the 
old Plotly `titlefont=` axis syntax now fails on current Plotly versions, 
so the dual-axis plot uses the modern nested `title=dict(...)` form. 
I also gave `load_config()` the same `tomllib`/`toml` fallback pattern 
we are now using elsewhere.

The test models have these expectations: 

- The damped pendulum has a 
negative largest Lyapunov exponent after its transient. 
- The normal  Lorenz model with
$$
\sigma=10,\qquad \rho=28,\qquad\beta=2.6
$$
has a positive exponent in its chaotic regime. 
- The `lorenz_attractor_unstable` model starts exactly at
$$
x=y=z=0,
$$
so its state can remain exactly at the unstable equilibrium while its 
tangent perturbation grows exponentially. That gives us a particularly 
good test that Lyapunov sensitivity and “chaos” are not synonyms.

I ran the combined Python test suite for the stability and Lyapunov work:
```
..............                                                    [100%]
14 passed in 1.05s
```

That includes independent RK4/Benettin reference calculations for all 
three models, generator/template checks, the DAE Jacobian sign 
regression, TOML controls, three-tab HTML generation, the requested 
blue/green styling, and the combined-analysis-tab option.

Models without `[lyapunov] enabled = true` still build the three-tab 
report; the Lyapunov tab simply explains that the diagnostic is not 
enabled. Likewise for stability if `[eigenvalues] all = true` is absent 
or false. So you do not need to enable every diagnostic for every 
development model.

**Command Lines:**

Just for future reference!

```bash
pytest -v tests/test_stability.py tests/test_lyapunov.py
```

and to actually see results,
```bash
python3 generate_julia_odesolver.py pendulum
julia models/pendulum_cmdl.jl
python3 plots4model.py pendulum
firefox models/pendulum.html  &>/dev/null&
```
and the others the same,
```bash
python3 generate_julia_odesolver.py lorenz_attractor
julia models/lorenz_attractor_cmdl.jl
python3 plots4model.py lorenz_attractor
firefox models/lorenz_attractor.html &>/dev/null&

python3 generate_julia_odesolver.py lorenz_attractor_unstable
julia models/lorenz_attractor_unstable_cmdl.jl
python3 plots4model.py lorenz_attractor_unstable
xdg-open models/lorenz_attractor_unstable.html
```

For all five models, the bash pattern really is now identical:
```bash
for model in \
    pendulum \
    lorenz_attractor \
    lorenz_attractor_unstable \
    mmm_0_3 \
    mmm_0_4
do
    echo "===== ${model} ====="

    python3 generate_julia_odesolver.py "${model}" &&
    julia "models/${model}_cmdl.jl" &&
    python3 plots4model.py "${model}"
    xdg-open models/${model}.html
done
```


### Pendulum Lyapnuov analysis example

Well, it works for one model. The webpage needs some work, but is ok.
The text part of the html report reads:
```
Lyapunov Analysis for Model: pendulum

Analysis time range: 20.1003 to 100
Recorded estimates: 800
Final λmax: -0.0414905
Mean over final 20%: -0.0461108
Tail standard deviation: 0.00528045
Classification: contracting
Discarded transient: 20.0
Renormalization interval: 0.1

Interpretation: the estimated largest Lyapunov exponent 
is negative, so nearby trajectories contract on average over 
the analysed interval.

Method: one tangent vector is evolved with the ODE Jacobian 
and periodically renormalized. The plotted quantity is the 
accumulated finite-time estimate of the largest Lyapunov exponent.
```

**How to read this?**

The Lyapunov analysis asks a simple question:

> If we start two copies of the model in almost exactly the same state, do
> their trajectories move closer together or farther apart as time passes?

Suppose the difference between two nearby states is initially some very small
quantity $\delta x(0)$.  Roughly speaking, the largest Lyapunov exponent
$\lambda_{\max}$ describes how that difference changes:

$$
|\delta x(t)| \sim |\delta x(0)| e^{\lambda_{\max} t}.
$$

The sign of $\lambda_{\max}$ is therefore the important part.

- If $\lambda_{\max}<0$, nearby trajectories tend to move together.  The
  dynamics are locally contracting.
- If $\lambda_{\max}>0$, nearby trajectories tend to move apart
  exponentially.  The system is sensitive to its initial conditions.
- If $\lambda_{\max}\approx0$, the separation neither clearly grows nor
  clearly decays.  The system may be neutral, periodic, or the numerical
  calculation may simply require a longer run.

A positive Lyapunov exponent is an important signature of chaos when the
trajectory remains on a bounded non-equilibrium attractor.  It is not,
however, sufficient by itself to prove that a system is chaotic.  An unstable
equilibrium can also have a positive Lyapunov exponent.

For the damped pendulum the report gives approximately

```text
Final lambda_max:          -0.0415
Mean over final 20%:       -0.0461
Tail standard deviation:    0.0053
Classification:             contracting
```
"For Dummies": The important result is that the largest Lyapunov 
exponent is negative.

---

#### More analysis

For example, taking
$$
\lambda_{\max}\simeq -0.046,
$$
the separation between two nearby pendulum trajectories behaves 
approximately like
$$
|\delta x(t)| \sim |\delta x(0)|e^{-0.046t}.
$$
Thus a small perturbation becomes progressively smaller rather than larger.

This is exactly what we expect physically from a damped pendulum.  Friction
removes energy, the oscillations die away, and different nearby initial
conditions eventually approach the same stable resting state.

The Lyapunov calculation therefore gives a trajectory-level confirmation of
the familiar statement that the damped pendulum is stable.


**Why discard the first part of the trajectory?**

The report says
```
Discarded transient: 20.0
```
The first part of a simulation can be atypical because the system is still
responding strongly to its chosen initial conditions.

For the pendulum, for example, the bob initially oscillates with relatively
large amplitude before damping brings it close to equilibrium.
We therefore ignore the first $20$ time units when accumulating the Lyapunov
estimate.  This is called discarding the **transient**.

The purpose is to measure the characteristic long-time dynamics rather than
the arbitrary details of how the simulation happened to start.


**Why is the analysis time range 20.1003 to 100?**

The Lyapunov calculation begins only after the transient has elapsed.
The simulation itself runs from approximately
$t=0$ to $t=100$,
but the first $20$ time units are excluded.  The first recorded estimate
therefore appears just after $t=20$.

The slight value
```
20.1003
```
rather than exactly `20.1` is a consequence of the numerical integrator's
internal stepping and is not physically significant.

**What is the renormalization interval?**

The report says
```
Renormalization interval: 0.1
```

To measure sensitivity, the program follows a tiny imaginary perturbation
vector alongside the ordinary model trajectory.

If the perturbation were allowed to grow or shrink indefinitely, it would
eventually become either numerically enormous or so small that floating-point
roundoff became important.

The program therefore repeatedly measures its change in length and then
rescales it back to unit length.

In this model that rescaling is performed approximately every
$$
\Delta t=0.1.
$$
The amount by which the perturbation had grown or shrunk before each
renormalization is retained.  These accumulated stretch factors are what
produce the Lyapunov exponent.

Renormalizing the vector does **not** alter the model trajectory.  It is 
only a numerical device used to measure the behaviour of an infinitesimal 
nearby trajectory.


**Why are there 800 estimates?**

The useful analysis interval is approximately
$$
100-20=80
$$
time units.  With a renormalization interval of about $0.1$,
this gives approximately
$$
\frac{80}{0.1}=800
$$
Lyapunov measurements. Thus the reported
```
Recorded estimates: 800
```
is exactly what we would expect.


**What does the final value mean?**

The report gives

```
Final lambda_max: -0.0414905
```
This is the accumulated finite-time estimate at the end of the 
simulation.

It should not be interpreted as a precise physical constant. 
Lyapunov exponents are asymptotic quantities: in principle 
they describe the limit obtained after observing the dynamics for 
a very long time.

A finite simulation therefore produces an estimate of that limiting value.


**Why also report the mean over the final 20 percent?**

Instead of trusting only the very last numerical sample, the program 
also examines the last portion of the calculation:
```
Mean over final 20%: -0.0461108
```
If the estimate is converging properly, the later values should 
cluster around a roughly stable value.

For the pendulum the late-time mean remains comfortably negative, so the
classification does not depend on one accidental final sample.

The program therefore bases its qualitative classification primarily on this
late-time behaviour.


**What does the tail standard deviation mean?**

The report gives
```
Tail standard deviation: 0.00528045
```
This measures how much the Lyapunov estimate fluctuates during the final
$20\%$ of the analysed trajectory.

The late-time estimate is roughly
$$
\lambda_{\max}=-0.0461\pm0.0053
$$
if the standard deviation is used merely as a descriptive measure of the
numerical spread.

This is **not** a statistical error bar in the usual experimental sense.
Successive Lyapunov estimates are strongly related to one another because they
come from the same evolving trajectory.
Its main purpose is diagnostic: it tells us whether the finite-time estimate
has settled reasonably well or is still varying strongly.

**What does "contracting" mean?**

The program classifies this result as

```text
contracting
```
because the late-time largest Lyapunov exponent is negative.

This means that infinitesimally nearby trajectories tend to converge rather
than diverge.
It does not mean that every state variable decreases with time.  For example,
the pendulum angle can increase during part of an oscillation.
"Contracting" refers instead to the **distance between nearby trajectories in
the system's state space**.


**Relationship to the ordinary stability analysis**

The Stability and Lyapunov tabs answer related but different questions.

The Jacobian stability calculation asks:

> If I perturb the system at this particular state, what does the 
local linearized dynamics predict?

The Lyapunov calculation asks:

> After following a perturbation along the actual trajectory for 
a substantial  period of time, does that perturbation grow or 
shrink overall?

At an equilibrium point the ordinary Jacobian eigenvalue calculation 
is the standard local stability test.

Lyapunov analysis is especially useful away from equilibrium because it
accumulates the effect of the changing Jacobian along the complete trajectory.

For the damped pendulum both analyses should agree: the equilibrium is stable
and the long-time trajectory is contracting.


**Summary for this run**

For this damped-pendulum simulation,
$$
\lambda_{\max}\approx -0.046.
$$
The negative sign means that nearby trajectories converge exponentially on
average.

The result is therefore consistent with the expected physical behaviour of a
damped pendulum: perturbations die away and the system approaches its stable
resting state.

The Lyapunov analysis is doing something slightly stronger than merely
observing that the plotted oscillations become smaller.  It directly tests
whether two infinitesimally neighbouring solutions become more alike as the
dynamics evolve.

One point as written above is that the `±0.0053` is descriptive 
numerical spread, not a conventional confidence interval. That 
distinction becomes important if we later use the same analysis 
on the Lorenz models.


### Slow downs and CPU Usage

One work-around if your solver is slow and tying up memory and CPU is 
to background it,
```bash
nice -n 15 julia models/pendulum_cmdl.jl &
```

***Be Notified** <br>
Run it with a trailing notification so you don't have to poll:
```
nice -n 15 julia models/pendulum_cmdl.jl > run.log 2>&1 && echo "done" || echo "FAILED";
```

If you want it genuinely in the shell background, use:
```bash
nice -n 15 julia models/pendulum_cmdl.jl > run.log 2>&1 &
```
then immediately do,
```bash
echo $!
```
which prints the Julia process PID. You can monitor it with:
```bash
tail -f run.log
```
and separately watch the Lyapunov output appear:
```bash
tail -f models/pendulum_lyapunov.csv
```
For low CPU and low I/O priority together, I would use:
```
nice -n 15 ionice -c 3 julia models/pendulum_cmdl.jl > run.log 2>&1 &
```
If you want the "done"/"FAILED" result while still backgrounding the 
whole pipeline:
```bash
(
    nice -n 15 ionice -c 3 julia models/pendulum_cmdl.jl > run.log 2>&1 \
        && echo "done" \
        || echo "FAILED"
) &
```

If you want the job to survive closing the terminal:
```bash
nohup nice -n 15 ionice -c 3 \
    julia models/pendulum_cmdl.jl \
    > models/pendulum_run.log 2>&1 &
```
then rejoin the process,
```bash
jobs -l
```
of `jobs` will show all jobs launched in your terminal. 
```bash
pgrep -af pendulum_cmdl     # lists matching PIDs and command lines
ps -o pid,etime,stat,cmd -C julia
```
`etime` shows how long it's been running, and `stat` shows 
`R` (running) or `S` (sleeping).

Or if it is still running try,
```bash
ps -C julia -o pid,ni,%cpu,%mem,cmd
```
and monitor output with:
```bash
tail -f models/pendulum_run.log
```
You can lower the priority of one already running process too:
```bash
renice 15 -p PID
ionice -c 3 -p PID
```


### Performance Issues

There was still a performance problem in my first version, however. It was 
functionally the Lyapunov-enabled version, but it is not yet 
performance-optimized.
The expensive part is that on every solver callback step it computes
$$
\exp(J\\,\Delta t)
$$
for the tangent vector. pendulum_cmdl With
```
dt = 0.01
t1 = 100.0
```
that is roughly 10,000 matrix exponentials, in addition to ForwardDiff 
Jacobian construction. pendulum_cmdl

For a $2\times2$ system that still should not be disastrous, but combined 
with the other existing overhead it can be very noticeable.

The other large overhead remains unchanged: it is still running an 
ordinary pendulum through
```
DAEProblem(...)
solve(prob, IDA(), dt=dt, adaptive=false, ...)
```
rather than 
```
ODEProblem(...); Tsit5(). pendulum_cmdl pendulum_cmdl
```
And the ordinary trajectory output still calls
```
flush(outfile)
```
on every one of those approximately 10,000 steps.

So I would characterize this version as:
Correct enough to run and test the Lyapunov pipeline, but not yet 
the version I would keep for production performance.

One minor thing to note: your generated Lyapunov analysis currently uses
```
transient=20.0
renormalize_dt=0.1
```
so nothing is accumulated until approximately $t=20$. The CSV itself 
will exist immediately because it is opened before solving, but initially 
it will contain only:
```
t,lambda_max
```
The numerical rows should begin after the transient.

After we establish that this pipeline works, I strongly recommend the 
next change be the performance cleanup: use an actual 
`ODEProblem + Tsit5()` 
for these explicit models and evolve the tangent equation without 
performing a fresh matrix exponential at every $0.01$ solver step. 
That should make a pendulum run lightweight again.



## Older Models

I had three earlier MMT models,m we can try to see if they are 
healthy too,
```bash
for model in mmm_0_1 mmm_0_2 mmm_0_3
do
    python3 generate_julia_odesolver.py "$model" &&
    julia "models/${model}_cmdl.jl" &&
    python3 plots4model.py "$model"
done
```


### Large HTML Output

The plots have a lot of points I guess, so are super large html files, 
up to 65 MB, too big for github. I removed them from the repo. 


## TODO



**2026-10-09:**  I should test Lyapunov analysis with Lorenz and ``mmm_0_4`. 
That is next chapter. Plus, the LLM I used recommended optimization of 
the Lyapunov analysis, I think we should do that. Inefficient code 
is nasty. 4

<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_01_macromodels_mosler">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../350_00_macromodels_lstm">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_01_macromodels_mosler">Macromodels — Mosler I</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../341_01_macromodels_mosler">Macromodels — Mosler III</a></td>
</tr>
</table>


