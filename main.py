import csv
import matplotlib.pyplot as plt

hqs = []
ot = []
st = []
with open ('set.csv') as d:
  data = csv.DictReader(d)
  for i in data:
    h = i['Headquarter']
    otf = float(i['Total OT\nHours'])
    stf = float(i['ST\nHours'])
    if h in hqs:
      index = hqs.index(h)
      ot[index] += otf
      st[index] += stf
    else:
      hqs.append(i['Headquarter'])
      ot.append(otf)
      st.append(stf)
      continue
new = zip(ot, st)
percent = []
for (o,s) in new:
  try:
    t = round((o/s)*100, 2)
  except ZeroDivisionError:
    t = 0
  percent.append(t)
  
for i in range(len(hqs)):
  print("{}: {}%".format(hqs[i], percent[i]))

plt.bar(hqs, percent)
plt.savefig("graph.png")