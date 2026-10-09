---
title: "Macromodels — Mosler II"
weight: 20
date: 2026-10-07
toc: true
katex: true
---

First a performance patch, then more lyapunov analysis tests.

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


