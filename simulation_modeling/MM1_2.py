# M/M/1 model  

import random 
import simpy 

random_seed = 101 
running_time = 60*8
interarrival_time = 5
service_time = 5.5

class Customer(object): 
    def __init__(self,env,counter,identity,time): 
        self.env=env 
        self.counter = counter 
        self.arrival_time=time
        self.customer_id = identity       
        print('Customer%s arrived at %0.2f' %(self.customer_id,self.arrival_time)) 
        env.process(self.service()) # start waiting the service

    def service(self): 
        counter_request = self.counter.request()
        yield counter_request
        print('Customer%s waited %0.2f minutes; started service at %0.2f' 
              %(self.customer_id, self.env.now-self.arrival_time,self.env.now))
        waiting_time = self.env.now - self.arrival_time # waiting time
        update_total_time(waiting_time) # update the total waiting time  
        update_num_customers(self.customer_id) # update the number of customers served     
        t = random.expovariate(1/ service_time)
        yield self.env.timeout(t) 
        print('Customer%s leaves the counter at %0.2f' 
              %(self.customer_id,self.env.now)) 
        self.counter.release(counter_request)
          
def customer_generator(env,counter):  
    n=0 # the first customer has number zero 
    Customer(env,counter,n,env.now)
    while True:       
        n = n + 1
        t = random.expovariate (1 / interarrival_time) # delay between arrivals            
        yield env.timeout(t)                                                                                                                                                          
        Customer(env,counter,n,env.now) 

def update_total_time(waiting_time):
    global total_time
    total_time += waiting_time

def update_num_customers(customer_id): 
    global num_customers 
    num_customers = customer_id+1

# main program 

random.seed(random_seed)

total_time = 0 # total waiting time for customers who entered service
num_customers = 0 # the number of customers who entered service

env=simpy.Environment()
    
counter = simpy.Resource(env, capacity=1)
    
env.process(customer_generator(env,counter))
    
env.run(running_time)

print('Average waiting time:%0.2f'%(total_time/num_customers))