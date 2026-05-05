import torch
import torch.nn as nn

loss_fn = nn.CrossEntropyLoss()

# logits (no probabilidades)
pred = torch.tensor([[2.0, 0.5, 0.3]])
target = torch.tensor([0])

loss = loss_fn(pred, target)
print(loss)