import torch
import torch.nn as nn

loss_fn = nn.BCEWithLogitsLoss()

logits = torch.tensor([0.8, -1.2, 2.0])
targets = torch.tensor([1.0, 0.0, 1.0])

loss = loss_fn(logits, targets)

print(loss)