#Tenemos un array, lo que el algoritmo debe hacer es sumar los numeros dentro de
#este array 



def miniMaxSum(arr):
    # Write your code here
 s = 0
 minnum = 9999999
 maxnum = 0
 n = len(arr)
 if i in range(n):
  s += arr[i]
 minnum = min(minnum,arr[i])
 maxnum = max(maxnum,arr[i])

 print(s-maxnum, s-minnum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
