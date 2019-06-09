#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:39:33 2019

@author: Matthew Dunlop

This file serves as a way of sending the user inputs to the desired pricing
method.
It can also be executed itself from the command line, so it can be used in
other projects
"""
import math as m
import numpy as np

import pricing_functions as pf # import all of the pricing functions

def Barrier_Option_Pricer(S = 60, K = 50, H1 = 65, H2 = 85, r = .05, T = 1,
                          sigma = .3, n = 260, nr = 4000,
                          plot = False, Var_red = 0, pr = 1,
                         ret = 0):
  '''
  #####################################################
  Helper Function for interpreting user preferences for
  Plotting and Variance Reduction.
  
  Intended for simplifying process of running the
  pricer for different numbers of simulations etc
  #####################################################
  INPUTS:
  S, K, H1, H2, r, T, sigma, n, nr have usual meanings
  
  plot   : Whether the function plots or not # not implemented as of 26-April
  Var_red: Which Variance Reduction Technique to use:
            = 0: Crude Monte Carlo Pricer used
            = 1: Antithetic Variates Technique used
  pr     : Decides whether t print the results or not. Default is 1, which
           prints the result. An other value and will not print.
  ret    : Decides whether to return the raw values as six objects
           By default, this is false. Set this to 1 to receive the results
           as raw objects.
           This is useful for benchmarking.
            
  
  '''
  # for exponent (risk-neutral)
  nu = r - .5 * sigma ** 2 # the drift of the stock price
  dt = T / n # time step size, by default this is one day.
  
  # now to select the method of computing the outputs.
  
  if Var_red == 0:
      # this is the crude monte carlo, which is slow.
      S_val, payoff, counter1, counter2 = pf.Crude_Monte_Carlo(S = S, K = K, H1 = H1, H2 = H2, r = r, T = T,
                          sigma = sigma, n = n, nr = nr,
                     nu = nu, dt=dt)
      
  elif Var_red == 1:
      # crude monte carlo with anithetic variate technique (AVT)
      S_val, payoff, counter1, counter2 = pf.AVT_Monte_Carlo(S = S, K = K, H1 = H1, H2 = H2, r = r, T = T,
                          sigma = sigma, n = n, nr = nr,
                     nu = nu, dt=dt)
  elif Var_red == 2:
      # Numpy optimized (NPO) crude monte carlo.
      # Numpy is much quicker but not as fast as PyTorch
      S_val, payoff, counter1, counter2 = pf.Crude_Monte_Carlo_NPO(S = S, K = K, H1 = H1, H2 = H2, r = r, T = T,
                          sigma = sigma, n = n, nr = nr,
                     nu = nu, dt=dt)
  elif Var_red == 3:
      # NPO with AVT
      S_val, payoff, counter1, counter2 = pf.AVT_Monte_Carlo_NPO(S = S, K = K, H1 = H1, H2 = H2, r = r, T = T,
                          sigma = sigma, n = n, nr = nr,
                     nu = nu, dt=dt)

  '''
  Each method returns:
      S_val    : Share value matrix
      payoff   : Option payoff matrix
      counter1 : Matrix of sum of days above barrier 1 for each path simulated
      counter2 : Matrix of sum of days above barrier 2 for each path simulated
  
  '''
  # now to discount to present value
  # uses the risk free rate
  PDisc = m.exp(-r*T)* payoff

  # mean & std for price
  price = PDisc.mean()
  p_std = np.std(PDisc)

  # mean & std for counters
  ave1 = counter1.mean()
  std1 = np.std(counter1)

  ave2 = counter2.mean()
  std2 = np.std(counter2)
  
  # to save GPU RAM
  del S_val, counter1, counter2
  
  if pr == 1:
    # print the output
    print("Counter1: \t Ave = {} \t Std Dev = {}".format(round(ave1,10),round(std1,10)))
    print("Counter2: \t Ave = {} \t Std Dev = {}\n".format(round(ave2,10),round(std2,10)))
    print("Price: \t Ave = ${} \t Std Dev = ${}".format(round(price,10),round(p_std,10)))
  if ret == 1:
    # return the raw output objects
    return ave1, std1, ave2, std2, price, p_std

if __name__ == "__main__":
    # execute the option pricer on separately
    # can be changed to take terminal arguments
    Barrier_Option_Pricer()