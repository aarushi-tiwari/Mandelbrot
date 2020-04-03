from matplotlib import pyplot as plt
from numpy import linspace


def square(n):
    return [n[0]**2-n[1]**2, 2*n[0]*n[1]]

def add(m, n):
    return [m[0]+n[0], m[1]+n[1]]

def stable(c): 
    z=[0,0]
    pos_threshold= [900,900]
    neg_threshold = [-900,-900]
    n =  0
    while n<100: 
        z= add(square(z), c)
        if z[0]> pos_threshold[0] or z[0]<neg_threshold[0]  or z[1]>pos_threshold[1] or z[1]<neg_threshold[1]:
            return False
        n+=1
    return True

def create_points(step, minimum, maximum):
    stable_x = []
    stable_y=[]
    unstable_x= []
    unstable_y= []
    for x in linspace(minimum[0],maximum[0], num=int((maximum[0]-minimum[0])/step)):
        for y in linspace(minimum[1],maximum[1], num=int((maximum[1]-minimum[1])/step)): 
            if stable([x,y]):
                stable_x.append(int((x+3)*100))
                stable_y.append(int((y+3)*100))
            else:
                unstable_x.append(int((x+3)*100))
                unstable_y.append(int((y+3)*100))

    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    ax.scatter(stable_x, stable_y, color='k')
    ax.scatter(unstable_x, unstable_y, color= 'b')
    plt.show()

create_points(.01,[-2,-1],[.5,1])


    

    
        
