import csv
import matplotlib.pyplot as plt

f=open('202005_population_gender.csv')
data = csv.reader(f)
m=[]
f=[]

name=input('찾고 싶은 지역의 이름을 말해주세요')
for row in data:
    if name in row[0]:
        for i in row[3:104]:
            m.append(-int(i.replace(',',''))) # -int(x) : 왼쪽에 그리기위해              

        for i in row[106:]:
            f.append(int(i.replace(',',''))) # d.replace(a,b) : 천다위의 경우 "1,234" 로 표기되기때문에 숫자로 바꿀수 없어서 ,제거
            
        break; #해당지역의 전체 인구데이터만 가져온다. csv파일은 전체인구, 동별인구가 리스트업되어 있다.    

plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family="Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+' 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성', color = 'green')
plt.barh(range(101), f, label='여성', color = 'purple')
plt.legend()
plt.show()
