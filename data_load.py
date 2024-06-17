import pandas as pd
import matplotlib.pyplot as plt


# load the csv from the data folder

training_frame = pd.read_csv('data/F16traindata_CMabV_2024.csv')
validation_frame = pd.read_csv('data/F16validationdata_2024.csv')

# remove data points where the Cm is above 0.3, as these are outliers
training_frame = training_frame[training_frame['Cm'] < 0.3]

# remove validation data points that lie outside the training data range
# validation_frame = validation_frame[validation_frame['beta_val'] < 0.17]
# validation_frame = validation_frame[validation_frame['beta_val'] > -0.17]

# create a 3D plot of the training data, for alpha, beta, and Cm
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(training_frame['alpha'], training_frame['beta'], training_frame['Cm'])
ax.scatter(validation_frame['alpha_val'], validation_frame['beta_val'], validation_frame['Cm_val'])
ax.set_xlabel('alpha')
ax.set_ylabel('beta')
ax.set_zlabel('Cm')
plt.show()





