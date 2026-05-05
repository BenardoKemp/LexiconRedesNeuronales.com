import torch

p = torch.tensor([0.5, 0.5])
entropy = -torch.sum(p * torch.log(p))

print(entropy)