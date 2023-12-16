import matplotlib.pyplot as plt

# Data
total_prompts = 1582
useful_prompts = 655
need_correction_prompts = 927
useful = 204
need_of_correction = 95

# Calculate the average number of prompts per "useful" and "needCorrection"
average_prompts_per_useful = useful_prompts / useful
average_prompts_per_need_correction = need_correction_prompts / need_of_correction

# Data for the bar chart
categories_bar = ['Useful', 'Need of Correction']
values_bar = [useful, need_of_correction]
colors_bar = ['blue', 'orange']

# Data for the line plot
categories_line = ['Average Prompts per Useful', 'Average Prompts per Need Correction']
values_line = [average_prompts_per_useful, average_prompts_per_need_correction]

# Plotting the bar chart
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(categories_bar, values_bar, color=colors_bar)
plt.xlabel('Categories')
plt.ylabel('Count')
plt.title('Counts of "Useful" and "Need of Correction"')

plt.show()  # Display the bar chart

# Plotting the line plot
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 2)
plt.plot(categories_line, values_line, marker='o', color='green', linestyle='-', linewidth=2, markersize=8)
plt.xlabel('Categories')
plt.ylabel('Average Number of Prompts')
plt.title('Average Prompts Distribution')

plt.show()  # Display the line plot
