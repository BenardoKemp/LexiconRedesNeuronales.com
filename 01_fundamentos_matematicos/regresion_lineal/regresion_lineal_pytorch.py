import torch

X = torch.tensor([[1.0], [2.0], [3.0]])
y = torch.tensor([[2.0], [4.0], [6.0]])

model = torch.nn.Linear(1, 1)

optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for _ in range(100):
    pred = model(X)
    loss = torch.mean((pred - y) ** 2)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(model(torch.tensor([[4.0]])))