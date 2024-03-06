import matplotlib.pyplot as plt

# Example data (replace with your actual data)
groups = ['StCS', 'CaS', 'CoS']
frequencies = [0, 8, 4]  # Frequency of each group

# Create bar plot
plt.bar(groups, frequencies, color='#59ae70', width=0.6)

# Add labels and title
plt.xlabel('Method Ordering Strategies')
plt.ylabel('Frequency')

# Show plot
plt.show()