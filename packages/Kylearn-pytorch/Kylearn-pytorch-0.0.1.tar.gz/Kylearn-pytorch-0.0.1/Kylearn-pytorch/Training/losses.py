import torch
import torch.nn.functional as F
from utils.embeddings import one_hot_embedding

def cross_entropy_loss(logits, real, smoothing=False):
    ''' Calculate cross entropy loss, apply label smoothing if needed. '''

    real = real.contiguous().view(-1).long()

    if smoothing:
        eps = 0.1
        n_class = logits.size(1)

        one_hot = torch.zeros_like(logits).scatter(1, real.view(-1, 1), 1)
        one_hot = one_hot * (1 - eps) + (1 - one_hot) * eps / (n_class - 1)
        log_prb = F.log_softmax(logits, dim=1)

        non_pad_mask = real.ne(0)
        loss = -(one_hot * log_prb).sum(dim=1)
        loss = loss.masked_select(non_pad_mask).sum()  # average later
    else:
        # loss = F.cross_entropy(logits, real, ignore_index=0, reduction='sum')
        loss = F.cross_entropy(logits, real)

    return loss


def mse_loss(pred, real):
    loss = F.mse_loss(pred, real)

    return loss