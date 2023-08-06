import numpy as np
import torch
import torch.nn as nn

class ComplexLinear(nn.Module):

    def __init__(self, in_features, out_features, bias=True):
        super(ComplexLinear, self).__init__()

        self.linear_re = nn.Linear(in_features, out_features, bias=bias)
        self.linear_im = nn.Linear(in_features, out_features, bias=bias)


    def forward(self, x): # shpae of x : [batch,channel*2,axis1,axis2]

        input_dim = x.size()[1] // 2
        real = self.linear_re(x[:, :input_dim]) - self.linear_im(x[:, input_dim:])
        imaginary = self.linear_re(x[:, input_dim:]) + self.linear_im(x[:, :input_dim])
        output = torch.cat((real, imaginary), dim=1)
        return output

if __name__ == "__main__":

    a = torch.randn(10,20)
    dense = ComplexLinear(10,20)
    b = dense(a)
    print(b.size())




