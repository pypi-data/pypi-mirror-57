import torch


class TorchCovarianceMatrix(object):

    def __init__(self, bias=False, device='cuda:0'):
        self.device = device
        self._input_dim = None  # will be set in _init_internals
        # covariance matrix, updated during the training phase
        self._cov_mtx = None
        # average, updated during the training phase
        self._avg = None
        # number of observation so far during the training phase
        self._tlen = 0

        self.bias = bias

    def _init_internals(self, x: torch.Tensor):
        """Init the internal structures.

        The reason this is not done in the constructor is that we want to be
        able to derive the input dimension and the dtype directly from the
        data this class receives.
        """
        x = x.type(torch.float64).to(device=self.device)
        # init dtype
        dim = x.shape[1]
        self._input_dim = dim
        # init covariance matrix
        self._cov_mtx = torch.zeros((dim, dim)).type(torch.float64).to(self.device)
        # init average
        self._avg = torch.zeros((dim)).type(torch.float64).to(self.device)
        self._tlen = 0

    def update(self, x):
        """Update internal structures.

        Note that no consistency checks are performed on the data (this is
        typically done in the enclosing node).
        """
        x = x.type(torch.float64).to(device=self.device)
        if self._cov_mtx is None:
            self._init_internals(x)
        # update the covariance matrix, the average and the number of
        # observations (try to do everything inplace)
        self._cov_mtx.data += torch.matmul(x.transpose(0, 1), x)
        self._avg.data += x.sum(dim=0)
        self._tlen += x.shape[0]

    def fix(self, center=True):
        """Returns a triple containing the covariance matrix, the average and
        the number of observations. The covariance matrix is then reset to
        a zero-state.

        If center is false, the returned matrix is the matrix of the second moments,
        i.e. the covariance matrix of the data without subtracting the mean."""
        # local variables
        tlen = self._tlen
        cov_mtx = self._cov_mtx
        avg = self._avg / tlen
        if center:
            avg_mtx = torch.ger(avg, avg)
            cov_mtx -= avg_mtx
        cov_mtx = cov_mtx / tlen
        return cov_mtx
