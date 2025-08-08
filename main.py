import numpy as np

days_per_sim = 30

def simulation(days_per_sim, lampdaDemand):
    dailDem = []
    for day in range(days_per_sim):
        randDemand = np.random.poisson(lampdaDemand)
        dailDem.append(randDemand)
    return dailDem

def sim_stats(dems):
    mean = np.mean(dems)
    std_dev = np.std(dems)
    bot_perc = np.percentile(dems, 5)
    top_perc = np.percentile(dems, 95)

    print(f"\nStatistics for {num_sims} simulations with daily demand of {lampdaDemand} units:")
    print(f"Mean: {mean:.2f}")
    print(f"Standard deviation: {std_dev:.2f}")
    print(f"Bottom 5th percentile: {bot_perc:.2f}")
    print(f"Top 95th percentile: {top_perc:.2f}")

def sim_Mdems(num_sims, days_per_sim, lampdaDemand):
    monthly_totals = []
    for sim in range(num_sims):
        monthly_total = 0
        for day in range(days_per_sim):
            daily_demand = np.random.poisson(lampdaDemand)
            monthly_total += daily_demand
        monthly_totals.append(monthly_total)
    return monthly_totals

def inv_level(monthly_totals, servLevel):
    required_inventory = np.percentile(monthly_totals, servLevel)
    print(f"\nFor service level of: {servLevel:.0f}%")
    print(f"At least {required_inventory:.0f} units in inventory required.")


while True:
    print("\nChoose your simulation options:")
    print("1: Input simulation options and run")
    print("2: Find optimal inventory level")
    print("3: Exit program")
    choice = int(input("Choice: "))

    if choice == 1:
        lampdaDemand = int(input("Average daily demand: "))
        num_sims = int(input("Amount of simulations: "))
        sim_demands = simulation(days_per_sim, lampdaDemand)
        sim_stats(sim_demands)

    elif choice == 2:
        lampdaDemand = int(input("Average daily demand: "))
        servLevel = float(input("Input service level in % (0 - 100): "))
        num_sims = int(input("Amount of simulations: "))
        monthly_demands = sim_Mdems(num_sims, days_per_sim, lampdaDemand)
        inv_level(monthly_demands, servLevel)
    
    elif choice == 3:
        print("Program terminated\nI'll be back 👍🔥🤖")
        break

    else: 
        print("Please input valid choice number")