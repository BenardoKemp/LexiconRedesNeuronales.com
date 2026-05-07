import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(1, 1),
    nn.Sigmoid()
)

x = torch.tensor([[2.0]])
print(model(x))
