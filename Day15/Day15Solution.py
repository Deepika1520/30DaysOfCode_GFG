def countTriplets(head,x):
    # code here
    tempdict={}
    h1=head
    
    while h1:
        if h1.val in tempdict:
            tempdict[h1.val]+=1
        else:
            tempdict[h1.val]=1
        h1=h1.nxt
    t1=head
    count=0
    while t1.nxt!=None:
        t2=t1.nxt
        while t2!=None:
            tempsum=x-(t1.val+t2.val)
            if tempdict.get(tempsum,0)!=0 and tempsum<t2.val:
                count+=1
            t2=t2.nxt
        t1=t1.nxt
    
    return count
    
 
class Node:
  def __init__(self,x):
      self.val=x
      self.nxt=None
      
if __name__=='__main__':
      t=int(input())
      for _ in range(t):
            line=input().strip().split()
            n=int(line[0])
            x=int(line[1])
            line=input().strip().split()
            
            head=Node(int(line[0]))
            tail=head
            for i in range(1,n):
                  tail.nxt=Node(int(line[i]))
                  tail=tail.nxt
            print(countTriplets(head,x))
