
import numpy as np
import pandas as pd
import random
import simpy
import scipy.stats as stats
from time import time
from tqdm.notebook import trange # Status Bar
import matplotlib.pyplot as plt
'''
Help Deks LTDA

It's a simple model real-based process, services, bussiness as:
    - Help Desk for customers
    - Product/Services sell and activation unit
    - Develop and exploit of software team
    - Medical Attention/Urgency
    - Assembly Lines

Help Desk LTDA Model

        Requirement -> Process #1 -> Process #2 -> End
The average rate of incoming tickets from the last month is λ = 15 tickets/hour (Poisson Distribution). This is an average of 4 minutes/ticket,
the ticket arrives into the backlog of Process #1 (Callen Backlog #1) waiting to being processed by Process 1.



Process #1
The Process #1 has 2 Agents and the studies show that the process cicle follows a Gamma Distribution with a mean of 17.9 minutes. Finalized the
process, the ticket goes to Backlog #2

Process #2
The Process#2 has 2 Agents and the process also follows a Gamma Distribution with a mean of 24.5 minutes. At the end of Process 2 the ticket
is considered closed.


Simulation
The simulated scenario has the following parameters.
    - Creation Rate of tickets: λ = 15 ticket/hour
    - Time between creation of tickets: 1/λ = 4 minutes/ticket
    - Parameters of the Gamma Distribution for the time in Process #1:
        * α = 9  (Shape parameter - Control the variability of the Process, that means, how spread out the processes times are)
        * β = 2  (Scale parameter - represents the average duration of each internal phase of the process)
        * Mean = 17.9 minutes (α*β)
    - Parameters of the Gamma Distribution for the time in Process #2:
        * α = 7
        * β = 3.5  
        * Mean = 24.5 minutes
The simulation time is going to be 8 hours (480 minutes), the measurements are going to be
    - Number of created Tickets in a Day
    - Number of the solved Tickets in a Day
    - Attendance level in a Day (Created/Solved * 100)
    - Lead Time end to end in a Day. It's the Mean timelife of a ticket from created to solved.
'''


def g(alpha, beta):
    # Return an aleatory number for a gamma function with alpha and beta parameters
    while True:
        yield stats.gamma.rvs(alpha, beta, 1)

NUM_EMPLOYEES_1 = 2  # Number of the agents for the process 1
NUM_EMPLOYEES_2 = 2  # Number of the agents for the process 2

# Alpha and Beta parameters
alpha_1 = 9.0
alpha_2 = 7.00
beta_1 = 2.0
beta_2 = 3.50

SUPPORT_TIME_1 = alpha_1 * beta_1  # Mean time of process 1
SUPPORT_TIME_2 = alpha_2 * beta_2  # Mean time of process 2
AVG_CUSTOMER_HOUR = 15             # Poisson λ

CUSTOMER_INTERVAL = 60/AVG_CUSTOMER_HOUR
SIM_TIME = 60 * 8

customers_handled = 0
arrival_times = []   # Corresponds to the time when the ticket goes to Backlog
wait_times_1 = []    # Corresponds to the time when the client enter a ticket until it's being processed by process #1
wait_times_2 = []    # Corresponds to the time when the ticket is in Backlog #2 until it's being processed by process #2
support_times_1 = [] # Corresponds to the time that takes the process #1
support_times_2 = [] # Corresponds to the time that takes the process #2
total_times = []     # Corresponds to the Ticket Lifetime (From time in Backlog #1 to the finish of process #2)


class HelpDesk(object):
    def __init__(self, env, num_employees_1, num_employees_2,
                 support_time_1, support_time_2,
                 alpha_1=alpha_1, beta_1=beta_1,
                 alpha_2=alpha_2, beta_2=beta_2,
                 verbose=False):
        self.env = env
        self.staff_1 = simpy.Resource(env, num_employees_1)
        self.staff_2 = simpy.Resource(env, num_employees_2)
        self.support_time_1 = support_time_1
        self.support_time_2 = support_time_2
        self.alpha_1 = alpha_1
        self.beta_1 = beta_1
        self.alpha_2 = alpha_2
        self.beta_2 = beta_2
        self.dist_1 = stats.gamma(a=self.alpha_1, loc=0, scale=self.beta_1)
        self.dist_2 = stats.gamma(a=self.alpha_2, loc=0, scale=self.beta_2)
        self.verbose = verbose

    def support_1(self, customer):
        # The process #1 works on the first part of requirement
        random_time_1 = self.dist_1.rvs(1)[0]
        #random_time_1 = random.gammavariate(self.alpha, self.beta)
        if self.verbose: print(f"*  Process #1 finalized for the Customer {customer} at {self.env.now:.2f}")
        yield self.env.timeout(random_time_1)

    def support_2(self, customer):
        # The process #2 works on the first part of requirement
        random_time_2 = self.dist_2.rvs(1)[0]
        #random_time_2 = random.gammavariate(self.alpha, self.beta)
        if self.verbose: print(f"** Process #2 finalized for the Customer {customer} a las {self.env.now:.2f}")
        yield self.env.timeout(random_time_2)

def customer(env, name, help_desk, verbose):
    # The customers (Each client has a name) create requirements (tickets) to be solved by the agents
    # THen the tickets of the customers start to be attended by an agent of process #1 and wait
    # until it finish the process #1, the ticket foes to backlog #2. The ticket starts to be attended by
    # an agent of process #2, the customers wait until is the process #2 is finished, then the ticket is solved

    arrival_time = env.now  # save the creation time of the ticket
    arrival_times.append(arrival_time)  # calculate the time when the ticket goes to backlog
    global customers_handled
    if verbose: print(f"Customer {name} ticket enter to Backlog #1 at {env.now:.2f}")
    with help_desk.staff_1.request() as request:
        yield request
        # Customer service start with the first agent
        if verbose: print(f"Customer {name}  starts being attended in process #1 at {env.now:.2f}")
        start_support_time_1 = env.now # Save the moment when the customer service starts
        wait_times_1.append(env.now - arrival_time) # calculates the time in the backlog #1

        yield env.process(help_desk.support_1(name))
        # Customer finish the first process
        if verbose: print(f"Customer {name} finish the process #1 at {env.now:.2f}")
        support_times_1.append(env.now - start_support_time_1) # calculates the time of the customer service in process #1

    if verbose: print(f"Customer {name} ticket enter to Backlog #2 at {env.now:.2f}!")
    with help_desk.staff_2.request() as request:
        yield request
        # Client goes to second agent
        start_support_time_2 = env.now # save the moment when start the customer service in process #2
        if verbose: print(f"Customer {name} starts being attended in process #2 at {start_support_time_2:.2f}")

        yield env.process(help_desk.support_2(name))
        # Customer end the second process and ends the customer service
        if verbose: print(f"Customer {name} ticke is solved at {env.now:.2f}")
        customers_handled += 1
        support_times_2.append(env.now - start_support_time_2) # calculate the customer service time of process #2
        total_times.append(env.now - arrival_time) # Calculate the total time for the ticket.

def setup(env, num_employees_1, num_employees_2, support_time_1, support_time_2, customer_interval, verbose=False):
    """
    Create the help desk, an initial number of clients and will create customer at a "CUSTOMER_INTERVAL" rate
    """
    # Instance of Help Desk
    help_desk = HelpDesk(env, num_employees_1, num_employees_2, support_time_1, support_time_2, verbose=verbose)

    # Create 5 inicial customers
    for i in range(1, 2):
        env.process(customer(env, i, help_desk, verbose=verbose))

    # Create more clients when the simulation is running
    while True:
        yield env.timeout(stats.expon.rvs(loc=0, scale=(customer_interval), size=1)[0])
        i += 1
        env.process(customer(env, i, help_desk, verbose=verbose))

RANDOM_SEED = 2 # Seed to replicate the executio

t0 = time()
print(f"Initialized the Help Desk - for {SIM_TIME} minutes")
#random.seed(RANDOM_SEED)  # help to replicate the results
np.random.seed(seed=RANDOM_SEED) 

# Create the simulation enviroment and start the setup process
env = simpy.Environment()
env.process(setup(env, NUM_EMPLOYEES_1, NUM_EMPLOYEES_2, SUPPORT_TIME_1, SUPPORT_TIME_2, CUSTOMER_INTERVAL, verbose=True))

# Execute
env.run(until=SIM_TIME)

print(f"\nClientes atendidos: {customers_handled}")
print(f"\nTiempo total de simulación: {(time() - t0):6.4f} segundos\n\n")
NA = customers_handled / len(arrival_times) # Nivel de atención
print(f"Cantidad de tickets creados:   {len(arrival_times)}") # cantidad tickets creados
print(f"Cantidad de tickets resueltos: {customers_handled}") # cantidad tickets resueltos
print(f"Nivel de atención:             {NA:5.3f}") # Nivel atención
print(f"Leadtime:                      {np.mean(total_times):5.3f}") # leadtime

plt.hist(total_times, bins=30, range=(0, 300))
plt.ylabel('Frecuencia')
plt.xlabel('Tiempo total de duración')
plt.title('Histograma')
plt.show()