def jobScheduling(arr,max_job):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][2]<arr[j+1][2]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    tracker=[False]*max_job
    job=[-1]*max_job
    for i in range(n):
        for j in range(min(max_job-1,arr[i][1]-1),-1,-1):
            if tracker[j]==False:
                tracker[j]=True
                job[j]=arr[i][0]
                break
    print(job)
# Driver Code
arr=[['j1',5,50],
['j2',3,60],
['j3',2,70],
['j4',4,55],
['j5',3,65],
['j6',2,75],
['j7',3,90]


]
jobScheduling(arr,5)