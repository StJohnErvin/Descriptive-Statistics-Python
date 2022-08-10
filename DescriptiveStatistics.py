## Descriptive Statistics

import statistics
import array as arr

friends_usage = [5,4,3,5,8,2,5,2,5,8,10,8,7,9,10,5,7,5,7,5,4,3,5,8,4]

sample_data = arr.array('i',friends_usage)
dataset = sample_data[0:5]
sample_data_list = dataset.tolist()

mean = statistics.mean(friends_usage)
mode = statistics.mode(friends_usage)
median = statistics.median(friends_usage)
pstdev = round(statistics.mode(friends_usage),2)
pvariance = round(statistics.pvariance(friends_usage),2)
srange = (max(friends_usage)-min(friends_usage))

variance = round(statistics.variance(sample_data_list),2)
stdev = round(statistics.stdev(sample_data_list),2)

print("Descriptive Statistics")
print("Mean : ",mean)
print("Mode : ",mode)
print("Median : ",median)
print("Range : ",srange)
print("Population Variance : ",pvariance)
print("Population Standard Deviation : ",pstdev)
print("Variance : ",variance)
print("Standard Deviation : ",stdev)

