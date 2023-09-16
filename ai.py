#this is the brain of the agent we're programming
import numpy as np
import torch 
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

#importing the packages for OpenAI and Doom
import gym
from gym.wrappers import SkipWrapper
from action_space import ToDiscrete

import experience_replay, image_preprocessing

#Bulding the AI


