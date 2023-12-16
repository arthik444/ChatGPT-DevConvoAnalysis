import matplotlib.pyplot as plt

# Data
categories = ['Bug-related', 'Error-messages', 'Syntax-challenges', 'Programming-language',
              'code-optimization', 'conceptual-understanding', 'develop-environment-setup',
              'version-control', 'Api-usage/Installation', 'security-concerns']

counts = [12, 46, 54, 206, 54, 141, 39, 19, 25, 0]
total = sum(counts)

# Calculate percentages for the pie chart
percentages = [(count / total) * 100 for count in counts]

# Plotting the bar chart
plt.figure(figsize=(10, 8))
plt.bar(categories, counts, color='lightblue')
plt.xlabel('Categories')
plt.ylabel('Percentage')
plt.title('Recurring Patterns - Counts')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping
plt.show()
