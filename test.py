# Define the groups: A_group and B_group contain predefined sets of numbers
A_group = {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 17, 18, 20, 22}  # Group A nodes
B_group = {9, 10, 15, 16, 19, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34}  # Group B nodes

# Create a dictionary to store the labels for each node
node_labels = {}

# Iterate through A_group and assign label "A"
for num in A_group:
    node_labels[num] = 1  # Assign "A" to numbers in A_group

# Iterate through B_group and assign label "B"
for num in B_group:
    node_labels[num] = 2  # Assign "B" to numbers in B_group

# Print only the labels without keys
print(list(node_labels.values()))
