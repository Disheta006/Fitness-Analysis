import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

days = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
weight = [80.5,80.2,80.3,79.8,79.9,79.5,79.2]
steps = [8000,12000,7000,10000,15000,11000,9000]
macros = [25,45,30]
label_macros = ['Protein','Carbs','Fats']

fig = plt.figure(figsize=(12,8))
gs = fig.add_gridspec(2,2)

ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1,:])

ax1.plot(days,weight,marker='o',color = 'tab:red',linewidth =3)
ax1.set_title("Body Weight Trend (kg)")
ax1.set_ylim(78,82)
ax1.annotate("Lowest!",xy=('Sun',79.2), xytext=('Fri',78.5)
             , arrowprops=dict(facecolor = 'black', shrink = 0.05))

ax2.pie(macros,labels=label_macros,autopct='%1.1f%%',explode=[0.1,0,0.1], shadow = True,)
ax2.set_title("Daily Macro Distribution")

colors = ['gray' if s < 10000 else 'green' for s in steps]
ax3.bar(days,steps,color=colors,alpha = 0.7)
ax3.axhline(10000,color = 'blue',linestyle = '--',label = 'Step Goal')
ax3.set_title("Daily Step Count")
ax3.legend()

plt.suptitle("Personal Health & Fitness Analysis", fontsize=18, fontweight='bold')
plt.tight_layout()

fig.savefig("Fitness_Project.png",dpi=300)
plt.show()

