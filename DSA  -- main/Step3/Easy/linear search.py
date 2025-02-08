def find(arr,e):
    for i in range(len(arr)):
        if arr[i]==e:
            return i

if __name__=="__main__":
    arr=[1,2,3,4,5]
    e=5
    res=find(arr,e)
    print(res if res!=None else -1)
        
        
