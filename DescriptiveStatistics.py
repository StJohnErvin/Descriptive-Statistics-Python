import statistics

friends_usage = [5,4,3,5,8,2,5,2,5,8,10,8,7,9,10,5,7,5,7,5,4,3,5,8,4]

mean = statistics.mean(friends_usage)
mode = statistics.mode(friends_usage)
median = statistics.median(friends_usage)
pstdev = round(statistics.mode(friends_usage),2)
pvariance = round(statistics.pvariance(friends_usage),2)
srange = (max(friends_usage)-min(friends_usage))

print("Descriptive Statistics")
print("Mean : ",mean)
print("Mode : ",mode)
print("Median : ",median)
print("Range : ",srange)
print("Population Variance : ",pvariance)
print("Population Standard Deviation : ",pstdev)

