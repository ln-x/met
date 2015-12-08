import matplotlib.pyplot as plt
import numpy as np

# Some dummy data
x = [1,2,3,4,5,6,7]
y = [1,3,3,2,5,7,9]

# Find the slope and intercept of the best fit line
slope,intercept=np.polyfit(x,y,1)

# Create a list of values in the best fit line
ablineValues = []
for i in x:
  ablineValues.append(slope*i+intercept)

# Plot the best fit line over the actual values
plt.plot(x,y,'--')
plt.plot(x, ablineValues, 'b')
plt.title(slope)
plt.show()