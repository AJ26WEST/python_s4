import scipy.stats as stats
mean=3.4
k=4
prob=stats.poisson.pmf(k,mean)
print("The poisson distribution is -",prob)
