sigmoid = torch.sigmoid(logits)

loss = loss_fn(sigmoid, targets)
