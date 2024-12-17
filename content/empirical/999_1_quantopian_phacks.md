---
title: Quantopian Series Notes
weight: 14
date: 2023-01-15
toc_depth: 1
katex: true
toc: true
---

A few highlights from the 
[Quantopian Series](https://gist.github.com/ih2502mk/50d8f7feb614c8676383431b056f4291) 
worth remembering for teaching. these will start off unordered, but after I 
write a half dozen or so I will try to impose some loose pedagogical order. 
(That just means the links will change, ok. So if referencing use the TOC and 
search box instead.)


## p-value Hacking

Ref: [Quantopian Lecture Series: p-Hacking and Multiple Comparisons Bias](https://www.youtube.com/watch?v=YiDfbYtgUPc).

### Terminology

* **False positive** --- a test indicates presence of an effect when in 
reality an oracle would say there is no effect.
* **False negative** --- a test indicates absence of an effect when in 
reality an oracle would say there is an effect.
* Think of the Null Hypothesis as the "negative" hypothesis ("there is no 
effect" or "there is no discernable distinction").
* **Multiple comparison bias** --- the more inferences that are made 
(e.g., estimated parameters) without sample consideration corrections, 
the more likely are errors in other inferences based upon the former. 

## Using p-values in hypothesis testing

In statistics you want to minimize both FP and FN, but if there is a tension 
in use of your resources you will probably want to minimize risk of getting 
false positives more than the risk of getting false negatives. (But this can 
depend upon context.) For example, in medical drug trials (a dodgy area of 
application) the default has to be "not release the drug" so you certainly 
want the bias to be for false negatives rather than false positives. A false 
positive is a bias towards releasing a drug (with possible side-effects) that 
is in fact a useless drug, maybe harmful in other ways.

A false negative is a bias towards not releasing a drug that would have had 
benefits. You never know the oracle of course, but you at least should know 
the odds.

$p$-values in hypothesis testing assume a lot! One is a distribution of the 
score of "fitness" (which could be a $t$-test, an $F$ score, a $\chi^2$ score, 
et cetera) the $p$-value is a probability --- _**but** you do **not** want to 
**use** it as a probability_!!!!

* Decide on what the qualitative and quantitative value of the test outcome is 
for you. For high risk choose a very "low significance" (say 1% or less).
* A significance level of 1% is a *high chance* 99% (assuming a bunch of 
stuff) of getting a true negative (NullHyp is oracle true & the test indicates 
it is true) or a false negative (NullHyp is oracle false & the test indicates 
it is true)...
* ... and a low chance (1%) of getting a false positive (NullHyp is oracle 
true & the test indicates it is false).

These interpretations of $p$-values are terrible dicey though:

* These are not absolute probabilities, they're conditional --- they are 
probabilities only *given* the assumptions of the model are correct (and 
Gaussian errors, whatever else the test statistic assumes, etc.)
* If you are in social sciences you might tolerate more false negatives 
(NullHyp is true & the test indicates it is false) but only as the cost for 
the pay-off of decreasing your rate of false positives.
* For a lot of problems the more hazardous (in real life terms) outcome is a 
false positive (NullHyp is true & test indicates it is false) --- this is 
because a true NullHyp is "There is no effect", so a false positive is going 
to bias you towards thinking there is an effect when according to a putative 
oracle there is none.

A better way perhaps to remember what the $p$-value is, is that it is simply 
the probability of getting a worse test statistic than what you observed, 
where "worse" is worse than what the NullHyp being true would imply.

The way you then _**use**_ the $p$-value is as a criterion for rejecting or 
accepting the NullHyp, you will not use the $p$-value *as* a probability, even 
though it is a conditional probability. You instead pre-choose a significance 
level *appropriate for your data + model context*. Then use the $p$-value as a 
cut-off. 

Emphasis is on *your* choice! Emphasis on that it is Bayesian 
(**given** the NullHyp is true).

### Best Practise 

**Best practice** is thus to figure out what a *sensible* significance level 
is *first*. Then in your code do *not* print out the $p$-value, instead print out 
*only*, either

**(1)** "no significant relationship indicated."   
&nbsp;&nbsp;&nbsp;&nbsp;or   
**(2)** "a significant relationship is indicated."   
&nbsp;&nbsp;&nbsp;&nbsp;or   
**(3)** "the test is inconclusive."   

(because language framing matters for non-meathead beings.) 

Also print the significance level you chose as a reminder, it gives the 
meaning to the word "significance". This takes eyes off the $p$-value, which 
is what you want for people reading your research. It is fine to look at the 
$p$-value to worry about things like sample size biases, desire to repeat a 
trial, and whatnot (the meta-statistics stuff).

But how would you "know" the test is inconclusive? Because a significance level 
cut-off (5% or whatever) is a binary distinction, so you'd only have the first 
two output statements coded.

**Better practice?** I would not choose one single cut-off, but a worst case 
and best case, so a range of significance levels. Ex. for extreme risk 
analysis maybe you want worst case acceptance of a false positive to be 0.01% 
(which is getting more like the 6-sigma level for particle physics research); 
and best case to be even more stringent, like 0.001%. 

*Alright!* Now in your code you can print out the third statement above, 
whenever the measured statistic yields a $p$-value in between your best and 
worst case significances.

If you are in social sciences those significance levels would be a bit absurd, 
you'd get too many false negatives (accepting NullHyp when the oracle would 
say it is false). But like we said, depending upon context that can often be 
better than more chance of false positives (rejecting NullHyp when the oracle 
would say it is true).

Always remember, a $p$-value test is highly dependent upon your choice of 
significance level.  It is a cut-off encoding your knowledge of a situation or 
context, it is not a machine telling you what the real world is like.

Before summarizing, one other point: **Multiple comparison bias** is not a 
thing in statistics, it is a mistake of mere mortals. You would never have 
such bias if you understood the statistics, you would always be making the 
appropriate corrections, which is the study of uncertainty and error 
propagation.

On very basic correction is the 
[Bon-Ferroni Correction](https://en.wikipedia.org/wiki/Bonferroni_correction) 
which the Quantopian [explains here](https://youtu.be/YiDfbYtgUPc?t=1694) 
but we can state it in one sentence: 

> Bon-Ferroni correction: if you use $m$ tests, in each use a significance 
level of $\alpha/m$ where $\alpha$ is your overall desired significance. You 
then should expect a fraction $\alpha$ of the tests pass, and $(1-\alpha)$ 
fail.

In this way the false positive rate when taking *all* the $m$ tests 
together is back to $\alpha$. If that's not the case within reasonable 
uncertainties then your model (or data) needs updating).

The Quantopian [lecture on p-hacking and multiple comparisons bias](https://www.youtube.com/watch?v=YiDfbYtgUPc0) 
is a good overview of this topic, with a few tips for people who are at risk of 
over-using neural networks and whatnot. A lecture is only as good though as the 
student is willing to take heed. In a dog-eat-dog world and rat-race people 
are prone to taking short-cuts and skipping the grind of testing. So just do 
not say you were never warned.

*Do the **out-of-sample testing** my dudes.* If you have the need to make it fun, 
use it to prank your colleagues. (Fudge their data, yo! Just don't forget to tell 
them afterwards.)

### In summary

Figure out what a *sensible* significance level range is *first* using your 
domain expert knowledge. Then in your code do not print out the $p$-value, 
instead print out only, either

**(1)** "no significant relationship indicated."  
&nbsp;&nbsp;&nbsp;&nbsp;or   
**(2)** "a significant relationship is indicated."   
&nbsp;&nbsp;&nbsp;&nbsp;or   
**(3)** "the test is inconclusive."

**Further TODO:** a $p$-value hypothesis test can be useful when you are in 
*Moderatistan* (Gaussians) but could be highly misleading if your underlying data 
source is fat-tailed. If you are dealing with fat-tails (first test for them 
using maximum values) and consider using a different type of hypothesis test, 
e.g., one that scores maximum values, not the medians or means.


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
<a href="./">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../099_2_funds_flows">Funds Flow</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="./">(TBD)</a></td>
</tr>
</table>


