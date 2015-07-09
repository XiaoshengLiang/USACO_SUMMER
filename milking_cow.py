f=open('milk2.in','r')
N=int(f.readline())

times=f.read().split('\n')

a=[[0 for i in range(2)] for j in range(N)]
for i in range(N):
	a[i][0]=int(times[i].split(' ')[0])
	a[i][1]=int(times[i].split(' ')[1])
a.sort()

min_time=a[0][0]
max_time=a[0][1]
ans1=max_time-min_time

for i in range(N-1):
        for j in range(1):
                if a[i+1][j]<a[i][j+1]:
			max_time=max(a[i+1][j+1],a[i][j+1])
                else:
			min_time=a[i+1][0]
			free_start=a[i][j+1]
			free_end=a[i+1][j]
			ans2=free_end-free_start

ans1=max(max_time-min_time,ans1)
ans2=max(free_end-free_start,ans2)

f=open('milk2.out','w')
f.write(str(ans1))
f.write(' ')
f.write(str(ans2))
f.close()


