# barrier-option-pricer
Path-dependent barrier option pricing application, scaled down to work on Heroku free tier.
Try it out [here](https://barrier-option-pricer.herokuapp.com/)

## What is a barrier option?
Barrier options are derivatives of an asset where payment depends on the price of the asset breaching a certain barrier price.

## What type of barrier option is this tool useful for?
This particular tool focuses on pricing an exotic barrier option where we cannot feasibly utilise analytical methods such as partial differential equations as the price conditions are too complicated.

* The exotic barrier option is path-dependent such that payoff depends on the number of days where the price of the option exceeds the barrier. There are two such barriers, `First Barrier Level` and `Second Barrier Level`, with day counts `Counter1` and `Counter2` respectively.
* Payoff resembles a Call Option, however it is more complex. Let (S<sub>t</sub>) be the share price at time t and K be the strike price. 
* The cut-off points 100 and 150 days used for payoff can both be configured in the app with `Counter 1 Level` and `Counter 2 Level` (it was not necessary for these to be variables in the project description)

Payoff is as follows:
![alt text](assets/payoff_desc.png)

## Setup:
Install the required packages in `requirement.txt`

Creating a new virtual environement is recommended.

```
conda create -n object_detection python=3.7
conda activate object_detection
```

Git clone the repo and change directory into it. Then pip install the packages in `requirement.txt`.
```
cd directory/you/want/to/clone/into
git clone https://github.com/cloud-annotations/object-detection-python.git
cd object-detection-python
pip install -r requirement.txt
```
Now test the application:
```
python app.py
```
Open a web browser and enter: `0.0.0.0:8050/`

## Pricing Methods



![alt text](assets/full_bench.png)

![alt text](assets/part_bench.png)
