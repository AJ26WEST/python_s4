import matplotlib.pyplot as plt
bins=[135,140,145,150,155]
st=[4,12,16,8]
plt.hist(bins[:-1],bins=bins,weights=st)
plt.xlabel("Height")
plt.ylabel("No of students")
plt.grid()
plt.title("HISTOGRAph")
plt.show()
