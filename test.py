from array import *
import numpy as np

global i1
global i2
class Beuron(object):
        #def init(self):#here common parameters can be initialised
        global energy #Number of loop can be run.
        energy=int(input("Avalable energy:"))
        
        def sensory_neuron1(self,energy):
                #Takes binary values generated as a result of sensing on and off touching by sensory_neuron1
                #if the current value in array travarsing is 1, then initialize a var with val 1 and pass to the requiered functions.
                energy_local_1=energy*2
                if energy_local_1>1: #energy value +ve that means the neuron is excited 
                        global input_array_1
                        input_array_1=array("count1",[]) # this is an array which stores the values of received by the sensory_neuron1 on each cycle
                        n1=int(input("Enter the number of sensory input1:")) 
                        for count1 in range(0,n1): #count1 is counter variable
                                sensory_input1=int(input())
                                if sensory_input1<0:
                                        sensory_input1=0
                                elif sensory_input1>0:
                                        sensory_input1=1
                                else:
                                        sensory_input1=0
                                input_array_1.append(sensory_input1)
                                energy_local_1=(energy_local_1-1)
                        return input_array_1 #this function returns x1 array
                else:
                        pass #do nothing
        
        def sensory_neuron2(self,energy): #this method takes the binary values generated as a result of sensing on and off touching by 
                energy_local_2=energy*2
                if energy>0:
                        global input_array_2
                        input_array_2=[] # x2 is an another array which stores the values of received by the sensory_neuron2 on each cycle
                        n2=int(input("Enter the no of sensory input2:\n"))
                        for count2 in range(0,n2):
                                sensory_input2=int(input()) 
                                if sensory_input2<0:
                                        sensory_input2=0
                                elif sensory_input2>0:
                                        sensory_input2=1
                                else:
                                        sensory_input2=0
                                input_array_2.append(sensory_input2)
                                energy_local_2=(energy_local_2-1)
                        return input_array_2 #this function returns x2 array
                else:
                        pass
                
        def memory1(self,input_array_1,input_array_2,i2,sensory_input1):
                energy_local_memorry_1=energy*7
                if energy_local_memorry_1>0:     
                        if input_array_1[sensory_input1]==1:       #need to improvise the logic in this point of code......--traversing the array,counter pov
                                if i2==1:
                                        i2=-1
                                        sum1=(np.add(input_array_1+input_array_2))+i2 #performing summation of parameters entering into the memory1
                                        if sum1>0 or sum1==1:
                                                ret_value1=1
                                                return ret_value1 #this positive value is returned to inhibitory_neuron1
                        #base condition for recursive call
                                                return memory1(x1,x2,i2)
                                                #recursive call, calling parameter and conditions need to specified
                
                else:
                                pass
                        #memory1(left_sensory_neuron())
        
        def memory2(self,input_array_2,input_array_1,i1,sensory_input2):
                if input_array_2[sensory_input2]==1:
                        if i1==1:
                                i1=-1
                                sum2=(np.add(input_array_2+input_array_1))+i1 #performing summation of parameters entering into the memory2
                                if sum2>0 or sum2==1:
                                        ret_value2=1
                                return ret_value2 #this positive value is returned to inhibitory_neuron2
                        #if ret_value2==1: #base condition
                                return memory2(x2,x1,i1) #recurisve caLL
                                #base condition need to specified -> based on energy input
                
        def inhibitory_neuron1(self):
                i1=-1
                return i1 
        #i1 will pass -ve value to m2 #i2 will pass -ve value to m1
        
        def inhibitory_neuron2(self):
                i2=-1
                return i2   
                             
        def muscle_1(args1,input_array_1): #value of m1 is getting passed as args1
                for count1 in range(len(input_array_1)):
                        print(input_array_1[count1])
                        if args1>1:
                                #expansion() #needs to be defined
                                print("Muscle_1 Expanded")
                        elif args1<0:
                                #contraction() #needs to be defined
                                print("Muscle_1 Contracted")
                        else:
                                pass #no expnasion no contraction
                                #s1 er value ta 1 ele m2 will contract
                        
        def muscle_2(args2,x2): #value of m2 is getting passed as args25
                print(x2)
                if args2>1:
                        #expansion()
                        print("Muscle_2 Expanded")
                elif args2<0:
                        #contraction()
                        print("Muscle_2 Contracted")
                else:
                        pass #no expansion and no contraction
                
obj1=Beuron()
obj1.sensory_neuron1(1)
obj1.sensory_neuron2(1)
obj1.memory1(input_array_1,input_array_2,i2=1)
obj1.memory2(input_array_1,input_array_2)

#distance->weights of the edges that form the network
