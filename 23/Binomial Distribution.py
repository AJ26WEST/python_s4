import scipy.stats as stats
n=6
p=0.25
k=4
succ4=stats.binom.pmf(k,n,p)
print("THe probability of 4 success is -",succ4)
suc1=1-stats.binom.pmf(0,n,p)
print("The probability of atleast 1 succes is",suc1)
