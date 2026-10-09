---
title: "Macromodels — Mosler II"
weight: 20
date: 2026-10-07
toc: true
katex: true
---

First a performance patch, then more lyapunov analysis tests.
Lastly today, a [special main seciton](#the-mmm-jg-model) on the `mmm_0_4`` model itself! 
Some of the good stuff.

## PukahaPai solver/performance update

This patch makes three related changes.  Note: I have this under `git` 
version control, so there is no verison numbering in the files. I do not 
plan on making any produciton versions either, it's 
all "this is the latest PukahaPai".

### 1. Honour `[solver].method`

A modeller can now select any simple zero-argument DifferentialEquations.jl
algorithm constructor exported in the Julia environment, for example:

```toml
[solver]
dt = 0.01
method = "Tsit5"
```
This generates an `ODEProblem` solved with `Tsit5()`.

The special method
```toml
method = "IDA"
```
generates a `DAEProblem` solved with `IDA()`.

For unusual cases the problem type can be stated explicitly:
```toml
problem_type = "ode"   # or "dae"
```
The generator deliberately does not maintain a small solver whitelist. 
A simple Julia constructor name such as `Vern7`, `RK4`, `Rodas5P`, or 
a dotted name such as `OrdinaryDiffEq.Vern7` is emitted as `<name>()`. 
Arbitrary Julia source in the TOML method field is rejected.

### 2. Decouple integration step, output sampling, and flushing

The solver section can now optionally specify solver particulars with:
```toml
[solver]
dt = 0.01
method = "Tsit5"
adaptive = false
output_dt = 0.05
flush_every = 10
abstol = 1e-8
reltol = 1e-6
```

`dt` controls the requested integration step when a fixed-step run is used.
`output_dt` controls the state-data sampling interval. These are different
numerical questions and should not be coupled.

The command-line solver uses `saveat=output_dt` and writes the CSV in 
one buffered pass after integration. It therefore does **not** 
call `flush()` once per row.

The (untested c.2026-09) GUI solver is a streaming producer, so it 
periodically 
flushes the state
CSV. `flush_every` is the number of written output rows between flushes. The
default is 10. There is no universal optimal flush interval: a smaller value
reduces GUI/data latency but causes more system calls; a larger value improves
I/O efficiency but allows more buffered data and longer display latency.

### 3. Remove the per-step matrix exponential from the Lyapunov diagnostic

The previous largest-Lyapunov calculation propagated the tangent vector with
```text
v <- exp(J * delta_t) * v
```
at every accepted solver step. A dense matrix exponential is unnecessarily
expensive, particularly as the number of state variables grows.

The replacement keeps the same frozen-Jacobian approximation over one solver
step but applies a fourth-order Runge--Kutta polynomial action to the vector:

```text
k1 = J v
k2 = J (v + h k1/2)
k3 = J (v + h k2/2)
k4 = J (v + h k3)
v  = v + h (k1 + 2 k2 + 2 k3 + k4)/6
```
This requires matrix-vector products rather than a dense matrix exponential.
The Benettin renormalization and CSV format are unchanged.

### Jacobian calculation

The templates now always generate an explicit `rhs!`. Stability and Lyapunov
diagnostics differentiate that RHS directly:
```text
J = df/du
```
Even when IDA is selected, the DAE residual is merely a wrapper
```text
F(du,u,t) = du - f(u,t).
```
This removes the old residual-Jacobian sign ambiguity from the generated
stability code.



## Solver/TOML Defaults

`output_dt = 0.05` is not the default. In the current generator, 
`output_dt` defaults to whatever `dt` is:

```python
output_dt = _positive_float(solver_config, "output_dt", dt)
```
So if the TOML has
```toml
[solver]
dt = 0.01
```
and omits `output_dt`, the generated solver uses
```text
output_dt = 0.01
```
The same generator currently uses these defaults:

```
### Solver options and defaults

The `[solver]` section supports the following fields.

```toml
[solver]
dt = 0.01
method = "Tsit5"
problem_type = "ode"
adaptive = false
output_dt = 0.01
flush_every = 10
abstol = 1e-8
reltol = 1e-6
```

Only `dt` is normally worth specifying explicitly for a simple model.
The remaining settings may be omitted unless a model requires something
different.

- `dt`
  - Default: `0.01`
  - Requested integration step.
  - Used directly for fixed-step integration.
  - For adaptive solvers it serves as the requested/initial step rather than
    forcing every accepted step to have this size.
- `method`
  - Default: `"Tsit5"`
  - Julia DifferentialEquations.jl algorithm constructor.
  - Examples include `"Tsit5"`, `"Vern7"`, `"RK4"`, `"Rodas5P"`, and `"IDA"`.
- `problem_type`
  - Default: inferred from `method`.
  - `"IDA"` implies `"dae"`.
  - Other solver methods default to `"ode"`.
  - May be explicitly set to `"ode"` or `"dae"` for unusual cases.
- `adaptive`
  - Default: `false`
  - If `false`, the integration uses the requested fixed timestep `dt`.
  - If `true`, the selected Julia solver may adapt its timestep according to
    `abstol` and `reltol`.
- `output_dt`
  - Default: the value of `dt`.
  - Controls the interval at which state data are written/saved for plotting.
  - This is independent of the numerical integration step.
  - For example, with
    ```toml
    dt = 0.001
    output_dt = 0.05
    ```
    the model may integrate at a fine timestep while only recording output
    every `0.05` time units.
- `flush_every`
  - Default: `10`
  - Applies primarily to the streaming GUI solver.
  - Controls how many written output rows are buffered before `flush()` is
    called.
  - The command-line solver writes its state CSV in one buffered pass after
    integration, so this setting has little or no relevance there.
- `abstol`
  - Default: `1e-8`
  - Absolute error tolerance used by adaptive solvers.
- `reltol`
  - Default: `1e-6`
  - Relative error tolerance used by adaptive solvers.

There is one subtle point worth documenting explicitly: `problem_type` does 
not have a literal fixed default such as `"ode"` in all cases. It is 
inferred. With `method = "IDA"` the default becomes DAE; otherwise it 
becomes ODE.

So for the common case this minimal section is sufficient:
```toml
[solver]
dt = 0.01
```
and is equivalent, under the current generator, to approximately:
```toml
[solver]
dt = 0.01
method = "Tsit5"
adaptive = false
output_dt = 0.01
flush_every = 10
abstol = 1e-8
reltol = 1e-6
```
with `problem_type = "ode"` inferred from `Tsit5`.

However, it is probably widser to flush output less often with 
say `output_dt = 0.05`.


## Likely next bottleneck

After the patches are all good, the next diagnostic cost to profile is 
the full **ForwardDiff** Jacobian constructed at every Lyapunov 
callback. For a model with many state variables, forming the 
complete `n x n` Jacobian can become
more expensive than the RK4 tangent propagation itself.

Two natural later optimizations are:

1. compute Jacobian-vector products `J*v` directly with automatic
   differentiation, avoiding construction of the full matrix for the
   largest-exponent calculation; or
2. augment the ODE with the tangent equation and let the selected Julia solver
   integrate state and tangent variables together.

The sparse stability diagnostic still needs the full Jacobian because it
computes eigenvalues.


## THe MMM JG Model

I have numbered this `mmm_0_4` The first `0` is for testing. Not for 
serious play. The idea is to eventually get to a realistic JG MMT model 
which would be `mmm_1_4`.

My first attemp was pretty terrible. SO I will not even show you the toml. 
But here is roughly what went bad:

---

### The Bad

The results show the JG labour pool rises monotonic (for the time period we 
ran up to t=50), which is unrealistic. U3 rises and `\lambda_F` drops, 
undesirable. The JG should be fairly minimal, just to soak up unemployed 
labour. The Firm and Government sector should be employing most labour. Thus 
somehow our model is focusing on the JG instead of desired Firm and Government 
services ($L_G$) output. We need to think of how to change that in the whole 
design. Perhaps we need `Y_G` to add to total output, or somehow feedback  to 
avoid `L_JG` taking up all the idle labour? Or maybe we need Firms to be 
allowed to borrow from banks for investment to maintain reasonable output per 
capita (a demand function), but regulate that with the interest payment 
constraint?

Other things to check:

`G_N` is negative, I presume that is because on the books it is the 
accumulated deficit? In another model it might be swapped fro interest 
earning bonds, so would be `G_D` and we woudl have interest payments to the 
"Firms" (presumed to hold most bonds)? But we are not doing a bonds model 
(fixed exchange rate mindset), correct? (Which is ok, since this can be our 
floating fx rate model without the foreign sector explicit.)
Thus it is fine of `G_N` gets more negative, that was expected.

Perhaps since total time = 50 is only six months nominally, we might want 
to run longer to see if the `L_JG` stops increasing? But in any case, it 
was going up too fast, suggesting the model is just plain bad, since the 
JG pool should cycle a bit just as a buffer. It should not be modelled as 
a preferred employment option.  The public sector proper `L_G` is the 
preferred option.

I read this as some sort of (hidden?) constraint on firm hiring implicit 
in our model. So we need to relax that somehow (but I do not know what 
it is). Perhaps lack of a proper Firm Investment function and Firm debt 
from bank credit, which was in an earlier model we had based on 
Steve Keen's Minsky + Banking model.

---

I felt it important to redesign the whole model, not just fiddle with 
parameters to see if something realistic could be eeked out. This is the \
**PukahaPai** development plan --- to hand end-users a few Base Case models
so that _they_ can just fiddle around with parameters (also called 
policy advice & analysis).

This also helps with public finance policy education, because there is a 
clear demarcation into two types of government policy:

1. Fiddling around with parameters (existing structure and regulations).
2. Policy ideology Big Picture stuff (changes the whole model, not just
parameters).



### The Good and the Ugly

(Second Thoughts.)

I think the redesign is fairly clear now, and the important diagnosis 
is not “the JG is attracting too much labour.” The JG was already 
residual. The structural problem was that the two regular-employment 
sectors were not given enough long-run demand to keep labour out of 
the buffer.

In the old model, regular government employment was essentially fixed 
in absolute headcount because
```
L_G = public_payroll / w_G
```
while population grew at 1% per year. Government goods spending was also 
fixed in nominal terms. Meanwhile private productivity grew at 2% per year. 
So over a long run, regular public employment and fiscal demand mechanically 
shrank relative to the size and productive capacity of the economy. The 
firm-employment equation then saw persistent excess supply and reduced 
`lambda_F`; the JG merely absorbed the residual. 

There is another important point: in this model the time unit is 
explicitly the year, so `t = 50` is fifty years, not six months.  With 
`beta=0.01` and `alpha_F=0.02`, that is a very long stress test. Over 
50 years population rises by about 65%, while private productivity rises 
by about 172%. A fixed nominal payroll and fixed nominal goods budget were 
therefore guaranteed to become progressively less important.

Considering how to amend these model mistakes I changed the architecture 
in four places.

First, proper public employment is now driven by desired real public 
services per person, rather than a fixed nominal payroll:
```
q_G_pc = q_G_pc0 * exp(gamma_G_service*t)
Q_G_des = q_G_pc * N
L_G = Q_G_des / A_G
```
With `gamma_G_service = alpha_G`, regular public employment remains at 
roughly a stable share of the labour force. This makes the causal 
interpretation clearer: the government decides what ordinary 
public services it wants, and labour demand follows from that.

Second, government purchases of private goods now scale with population:
```
Q_goods = q_goods_pc * N
G_goods = P_G * Q_goods
```
instead of remaining a fixed nominal budget for 50 years.

Third, I reintroduced a simple private gross-investment demand term:
```
I_real = iota_F * Q_F
I_nom  = P * I_real
```
with `iota_F = 0.08`. This is intentionally not yet a Minsky/Keen 
bank-credit model. It simply recognizes that private output is not all 
consumption output. Financing should be added separately, with 
explicit bank assets, firm liabilities, interest, principal repayment, 
and so forth.

Fourth, firms now plan a modest spare-capacity margin:
```
u_F_target = 0.95
Q_required = Q_demand / u_F_target
```
so they do not wait until demand exactly equals maximum current 
production before hiring.

That gives the revised labour logic:
```
regular government employment
        +
private employment
        +
JG residual
        =
labour force
```
and the JG remains the residual buffer rather than an alternative 
preferred employer, as it is _supposed to be by design._.

I also changed the wage hierarchy in the reference calibration to
```
w_JG = 0.60
w_F  = 0.88
w_G  = 1.10
```
so the JG is visibly the lowest-paid buffer, regular public service is the 
highest-paid public option, and firms still employ the majority of labour.

On an independent numerical check of the revised equations, the JG share 
stays in roughly the 4–6% range over the 50-year stress test rather than 
taking over the labour force. `lambda_F` stays around 0.93–0.94 instead 
of monotonically collapsing. That is much closer to the behavior we want 
from a baseline JG model.

On `G_N`: yes, your interpretation is basically right. In this model it 
is the signed consolidated government net financial position, not a 
Treasury bank account. The Godley structure conserves
```
F_D + W_D + G_N = constant
```
so if the private sector accumulates positive net financial assets, `G_N` 
is correspondingly negative. The old model explicitly used that convention. 

I would not rename it `G_D`. That would make it look like a positive 
government bank deposit, which is not what it represents.

And I would make one correction to the bonds point: government bonds are 
not specifically a “fixed exchange-rate mindset.” Floating-currency 
governments also issue bonds. In an MMT treatment they need not be 
interpreted as a financing necessity; they can be modeled as 
interest-bearing government liabilities held by households, firms, banks, 
pension funds, etc. So a later bond model could add explicit security 
stocks and interest flows while retaining the same floating-currency 
framework.

On bank credit: I think your instinct is right that it belongs in the next 
layer, but it is not the cause of this particular failure. The current model 
did not constrain firms by debt service; it had no such banking constraint at 
all. Its constraint was lack of effective demand. Bank lending will matter once 
we introduce a real capital stock and an investment function such as:

```
expected sales
    -> desired investment
    -> bank credit
    -> capital accumulation
    -> higher productive capacity
    -> debt service
    -> possible slowdown / deleveraging
```
That would make a good `mmm_0_5`. I will first establish the JG buffer 
architecture cleanly in `mmm_0_4`, which is what this redesign does.

**One further point I recommend:** for this model, plot 
`lambda_JG = L_JG/N` and `u3_rate = U3/N`, not just the absolute 
`L_JG`. With a growing population, the absolute number of JG workers 
can rise while the buffer share is actually stable or falling. The 
revised TOML adds those diagnostics explicitly.

***Little Note:** It was very nice to just be able to edit TOML! No coding 
anymore. At least for a short while. The dearpygui is still on the horizon.


## Reports (important!) 

I had some dopey plots. So wrote this teaching note up!

For MMT, `G_N` is largely meaningless!  Plus, this pair is 
incommensurate, `G_N`, `debt_to_GDP`
one is in `$` the other is a pure time dimension  `[G_N/GDP ] ~ years`. 

**Exercise:** 

So what we really want is a pair here of commensurate quantities that have 
a meaningful comparison story.  Prosperity is crudely GDP per capita? 
Can we have that, plus one other quantity that is comparable but 
complementary?  I do not yet have an energy consumption function like 
a Leontieff model, but we could make one, to show Real energy use 
per capita?  Or for now, can you suggest something else in the meantime?

**Solution:**

On dimensions, in the strict stock–flow sense:
$$
[G_N]=\text{currency},\qquad [Y]=\frac{\text{currency}}{\text{year}},
$$
so
$$
\left[\frac{G_N}{Y}\right]=\text{year}.
$$
“Debt-to-GDP ratio” is conventionally spoken of as dimensionless because 
GDP is normally reported as an annual flow and the year is implicitly 
absorbed into the reporting convention. But mathematically it is a 
stock-to-flow ratio with the interpretation of a time scale. For an 
MMT model, I agree that it is not especially illuminating as a primary 
Dynamics plot.

For a better plot pair, you could use a prosperity-versus-living-standard 
comparison with the same units:
```toml
"Y_pc", "C_pc"
```
where both are nominal flows per person per year:
```toml
Y_pc = "Y_exp_nom/N"
C_pc = "C/N"
```
Both have dimensions
$$
\frac{\text{currency}}{\text{person}\cdot\text{year}}.
$$
The comparison story is quite useful:

- `Y_pc`: total nominal output/income generated per person;
- `C_pc`: household consumption expenditure per person.

So the gap between them is not “waste”; it includes investment and 
government production/expenditure. But the pair tells you whether 
rising aggregate prosperity is actually translating into rising 
household consumption.

So for the plot Dynamics tab we can have this layout:
```toml
time_series = [
    "P", "pi_rate",
    "lambda_F", "lambda_G",
    "lambda_regular", "lambda_JG",
    "F_D", "W_D",
    "Y_pc", "C_pc"
]
```

**Exercise:**

Can you improve on the above solution? (Think about Price.)

**Solution:**

The first solution uses nominal per-capita quantities. If `P` is 
moving materially, part of their growth is inflation. For economic 
interpretation I would therefore go one step further and add real 
counterparts:
```toml
Y_real_pc = "Y_exp_nom/(P*N)"
C_real_pc = "C/(P*N)"
```
Then the preferred final pair becomes
```toml
"Y_real_pc", "C_real_pc"
```
with dimensions of your private-good-equivalent quantity per person 
per year.

That is probably the best temporary prosperity pair.

There is a conceptual imperfection here: dividing all of `Y_exp_nom` by 
the private price `P` implicitly uses the private-goods price as a 
deflator even for public services. Since the model has public output 
valued through payroll rather than a proper public-service price index, 
this is only a real-GDP proxy. For `mmm_0_4`, I think that is acceptable 
as long as we label it honestly.

A slightly cleaner formulation would therefore be:
```toml
C_real_pc = "(C/P)/N"
Y_real_pc = "(Q_F + Q_G + Q_JG)/N"
```
but this assumes `Q_F`, `Q_G`, and `Q_JG` are genuinely commensurable 
real-output units. At present they are not quite: one is private goods, 
the others are public/JG services with different productivity 
normalizations. So I prefer the deflated-expenditure proxy for now.

**Exercise:** 

What might you do for a simple energy analysis? 

**Solution:**

I think real energy use per capita will eventually be a  good 
additional welfare/resource diagnostic, but it would not be commensurate 
with GDP per capita:
$$
[E_{\rm pc}] = \frac{\text{energy}}{\text{person}\cdot\text{year}},
$$
versus
$$
[Y_{\rm pc}] = \frac{\text{currency or real-output units}}
     {\text{person}\cdot\text{year}}.
$$
So I would not overlay them as a paired plot unless you normalize both 
to indices, e.g.
$$
\hat Y_{\rm pc}(t)=\frac{Y_{\rm pc}(t)}{Y_{\rm pc}(0)},\qquad
\hat E_{\rm pc}(t)=\frac{E_{\rm pc}(t)}{E_{\rm pc}(0)}.
$$
Then both are dimensionless and you get an interesting “prosperity 
versus resource intensity” story.

For now, my preferred pair is therefore:
```toml
Y_real_pc = "Y_exp_nom/(P*N)"
C_real_pc = "C/(P*N)"
```
and:
```toml
time_series = [
    "P", "pi_rate",
    "lambda_F", "lambda_G",
    "lambda_regular", "lambda_JG",
    "F_D", "W_D",
    "Y_real_pc", "C_real_pc"
]
```

That leaves `G_N` available as an accounting diagnostic without 
pretending it is one of the most economically informative headline 
variables. (It _is_ in our media in the present Neoliberal era, but it 
should not be.)




<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_02_macromodels_mosler">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../350_00_macromodels_lstm">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_02_macromodels_mosler">Macromodels — Mosler II</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../350_00_macromodels_lstm">Macromodels — LSTM/CNN</a></td>
</tr>
</table>


