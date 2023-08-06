import numpy as np
import torch
import torch.nn as nn
import torch.autograd as autograd
import torch.nn.functional as F
import numpy



if __name__ == "__main__":
    c = torch.randn((2,2,5))
    d = c[0, 0 ,:3]
    print(d.size())

