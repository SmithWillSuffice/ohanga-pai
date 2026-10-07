---
title: "Macromodels — Mosler"
weight: 18
date: 2026-10-06
toc: true
katex: true
---

Notes for a minimal JG MMT model.  This is my **PukahaPai** Project.

There is no terrific Zulip, Slack or Discord server, but if I do 
collaborate later on it will probably be [Zulip](https://zulip.com/).

## MMT Macroeconomic ODE Modelling Framework

This is a hybrid DearPyGUi, Python code Gen, Julia ODE solver templates, 
TOML model specification suite.

The project has a modular design, and a substantial amount of the 
numerical infrastructure has already been implemented. The immediate 
priority should be restoring and validating the command-line modelling 
workflow before continuing with the Dear PyGui interface.

## 1. The overall project

PukahaPai is intended to become a general-purpose ODE/DAE modelling 
framework, with particular emphasis on Modern Monetary Theory (MMT), 
Minsky-style macroeconomic dynamics, and stock-flow-consistent accounting.

It is a slimmer, faster, more flexible alternative to Keen's Ravel+Minksy™. 
With data fetching tools via the BIS, FRED, OECD available I do not 
see much need for code-bloat advanced features of Minksy™ --- that on 
GNU-Linux were not working out-of-the-box.

The fundamental architecture is:

```text
               TOML Model Specification
                         |
                         v
              Python Model Preprocessor
                         |
             +-----------+-----------+
             |                       |
             v                       v
       Godley Tables          ODE Specifications
             |                       |
             +-----------+-----------+
                         |
                         v
                Julia Code Generator
                         |
              +----------+----------+
              |                     |
              v                     v
        Command-line           GUI-compatible
        Julia Solver            Julia Solver
              |                     |
              v                     v
          CSV Output          Shared Memory
              |                     |
              v                     v
         Plotly Reports        Dear PyGui
              |
              v
       Stability Analysis
```

There are three reasonably independent layers.

**Layer I — Mathematical modelling.** A TOML specification completely 
describes an ODE system, including parameters, state variables, initial 
conditions, auxiliary equations, integration settings, and output 
requirements.

**Layer II — Numerical simulation.** Python generates Julia source code, 
which is subsequently executed using the DifferentialEquations.jl ecosystem.

**Layer III — User interface and visualization.** Python provides 
interactive plotting, stability analysis, report generation, and 
eventually a Dear PyGui control interface.

The deliberate separation between Layers I–II and Layer III is a 
particularly useful architectural decision. It means the GUI can be 
developed later, or even before the macroeconomic modelling becomes 
productive (using the POorenz and Pendulum examples).


## 2. Project structure

The important components are:

| File or directory | Purpose |
|---|---|
| `README.md` | Public introduction |
| `README_pukahapai.md` | Main development notebook and TODO list |
| `models/` | TOML specifications, generated Julia programs, CSV data, HTML reports |
| `generate_julia_odesolver.py` | Principal Julia source-code generator |
| `templates/` | Jinja2 templates for Julia solvers |
| `godley_check.py` | Godley transaction table verification and documentation |
| `odemodel2tex.py` | Mathematical documentation generator |
| `plots4model.py` | Interactive Plotly report generation |
| `plot_utils.py` | Plotting and auxiliary-variable computation |
| `stability.py` | Jacobian eigenvalue visualization and analysis |
| `dpg_utils/` | Dear PyGui and shared-memory support |
| `tests/` | Regression tests for numerical examples |
| `docs/` | LaTeX documents, PDFs, and illustrations |
| `pukahaPai.py` | DearPyGui controller+viewer with shared memory. |

There are also several large CSV and HTML outputs from previous 
simulation runs.

## 3. The TOML modelling system

This is the core of the project.

Consider the damped pendulum specification:

```toml
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

[equations.ode]
f_theta = "omega"
f_omega = "-damping * omega - (g / length) * sin(theta)"

[tspan]
t0 = 0.0
t1 = 100.0

[solver]
dt = 0.01
method = "Tsit5"
```

The specification describes
$$
\begin{align*}
\frac{d\theta}{dt} &= \omega, \\\\
\frac{d\omega}{dt} &=-\gamma\omega-\frac{g}{L}\sin\theta.
\end{align*}
$$

The current design allows users to specify the mathematical system 
without knowing Julia programming.  ThePython generator handles the 
translation.


### An important additional feature

The specification also supports equations depending upon other time 
derivatives.

For example,
$$
\frac{du}{dt} = u \left(
   \Phi+\frac{\varpi}{\lambda}
   \frac{d\lambda}{dt} + \frac{1}{P}\frac{dP}{dt}- \alpha
\right).
$$

The generator detects references such as `f_lambda` and `f_P`, then sorts 
the derivative calculations into a suitable evaluation order.
This is implemented through a dependency graph and topological sorting.

One limitation is that circular dependencies between derivative 
expressions are rejected. The current system therefore supports acyclic 
derivative dependencies, rather than arbitrary implicit 
differential-algebraic systems.

## 4. Julia numerical solvers

My generator produces two versions of each model:

```text
models/pendulum_cmdl.jl
models/pendulum_gui.jl
```

The first is the standalone solver.

The second is intended for GUI integration.

### Numerical method

The Julia templates construct a residual equation of the form
$$
F(\dot{\mathbf{x}},\mathbf{x},t) = \dot{\mathbf{x}}-\mathbf{f}(\mathbf{x},t)=0.
$$
They then construct a `DAEProblem` and use the Sundials IDA integrator.

For example:

```julia
prob = DAEProblem(
    dae!,
    du0,
    u0,
    tspan,
    differential_vars = [true, true]
)

sol = solve(
    prob,
    IDA(),
    dt=dt,
    adaptive=false,
    callback=cb,
    abstol=1e-8,
    reltol=1e-6
)
```

This is slightly more general than using an explicit `ODEProblem`.

However, there is an important distinction between the design and 
implementation.

**The current templates always use `IDA()`.**

Although the TOML file accepts

```toml
[solver]
method = "Tsit5"
```

the selected method is not actually passed to `solve`.

Consequently, the configurable integration algorithm is presently an 
intended feature rather than a functioning one.

**TODO:** I would recommend fixing this during the initial restoration phase.

For standard ODE models, we should support `ODEProblem` directly, 
while retaining `DAEProblem` where required.


## 5. Existing mathematical models

You have five TOML specifications.

| Model | Status | Purpose |
|---|---|---|
| `pendulum` | Previously tested | Simple damped oscillator |
| `lorenz_attractor` | Previously tested | Nonlinear chaotic dynamics |
| `mmm_0_1` | Incomplete | Initial Minsky macroeconomic model |
| `mmm_0_2` | Partially operational | Monetary macroeconomic model |
| `mmm_0_3` | Incomplete | Sectoral balances with Godley tables |

The first two constitute the numerical regression-test suite.

### Pendulum

Tests two coupled differential equations and produces both time-series and phase-space plots.

### Lorenz attractor

Tests a nonlinear, three-dimensional dynamical system:
$$
\begin{align*}
\dot{x} &= \sigma(y-x),\\\\
\dot{y} &= x(\rho-z)-y,\\\\
\dot{z} &= xy-\beta z.
\end{align*}
$$

Its chaotic behaviour makes it useful for checking numerical reproducibility and sensitivity.

### Minsky models

These are where opur (me alone at present, but I am following on from 
Steve keen and Ty Keynes) actual economic research begins.

The progression from `mmm_0_1` to `mmm_0_3` is significant.

The first models attempt to describe aggregate dynamics using a small 
number of state variables.

The third introduces explicit monetary accounts, allowing stock-flow 
consistency to become part of the construction of the dynamical system.

## 6. The macroeconomic modelling programme

The PukahaPai project is a slightly broader research programme than 
simply solving differential equations, and narrower than a general 
purpose ODE solver helper.

There are three proposed economic policy regimes.

| Regime | Policy objective | General approach |
|---|---|---|
| MMT Owl | Full employment | Job Guarantee and fiscal stabilization |
| Post-Keynesian Dove | Price stability | Fiscal adjustments responding to inflation |
| Neoliberal Hawk | Deficit/debt targeting | Fiscal adjustments responding to public debt |

The intention is to compare macroeconomic performance across regimes.

Our central hypotheses concern employment, productivity, stability, 
inflation, and distributional outcomes.
The MMT baseline includes a Job Guarantee, with ZIRP as a 
monetary-policy reference case.

The underlying design assumes monetary sovereignty and treats unemployment 
as a policy variable rather than accepting a NAIRU constraint.

### Forecasting philosophy

An important principle in my earlier notes is that nonlinear macroeconomic 
forecasting has a limited useful horizon.
I envisage short-horizon empirical forecasting, while retaining 
long-horizon simulations for theoretical policy experiments.

In particular, we want to explicitly recognize that a policy regime may 
change before a long-run forecast could be realized.


### Intended applications

The principal applications are:

1. New Zealand macroeconomic forecasting and policy counterfactuals.
2. Monte Carlo comparisons of policy regimes.
3. Interactive policy simulations in which the user changes the 
government's response functions during a run.

The third application provides much of my motivation for the GUI, though I 
am a bit slack on getting a GUI, since I might never use it.


## 7. Godley tables and stock-flow consistency

This is one of the most important components for future development.

My current TOML format includes a special section:

```toml
[godley]

T1 = [
    "F_D",
    "W_D",
    "u*lambda*A*N",
    "Worker wages"
]
```

This represents a transaction transferring wages from firm deposits to 
household deposits. The generator interprets the transaction as 
contributions to two time derivatives.

For example,
$$
\begin{align*}
\left.\frac{dF_D}{dt}\right|\_{\mathrm{wages}} &= -u\lambda AN,\\\\
\left.\frac{dW_D}{dt}\right|\_{\mathrm{wages}} &= +u\lambda AN.
\end{align*}
$$

Adding these contributions gives
$$
\left.
\frac{d(F_D+W_D)}{dt}
\right|_{\mathrm{wages}}=0.
$$

Thus, the transaction preserves the aggregate deposits represented by 
those accounts.

This illustrates the underlying accounting principle:

> **Every transaction has offsetting accounting entries.**

The preprocessor collects all contributions for each account and 
generates its corresponding differential equation.

### What has been implemented

`parse_godley_flows()` in `generate_julia_odesolver.py` already performs 
this translation.

The separate utility `godley_check.py` generates readable Godley tables 
as Markdown and LaTeX, with optional PDF compilation.

This is a useful beginning for stock-flow-consistent modelling, but I 
left it unfinished and not fully tested..

### What remains unresolved

The Godley implementation is still rudimentary.

It treats transactions as transfers between two accounts, but does not 
yet provide a comprehensive system of balance-sheet constraints and 
accounting validation.

For example, a full implementation should distinguish between:

- Financial assets and liabilities.
- Sectoral income and expenditure flows.
- Transactions changing the composition of assets.
- Transactions creating or extinguishing financial claims.
- Valuation changes and other non-transaction adjustments.

That distinction becomes important when modelling bank lending, repayment, government debt, and central-bank operations.

We should eventually introduce automated accounting-identity checks.


## 8. The Dear PyGui architecture

My intention was to use Dear PyGui as an optional control interface.
I was experimenting with Python–Julia interoperability through POSIX 
shared memory.

The principal module is:

```text
dpg_utils/shared.py
```

It uses Python's

```python
multiprocessing.shared_memory
```

to allocate shared memory accessible by both processes.

The shared data structure contains:

- Solver state.
- Start time.
- End time.
- Model parameters.

Julia's corresponding generated structure is intended to access the 
same memory using `Mmap`.

The design is a simple flow:

```text
        Dear PyGui
            ↓
       Python Controller
            ↓
       Shared Memory
            ↓
        Julia Solver
```

This arrangement is intended to allow numerical computation and GUI 
interaction to proceed in separate processes.

### Current implementation status

The code indicates that shared-memory interoperability was being 
developed, but it is not yet fully integrated.

**TODO:** In particular, the generated Julia GUI solver contains 
the shared-memory 
reading functions, but the integration routine does not actually use them to 
control the model parameters or respond to start/stop commands.

**TODO:**  There is also a filename mismatch: the Python launcher looks 
for `models/<name>.jl`, whereas the generator produces `models/<name>_gui.jl`.

More importantly, the Julia GUI template does not currently bind the 
model parameters used by its equations.
These issues will have to be fixed before the GUI path can be considered 
operational.

I will leave them alone temporarily.

Thee command-line modelling framework can progress independently.

## 9. Visualization and reporting

This component is more developed than the GUI.

THe current workflow is:

```bash
./generate_julia_odesolver.py pendulum

julia models/pendulum_cmdl.jl

./plots4model.py pendulum
```

The resulting CSV file is processed by Python.

Plotly generates an HTML report containing interactive time-series plots 
and phase-space plots.

For suitable models, the reporting system also supports numerical 
stability analysis.

The output has two principal browser tabs:

**Simulation Results:** State variables, auxiliary quantities, and 
phase-space trajectories.

**Stability:** Eigenvalues, stability plots, and diagnostic information.

### Derived variables

One useful feature is the ability to calculate auxiliary quantities 
after numerical integration.

For example, if the ODE state includes the employment rate $\lambda$, 
productivity $A$ can be derived from
$$
A(t)=A_0e^{\alpha t},
$$
and employment from
$$
L(t)=\lambda(t)N(t).
$$
The plotting utilities can calculate these quantities from the simulated 
state trajectories.

This avoids unnecessarily enlarging the ODE system.

### Stability analysis

My stability routines use `ForwardDiff` to calculate Jacobians and 
subsequently determine eigenvalues.

**TODO!!!**

**I think there is a mathematical issue requiring attention!**

The Julia template currently differentiates the DAE residual
$$
F(\dot{\mathbf{x}},\mathbf{x},t) = \dot{\mathbf{x}}-\mathbf{f}(\mathbf{x},t)
$$
with respect to $\mathbf{x}$ while holding $\dot{\mathbf{x}}$ fixed.

Therefore,
$$
\frac{\partial F}{\partial\mathbf{x}} = -\frac{\partial\mathbf{f}}{\partial\mathbf{x}}.
$$

For an explicit ODE, the stability matrix is instead
$$
J=\frac{\partial\mathbf{f}}{\partial\mathbf{x}}.
$$
Consequently, the reported eigenvalues have the opposite sign from 
the conventional dynamical stability eigenvalues.

This should be corrected/checked before using the stability reports for 
economic interpretation. It shoudl suffice to use the Lorenz model to check.


## 10. Preliminary code audit

I performed an initial static inspection and ran the Python code 
generator against all five TOML specifications.

All five successfully generated their corresponding Julia source files.

This establishes that the basic TOML parsing and Jinja2 rendering 
process works in the present environment.

It does not establish that the generated Julia programs execute correctly.

Julia is not installed in this execution environment, so I have not run 
the numerical solvers or their integration tests.

The archive records successful Pendulum and Lorenz tests from July 2025.

### Problems identified

**TODO's: (several)**
 
| Component | Finding | Priority |
|---|---|---|
| Code generator | Generates all five models successfully | Working |
| Julia templates | TOML solver method is ignored | Medium |
| Initial conditions | Values depend on TOML insertion order rather than declared state order | High |
| `mmm_0_1` | Initial condition uses `u` rather than `u_s` | High |
| `mmm_0_2` | Contains probable double-counting of depreciation in the employment equation | High |
| `mmm_0_3` | Missing initial conditions for eight financial state variables | Critical |
| `mmm_0_3` | Missing derivative equations for four state variables | Critical |
| `mmm_0_3` | Contains undefined parameters and self-referential auxiliary expressions | Critical |
| Stability analysis | Incorrect Jacobian sign for explicit ODE stability | High |
| GUI | Main controller missing from archive | High |
| GUI interoperability | Shared-memory control path incomplete | High |
| Testing | Tests have not been rerun with current Julia | High |

The TOML specifications need more rigorous validation before generating 
Julia code.

For example, every declared state variable must have an initial condition, 
and every state must have a corresponding differential equation or an 
explicitly supported algebraic constraint.

The current generator does not enforce these conditions.

### An additional numerical concern

**TODO:** The CSV-writing callback is triggered by internal 
integration steps rather  than a prescribed output grid.
This explains why the current historical regression tests record very 
small early time steps despite specifying `dt = 0.01`.

We should distinguish the solver's internal step size from the desired 
output sampling interval.

That will also make the tests more reproducible.


## 11. Recommended development sequence

So (today) I am comming back to **PukahaPai** afgter about a year break. 
Difficult!  In future I think a good LLM should help with re-kick-starting 
these sorts of big-for-one-guy projects and be able to diagnose 
issues and recommend development plans, but we should also continue 
writing more unit tests. (I recall one project that just would not run,
but Once Upon a Time I thought I had left it in a running state!)

FOr now I will try dividing the renewed development into four phases.

### Phase A — Restore the numerical framework

First, establish that the pendulum and Lorenz models work reliably.

We should verify generation, execute the Julia solvers, check the CSV 
outputs, and reproduce the existing Plotly reports.

Then correct the generator's initial-condition ordering and solver-method 
handling.

The desired result is a dependable workflow requiring only a TOML 
specification and two commands to generate and execute a model.

### Phase B — Complete the first macroeconomic model

Seems a bit boring to regress, but I should probably start with 
running `mmm_0_2.toml`.

It has four state variables:
$$
\mathbf{x}(t)=
\begin{pmatrix}
P(t)\\\\
D(t)\\\\
u_s(t)\\\\
\lambda(t)
\end{pmatrix}.
$$

These represent prices, debt, wage share, and employment.

Its equations incorporate the Phillips response, government expenditure, 
taxation, and capital accumulation.

It is sufficiently small to inspect analytically while being much closer 
to the intended macroeconomic research than the Pendulum or Lorenz examples.
But in any case, we surely want Stability unti tests to work on Pendulum 
and Lorenz.

We should check the dimensional consistency and accounting interpretation 
of each equation before accepting its numerical trajectories.

### Phase C — Implement stock-flow-consistent models

Next, repair/upgrade `mmm_0_3.toml` and develop its Godley-table accounting.

This would establish the architecture needed for more sophisticated 
MMT simulations.

A key objective should be automatic verification that every financial 
flow satisfies the intended accounting identities.

### Phase D — Restore the GUI

Only after the core numerical system is reliable would I recommend 
returning to Dear PyGui.

The GUI can then become an interface for loading saved models, editing 
permitted parameters, running simulations, and comparing policy regimes.

There is no reason for it to control the design of the macroeconomic 
models themselves.

## 12. Overall assessment c.2026

(I might do one of these assessments every couple of years until I am 
happy or give up.)

The components I am happy-ish about are the TOML-to-Julia source generator, 
the standalone simulation architecture, the automated plotting facilities, 
and the beginning of Godley-table preprocessing, ... or really just the 
architecture ... I think each compoennt needs major work.

The main development gap (today) is in the **macroeconomic model specifications and their validation**.  I am not so woprried about the broken GUI.

Going forward post 2026, I will preserve the existing architecture I had 
from c.2024, rather than undertake a rewrite.

The three most important principles going forward should be:

1. **TOML remains the authoritative mathematical specification.** The 
numerical solver and visualization systems are generated from it.
2. **Stock-flow consistency becomes a testable mathematical invariant.** We 
should not rely solely on manually inspecting Godley tables.
3. **The GUI remains optional.** All mathematical models, numerical 
solvers, and diagnostic reports must operate independently of Dear PyGui.

The immediate next step should be a **systematic restoration and debugging of the TOML → Julia → CSV → Plotly pipeline**, 
using the existing pendulum and Lorenz regression tests, followed 
by `mmm_0_2`.


<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../340_00_macromodels_minsky">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../350_00_macromodels_lstm">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../340_00_macromodels_minsky">MM—XXX.0, Minsky</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../350_00_macromodels_lstm">Macromodels — LSTM/CNN</a></td>
</tr>
</table>


