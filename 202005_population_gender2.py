import csv
import matplotlib.pyplot as plt

f=open('202005_population_gender.csv')
data = csv.reader(f)
size=[]
m=0
f=0
name=input('찾고 싶은 지역의 이름을 말해주세요')
for row in data:
    if name in row[0]:
        for i in range(101):
            m += int(row[i+3].replace(',','') )         
            f += int(row[i+106].replace(',',''))      
        break; #해당지역의 전체 인구데이터만 가져온다. csv파일은 전체인구, 동별인구가 리스트업되어 있다.    
size.append(m)
size.append(f)

plt.rc('font',family='Malgun Gothic')
label = ['남','여']
color = ['green', 'purple']
plt.axis('equal') 
plt.pie(size, labels=label, autopct="%.1f%%", colors=color, startangle=90, explode=(0,0.1)) #default angle = 3시방향, 반시계방향으로 

plt.title(name+' 남녀 성별 비율')
plt.legend()
plt.show()
