from sklearn.metrics import brier_score_loss

y_true = [1, 0, 1, 1]
y_prob = [0.9, 0.2, 0.8, 0.6]

score = brier_score_loss(y_true, y_prob)
print(score)