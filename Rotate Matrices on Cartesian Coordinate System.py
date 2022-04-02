"""
- First of all, I created the main function that will allow us to rotate the matrix. 
- I created an additional function to help calculate angles and axes. 
- Then I converted the angles from degrees to radians to make it easier to calculate and I separated the axes 
 according to 3 conditions using if-elif-else. 
- I created a separate additional function for coordinates. 
- Finally, I combined the “rotation” and “coord” functions.
"""
import numpy as np 
import math as m

def nvec(degree,axis,x,y,z):
    
        def rotation(degree,axis):

            degree=m.radians(degree)
            sinus = np.sin(degree)
            coss = np.cos(degree)
  
            if axis == 1:
                hyper = np.stack([[1, 0, 0],[0, coss, -sinus], [0, sinus, coss]])

            
            elif axis == 2:
                hyper = np.stack([[coss, 0, sinus], [0, 1, 0],[-sinus, 0, coss]])

            
            elif axis == 3:
                hyper = np.stack([[coss, -sinus, 0], [sinus, coss, 0],[0, 0, 1]])


            else:
                pass
            return hyper

        def coord(x,y,z):

            v1=np.array([[x],[y],[z]])
            
            return v1
        

        return np.dot(rotation(degree,axis),coord(x,y,z))
