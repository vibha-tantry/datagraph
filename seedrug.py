import drugs
import matplotlib.pyplot as plt
import math
import numpy as np

list_of_report = drugs.get_reports()

def makeAvg(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
        average = sum/len(list)
    return average

mari = []
ageRange26mari = []
for n in list_of_report:
    ageRange26mari.append(n["Totals"]["Marijuana"]["Used Past Month"]["26+"])
avg1 = makeAvg(ageRange26mari)
mari.append(avg1)

ageRange1825mari = []
for n in list_of_report:
    ageRange1825mari.append(n["Totals"]["Marijuana"]["Used Past Month"]["18-25"])
avg2 = makeAvg(ageRange1825mari)
mari.append(avg2)

ageRange1217mari = []
for n in list_of_report:
    ageRange1217mari.append(n["Totals"]["Marijuana"]["Used Past Month"]["12-17"])
avg3 = makeAvg(ageRange1217mari)
mari.append(avg3)

print("marijuana use in past month, ages 26+, 18-25, 12-17 respectively: " + str(mari))


alc = []
ageRange26alc = []
for n in list_of_report:
    ageRange26alc.append(n["Totals"]["Alcohol"]["Use Past Month"]["26+"])
avg4 = makeAvg(ageRange26alc)
alc.append(avg4)

ageRange1825alc = []
for n in list_of_report:
    ageRange1825alc.append(n["Totals"]["Alcohol"]["Use Past Month"]["18-25"])
avg5 = makeAvg(ageRange1825alc)
alc.append(avg5)

ageRange1217alc = []
for n in list_of_report:
    ageRange1217alc.append(n["Totals"]["Alcohol"]["Use Past Month"]["12-17"])
avg6 = makeAvg(ageRange1217alc)
alc.append(avg6)

print("alcohol use in past month, ages 26+, 18-25, 12-17 respectively: " + str(alc))


tob = []
ageRange26tob = []
for n in list_of_report:
    ageRange26tob.append(n["Totals"]["Tobacco"]["Use Past Month"]["26+"])
avg7 = makeAvg(ageRange26tob)
tob.append(avg7)

ageRange1825tob = []
for n in list_of_report:
    ageRange1825tob.append(n["Totals"]["Tobacco"]["Use Past Month"]["18-25"])
avg8 = makeAvg(ageRange1825tob)
tob.append(avg8)

ageRange1217tob = []
for n in list_of_report:
    ageRange1217tob.append(n["Totals"]["Tobacco"]["Use Past Month"]["12-17"])
avg9 = makeAvg(ageRange1217tob)
tob.append(avg9)

print("tobacco use in past month, ages 26+, 18-25, 12-17 respectively: " + str(tob))


ill= []
ageRange26ill = []
for n in list_of_report:
    ageRange26ill.append(n["Totals"]["Illicit Drugs"]["Used Past Month"]["26+"])
avg10 = makeAvg(ageRange26ill)
ill.append(avg10)

ageRange1825ill = []
for n in list_of_report:
    ageRange1825ill.append(n["Totals"]["Illicit Drugs"]["Used Past Month"]["18-25"])
avg11 = makeAvg(ageRange1825ill)
ill.append(avg11)

ageRange1217ill = []
for n in list_of_report:
    ageRange1217ill.append(n["Totals"]["Illicit Drugs"]["Used Past Month"]["12-17"])
avg12 = makeAvg(ageRange1217ill)
ill.append(avg12)

print("illicit drug use in past month, ages 26+, 18-25, 12-17 respectively: " + str(ill))

total = [mari, alc, tob, ill]



np.random.seed(0)

n_bins = 4
x = [[avg1], [avg2], [avg3], [avg4], [avg5], [avg6], [avg7], [avg8], [avg9], [avg10], [avg11], [avg12]]

#fig, axes = plt.subplots(nrows=2, ncols=2)
#ax0, ax1, ax2, ax3 = axes.flatten()

colors = ['red', 'tan', 'lime', 'red', 'tan', 'lime', 'red', 'tan', 'lime', 'red', 'tan', 'lime']
age = ["12-17", "18-25", "26+"]
plt.hist(x, n_bins, histtype='bar', color=colors, label=age, orientation = 'horizontal')
plt.legend(prop={'size': 5})
plt.title('pls help')
plt.axis([0, 2, 0, 200000])

plt.show()
