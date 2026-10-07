---
title: "Macromodels — Mosler"
weight: 18
date: 2026-10-06
toc: true
katex: true
---

I have prepared a first implementation of `mmm_0_4.toml`, below is 
some documentaiton for mulling over. How to convince a Neoclassical this 
is better than thars?

## Initial O̶w̶l̶e̶r̶i̶e̶s̶ Worries

I was woprried about closing the ODE system, since we introduce the JG, but 
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

You can thus change the toml spec say to,
```toml
premium_F = -0.2
# or premium_F = 0.0
```

The positive reference wage $w_0$ also resolves an important problem: 
setting $w_{JG}=0$ does not eliminate the government's nominal 
price anchor.

Government wages and procurement prices remain defined.

The Job Guarantee is activated precisely when $w_{JG}>0$.

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
to firm production capacity.

Then the firm's desired price is
$$
P_{\mathrm{target}} = (1+m)\frac{w_F}{A_F} \exp(\eta_p e).
$$
The price ODE becomes
$$
\boxed{
\dot P = \tau_P(P_{\mathrm{target}}-P).
}
$$

Inflation is therefore
$$
\pi(t) = \frac{\dot P}{P}.
$$

This provides two mechanisms: a nominal price reference transmitted 
through government wage policy, and an endogenous private-sector 
price response.

Importantly, government wage policy does not mechanically determine 
every private price. Private prices can still change because of 
productivity, markup behaviour, and excess demand.

This distinction could become central to our experiments, maybe worht 
a Dirtbag MMT preprint.

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

One terminology distinction matters. My proposed $U3=N - L_F - L_G$ is 
useful as a measure of _non-JG labour-market slack_. It is not the 
conventional published U-3 unemployment statistic when those workers 
are employed by the JG. But I am ok calling it U3 since there is 
no US BLS statistic for a JG provision yet!


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

## 6. Preliminary numerical checks

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


## 7. Three modelling decisions

Before we develop this further, I would particularly like to nuance 
judgement on three or four issues:

**First: ordinary government employment.** I used a nominal public 
payroll budget rather than a workforce-share target. This seems compatible 
with my objectives, but it still represents an independent fiscal spending 
decision. Alternatively, we could derive government hiring from a demand for 
public services?

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


### First Attmepts

Keep `mmm_0_4` as a deliberately minimal model of government price 
anchoring and the JG labour buffer.**

The initial system has five ODE state variables:
$$
\mathbf{x} = (P,\lambda_F,F_D,W_D,G_N).
$$
This is considerably simpler than introducing a complete capital 
accumulation and banking system immediately.

Here is a nerdy question?:

> Can we decide whether the proposed **government payroll closure and fixed firm wage premium** adequately express my macroeconomic assumptions or intuitions?

Dunno.


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
<a href="../350_00_macromodels_lstm">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../341_00_macromodels_mosler">Macromodels — Mosler I</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../350_00_macromodels_lstm">Macromodels — LSTM/CNN</a></td>
</tr>
</table>


