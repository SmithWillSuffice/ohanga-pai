---
title: "NZ Macroconomic — I"
weight: 6
date: 2024-12-20
cover: ""
coverAlt: ""
toc: true
katex: true
tags: []
---

A new series on some aspect of NZ macroeconomics. Topics are just 
whatever I bother to look at and write-up.  Today, the Real NZ government 
surplus(deficit).

## NZ Government Real Deficit

This is topical whenever there is a significant inflation event, and 
such has occurred post-COVID.

We need a formula that can show how a nominal deficit can become a 
real surplus from the non-government sector's perspective when 
inflation is high enough.

The question is about how inflation affects the real value of 
government debt. Inflation can can turn a nominal deficit into a 
real surplus! That's bad for an economy with a growing population.


The basic formula would be:
$$
\text{Real Deficit} = \text{Nominal Deficit} - (\text{Inflation Rate}\times \text{Outstanding Debt})
$$
For example, if:  
**(i)** Nominal deficit = $1 trillion  
**(ii)** Outstanding debt = $30 trillion  
**(iii)** Inflation = 5%  
then,
$$
\text{Real deficit} = 1T - (0.05 \times 30T) = 1T - 1.5T = -0.5T
$$
This would actually be a real surplus of 500 billion, despite the 
nominal deficit.

Why are we using the government debt as the adjuster?

Let's think this through:

1. A nominal deficit of $1T means the government is injecting 1T of 
purchasing power into the non-government sector.

2. At the same time, inflation (say 5%) is reducing the real value 
of all nominal assets held by the non-government sector, including 
government securities (the $30T).

The original formula actually does capture this correctly:
Real deficit = Nominal deficit - (Inflation Rate × Outstanding Debt)

This works because:
**(i)** The nominal deficit represents new purchasing power injected
**(ii)** (Inflation Rate × Outstanding Debt) represents the loss of 
real purchasing power on existing government securities held by the 
non-government sector

This negative value (real surplus) means the non-government sector is 
actually losing purchasing power in real terms, despite the nominal 
deficit, because inflation's erosion of the value of their government 
asset holdings exceeds the new purchasing power injection.

### Back-of-the-envelop Real Deficit(Surplus)

[NZ Treasury statement 2023](https://www.treasury.govt.nz/sites/default/files/2023-10/fsgnz-2023.pdf) was:
* Net GovDebt = 18% of GDP.
* GDP = \$2.52175506110 USD.  NZ-Tsy nominal GDP = \$3.95896 NZD.
* Expenditure (core)= 1,276 billion nzd.
* Revenue (core) = 1.124 billion nzd.
* Expenditure total = 1.61822 billion.
* CPI inflation = 5.7% (average), mid-year was 5.3%.


GDP agrees with [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=NZ). To convert to NZD the 
effective exchange rate was 1.5699 nzd per usd. Looks about right, daily 
was around 1.55 to 1.75.

So Net GovDebt = $3.95896\times 0.18$ $= 0.7126$ billion nzd. FRED
series `NZLGGXWDGG01GDPPT` has GrossGovDebt = 31.35% of GDP = $1.247$ billion nzd.

Nominal deficit = $1.276 - 1.124 = 0.152$ billion nzd.

Plugging this in:
$$
\text{Real deficit} = 0.152 - 0.057\times 1.247 = 0.081 \, \text{bil. nzd}
$$



To validate with external data like FRED and OECD, today, at the time 
of writing,  I needed 
the [2022 Treasury Statement:](https://www.treasury.govt.nz/sites/default/files/2022-10/fsgnz-2022_2.pdf):

* GDP = 3.59476 billion nzd.
* Net GovDebt = 0.61829872 billion nzd or 17.2% of GDP.
* Gross GovDebt = 1.18986556 billion or 33.1% of GDP.

Check: From OECD and FRED:
* FRED `NZLGGXWDGG01GDPPT`: GovDebt (total) 31.9% of GDP.
* OECD: Gross GovDebt (total) 59.59% of GDP.

Unfortunately, the API for Treasury data is an excel spreadsheet 🤣.
But I am glad I checked, since it looks like I had been using the 
wrong FRED series `DEBTTLNZA188A` instead of the series more in alignment 
with NZ Treasury which is `NZLGGXWDGG01GDPPT`.

It is probably a good thing what matters for MMT analysis is more the 
change in the GovDebt. Since the outstanding absolute debt is really just 
a price level effect, and we know the price level roughly from other data.
Further, what matters is relative prices, price::wage ratio for necessary 
goods, and purchasing power, not the absolute price level. 




## Time Series Automation

I thought it worthwhile automating a time series for the Real Deficit.
It might be published somewhere, but repetition does not hurt.


## The USA Case

For empirical data input we have:
1. MTSDS133FMS - Monthly Treasury Statement (Federal Surplus or Deficit)
2. PCEPI or CPI - Price indices for inflation adjustment.
3. Outstanding Debt Effect: the real deficit/surplus calculation should 
account for how inflation erodes the real value of the existing .
debt stock, not just the nominal deficit flow. We'll need:
  - Total outstanding government debt (we can use GFDEBTN from FRED).

The FRED series ID's just given will let you run a USA analysis, but 
we are interested in the NZ analysis at Ōhanga Pai. 

## The NZ Case

I think we can fetch most stuff from the FRED, but if not the BIS portal 
is a good first fallback, then the OECD portal. The latter two are 
clunkier to navigate, but here are some tips.

First, you only need to do this once, since we will get python code 
for automating future data updates.

* Go to <https://data.bis.org/>
* In the search box type a short accurate description of the series you 
want, .e.g `NZ government total debt`.
* Select from the result the series that looks like a closest match. For 
example, I selected <https://data.bis.org/topics/LBS/BIS,WS_LBS_D_PUB,1.0/Q.S.C.D.TO1.A.5J.A.5A.G.NZ.N>
* Up on the top right of the webpage, above the Bookmark button 
click the "Export" button,
* Click on the "Code Snippet" tab.
* Python radio button is default, so now just scroll down to the code 
snippet and copy using the copy button icon. Paste into your python 
script.
* Note the BIS units for this series are US$mil., so we do not need to 
convert (our other islm data series were converted to millions of usd.)

Others for CPI (proxy for Inflation) and the deficit(surplus) :
```
TODO
CPI?
Deficit?
```

The BIS are a bit of a pain, since the `TIME_DATE` column has 
format `yyyyy-Qn`.

We want to convert Quarters into `yyyy-mm-01` dates. The BIS docs suggests 
the quarters are ending, so we want our actual datetimes to be end of 
March, September and December, but offset one day to 1st of the next 
month. So the quarters I use are e.g.,
```
2024-01-01 
2024-04-01
2024-07-01 
```
This function will do that for you:
```python
def convert_quarter_to_date(quarter_str):
    period = pd.Period(quarter_str, freq='Q')
    start_of_next_quarter = period.asfreq('Q-JAN').start_time + pd.DateOffset(months=3)
    first_of_last_month = start_of_next_quarter - pd.DateOffset(months=1)
    return first_of_last_month
```



#### Problems

**Problem 1.**  
An immediate problem was that the BIS data set I choose did not look 
like the NZ government debt. It was some obscure banking composite. But 
it might be close to the series we ultimately want. So I had a go at 
using the OECD SDMX-JSON Rest-API.


**Problem 2.**  
The OECD Gross GovDebt figures are ballpark 59% of GDP (2022), whereas 
NZ Treasury quotes 33.1%. 

The FRED series `DEBTTLNZA188A` is close to the OECD. No good!

The FRED series `NZLGGXWDGG01GDPPT` is closer to NZ Treasury, but 
starts at 2016. SO is not so useful.

I think we should be using the NZ Treasury Statements. But they are excel 
spreadsheet files. I did automate some of that, so will return to look at 
making a cron job for updating the data. The main thing is not not mess 
with the historical data, and only do a most recent years update/append.


### OECD API

The Expenditure and Revenue series from the OECD are useful for comparing 
with the NZ Treasury data pull. This is just for data validation. I prefer 
to use the NZ Treasury Statements as the main source.

The NZ Government Expenditure and Revenue series seem to be available, 
the difference of these two aught to be our $(G-T)$. Also a 
'Gross debt of general government' series is published, the year-on-year 
change in that should be close tot $G-T)$.  All these series are in 
units '% of GDP', so we need to fetch the GDP data too.

In case I forget, here is the way to get this data.

* Go to the explorer <https://data-explorer.oecd.org/>
* Put in a search, "Government expenditure" should do the trick, or 
"National Accounts at a Glance (NAAG) Chapter 6: Government". 
I actually got there from a higher level overview of the OECD statistics 
here: <https://www.oecd.org/en/data/indicators/general-government-deficit.html?oecdcontrol-8478925713-var1=NZL>.
* Deselect all the _other_ countries in the Region filter, I left New Zealand 
and the USA, since I want to check the USA against the FRED as my initial 
data validation.
* We should be on the "NAAG Chapter 6: Government" page.
* In the Measure filter select what you want, I went for (1) Expenditure, 
(2) Revenue. (We do not want the "Gross debt" series since that confounds 
cross-border stuff and "all currencies".)
* In the Time period filter select the max range (1970 to present).
* Click on the Chart header to check the plot is ok.
* Click on "Developer API" on the top right of the dashboard.
* Change "SDMX flavour:" to "Time series" option.
* Copy the supplied Data query URL.

Now we need to paste this URL into our python script and make the 
request.

Your python snippet or URL will have the present date hard-coded, so it 
is good to make a str replacement in your script for this, so that you do 
not have to change the code in the future.

After all this it is a good idea to compare, at least between your eye balls, 
with FRED series. You want to check the numbers and units roughly match. 
Often FRED gets the raw data from the BIS or OECD, so often they are a 
perfect match.

Other series needed:
```
fredapi
--------
gov_debt :  'DEBTTLNZA188A',  'unit': 'pct_gdp'
cpi : 'MKTGDPNZA646NWDB'
gdp: 'MKTGDPNZA646NWDB', 'unit': 'usd_current'
```

Things to later check for data validation:
```
OECD has GDP per capita in USD:
https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_HCPC,/A.NZL...B1GQ_POP.......?startPeriod=1960&endPeriod=2023
```
So for that we need Population and Exchange rate:
```
nz_pop: 
-------
https://sdmx.oecd.org/public/rest/data/OECD.ELS.SAE,DSD_POPULATION@DF_POP_HIST,/NZL..PS._T._T.?startPeriod=1950&endPeriod=2022

usd_nzd:
--------
fredapi: 'CCUSMA02NZM618N'

bis: 
<https://data.bis.org/topics/XRU/BIS,WS_XRU,1.0/M.NZ.NZD.E>
import pandas as pd
urls = ["https://stats.bis.org/api/v2/data/dataflow/BIS/WS_XRU/1.0/M.NZ.NZD.E?format=csv"]
df = pd.concat([pd.read_csv(url) for url in urls])
```


<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_2_funds_flows">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../101_nzecon_ii">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_2_funds_flows">Fund sFlow</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../101_nzecon_ii">NZ Econ II</a></td>
</tr>
</table>

