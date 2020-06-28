import csv
import matplotlib.pyplot as plt
import math

f=open('202005_population_gender.csv')
data = csv.reader(f)
size=[]
m=[]
f=[]
diff=[]
name=input('찾고 싶은 지역 이름을 말해주세요')
for row in data:
    if name in row[0]:
        for i in range(101):
            m.append(int(row[i+3].replace(',','') )  )       
            f.append(int(row[i+106].replace(',',''))  )   
            diff.append(m[i]-f[i])
            size.append(math.sqrt(m[i]+f[i]))   #sqrt() 제곱근함수
        break;     

plt.style.use('ggplot') #격자무늬
plt.figure(figsize=(10,5), dpi=100)
plt.rc('font',family='Malgun Gothic')
plt.title(name+' 남녀 성별 인구분포')

#꺽은선 그래프로 그리기
#plt.plot(m, label="남", color='green')
#plt.plot(f, label="여", color='purple')


#차이를 막대그래프로 그리기
#plt.bar(range(101), diff, label="위 : 남성이 많다. 아래: 여성이 많다")


#산점도를 이용하여 분포도 그리기
#'''
plt.scatter(m,f, s=size, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'black', label='기준선') #기준선표시
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
#'''


plt.legend()
plt.show()
