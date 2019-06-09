#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:27:50 2019

@author: Matthew Dunlop
"""

'''
This script contains the Monte Carlo Option Pricing functions.

~~ Removed PyTorch components to reduce size and be deployed on Heroku.
~~ Removed payoff function which was written in c as this did not play nicely
    with Heroku.
        
    
'''

# imports:
import math as m # for math operations
import numpy as np # for array operations

def typed_payoff(S_val,
               counter1,
               counter2,
              K,
              rq1,
              rq2):
  n = len(counter1)
  payoff = np.empty(n)
  for i in range(n):
    if (S_val[i,-1] > K) and (counter2[i] >= rq2):
        payoff[i] = S_val[i,-1] - K + 20
    elif (S_val[i,-1] > K) and (counter1[i] >= rq1) and (counter2[i] < rq2):
        payoff[i] = S_val[i,-1] - K
    elif (S_val[i,-1] > K) and (counter1[i] < rq1):
        payoff[i]= 10
    else:
        payoff[i] = 0
  return payoff

def Crude_Monte_Carlo(S = 60, K = 50, H1 = 65, H2 = 85, r = .05, T = 1,
                          sigma = .3, n = 260, nr = 4000,
                     nu = 1, dt=1, rq1 = 100, rq2 = 150):
  '''
  #####################################################
  INPUTS:
  S, K, H1, H2, r, T, sigma, n, nr have usual meanings
  
  #####################################################
  OUTPUTS:
  S_val    : share price matrix
  payoff   : payoff matrix
  counter1 : number of days per path exceeding barrier 1
  counter2 : number of days per path exceeding barrier 2
  
  '''
  payoff = np.zeros((nr,1)) # set up the paoff matrix
  
  # instantiate share price and random matrices
  S_val = np.zeros((nr,n+1)) 
  rand = np.random.randn(nr,n)
  

  # instantiate counter matrices
  counter1 = np.zeros((nr,1))
  counter2 = np.zeros((nr,1))
  
  # simulate stock price via MC (and increment counters)
  S_val[:,0] = S
  for i in range(nr):
      for j in range(1,n+1):
          S_val[i,j] = S_val[i,j-1] * m.exp(nu*dt + sigma * dt **.5 * rand[i,j-1])

          if S_val[i,j] > H2:
              counter1[i] += 1
              counter2[i] += 1
          elif S_val[i,j] > H1:
              counter1[i] += 1

  # compute payoff of each sim
  for i in range(nr):
      if (S_val[i,-1] > K) and (counter2[i] >= rq2):
          payoff[i] = S_val[i,-1] - K + 20
      elif (S_val[i,-1] > K) and (counter1[i] >= rq1) and (counter2[i] < rq2):
          payoff[i] = S_val[i,-1] - K
      elif (S_val[i,-1] > K) and (counter1[i] < rq1):
          payoff[i]= 10
      else:
          payoff[i] = 0
  return S_val, payoff, counter1, counter2

def AVT_Monte_Carlo(S = 60, K = 50, H1 = 65, H2 = 85, r = .05, T = 1,
                          sigma = .3, n = 260, nr = 4000,
                     nu = 1, dt=1, rq1 = 100, rq2 = 150):
  '''
  #####################################################
  INPUTS:
  S, K, H1, H2, r, T, sigma, n, nr have usual meanings
  
  #####################################################
  OUTPUTS:
  S_val    : share price matrix
  payoff   : payoff matrix
  counter1 : number of days per path exceeding barrier 1
  counter2 : number of days per path exceeding barrier 2
  
  '''
  payoff = np.zeros(( int(nr/2), 1))
  
  # instantiate result, payoff, and random matrices
  S_val = np.zeros((nr,n+1))
  rand = np.random.randn(int(nr/2),n)
  
  # instantiate counter matrices
  counter1 = np.zeros((nr,1))
  counter2 = np.zeros((nr,1))
  
  # simulate stock price via MC (and increment counters)
  S_val[:,0] = S
  for i in range(0, nr, 2):
      # taking two steps at a time in the share value dataframe
      for j in range(1,n+1):
          S_val[i,j] = S_val[i,j-1] * m.exp(nu*dt + sigma * dt**0.5 * rand[int(i/2),j-1])
          S_val[i+1,j] = S_val[i+1,j-1] * m.exp(nu*dt - sigma * dt**0.5 * rand[int(i/2),j-1])

          if S_val[i,j] > H2:
              counter1[i] += 1
              counter2[i] += 1
          elif S_val[i,j] > H1:
              counter1[i] += 1
          # repeat for the antithetic row:
          if S_val[i+1,j] > H2:
              counter1[i+1] += 1 # counter for the antithetic row
              counter2[i+1] += 1
          elif S_val[i+1,j] > H1:
              counter1[i+1] += 1

  # compute payoff of each sim
  for i in range(0, nr, 2):
      # Want to take average of positive and negative paths to save memory
      if (S_val[i,-1] > K) and (counter2[i] >= rq2):
          # payoff[i] = S_val[i,-1] - K + 20
          p = S_val[i,-1] - K + 20
      elif (S_val[i,-1] > K) and (counter1[i] >= rq1) and (counter2[i] < rq2):
          # payoff[i] = S_val[i,-1] - K
          p = S_val[i,-1] - K
      elif (S_val[i,-1] > K) and (counter1[i] < rq1):
          # payoff[i]= 10
          p = 10
      else:
          # payoff[i] = 0 # not necessary b/c all were initialized to 0
          p = 0

          # now payoff for the negative path:
      if (S_val[i+1,-1] > K) and (counter2[i+1] >= rq2):
          # payoff[i] = S_val[i,-1] - K + 20
          n = S_val[i+1,-1] - K + 20
      elif (S_val[i+1,-1] > K) and (counter1[i+1] >= rq1) and (counter2[i+1] < rq2):
          # payoff[i] = S_val[i,-1] - K
          n = S_val[i+1,-1] - K
      elif (S_val[i+1,-1] > K) and (counter1[i+1] < rq1):
          # payoff[i]= 10
          n = 10
      else:
          n = 0
      payoff[int(i/2)] = 0.5*p + 0.5*n
  return S_val, payoff, counter1, counter2

def Crude_Monte_Carlo_NPO(S = 60, K = 50, H1 = 65, H2 = 85, r = .05, T = 1,
                          sigma = .3, n = 260, nr = 4000,
                     nu = 1, dt=1, rq1 = 100, rq2 = 150):
  '''
  ~Numpy Optimized~
  Remove the For Loops in Crude_Monte_Carlo()
  
  #####################################################
  INPUTS:
  S, K, H1, H2, r, T, sigma, n, nr have usual meanings
  
  #####################################################
  OUTPUTS:
  S_val    : share price matrix
  payoff   : payoff matrix
  counter1 : number of days per path exceeding barrier 1
  counter2 : number of days per path exceeding barrier 2
  
  '''
  # get random matrix
  rand = np.random.randn(nr,n)
  # simulate stock price via MC (and increment counters)
  S_val = S * np.cumprod(np.exp((nu)*dt+sigma*np.sqrt(dt)*rand), axis=1)
  counter1 = (S_val >= H1).sum(axis = 1)
  counter2 = (S_val >= H2).sum(axis = 1)
  # compute payoff of each sim
  payoff = typed_payoff(S_val, counter1, counter2, K, rq1, rq2)
  return S_val, payoff, counter1, counter2

def AVT_Monte_Carlo_NPO(S = 60, K = 50, H1 = 65, H2 = 85, r = .05, T = 1,
                          sigma = .3, n = 260, nr = 4000,
                     nu = 1, dt=1, rq1 = 100, rq2 = 150):
  '''
  ~Numpy Optimized Option Anthithetic Variates Technique~
  Remove the For Loops in Crude_Monte_Carlo()
  
  #####################################################
  INPUTS:
  S, K, H1, H2, r, T, sigma, n, nr have usual meanings
  
  #####################################################
  OUTPUTS:
  S_val    : share price matrix
  payoff   : payoff matrix
  counter1 : number of days per path exceeding barrier 1
  counter2 : number of days per path exceeding barrier 2
  
  '''
  # only need half of the random matrix:
  rand = np.random.randn(int(nr/2),n)
  # simulate stock price via MC (and increment counters)
  # need positive and negative
  S_val_p = S * np.cumprod(np.exp((nu)*dt+sigma*np.sqrt(dt)*rand), axis=1)
  S_val_n = S * np.cumprod(np.exp((nu)*dt-sigma*np.sqrt(dt)*rand), axis=1)
  # This is justified as we take the mean of payoff anyway, ie. 0.5*positive_path + 0.5*negative_path
  S_val = np.append(S_val_p, S_val_n, axis = 0)
  counter1 = (S_val >= H1).sum(axis = 1)
  counter2 = (S_val >= H2).sum(axis = 1)
  # compute payoff of each sim
  payoff_p = typed_payoff(S_val[:int(nr/2),], counter1[:int(nr/2),], counter2[:int(nr/2),], K, rq1, rq2)
  payoff_n = typed_payoff(S_val[int(nr/2):,], counter1[int(nr/2):,], counter2[int(nr/2):,], K, rq1, rq2)
  payoff = 0.5*payoff_p + 0.5*payoff_n
  return S_val, payoff, counter1, counter2
