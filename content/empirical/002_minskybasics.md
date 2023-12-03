---
title: "Minsky Model Batch Jobs"
weight: 3
description: ""
date: 2022-12-01
lastmod: 2023-12-01
cover: ""
coverAlt: ""
toc: true
katex: true
tags: []
---

```
TODO: incomplete.
Could not actually get minsky running on the cmdl.
REST API was not working.
```

We are working on artificial neural net models for S&P500 time series 
forecasting, but before all that research is released I wanted to give the 
community some tips and tricks for using the system dynamics software Minksy™, 
which is Steve Keen and hpcoder's project, you can get open source releases on 
sourceforge here.

Sine this is the first post on Minksy-SD, I will begin with a minimal set-up 
introduction. But will not explain the model.  To build a model you currently 
have to open the GUI, which is a bit gross. But if you are familiar with other 
system dynamics tools like Simulink or VisSim you should have no problem.

A huge advantage of Minksy is it is open source, so you will soon hopefully 
find a growing community of users and support. VisSim and Simulink obviously 
have an enormous head-start, but in macroeconomics I think Minksy is poised to 
take a lead. If not, it is still the best tool for macroeconomics simulations 
in my humble opinion.

The aim of this article is to learn to use the bash command-line interface to 
create and simulate a simple endogenous money model with banks but no 
government sector.

## Setting Up Minsky™


Install Minsky: First, you need to install Minsky on your system. The 
installation process varies depending on your operating system. For instance, 
on Debian/Xubuntu based distros, you can use the following commands to install 
Minsky (for xubuntu-22.04):

```bash
$ echo 'deb http://download.opensuse.org/repositories/home:/hpcoder1/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/home:hpcoder1.list
$ curl -fsSL https://download.opensuse.org/repositories/home:hpcoder1/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_hpcoder1.gpg > /dev/null
$ sudo apt update
$ sudo apt install minsky-beta
```

If you are using a different or older release, please be advised to grab the install 
sequence commands from 
[sourceforge here](https://software.opensuse.org/download.html?project=home%3Ahpcoder1&package=minsky-beta) 
(don't just copy & paste the above).


### Basic Endogenous Money Model

I've found the minimally useful macroeconomics models for testing your set-up, 
are the banking models using Godley tables. You can find canned models on 
Steve Keen's website. These are a good way to learn how to use Minsky without 
tedious learning from basics. Why would you not learn the basics? Perhaps you 
already know some MMT and just want to get on with modelling, and perhaps you 
find it all intuitive and just need a model to start hacking.

I've always thought the basic Minsky models are just for teaching the tools, 
not for macroeconomics.

For decent macroeconomics you need a proper MMT model, so at least a government 
sector and a non-government sector, and Steve Keen always recommends sticking 
in the banking sector too, separate to both government and non-government. 
Why? Because then you get to tweak the credit creation dynamics.

Of course, a Mosler model (just two-sectors) can be just as good, but will 
aggregate households, firms, foreign sectors, and will aggregate the banking 
sector into the government sector. Which is sort-of fine.

What you do **_not_** want to do with a Mosler model is put the banks into the 
non-government sector, that would be incredibly stupid. Because what you want 
to see is the effect of monetary and fiscal policy on firms and households. 
Banks are agents of the state, so they have to go into the government.

This is true, even if you think banks in the real world be private sector 
entities. they are not. Not for purposes of MMT analysis. They are run by 
private individuals and have shareholders, but they act as agents of the 
state, issuing tax credits in the form of promises to repay (bank credit, or 
what people refer to as a "bank loan").  These, for all intents and purposes, 
are just one other way the government issues it's tax credits, with private 
individuals running the banks on behalf of the government, loosely regulated.

### Model building outline

I will not show you screenshots of the GUI, this is better done in video 
format, which I might get around to posting on youtube later. But if you are 
in a rush then go see 
[Ty Keyne\'s tutorials](https://www.youtube.com/watch?v=xzy5iYsf0fA&list=PLUewi-IqLtRRqcVni88dqg73O_9zOGLiX) 
on how to use Minksy™ [here](https://www.youtube.com/watch?v=xzy5iYsf0fA&list=PLUewi-IqLtRRqcVni88dqg73O_9zOGLiX).

Once you are done, save the model as a `.mky` file in a convenient location. 
For this example, let's assume the file is called `endogenous.mky`.

For this tutorial I will use the example from hpcoder's github here: 
[Examples](https://github.com/highperformancecoder/minsky/tree/master/examples).
I grabbed the 
[EndogenousMoney.mky](https://github.com/highperformancecoder/minsky/blob/master/examples/EndogenousMoney.mky) 
model, saved it to my practice folder.



## The REST API

Minsky now comes with a REST (representational state transfer) API, so you can 
control a minsky simulation without the GUI.

First start the Minsky REST server  by running the following command in 
the terminal:
```bash
minsky --rest-server
```
Open a browser and navigate to the Minsky REST server endpoint. By default, 
the REST server endpoint is http://localhost:8080. You should see a welcome 
message if the server is running.

Create a new simulation or load an existing one in Minsky. To create a new 
simulation, click on "File" -> "New" and choose the appropriate model type. To 
load an existing simulation, click on "File" -> "Open" and select the 
simulation file.

Define the simulation parameters using the REST API. You can use the REST API 
to set the simulation parameters, such as the time horizon and the initial 
values of variables. The REST API documentation can be found at 
`http://localhost:8080/docs`.

Run the simulation using the REST API. You can use the REST API to run the 
simulation and retrieve the results. The REST API documentation provides 
details on how to run simulations and retrieve results.

Analyze the simulation results. Once the simulation is complete, you can 
analyze the results using various tools, such as Python, Excel, or R.

To control the simulation from the command line, you can use tools such as 
curl or http to send requests to the Minsky REST server. For example, to 
set the simulation time horizon to 100 and the initial value of a variable 
to 10, you can use the following command:

```bash
curl -X POST http://localhost:8080/simulation/parameters -d '{"duration": 100, "variables": {"variable_name": 10}}'

```

To control the simulation from a browser, you can use the REST API 
documentation at `http://localhost:8080/docs` to send requests and retrieve results.








#### Simulate the model

You can now use the Minsky command-line interface to simulate the model and 
generate time-series data for the relevant variables. Open a terminal window 
and navigate to the directory where you saved the `.mky` file. Then, run the 
following command:
```bash
$ minsky run endogenous.mky
```
This will start the simulation and generate a `.csv` file with the time-series 
data for the relevant variables. By default, the output file is called 
`output.csv` and is saved in the same directory as the `.mky` file.

If you want to specify the name and location of the output file, you can use the 
`-o` option, as follows:
```bash
$ minsky run -o foo_output.csv endogenous.mky
```
This will generate the output file `foo_output.csv` in the current directory.

Note that there are many other options and parameters that you can use with 
the minsky command-line interface. For more information, see the Minsky 
documentation.


## Batch processing

Once you've checked the base model runs ok, you can now feed it changes 
of parameters and run in a batch, as you'd do for any bash scripting.

### Summary

Hopefully this can get you started with using Minsky. I know I've left this article sort on specifics, but if you wish to 
[donate](https://ko-fi.com/achrononmaster/) and ask for help, please do, I 
will not promise you anything except some words, but you can be the judge 
of whether I might have anything useful to tell you.


<table style="border-collapse: collapse; border=0;">
    <colgroup>
       <col span="1" style="width: 25%;">
       <col span="1" style="width: 10%;">
       <col span="1" style="width: 25%;">
    </colgroup>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../001_ohangapai_projects">Previous chapter</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">Back to</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../099_1_macro_trader">Next chapter</a></td>
</tr>
<tr style="border: 1px solid color:#0f0f0f;">
<td style="border: 1px solid color:#0f0f0f;">
<a href="../001_ohangapai_projects">OHP Projects</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:center;">
<a href="./">TOC</a></td>
<td style="border: 1px solid color:#0f0f0f; text-align:right;">
<a href="../099_1_macro_trader">Macrotrader I</a></td>
</tr>
</table>

