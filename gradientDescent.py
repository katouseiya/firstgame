import computeCost as com
import numpy as np
import matplotlib.pyplot as plt

def gradientDescent(X,y,theta,alpha,num_iters):
    m = y.shape[0]
    theta_X = theta.shape[0]
    J = np.zeros((num_iters,1,))
    kazu = np.zeros((num_iters,1,))
    X_2 = np.zeros((m,1,))
    for i in range(m):
        X_2[i,0] = X[i,1]*X[i,1]
    
    X = np.block([X,X_2])
    for iter in range(num_iters):
        delta = np.zeros((theta_X,1,))
        middle_0 = np.zeros((m,1,))
        middle_1 = np.zeros((m,1,))
        middle_2 = np.zeros((m,1,))
        delta = np.zeros((3,1,))
        
        
        for j in range(m):
            middle_0[j,0] = (theta[0,0]*X[j,0] + theta[1,0]*X[j,1] + theta[2,0]*X[j,1]*X[j,1] - y[j,0])*X[j,0]
            middle_1[j,0] = (theta[0,0]*X[j,0] + theta[1,0]*X[j,1] + theta[2,0]*X[j,1]*X[j,1] - y[j,0])*X[j,1]
            middle_2[j,0] = (theta[0,0]*X[j,0] + theta[1,0]*X[j,1] + theta[2,0]*X[j,1]*X[j,1] - y[j,0])*X[j,1]*X[j,1]
        delta[0,0] = (1/m)*sum(middle_0)
        delta[1,0] = (1/m)*sum(middle_1)
        delta[2,0] = (1/m)*sum(middle_2)

        theta[0,0] = theta[0,0] - (alpha)*(delta[0,0])
        theta[1,0] = theta[1,0] - (alpha)*(delta[1,0])
        theta[2,0] = theta[2,0] - (alpha)*(delta[2,0])

        J[iter,0] = com.costFunctionJ(X,y,theta)
        kazu[iter,0] = num_iters
    plt.plot(J,kazu)
    plt.show()
    

    
    
        
        
                

        
        
