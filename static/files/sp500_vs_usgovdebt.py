#!/usr/bin/env python3
'''
SP500--Debt Indicator Series
==========================

One-off script to plot current history of the US SP500 against US government debt.

REQUIRES: Your FRED API key stored as an envar, so accessible from 
os.environ['FRED_API_KEY'] 


|Copyright 2025, Bijou M Smith
|Licence: GPL.v3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
'''
import os
from fredapi import Fred
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests
import http.server
import socketserver
import webbrowser
import threading
import time
import socket
import subprocess
import sys

fred = Fred(api_key=os.environ['FRED_API_KEY'])
_CSVFILE = 'SP500_vs_usdebt.csv'

def kill_process_on_port(port):
    """Kill any process using the specified port"""
    try:
        # Find process using the port
        result = subprocess.run(['lsof', '-ti', f':{port}'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            pid = result.stdout.strip()
            subprocess.run(['kill', '-9', pid])
            print(f"Killed process {pid} on port {port}")
            time.sleep(1)
    except Exception as e:
        print(f"Could not kill process on port {port}: {e}")

def is_port_available(port):
    """Check if port is available"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return True
        except OSError:
            return False

def start_server(port=48888):
    """Start server with port checking"""
    if not is_port_available(port):
        print(f"Port {port} is in use. Attempting to free it...")
        kill_process_on_port(port)
    
    Handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Server running at http://localhost:{port}/")
        httpd.serve_forever()


def plot_results(fetch_new=False, open_browser=True):
    '''
    Fetches and plots S&P 500 history versus US government net debt.
    Data is fetched from Yahoo Finance for SPX ('^GSPC') and FRED for US debt ('GFDEBTN').
    Plots are displayed in the browser using Plotly, and users can save to PNG from there.
    Data is saved to a CSV file for faster subsequent access.

    Args:
        fetch_new (bool): If True, forces fetching new data from sources.
                          If False (default), tries to read from CSV first.
                          If CSV does not exist, it will automatically fetch new data.
    Returns:
        pd.DataFrame: The DataFrame containing the combined SPX and US Debt data.
    '''
    global _CSVFILE
    df = pd.DataFrame() # Initialize an empty DataFrame

    if fetch_new or not os.path.exists(_CSVFILE):
        print(f"Fetching new data (fetch_new={fetch_new}, CSV exists={os.path.exists(_CSVFILE)})...")
        # Fetch US Debt from FRED (monthly data for better alignment with SPX daily)
        usdebt_data = fred.get_series('GFDEBTN') 
        # Convert series to dataframe
        usdebt_df = pd.DataFrame(usdebt_data, columns=['US_Debt'])

        sp500_data = yf.download('^GSPC', start='1970-01-01', end='2025-01-05',  progress=False)
        sp500_df = sp500_data['Close']
        sp500_monthly = sp500_df.resample('MS').mean()
        quarterly_months = [1, 4, 7, 10]
        sp500_quarterly = sp500_monthly[sp500_monthly.index.month.isin(quarterly_months)]
        df = pd.concat([sp500_quarterly, usdebt_df], axis=1)
        df.columns = ['SP500', 'US_Debt']
        df = df.dropna()


        # Convert US_Debt to a numerical type if it's not already
        df['US_Debt'] = pd.to_numeric(df['US_Debt'], errors='coerce')
        df = df.dropna(subset=['US_Debt'])

        # Save to CSV
        df.to_csv(_CSVFILE, index=True, date_format='%Y-%m-%d')
        print(f"New data fetched and saved to {_CSVFILE}")
    else:
        print(f"Reading data from existing CSV file: {_CSVFILE}...")
        # Read from CSV
        df = pd.read_csv(_CSVFILE, index_col=0, parse_dates=True)
        # Ensure column types are correct after reading from CSV
        df['SP500'] = pd.to_numeric(df['SP500'], errors='coerce')
        df['US_Debt'] = pd.to_numeric(df['US_Debt'], errors='coerce')
        df = df.dropna()
        print("Data loaded from CSV.")


    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=df.index, y=df['SP500'], name="SP500", line=dict(color='orange')),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=df.index, y=df['US_Debt'], name="US Government Net Debt", line=dict(color='lightblue')),
        secondary_y=True,
    )

    # Add figure title and axis titles
    fig.update_layout(
        title_text="<b>SP500 vs. US Government Net Debt</b>",
        template="plotly_dark",
        hovermode="x unified",
        legend=dict(x=0.01, y=0.99, bordercolor="Black", borderwidth=0),
        title_x=0.5, # Center the title
        paper_bgcolor='black',
        plot_bgcolor='black', 
    )

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>SP500</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>US Government Debt (M$)</b>", secondary_y=True)

    # Show the plot
    # fig.show()

    fig.write_html("SP500_vs_usdebt.html")
    # Modify the HTML file
    with open("SP500_vs_usdebt.html", "r") as f:
        html_content = f.read()
    # Add CSS to make background black
    css_insert = """
    <style>
    body, html {
        background-color: black !important;
        margin: 0;
        padding: 0;
    }
    </style>
    </head>
    """

    # Replace the closing head tag
    html_content = html_content.replace("</head>", css_insert)

    # Write back the modified HTML
    with open("SP500_vs_usdebt.html", "w") as f:
        f.write(html_content)

    if open_browser:
        # Check if the port is available before starting the server
        if not is_port_available(48888):
            print("Port 48888 is in use. Attempting to free it...")
            kill_process_on_port(48888)
        else:
            print("Port 48888 is available, starting server...")
        # Start server
        server_thread = threading.Thread(target=start_server, args=(48888,))
        server_thread.daemon = True
        server_thread.start()

        time.sleep(1)
        webbrowser.open("http://localhost:48888/SP500_vs_usdebt.html")

        print("Server running on port 48888.\nhttp://localhost:48888/SP500_vs_usdebt.html\nPress Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nServer stopped.")
        
    print(f"Plot saved as SP500_vs_usdebt.html")
    return df




def granger_analysis(df):

   # --- Step 1: Check for Stationarity and Difference the Data ---
   # A common check for stationarity is the Augmented Dickey-Fuller (ADF) test.
   # For simplicity and given typical economic series, we'll directly apply differencing.
   # Differencing once (d=1) is often a good starting point for financial/economic data.
   df_diff = df.diff().dropna()

   print("Shape of differenced data:", df_diff.shape)
   print("First 5 rows of differenced data:\n", df_diff.head())

   # --- Step 2: Determine Max Lags for Granger Causality Test ---
   # A reasonable range for monthly data could be 1 to 12 or 24 lags.
   # We'll test up to a maximum of 6 lags for demonstration.
   max_lags = 6

   # --- Step 3: Perform Granger Causality Tests ---

   print("\n--- Testing if US_Debt Granger-causes SP500 ---")
   # Null Hypothesis: US_Debt does NOT Granger-cause SP500
   # The function expects the dependent variable first, then the potential causal variable.
   # So, for US_Debt -> SP500, we pass ['SP500', 'US_Debt']
   granger_results_debt_to_SP500 = grangercausalitytests(df_diff[['SP500', 'US_Debt']], maxlag=max_lags, verbose=False)

   # Interpret results for US_Debt -> SP500
   print("\nResults for US_Debt Granger-causing SP500:")
   for i in range(1, max_lags + 1):
      test_result = granger_results_debt_to_SP500[i][0]
      p_value_f = test_result['ssr_ftest'][1]
      p_value_chi2 = test_result['lrtest'][1]
      print(f"Lag {i}:")
      print(f"  F-test p-value: {p_value_f:.4f}")
      print(f"  Chi-squared p-value: {p_value_chi2:.4f}")
      if p_value_f < 0.05:
         print(f"  --> Reject null hypothesis at 5% significance: US_Debt *does* Granger-cause SP500 at lag {i}")
      else:
         print(f"  --> Fail to reject null hypothesis: US_Debt does NOT Granger-cause SP500 at lag {i}")

   print("\n--- Testing if SP500 Granger-causes US_Debt ---")
   # Null Hypothesis: SP500 does NOT Granger-cause US_Debt
   # For SP500 -> US_Debt, we pass ['US_Debt', 'SP500']
   granger_results_SP500_to_debt = grangercausalitytests(df_diff[['US_Debt', 'SP500']], maxlag=max_lags, verbose=False)

   # Interpret results for SP500 -> US_Debt
   print("\nResults for SP500 Granger-causing US_Debt:")
   for i in range(1, max_lags + 1):
      test_result = granger_results_SP500_to_debt[i][0]
      p_value_f = test_result['ssr_ftest'][1]
      p_value_chi2 = test_result['lrtest'][1]
      print(f"Lag {i}:")
      print(f"  F-test p-value: {p_value_f:.4f}")
      print(f"  Chi-squared p-value: {p_value_chi2:.4f}")
      if p_value_f < 0.05:
         print(f"  --> Reject null hypothesis at 5% significance: SP500 *does* Granger-cause US_Debt at lag {i}")
      else:
         print(f"  --> Fail to reject null hypothesis: SP500 does NOT Granger-cause US_Debt at lag {i}")

   print("\n--- Important Considerations ---")
   print("1. Granger causality indicates predictive power, not true cause-and-effect.")
   print("2. The choice of 'max_lags' significantly impacts results.")
   print("3. Stationarity of the series is a critical assumption. Differencing is a common way to achieve it.")
   print("4. Economic theories and other statistical tests should complement these findings.")


if __name__ == '__main__':
   import sys
   if 'FRED_API_KEY' not in os.environ:
      print("Please set the FRED_API_KEY environment variable.")
      sys.exit(1)
   #df = plot_results()
   df = plot_results(open_browser=False)  # Focus on Granger
   granger_analysis(df)
