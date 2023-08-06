import torch
import numpy

def _fft(X, rank):
    X = torch.from_numpy(X)
    X = X.float()
    input_dim = X.size()[1] // 2
    X_re = X[:, :input_dim]
    X_im = X[:, input_dim:]

    if not(X_re.size() == X_im.size()):

        raise ValueError("real and imaginary tensors must have the same dimension.")

    if not(X_re.dim() >= rank+1 and X_im.dim() >= rank+1):

        raise ValueError("Inputs must have at least {} dimensions.".format(rank+1))

    X = torch.stack((X_re, X_im), dim=-1)
    X = torch.fft(X, rank)


    if X.dim() == 3:
        size = X.size()[:2]
        X_re = X[:, :, 0].view(size)
        X_im = X[:, :, 1].view(size)
        X = torch.cat((X_re, X_im), dim=1)

    elif X.dim() == 4:

        size = X.size()[:3]
        X_re = X[:, :, 0].view(size)
        X_im = X[:, :, 1].view(size)
        X = torch.cat((X_re, X_im), dim=1)

    X = X.numpy()


    return X

if __name__ == "__main__":

    a = torch.randn(5,100)
    b = _fft(a, rank=1)
    print(b.size())





