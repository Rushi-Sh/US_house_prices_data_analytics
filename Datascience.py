import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv(r"C:\Users\rushi\Desktop\CS FILES\Data Science\US_House_Price.csv")
df = pd.DataFrame(data)

# # For const_price_index
#
# # Sort the DataFrame by the 'Year' column
# df.sort_values(by='Year', inplace=True)
#
# # Generate x values
# x = df["const_price_index"].values
#
# # Calculate the derivative of the function
# df_dx = np.gradient(x)
# list1 = df_dx.tolist()
#
# # Calculate the cumulative sum (integration) of the function
# integrated_values = np.cumsum(x)
#
# # Store integrated values in a list
# integrated_list = integrated_values.tolist()
#
# # Generate y values (assuming 'Year' is a column in your dataset)
# y = df["Year"].values
#
# # Find global maxima and minima indices
# max_index = np.argmax(list1)
# min_index = np.argmin(list1)
#
# # Plot the function and its derivative
# plt.figure(figsize=(10, 8))
#
# plt.subplot(3, 1, 1)
# plt.plot(y, x, label='Function (Const Price Index)')
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Const Price Index')
#
#
# plt.subplot(3, 1, 2)
# plt.plot(y, df_dx, label='Derivative of Const Price Index')
# plt.scatter(y[max_index], df_dx[max_index], color='red', label=f'Global Maxima: {y[max_index]}')
# plt.scatter(y[min_index], df_dx[min_index], color='green', label=f'Global Minima: {y[min_index]}')
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Derivation of Const Price Index')
#
#
# plt.subplot(3, 1, 3)
# plt.plot(y, integrated_list, label='Integration of Const Price Index')
# plt.legend()
# plt.xlabel('Year')
# plt.ylabel('Integration of Const Price Index')
#
#
# plt.tight_layout()
# plt.show()


# For GDP

# Generate x values
x = df["GDP"].values

# Calculate the derivative of the function
df_dx = np.gradient(x)
list1 = df_dx.tolist()

# Calculate the cumulative sum (integration) of the function
integrated_values = np.cumsum(x)

# Store integrated values in a list
integrated_list = integrated_values.tolist()

# Generate y values (assuming 'Year' is a column in your dataset)
y = df["Year"].values

# Find global maxima and minima indices
max_index = np.argmax(list1)
min_index = np.argmin(list1)

# Plot the function and its derivative
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(y, x, label='Function (GDP)')
plt.legend()
plt.xlabel('Year')
plt.ylabel('GDP')


plt.subplot(3, 1, 2)
plt.plot(y, df_dx, label='Derivative of Const Price Index')
plt.scatter(y[max_index], df_dx[max_index], color='red', label=f'Global Maxima: {y[max_index]}')
plt.scatter(y[min_index], df_dx[min_index], color='green', label=f'Global Minima: {y[min_index]}')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Derivation of GDP')


plt.subplot(3, 1, 3)
plt.plot(y, integrated_list, label='Integration of Const Price Index')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Integration of GDP')


plt.tight_layout()
plt.show()