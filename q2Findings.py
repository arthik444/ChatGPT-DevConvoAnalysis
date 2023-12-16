import matplotlib.pyplot as plt

# Data
identical = 86
similar = 175
different = 39
total = identical + similar + different

# Data for the pie chart
labels = ['Identical', 'Similar', 'Different']
sizes = [identical, similar, different]
colors = ['blue', 'orange', 'green']

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
plt.title('Same Prompts on Different Chats')

plt.show()
