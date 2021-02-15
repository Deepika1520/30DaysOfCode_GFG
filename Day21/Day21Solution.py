class Solution:
    def traverse(self, n):
        if not n:
            return (0,2)
        
        vaccineKitL , distL = self.traverse(n.left)
        vaccineKitR , distR = self.traverse(n.right)
        
        if max(distL,distR) == 3:
            return (vaccineKitL+vaccineKitR+1 , 1)
        
        return ( vaccineKitL+vaccineKitR , 1+min(distL,distR) )

    def supplyVaccine(self, root):
        vaccineKit,dist = self.traverse(root)
        if dist==3:
            return vaccineKit+1
        return vaccineKit
