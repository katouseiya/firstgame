import numpy as np
def  costFunctionJ(X,y,theta):
    m = y.shape[0]

    X_prediction = np.matrix(X)
    theta_prediction = np.matrix(theta)

    predictions = (X_prediction) * (theta_prediction)

    sqrErrors = np.power((np.matrix(predictions) - np.matrix(y)),2)
    

    return 1/(2*m) * sum(sqrErrors)
