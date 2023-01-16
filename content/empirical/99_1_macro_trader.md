---
title: "Macro Trading 1 - Intro"
description: ""
date: 2022-10-01
lastmod: 2019-10-01
cover: ""
coverAlt: ""
toc: true
katex: true
tags: []
---

Macro trading is something I've only recently looked into, not as a trader, 
but as an academic seeking more real world experience. 
Macro trading models can benefit from MMT, but do not really use a bare 
Keen--Minksy model because of the need to model markets, which are sub-macro.
So I place macro trading models in a category of mesoscopic MMT analysis.

## The MMT Macro Trader Paradigm

Douglas over at [Doug - MMT Macro Trader](https://www.youtube.com/@MMTMacroTrader) 
does a terrific job of using Bayesian models and MMT fiscal flow analysis to get very, 
*very* good 30 day predictions for the S&P forward market. 

There are other MMT traders, like the hedge fund managers at Mosler's old company, 
but they do not discuss their work on social media, so I will instead be focusing 
on Doug's work. 
One of the experts, [Shanjiv Sharma,](https://www.linkedin.com/in/sanjiv-sharma-93443b36/) 
at Mosler's old firm AVN/III, and now at 
[Naila Inc.,](https://www.linkedin.com/in/sanjiv-sharma-93443b36/) 
gives a talk on his modelling in the UMKC Conference here 
[MMT and Real World Financial Market Practitioners](https://www.youtube.com/watch?v=N8FhDsuJnvk) 
but it's insufficient to figure out how exactly he uses MMT, 
he just says he does, and points to some principles and some chart results.
(By the way, Shanjiv was at Lehman Brothers prior to 1995, and saw the rot there! Just sayin').

The purpose (for us at Ōhanga Pai) is not to "make money," since we do not believe 
ethical playing of the [Negative Sum game](https://medium.com/@shashikantsharma_39650/the-negative-sum-game-of-trading-3f34e527d555) of options trading is possible (net it's a losing game, 
so only a few winners prosper). 
Note that stock and options trading is prime facie a Zero Sum Game, 
but the brokerage and transactions and tax fees  make it irreducibly a 
Negative Sum game (there can be winners, but there'll be more losers in raw dollar terms).


But I respect Douglas. He knows the score, and any market gains he makes are at 
the knowing risk of the losers. The losers are willing market participants, 
who aught to ethically know the score as well before playing the stock market. 
You should (morally) know you are taking a gamble before trading purely financial 
assets. And even if a company is in the business of real goods production 
(like a timber or construction firm) their stocks are just 'pieces of paper' 
or spreadsheet entries, which are worthless unless you can find someone willing 
to take them off you for dollars or pizza.

Always remember the stock holder is at the bottom of the debt pyramid. 
That means when a company is liquidated the stock holder is the last to be redeemed. 
Creditors are by law at the top of the pyramid. So if you really want secure low risk, 
get your money *first* then loan it to a firm that you trust and believe in. 
Don't buy their stock!

The problem for small investors is they cannot lend to a firm in general, 
the firm gets their money through stock sales. 
As long as you know these risks, then the gambling is all on you to shoulder.

The thing about financial markets is that they are profiting off other people 
in the market, and this has **_no impact whatsoever_** upon a government's 
fiscal capacity to fully employ all labour. So the social impact of financial 
trading is not inherently parasitic, what's parasitic is the rentier sector 
profiting off workers. 

Basic S&P trading is not that, at worst it profits from pension fund managers 
who are stupid and are gambling away future retiree pensions. 
That's what is rentier, and I am fundamentally philosophically ethically 
opposed to that sector existing.
See the post on [Pensions and Superannuation Funds.](/ohanga-pai/questions/12_pension_funds)


## Learning the fintec Jargon

As a physicist who's main project is topological 4-geon theory, 
my main obstacle to getting S&P trading going for proof-in-principle MMT is a 
good framework for analysis was just learning the jargon. 
SO that's what this article will be about. 
It might grow to an unseemly length over time, 
so if you are visiting Ōhanga Pai a few years after first visiting be aware 
there will be fresher updates and corrected errors.

For most of the rest of this page it'll be pretty boring to you who want to get 
on with learning the modelling. 
To mathc your boredom I''ve mostly cut & pasted from a few websites.

### What is a Fixed-Income Security?

A fixed-income security, or debt security,is a claim on a particular periodic 
income stream from interest paid on borrowed funds. 
Fixed-income securities are named so because they guarantee a stream of income 
that is determined by a fixed formula.

There are several different types of financial instruments that make up the 
fixed-income market, but the most commonly traded are government or corporate bonds.

This is what AVN/III were trading.

### What is relative value trading?

I can read this and not really know what it means, because "what is risk?" 
But anyway...
 
Relative value can be defined as expected price convergence of contracts or 
portfolios with similar risk profiles. 
For fixed income this means similar exposure to duration, convexity and credit risk. 
The causes of relative value are limited arbitrage capital and aversion to the 
risk of persistent divergence. 
 
Relative value in the fixed income space has been pervasive and persistent. 
Relative value trades can be based on parametric estimation of yield curves 
or comparisons of individual contracts with portfolios that replicate their 
essential features. The latter appear to have been more profitable in the past.
 
### Hence: fixed income relative value trading...

... is a thing.

There seems to be a paradox or inconsistency here. How can fixed income 
securities trade at relative values?

Bonds emitted by the same issuer with the same cash flows should *theoretically* have the 
same prices and yields. This is the law of one price. 

In practice, however, deviations from the law of one price are pervasive in 
the bond market.  Already hitting the real world we've got violations of 
neoclassical economics, take note! But no violation of MMT yet, since nothing 
stock--flow inconsistent has yet been seen.

Deviations can be large --- as in 2008 --- or they can be small --- 
as in 2014 --- but they are rarely absent.  
For example, at the height of the global financial crisis, the difference in 
yields between very similar bonds issued by the US Treasury exceeded 100 basis points. 
Such a large difference can persist for extended periods of time, 
even in normal times.
This points to the existence of limits to arbitrage in fixed income markets.

((Arbitrage of course brings a system somewhat back to neoclassical assumptions, 
but never exactly, since arbitrage is never instantaneous. Arbitrage is like a 
driving or damping force on a pendulum, it can overshoot, then you get oscillations, 
no guaranteed market equilibrium.))

Read more [here.](https://research.macrosynergy.com/fixed-income-relative-value-basics/)

If you are a serious trader, it's important to diversify, and so it is good to understand not only bond markets (~fixed income) but also stock markets. 

For MMT traders, we have tools for macroeconomic analysis, and so the only trading I am, 
for now, prepared to look at from an MMT perspective is Index trading, 
which means trading using index funds, and that means gathering stock market index data, 
not detailed individual firm data. So in the USA this would be the 
S&P (Standard & Poors 500), and in New Zealand the NZX.

## What are Derivatives?

[Derivatives](https://www.investopedia.com/terms/d/derivative.asp) are 
basically fictional financial instruments. 
All that means is that people create them, but once created they are subject to legal 
conditions and can be traded. 

They are created usually by bundling a whole lot of primary assets, 
like different stocks, or bonds, currencies, corporate debt, mortgage debt 
payment obligations, or options. Even "interest rates" can be made into 
derivatives --- you can have people placing bets on interest rate movements. 
That's kind of f*ked up don't you think?

Your answer is, "Yes."

Personally, I think Derivatives are evil. They link too many otherwise independent 
financial assets, and instead of spreading risk thin, this create macro instability. 
The 2008 global financial crash was largely caused by both mortgage fraud and the 
mortgage backed debt securities. 

When a whole lot of poor people stopped being able to pay their mortgages, 
this caused a massive collapse on the CDO market. 
The real home values had been artificially "inflated" by unscrupulous 
real estate appraisers too, which did not help, since to smarter people the 
mortgage backed securities were thus obviously toxic.

It was all parasitic upon the real economy (real housing and whatnot), 
and governments could have thus bailed out the home owners who still had a 
share in something real and useful, but that was not the way it was handled, 
and the results were catastrophic for poor home owners who had got into 
unpayable mortgage debt.

If a nation is going to allow Derivatives to be traded, the economist 
Randall Wray has a good idea that would eliminate most of the systemic risk, 
which is that all obligations issued by a bank should be permanently held by that bank, 
and cannot be sold nor collateralized and then on-sold in amorphous bundles of 
"debt instruments." 

## What is the S&P?

The [S and P 500](https://www.investopedia.com/terms/s/sp500.asp) is an index of the top 500 performing companies listed on the US stock market. 
"Index" means there is a ranking to the firms. 
The ranking is a weighted index by market capitalization estimates. These are not exact. 
The company Standards & Poors (a credit rating agency) publishes the index, 
so investors rely upon their trustworthiness. 

The S&P 500 is the basis for investment for many investments, including futures contracts, 
mutual funds, and ETFs.

You cannot directly invest in "the S&P 500" because it's only an index, 
but you *can* invest in one of the many funds that use it as a benchmark, 
by tracking the composition and performance of the particular funds.

There are of course many other published indices you might also use as an alternative.
One of the more well-known is the [Dow Jones Industrial Average (DJIA)](https://www.investopedia.com/terms/d/djia.asp), 
but this is not often used by institutional investors, the DJIA is used by 
retail sector investors. 

For example, if you yourself run a retail firm, but you'd like to hedge or 
spread your risk by investing in other firms that are in some sense "orthogonal" 
to your firm in their exposure to financial risk.
(That just means, when economic or environmental conditions, like bad weather, 
negatively effect your firm, the other firm may profit or be unaffected.)

Another index is the [Nasdaq,](https://www.investopedia.com/terms/n/nasdaq.asp) which is a global electronic marketplace for 
trading securities associated mostly with the technology sector. 
It is an index of more than 3,700 stocks that includes technology giants like 
Apple Inc, Alphabet (Google), and Microsoft. 

## What are the SPX and SPY?

The are **_actual funds__** so you can invest in them.

The SPY is an exchange-traded fund (ETF) that tracks the performance of the S&P 500. 
An ETF is a marketable security that acts like an index fund but is tradable 
like a common stock on a stock exchange.

There are key differences between SPX and SPY options. 
These differences can go into an investors decisions about which option best 
fits their investing strategy.

* **SPX options are European-style options** and so can only be exercised on the expiration date. 
* **SPY options are American-style options** and so can be exercised anytime between the time of purchase and the expiration date.
* SPX options do not pay dividends whereas SPY options do. 
* SPY options dividends are paid quarterly, usually at the options expiration in 
March, June, September, and December.
* SPX options tend to be about 10 times the price of SPY options, so that can be an issue if you do not have a lot of cash to start with.

When looking to invest in the S&P 500, SPX and SPY options are similar assets 
with a high trading volume that investors can use to enter, and exit, 
a position in the S&P 500 index. The fact they are "high trading volume" 
means that if you have a mathematical (or astrological) strategy you can 
almost always find a deal you can trade, i.e., you can almost always buy or sell 
at currently offered prices.
(Think of this as like a grocery shop pretty much always having the goods you 
want on its shelves. If trading volume is low the shelf might be bare.)

A few more distinctions between SPX and SPY:
* SPX options are settled in cash since the underlying asset itself is not traded. SPY options are settled in shares since the underlying asset itself is traded on exchanges.
* All SPX options, except for those that expire on the 3rd Friday of the month, expire at the close of business on expiration Friday. SPX options that expire on the 3rd Friday stop trading the day before the 3rd Friday. All SPY options expire at the close of business on expiration Friday.
* An SPX option with the same strike price and expiration date as an SPY option is approximately 10 times the value of an SPY option. 

The SPX and SPY options are great tools to use when an investor wants to profit 
off an increase or decrease in the S&P 500 index. 
Choosing between the SPX and the SPY option is entirely up to the investor to 
decide which option fits their investing strategy best.


### New Zealand Equivalents

We have the [NZX or NZSX,](https://www.nzx.com/markets/nzdx) which is the 
"main board" for the NZ Stock Exchange. 
For securities we have the [NZXD.](https://www.nzx.com/markets/NZDX) 
For derivatives we have the [NZCX](https://www.nzx.com/markets/NZCX/overview)

We are heavily agriculture based too, so we have a board called [SGX-NZX  Dairy Derivatives.](https://www.nzx.com/markets/nzx-dairy-derivatives/dairy)
as well as the "[Fonterra Shareholder\'s Market (FSG or FSM)](https://www.nzx.com/markets/NZZX)"

Ad there is a **_whole bunch_** of other index funds you can [view here.](https://www.nzx.com/markets/indices)  New Zealand is a one of the most corruption-free countries in the world, 
so is a good "safe" place for investors even though the market volumes are 
low compared to Europe and the USA. 
("Safer"" in fintec does not mean great returns, it means the underlying 
*real* economy more substantially and accurately reflects the 
"fictional" *nominal* price data.)


[Next chapter (MT-2 Flow of Funds)](../99_2_funds_flows)  
[Previous chapter (Projects Overview)](../1_ohangapai_projects)   
[Back to Empirical Pages](../)
