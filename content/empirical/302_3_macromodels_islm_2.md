---
title: "Macromodels III --- IS-LM"
weight: 8
date: 2024-12-06
toc: true
katex: true
---

Things get a bit messy now. If you inspect the code for our OpenEconomyISLMModel class in the python module, you will see we've 
added a time series analysis class ``TimeSeriesISLMModel``
which will help us run some quasi-predictive tests against real world data.

Recall byb"quasi-predictive" we run immediately into troubles since IS-LM is a
static equilibrium model. The idea of bastardizing Keynes General Theory is to
at least pay a little bit of homage to Keynes and try to make the ISLM model a
moving equilibria (whatever that means!) We will take it to mean there is a lag
somewhere between 1 and 12 months at which point the economy has "figured out"
what Income and interest rate "should have been". We do not know the lag, so we
just run all the lags we want and see which fits best with the empirical data.

Seems reasonable? Yes, but then we need to go about fetching data, and 
unfortunately the only economy that has decent data I am personally familiar 
with fetching is the USA.  That is just a bias, since I've worked with the FRED API 
before. If your country published accessible data then you can conduct a similar analysis for your country. But honestly, why bother? We are aiming to show 
that you should never use ISLM! Maybe ISLM will turn out to be a good model for your country? Who knows!? But that would be fairly accidental and bizarre.


## Data Preparation

No pain, no gain.

### Interest Rates

We can try either FRED  Commercial Lending Rate series: `PRICELB`=Prime Loan
Rate, or `MPRIME`=Monthly Prime Lending Rate. I opted for 'MPRIME'. You
definitely do not want the fedfunds rate or interbank rate, since that's merely
the floor rate or the 'policy rate'. It determines the commercial rate, but we
do not want to bother modelling that function since we have the raw data.


### Foreign Interest Rate ($r^\ast$)

This is a tough one. Defining an effective foreign interest rate is complex. 
Suggestions:
   - G7 or G20 benchmark rates
   - Specific series:
     * `USGG10M`: US 10-Year Government Bond Yield (benchmark)
     * International equivalents:
       - ECB Reference Rate
       - Bank of Japan Policy Rate
       - Bank of England Base Rate

**Another option**: Create a trade-weighted composite rate based on: (1) Weights
of major trading partners; (2) Their respective government bond yields or central
bank rates. If you wanted to go to that effort, then the last step would be
putting your data into the proverbial calculator...

Foreign Interest Rate Composite:
```python
def compute_weighted_foreign_rate(trade_weights, countries):
    """
    Compute trade-weighted foreign interest rate
    
    Args:
    - trade_weights: Dict of country trade weights
    - countries: Dict of country interest rate series
    
    Returns:
    Composite weighted foreign interest rate
    """
    composite_rate = sum(
        weight * rate 
        for country, weight in trade_weights.items()
        for rate in [countries[country]]
    )
    return composite_rate
```

If you want to be a bit lazy I think it is ok to use the `USGG10M` as a proxy
for $r^\ast$, since while it is not the foreign_interest_rate, is it a
reasonable proxy for $r^\ast$ given that investment in bonds is pretty much a
subtraction from investment in domestic production? Whether this is a reasonable
argument I am not sure, but you can take it up with your local ISLM guru. If it
means our whole analysis is unfair to ISLM well... suck on it!


### National Income ($Y$)

I think we have to use nominal GDP since the other series will be in USD units, or millions of USD ("usd_mil"). The FRED series is `GDP`.

### Autonomous Consumption ($C_0$)

One of these was recommend, 
   - `PCE`=Personal Consumption Expenditures
   - `DPCERL`=Personal Consumption Expenditures, Chained 
   
I went with 'OPCE', but I gathered 'DPCERL' in my CSV file anyway, since it is
no bother to re-run our entire analysis with the alternates in case there is a
big difference.

### Consumption Sensitivity ($c_y$)

We derive this from change in consumption relative to income change
Compute from `PCE` and `PINTMKT` time series.

### Investment Sensitivity ($b$)

We have to doa computation, using the series `GPDI`=Gross Private Domestic
Investment. Then we can compute sensitivity from investment changes relative to
interest rate.

### Autonomous Investment ($I_0$)

We can use `GPDI`=Gross Private Domestic Investment, then look for the
baseline/trend component.

### Net Government Expenditure $(G-T)$

We can use `FDDSR`=Federal Surplus or Deficit.

### Liquidity Preference Parameter ($\ell$)

Two measures of velocity of money can be used,
   - `M2V`: Velocity of M2 Money Stock
   - `M1V`: Velocity of M1 Money Stock
















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
<a href="../301_2_macromodels_islm">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../303_4_macromodels_dsge">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../301_2_macromodels_islm">MM—I, Intro</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../303_4_macromodels_dsge">MM—III, DSGE</a></td>
</tr>
</table>


