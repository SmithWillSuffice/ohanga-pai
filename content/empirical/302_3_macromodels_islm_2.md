---
title: "Macromodels III --- IS-LM"
weight: 10
date: 2024-12-06
toc: true
katex: true
---

Things get a bit messy now. If you inspect the code for our OpenEconomyISLMModel class in the python module, you will see we've 
added a time series analysis class ``TimeSeriesISLMModel``
which will help us run some quasi-predictive tests against real world data.

Recall by "quasi-predictive" we run immediately into troubles since IS-LM is a
static equilibrium model. The idea of bastardizing Keynes' General Theory is to
at least pay a little bit of homage to Keynes and try to make the ISLM model a
moving equilibria (whatever that means!) We will take it to mean there is a lag
somewhere between 1 and 12 months at which point the economy has "figured out"
what Income and interest rate "should have been". We do not know the lag, so we
just run all the lags we want and see which fits best with the empirical data.

Seems reasonable? Yes, but then we need to go about fetching data, and
unfortunately the only economy that has decent data I am personally familiar
with fetching is the USA.  That is just a bias, since I've worked with the FRED
API before. If your country published accessible data then you can conduct a
similar analysis for your country. But honestly, why bother? We are aiming to
show that you should never use ISLM! Maybe ISLM will turn out to be a fit (as in
parameter adjusted) model for your country? Who knows!? But that would be fairly
accidental and bizarre.


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
     * `IRLTLT01USM156N`: US 10-Year Government Bond Yield (benchmark)
     * International equivalents:
       - ECB Reference Rate
       - Bank of Japan Policy Rate
       - Bank of England Base Rate

The series 'DGS10' is daily data otherwise comparable to 'IRLTLT01USM156N',  
but we only need monthly frequency, so I prefer the latter for the ISLM study.

**Another option**: Create a trade-weighted composite rate based on: (1) Weights
of major trading partners; (2) Their respective government bond yields or central
bank rates. If you wanted to go to that effort, then the last step would be
putting your data into the proverbial calculator...

Here is how you might start with computing a Foreign Interest Rate Composite:
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

If you want to avoid the worry, just eliminate the foreign sector from your
model! However, looking at the trade data the USA is still a big net importer,
so this should have a significant effect on the macroeconomic variables and
outputs we wish to model.  If you want to write this up for a term paper for a
vegetative economics professor you could try this sort of little discussion to
justify using the US 10 year bond yield as a reasonable proxy for a
'foreignInterestRate' input.

Using the US 10-Year Treasury Yield as a proxy for $r^*$ is a reasonable
rough approach for the following reasons:

* Global Benchmark: The US 10-year bond yield is widely regarded as a global
  benchmark for interest rates. It is influenced by international factors, such
  as global demand for USD-denominated assets.
* Foreign Holdings: Foreign investors hold significant amounts of US government
  bonds. Changes in the 10-year yield can reflect shifts in global interest rate
  expectations and investment preferences.

Caveats:

* The US 10-year yield primarily reflects US government bond risk and liquidity
  premia, so it may not fully capture foreign central bank or private market
  conditions.
* If your analysis heavily depends on exchange rate dynamics, the divergence
  between US and global monetary policies might need finer calibration.

If you want to be a bit lazy then, I think it is ok to use the `IRLTLT01USM156N`
as a proxy for $r^\ast$, since while it is not the foreign_interest_rate, is it
a reasonable proxy for $r^\ast$ given that investment in bonds is pretty much a
subtraction from investment in domestic production? Whether this is a reasonable
argument I am not sure, but you can take it up with your local ISLM guru. If it
means our whole analysis is unfair to ISLM well... suck on it!


### National Income ($Y$)

I think we have to use nominal GDP since the other series will be in USD units, or millions of USD ("usd_mil"). The FRED series is `GDP`.

### Net Government Expenditure $(G-T)$

We can use `MTSDS133FMS`=Federal Surplus or Deficit.

### Autonomous Consumption ($C_0$)

One of these was recommend, 
   - `PCE`=Personal Consumption Expenditures
   - `DPCERL`=Personal Consumption Expenditures, Chained 
   
I went with 'OPCE', but I gathered 'DPCERL' in my CSV file anyway, since it is
no bother to re-run our entire analysis with the alternates in case there is a
big difference.

### Consumption Sensitivity ($c_y$)

We derive this from change in consumption relative to income change
Compute from `PCE` and `PI` time series.

### Investment Sensitivity ($b$)

We have to do a computation, using the series `GPDI`=Gross Private Domestic
Investment. Then we can compute sensitivity from investment changes relative to
interest rate.

### Autonomous Investment ($I_0$)

We can use `GPDI`=Gross Private Domestic Investment, then look for the
baseline/trend component.

### Money Supply ($M$)

I used the `M2SL` series, the M2 money stock.

### Liquidity Preference Parameter ($\ell$)

Two measures of velocity of money can be used,
   - `M2V`: Velocity of M2 Money Stock
   - `M1V`: Velocity of M1 Money Stock

Since I chose `M2SL` for supply (stock) I need to use `M2V` for velocity.


## Data Processing

Do we have five parameters to estimate then? Let's go through these in detail.
The FRED API data pulls script I have is a bit lengthy, since I need to
interpolate some Quarterly series to Monthly, and down-sample some weekly series
to monthly. But you can get it from the github repo.

The FRED series I download are not all used, but I think are sufficient. 
The dictionary I use is,
```python
series_dict = {
    'GDP': {'name': 'Gross Domestic Product', 'type':'flow','freq':'Q', 'unit':'bil'},
    'MPRIME': {'name': 'Bank Prime Loan Rate', 'type':'stock','freq':'M', 'unit':'%'},
    'FEDFUNDS': {'name': 'Federal Funds Rate', 'type':'stock','freq':'M', 'unit':'%'},
    'IRLTLT01USM156N': {'name': '10-Year Treasury', 'type':'stock', 'freq':'M', 'unit':'%'},
    'PCE': {'name': 'Personal Consumption Expenditures', 'type':'flow','freq':'M', 'unit':'bil'},
    'PI': {'name': 'Personal Income', 'type':'flow','freq':'M', 'unit':'bil'},
    'DSPI': {'name': 'Disposable Personal Income', 'type':'flow','freq':'M', 'unit':'bil'},
    'GPDI': {'name': 'Gross Private Domestic Investment', 'type':'flow', 'freq':'M', 'unit':'bil'},
    'MORTGAGE30US': {'name': '30-Year Fixed Mortgage Rate', 'type':'stock','freq':'W', 'unit':'%'},
    'DTWEXAFEGS': {'name': 'Trade-Weighted Exchange Rate (Advanced Economies)', 'type':'stock','freq':'M', 'unit':'None'},
    'DTWEXBGS': {'name': 'Trade-Weighted Exchange Rate (Broad)', 'type':'stock','freq':'M', 'unit':'None'},
    'M2V': {'name': 'M2 Money Velocity', 'type':'stock', 'freq':'Q', 'unit':'None'},
    'M2SL': {'name': 'M2 Money Stock', 'type':'stock', 'freq':'M', 'unit':'bil'},
    'M1V': {'name': 'M1 Money Velocity', 'type':'stock', 'freq':'Q', 'unit':'None'},
    'NETEXP': {'name': 'Net Exports of Goods and Services', 'type':'flow', 'freq':'Q', 'unit':'bil'},
    'MTSDS133FMS': {'name': 'Monthly Treasury Statement Deficit', 'type':'flow', 'freq':'M', 'unit':'mil'},
}
```
I did not automate fetching the 'type', 'freq' and 'unit' values, I wrote them
in by hand, so you should double chack them for yourself.


### Autonomous Consumption ($C_0$ and sensitivity $c_y$)

To estimate $c_0$ and $c_y$, we'll need to separate the baseline consumption
that occurs regardless of income from the income-dependent consumption. We can
use PCE (Personal Consumption Expenditures) and PI (Personal Income) to estimate
the consumption function:  $C = C_0 + c_y Y$.

Explicit code for this could be:
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller


def estimate_autonomous_consumption(pce, pi):
    """
    Estimate autonomous consumption (C0) using PCE and Personal Income data
    
    Parameters:
    pce (pandas.Series): Personal Consumption Expenditures time series
    pi (pandas.Series): Personal Income time series
    
    Returns:
    dict: Dictionary containing C0, cy, R-squared, and other statistics
    """
    # Ensure data is properly aligned and clean
    data = pd.DataFrame({
        'PCE': pce,
        'PI': pi
    }).dropna()
    # Prepare data for regression
    X = data['PI'].values.reshape(-1, 1)
    y = data['PCE'].values
    # Run regression with statsmodels for detailed statistics
    X_sm = sm.add_constant(X)
    model_sm = sm.OLS(y, X_sm).fit()
    # Calculate basic regression with sklearn for prediction purposes
    reg = LinearRegression().fit(X, y)
    
    # Compute statistics
    results = {
        'C0': float(model_sm.params[0]),  # Autonomous consumption
        'cy': float(model_sm.params[1]),  # Marginal propensity to consume
        'r_squared': model_sm.rsquared,
        'adj_r_squared': model_sm.rsquared_adj,
        'p_values': model_sm.pvalues.tolist(),
        'std_errors': model_sm.bse.tolist(),
        'regression_summary': model_sm.summary()
    }
    # Add confidence intervals
    conf_int = model_sm.conf_int()
    results['C0_conf_int'] = conf_int[0].tolist()
    results['cy_conf_int'] = conf_int[1].tolist()
    
    # Add diagnostic statistics
    results['durbin_watson'] = sm.stats.stattools.durbin_watson(model_sm.resid)
    return results

def analyze_consumption_stationarity(pce, pi):
    """
    Analyze stationarity of consumption and income series
    
    Parameters:
    pce (pandas.Series): Personal Consumption Expenditures time series
    pi (pandas.Series): Personal Income time series
    
    Returns:
    dict: Dictionary containing stationarity test results
    """
    results = {}
    # Test PCE stationarity
    pce_adf = adfuller(pce.dropna())
    results['pce_adf_stat'] = pce_adf[0]
    results['pce_adf_pvalue'] = pce_adf[1]
    # Test PI stationarity
    pi_adf = adfuller(pi.dropna())
    results['pi_adf_stat'] = pi_adf[0]
    results['pi_adf_pvalue'] = pi_adf[1]
    return results
```

I add the $C_0$ and $c_y$ values as new columns to my `fred_df` dataframe 
in memory, but I do not overwrite my fred csv file, I save the ISLM 
parameter results to a separate CSV, `islm_series.csv`. If you want to 
see my wrapper script just check the github repo.

I also save the stationarity analysis results to separate json files. But I have
not inspected them, since I already know ISLM is a bad model.  Ive included the
stationarity analysis for you so you can write a term paper for your Turnip-head
(opr Potato-head, as the case may be)  economics professor.


### Investment Sensitivity ($b$)

We can estimate the investment sensitivity parameter $b$ using GPDI and interest
rate data. We'll need to isolate how investment responds to interest rate
changes while controlling for other factors.


Explicit code for this could be:
```python
# ... previous imports
from statsmodels.tsa.filters.hp_filter import hpfilter


def estimate_investment_sensitivity(gpdi, interest_rate, gdp, control_for_output=True):
    """
    Estimate investment sensitivity (b) to interest rate changes.
    
    Parameters:
    gpdi (pandas.Series): Gross Private Domestic Investment
    interest_rate (pandas.Series): Interest rate series (e.g., MPRIME)
    gdp (pandas.Series): GDP series for controlling output effects
    control_for_output (bool): Whether to include GDP as control variable
    
    Returns:
    dict: Dictionary containing b, statistical measures, and diagnostic tests
    """
    # Create first differences to address potential non-stationarity
    d_gpdi = gpdi.pct_change()
    d_interest = interest_rate.diff()
    d_gdp = gdp.pct_change() if control_for_output else None
    
    # Align data and remove NAs
    data = pd.DataFrame({
        'Investment_Change': d_gpdi,
        'Interest_Change': d_interest,
        'GDP_Change': d_gdp if control_for_output else np.nan
    }).dropna()
    
    # Prepare regression variables
    if control_for_output:
        X = data[['Interest_Change', 'GDP_Change']]
    else:
        X = data[['Interest_Change']]
    
    y = data['Investment_Change']
    # Add constant and run regression
    X_sm = sm.add_constant(X)
    model = sm.OLS(y, X_sm).fit()
    # Calculate investment sensitivity (b)
    # Note: We take negative of coefficient since IS curve uses -b(r-r*)
    results = {
        'b': float(-model.params['Interest_Change']),
        'b_std_error': float(model.bse['Interest_Change']),
        'b_p_value': float(model.pvalues['Interest_Change']),
        'r_squared': model.rsquared,
        'adj_r_squared': model.rsquared_adj,
        'regression_summary': model.summary()
    }
    # Add confidence intervals
    conf_int = model.conf_int()
    results['b_conf_int'] = [-float(conf_int.loc['Interest_Change'][1]), 
                            -float(conf_int.loc['Interest_Change'][0])]
    
    # Add diagnostic tests
    results['durbin_watson'] = sm.stats.stattools.durbin_watson(model.resid)
    return results


def analyze_investment_components(gpdi, interest_rate):
    """
    Decompose investment series into trend and cyclical components
    to better understand interest rate sensitivity.
    
    Parameters:
    gpdi (pandas.Series): Gross Private Domestic Investment
    interest_rate (pandas.Series): Interest rate series
    
    Returns:
    dict: Dictionary containing cyclical analysis results
    """
    # Apply HP filter to decompose investment
    cycle, trend = hpfilter(np.log(gpdi), lamb=1600)  # Using standard lambda for quarterly data
    
    # Calculate correlation between cyclical component and interest rates
    aligned_data = pd.DataFrame({
        'cycle': cycle,
        'interest': interest_rate
    }).dropna()
    
    correlation = aligned_data['cycle'].corr(aligned_data['interest'])
    
    return {
        'cycle': cycle,
        'trend': trend,
        'interest_rate_correlation': correlation
    }
```
As before, you can organize your wrapper scripts to add the $b$ 
computations to your CSV files.


### Autonomous Investment ($I_0$)

We can use GPDI=Gross Private Domestic Investment, then look for the
baseline/trend component.  Taking raw GPDI as $I_0$ would be inaccurate because
GPDI includes both autonomous investment ($I_0$) and the interest-sensitive
component ($-b(r-r^\ast)$) that we already estimated. We need to decompose these
components.

Explicit code for this job:
```python
# previous imports
from statsmodels.tsa.seasonal import seasonal_decompose


def estimate_autonomous_investment(gpdi, ir, b_estimate):
    """
    Estimate autonomous investment (I0) by decomposing GPDI and removing
    interest rate sensitive components.
    
    Parameters:
    gpdi (pandas.Series): Gross Private Domestic Investment
    interest_rate (pandas.Series): Interest rate series
    b_estimate (float): Previously estimated interest rate sensitivity
    
    Returns:
    dict: Dictionary containing I0 estimates and decomposition components
    """
    # Align series and clean data
    data = pd.DataFrame({
        'GPDI': gpdi,
        'interest_rate': ir
    }).dropna()
    
    # Method 1: HP Filter approach
    cycle, trend = hpfilter(np.log(data['GPDI']), lamb=14400)  # Lambda for monthly data

    # Method 2: Remove interest rate component
    interest_component = b_estimate * (data['interest_rate'] - data['interest_rate'].mean())
    adjusted_investment = data['GPDI'] + interest_component  # Add because IS curve has -b(r-r*)

    # Method 3: Seasonal decomposition
    seasonal_result = seasonal_decompose(data['GPDI'], period=12, extrapolate_trend='freq')
    # Compute different I0 estimates
    results = {
        'I0_hp': np.exp(trend),  # HP filter trend
        'I0_interest_adjusted': adjusted_investment,  # Interest-adjusted series
        'I0_seasonal_trend': seasonal_result.trend,  # Seasonal decomposition trend
        
        # Store decomposition components
        'hp_cycle': cycle,
        'hp_trend': trend,
        'seasonal_trend': seasonal_result.trend,
        'seasonal_seasonal': seasonal_result.seasonal,
        'seasonal_residual': seasonal_result.resid,
        
        # Basic statistics
        'mean_I0_hp': float(np.exp(trend).mean()),
        'mean_I0_interest_adjusted': float(adjusted_investment.mean()),
        'mean_I0_seasonal': float(seasonal_result.trend.mean())
    }
    # Compute confidence bands using rolling statistics
    window = 12  # One year rolling window
    results['I0_rolling_mean'] = adjusted_investment.rolling(window=window).mean()
    results['I0_rolling_std'] = adjusted_investment.rolling(window=window).std()
    results['I0_upper_band'] = results['I0_rolling_mean'] + 2 * results['I0_rolling_std']
    results['I0_lower_band'] = results['I0_rolling_mean'] - 2 * results['I0_rolling_std']
    
    return results

def analyze_I0_stability(gpdi, interest_rate, b_estimate, window_sizes=[6, 12, 24]):
    """
    Analyze the stability of I0 estimates across different time windows
    
    Parameters:
    gpdi (pandas.Series): Gross Private Domestic Investment
    interest_rate (pandas.Series): Interest rate series
    b_estimate (float): Previously estimated interest rate sensitivity
    window_sizes (list): List of rolling window sizes to test
    
    Returns:
    dict: Dictionary containing stability analysis results
    """
    stability_results = {}
    for window in window_sizes:
        # Calculate rolling estimates
        rolling_data = estimate_autonomous_investment(
            gpdi.rolling(window=window).mean(),
            interest_rate.rolling(window=window).mean(),
            b_estimate
        )
        
        stability_results[f'window_{window}'] = {
            'mean': float(rolling_data['mean_I0_hp']),
            'std': float(rolling_data['I0_rolling_std'].mean()),
            'coefficient_of_variation': float(
                rolling_data['I0_rolling_std'].mean() / rolling_data['mean_I0_hp']
            )
        }
    return stability_results
```

We are almost done, just one more to go.



###  Liquidity Preference Parameter ($\ell$)

Two measures of velocity of money can be used, M2V: Velocity of M2 Money Stock
M1V: Velocity of M1 Money Stock.  In the IS-LM model, the liquidity preference
parameter $\ell$ represents the sensitivity of money demand to the interest
rate. We'll need to do more than just look at velocity measures, since we need
to estimate how money demand responds to interest rate changes.

Explicit code:
```python
# ... previous import
from statsmodels.tsa.api import VAR


def estimate_liquidity_preference(m1v, m2v, interest_rate, gdp, money_supply):
    """
    Estimate liquidity preference parameter (lp) using money velocity and other monetary data
    
    Parameters:
    m1v (pandas.Series): Velocity of M1 Money Stock
    m2v (pandas.Series): Velocity of M2 Money Stock
    interest_rate (pandas.Series): Interest rate series
    gdp (pandas.Series): GDP series
    money_supply (pandas.Series): Money supply (M1 or M2)
    
    Returns:
    dict: Dictionary containing ℓ estimates and diagnostic statistics
    """
    # Calculate real money balances (M/P)
    # Using GDP deflator implicit in velocity measure since V = PY/M
    real_money = money_supply / (gdp / money_supply * m1v)
    
    # Take logs for elasticity interpretation
    log_real_money = np.log(real_money)
    log_gdp = np.log(gdp)
    
    # Prepare data for regression
    data = pd.DataFrame({
        'log_real_money': log_real_money,
        'log_gdp': log_gdp,
        'interest_rate': interest_rate
    }).dropna()
    
    # Estimate money demand equation: log(M/P) = log(Y) - ℓr
    X = sm.add_constant(data[['log_gdp', 'interest_rate']])
    y = data['log_real_money']
    model = sm.OLS(y, X).fit()
    
    # Extract ℓ (negative of interest rate coefficient)
    results = {
        'lp': float(-model.params['interest_rate']),
        'lp_std_error': float(model.bse['interest_rate']),
        'lp_p_value': float(model.pvalues['interest_rate']),
        'income_elasticity': float(model.params['log_gdp']),
        'r_squared': model.rsquared,
        'regression_summary': model.summary()
    }
    
    # Add VAR analysis for dynamic relationships
    var_data = pd.DataFrame({
        'real_money': log_real_money,
        'gdp': log_gdp,
        'interest': interest_rate
    }).dropna()
    
    var_model = VAR(var_data)
    var_results = var_model.fit(maxlags=12, ic='aic')
    
    # Compute long-run elasticity from VAR
    irf = var_results.irf(periods=24)
    cumulative_response = np.cumsum(irf.irfs[:, 0, 2])  # Response of money to interest
    
    results['var_long_run_lp'] = float(-cumulative_response[-1])
    
    # Add alternative estimates using M2 velocity
    # Similar calculation but using M2V
    real_money_m2 = money_supply / (gdp / money_supply * m2v)
    log_real_money_m2 = np.log(real_money_m2)
    
    data_m2 = pd.DataFrame({
        'log_real_money': log_real_money_m2,
        'log_gdp': log_gdp,
        'interest_rate': interest_rate
    }).dropna()
    
    X_m2 = sm.add_constant(data_m2[['log_gdp', 'interest_rate']])
    y_m2 = data_m2['log_real_money']
    model_m2 = sm.OLS(y_m2, X_m2).fit()
    
    results['lp_m2'] = float(-model_m2.params['interest_rate'])
    results['lp_m2_std_error'] = float(model_m2.bse['interest_rate'])
    
    return results

def analyze_stability(m1v, m2v, interest_rate, gdp, money_supply, window_sizes=[12, 24, 36]):
    """
    Analyze stability of ℓ estimates across different time windows
    
    Parameters:
    [same as above]
    window_sizes: List of rolling window sizes for stability analysis
    
    Returns:
    dict: Dictionary containing stability analysis results
    """
    stability_results = {}
    for window in window_sizes:
        rolling_ell = pd.Series(index=m1v.index[window:])
        
        for i in range(len(m1v) - window):
            slice_results = estimate_liquidity_preference(
                m1v[i:i+window],
                m2v[i:i+window],
                interest_rate[i:i+window],
                gdp[i:i+window],
                money_supply[i:i+window]
            )
            rolling_ell.iloc[i] = slice_results['lp']
            
        stability_results[f'window_{window}'] = {
            'mean_lp': float(rolling_ell.mean()),
            'std_lp': float(rolling_ell.std()),
            'cv_lp': float(rolling_ell.std() / rolling_ell.mean())
        }
    return stability_results
```

I think that's it for data collection. This chapter has not given you the full
code, but it is a good exercise to organize a script for this yourself. 

The next thing is to run some scenarios and test the model.


<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../302_3_macromodels_islm_2">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../303_4_macromodels_islm_3">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../302_3_macromodels_islm_2">MM—II, Intro</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../303_4_macromodels_islm_3">MM—IV, ISLM part-3</a></td>
</tr>
</table>


