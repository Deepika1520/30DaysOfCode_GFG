class Solution:
    def storein(self, root, lvl, lin, llv):
        if not root:
            return
        # recur for left subtree
        self.storein(root.left,lvl+1,lin,llv)
        # store inorder
        lin.append(root.data)
        llv.append(lvl)
        self.storein(root.right,lvl+1,lin,llv)
    
    def shortestRange(self, root):
        #  inOrder: stores inorder traversal of the bst
        #  level: stores level of ith node in inorder traversal
        inorder=[]
        level=[]
        self.storein(root,0,inorder,level)
        '''
            cntZero: counts number of zeros
            i: left pointer (initially at 0)
            j: right pointer
            k: index of root in inorder traversal 
            maxDepth: maximum depth of bst
            Note: these pointers are on the inorder traversal of the tree
        '''
        i=j=k=cntzero=0
        maxDepth=max(level)+1
        #  stores number of nodes at ith level
        depth=[0]*maxDepth
        # first count number of nodes at ith level till the root 
        #  right pointer initially is at root's index in inorder traversal of bst
        for k in range(len(level)):
            depth[level[k]]+=1
            if level[k]==0:
                j=k
                break
        #  count number of levels where there are 0 nodes in the range inorder[i] to inorder[j]
        cntzero=depth.count(0)
        #  intially shortest range is [x, y]
        #  x=node at 0th index
        #  y=node at last index
        #  i.e. the whole tree
        x,y=inorder[0],inorder[-1]
        # if currently picked range contains all levels change x and y accordingly
        if cntzero==0:
            x,y=inorder[i],inorder[j]
    
        # left pointer can at most go upto root's index(i.e. k)
        # right pointer can go upto last index of inorder traversal of tree
        while i<=k and j<len(inorder):
            #  while right pointer doesn't reach last index 
            #  and the current range doesn't contain all levels
            while j<len(inorder):
                #  if cntZero is 0 then this range contains all levels
                if cntzero==0:
                    #  if previous range is large then change the range
                    if (y-x) > (inorder[j]-inorder[i]):
                        x,y=inorder[i],inorder[j]
                    break
                j+=1
    
                if j>= len(inorder):
                    break
                #  if new level is discovered by this range then cntZero is decreased by 1
                if depth[level[j]]==0:
                    cntzero-=1
                depth[level[j]]+=1
            #  while current range contains all levels 
            # we can shift the left pointer by +1
            while not cntzero and i<=k:
                if (y-x)>(inorder[j]-inorder[i]):
                    x,y=inorder[i],inorder[j]
                depth[level[i]]-=1
                #  if this level is outside the current range then cntZero is increased by 1
                if depth[level[i]]==0:
                    cntzero+=1
                i+=1
        return (x,y)
