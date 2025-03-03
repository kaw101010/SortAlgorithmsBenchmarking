import matplotlib.pyplot as plt

file_name = "output.txt"

sizes = []
insertion_times = []
merge_times = []

# Read and parse the file
with open(file_name, "r") as file:
    for line in file:
        # Expected n=10, Insertion=1.418e-06s, Merge=5.354e-06s
        parts = line.strip().split(", ")

        # Extract values
        size = int(parts[0].split("=")[1])
        insertion_time = float(parts[1].split("=")[1][:-1])
        merge_time = float(parts[2].split("=")[1][:-1])

        sizes.append(size)
        insertion_times.append(insertion_time)
        merge_times.append(merge_time)

# Plot the extracted data
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, marker='o', linestyle='-', label='Insertion Sort', color='orange')
plt.plot(sizes, merge_times, marker='s', linestyle='-', label='Merge Sort', color='red')

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Performance")

## log scale for better visualization
plt.yscale("log")
plt.xscale("log")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()
