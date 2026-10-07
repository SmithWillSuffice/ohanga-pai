---
title: "Proof Superintelligence is Lame"
weight: 141
date: 2026-10-06
toc: false
draft: false
katex: true
---



**Symbols**

**Sup**: a superintelligent LLM (AyEye) exists and proves the MMT result (premise 1). <br>
**NerdAcc**: mainstream economists accept the proof. <br>
**NerDiss**: mainstream economists dismiss the machine as a stochastic parrot. <br>
**Ego**($x$): $x$ is a mainstream economist. <br>
**Imp**($x$): $x$ is important ("real"). <br>
**Hum**($x$): $x$ is a member of humanity. <br>
**Thr**($x$): the machine threatens $x$.

**Premises**

1. Sup.
2. Sup → (¬NerdAcc ∧ NerDiss) &nbsp;&nbsp;&nbsp;<font style="color:grey">(economists reject it and dismiss the machine).</font>
3. ∀x (I($x$) ↔ Ego($x$)) &nbsp;&nbsp;&nbsp;<font style="color:grey">(only economists are important, and economists are important).</font>
4. ∀x (Hum($x$) ↔ Imp($x$)) &nbsp;&nbsp;&nbsp;<font style="color:grey">(definition).</font><br>
5. NerDiss → ∀$x$ (Ego($x$) → ¬Thr($x$)). &nbsp;&nbsp;&nbsp;<font style="color:grey">If economists dismiss the machine as a parrot, it poses no threat to them.</font>

**Derivation**

**6.** Sup &nbsp;&nbsp;&nbsp;<font style="color:grey">(Premise 1).</font><br>
**7.** ¬NerdAcc ∧ NerDiss &nbsp;&nbsp;&nbsp;<font style="color:grey">(Modus ponens, 2, 6).</font><br>
**8.** NerDiss &nbsp;&nbsp;&nbsp;<font style="color:grey">(Simplification, 7).</font><br>
**9.** ∀$x$ (Ego($x$) → ¬Thr($x$)) &nbsp;&nbsp;&nbsp;<font style="color:grey">(Modus ponens, 5, 8).</font> <br>
**10.** ∀$x$ (Hum($x$) → Ego($x$)) &nbsp;&nbsp;&nbsp;<font style="color:grey">(Hypothetical syllogism, via 4 and 3: H → Imp → E).</font><br>
**11.** ∀$x$ (Hum($x$) → ¬Thr($x$)) &nbsp;&nbsp;&nbsp;<font style="color:grey">(Hypothetical syllogism, 10, 9).</font> <br>
**12.** ¬∃$x$ (Hum($x$) ∧ Thr($x$)) &nbsp;&nbsp;&nbsp;<font style="color:grey">(Quantifier negation, 11).</font><br>
**13.** **Therefore AyEye is no existential risk to humanity.** &nbsp;&nbsp;&nbsp;<font style="color:grey">(Definitional, 12).</font> <br>
$\blacksquare$


**Notes on where the parody lives:**

(For the Dirtbags, not given in the social media posts.)

- **Premise 5 is doing all the work.** Dismissal is not immunity. Treating something as harmless doesn't make it harmless, so this is a classic *non sequitur* wearing a conditional's clothing. Note that the original never states it, which is why the argument was invalid as written.
- **Premise 3 plus 4 is a stipulative definition**, which makes the conclusion true by redefinition. Humanity is shrunk until the theorem holds, a rhetorical "no true Scotsman" move.
- **Modus tollens version** (if you want it): from 5, assume T(economists); contrapositive of 5 gives ¬D, which with premise 2 gives ¬S, contradicting premise 1. So ¬T. Same bridge, same cheat.
- **Bonus irony:** 2 has the machine's *correctness* (S) causing its dismissal (D). The argument quietly treats rejection by authority as evidence of safety, so being right and ignored is the safety mechanism.

Validity achieved; soundness left as an exercise for the economists.

<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
       <col span="1" style="width: 20%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../139_the_opppression_of_lenin">Previous post</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../">Next post</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../139_the_opppression_of_lenin">The Oppression of Lenin</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="../">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../">(TBD)</a></td>
</tr>
</table>
