# Pseudo Code of Batch Gradient Descent

for i in range(EPOCHS):
   grad = evaluateGradinet(Data, params, cost function)
   params = params - learning_rate*grad
