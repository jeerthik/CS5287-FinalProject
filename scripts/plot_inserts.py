import numpy as np
import matplotlib.pyplot as plt

def calculate_percentile_markers(arr):

	markers = []
	percents = [.9, .95, .99]
	diff = np.max(arr) - np.min(arr)

	for i in range(len(percents)):
		markers.append(int(percents[i] * diff))

	return markers

iterations = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
client_1_results = np.sort(np.array([9.028955725, 11.109154429, 18.124794267, 35.918388631, 14.212208557000011, 11.685855539999991, 11.951195237999997, 8.731465123000007, 8.324462451999992, 9.867933739000023]))
client_5_results = np.sort(np.array([14.920296171, 41.768099882, 10.264401846999995, 19.768363051999998, 41.37886214700001, 10.524089259999982, 22.562194175000002, 41.03852522700001, 22.234558094999983,29.937313165000006]))
client_10_results = np.sort(np.array([13.325902329,13.000076413,14.824416009,13.364173149000003,14.657134909,16.453100893,12.78013352299999,11.93847719,11.756486045999992,12.484378062000005]))
client_20_results = np.sort(np.array([11.062498475,14.85848739,12.916033823000003,11.654170536999999,15.262387158000003,13.25751198799999,16.359566484,13.59160893299999,14.548032789000004,11.927705697999983]))

print("===== CouchDB Insertion Times =====")
print(client_1_results)
print(client_5_results)
print(client_10_results)
print(client_20_results)
print("===================================")

print("10th iteration for 1 client: " + str(client_1_results[9]))
print('10th iteration for 5 cleints: ' + str(client_5_results[9]))

# c1_markers = calculate_percentile_markers(client_1_results)
# c5_markers = calculate_percentile_markers(client_5_results)
# c10_markers = calculate_percentile_markers(client_10_results)
# c20_markers = calculate_percentile_markers(client_20_results)

# print("1 client line markers: {}".format(c1_markers))

plt.title("CouchDB Insertion Time")
plt.xlabel("Trial iterations")
plt.ylabel("Time (seconds) to execute 100 insertions")
plt.xticks(iterations)
c1_line = plt.plot(iterations, client_1_results, color = "blue", label = "1 client", marker = "o")
c5_line = plt.plot(iterations, client_5_results, color = "green", label = "5 clients", marker = "o")
c10_line = plt.plot(iterations, client_10_results, color = "pink", label = "10 clients", marker = "o")
c20_line = plt.plot(iterations, client_20_results, color = 'purple', label = "20 clients", marker = "o")

# plt.axvline(x = 9, color = "yellow", linestyle = "dashed", label = "90%")
# plt.axvline(x = 9.5, color = "orange", linestyle = "dashed", label = "95%")
# plt.axvline(x = 9.9, color = "red", linestyle = "dashed", label = "99%")
plt.legend(loc = "upper left")
plt.show()