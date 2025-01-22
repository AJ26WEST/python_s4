import matplotlib.pyplot as plt
categories=["AFRICA","ASIA","EUROPE","North America","Oceania","South America","SOviet"]
y=[11.7,10.4,1.9,9.4,3.3,6.9,7.9]
plt.bar(categories,y)
plt.xticks(rotation=45)
plt.xlabel("Continent")
plt.ylabel("sq miles")
plt.grid()

plt.title("BAR GRAPH")
plt.show()
