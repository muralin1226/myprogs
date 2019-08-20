### perent class

class master:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def disply(self):
        print(self.firstname,self.lastname)
        return ''


x =master('Murali','N')
#print(x.disply())

class slave(master):
    def __init__(self,name,occ):
        self.name =name
        self.occupation =occ
        #master. __init__(self,fname,lname)
    def disply(self):
        print("Accessing parent class")
        print(self.name,self.occupation)
        return ''

y = slave('murali','it emp')
z = master('abc','a')

print(y.disply())
print(z.disply())

print(id(x))
print(id(y))
print(id(z))