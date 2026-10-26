class Tree:
    def __init__(self,data):
        self.data=data
        self.child=[] # list is used to represent the Tree DSA


    def addChild(self,value):
        self.child.append(value)

    def __str__(self,level =0):
        ret = "  "*level +str(self.data)+ "\n"
        for child in self.child:
            ret+=child.__str__(level+1)
        return ret


# create nodes
rootNode = Tree("Drinks")
hot = Tree("Hot")
cold = Tree("Cold")
tea = Tree("Tea")
coffee = Tree("Coffee")
nonalcoholic = Tree("Non-Alcoholic")
alcoholic = Tree("Alcoholic")


#add child nodes
rootNode.addChild(hot)
rootNode.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(nonalcoholic)
cold.addChild(alcoholic)

print("Tree Structure:")
print(rootNode)