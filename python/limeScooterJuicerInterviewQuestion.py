# [1,6,3] -> [1,2,1] -> 4
# [2,6,7,9,4,2] -> [1,2,3,4,2,1] -> 13
# [1,7,5,3,1,9] -> [1,4,3,2,1,2] -> 13
# [3,6,3,2] -> [1,3,2,1] -> 7
# [1,4,4] -> [1,2,1] -> 4
# [1,4,4,2] -> [1,2,2,1] -> 6 or 7 since the 2 could be a 3
# [priority value of scooters] -> [recharge payouts for each scooter] -> sum pf recharage payouts

# Given an input array of priority recharge values of scooters,
# output the sum of the minimum recharge payouts of all the scooters.
# Constraints: Each scooter must have a minimum recharge payout of value $1, 
# scooters with larger priority values than its neighbours must have
# higher recharge payouts than them and similarly scooters with lower priority
# values must have lower recharge payouts than their neighbours. If the
# scooters are not neighbours, the constraint does not apply.

def juicer(scooters):                                
    costs = [1] * len(scooters)
    i = 1
    while i < len(scooters):
        # check the scooter before the current scooter and if the current priority value 
        # is greater than previous, then its recharge payout is 1 greater than the previous 
        # scooter's payout
        if scooters[i-1] < scooters[i]:
            costs[i] = costs[i-1] + 1
            i+=1
        # when the current scooter priority value is less then the previous one,
        # we want to start keeping track of the how many following scooters
        # have less priority values
        else:
            j = i
            # The start of the tracking, i, needs to be the previously assigned recharge payout
            # as it will need to be reassigned after determing how many proceeding scooters are
            # are less then its predeccesor 
            i -=1
            payout = 1
            # keep increasing the payout by 1 while the current scooter priority value
            # is less than the previous. This keeps track of the total payout each iterating scooter
            # will recieve, and j keeps track of the final index of scooters that are less then its
            # previous scooter
            while j < len(scooters) and scooters[j-1] >= scooters[j]:
                payout += 1
                j+=1
            # once we reach a scooter the current priority value is greater than the previous
            # we need to unload those payouts in decrements to the unassigned iterated scooters, i -j
            while i < j:
                # since we know the first scooter at index i is the start of the tracking
                # we know that scooter had a higher priority value than scooter at i-1
                # so we still need to ensure the initial constraint is true such that 
                # its recharge payout is larger than its previous. So if payout still isnt 
                # larger than the i-1 scooter payout, we have no choice but to make it 
                # 1 greater than the previous one to satisfy it
                if payout<=costs[i-1] and scooters[i-1]< scooters[i]:
                    costs[i] = costs[i-1] +1
                # Otherwise, iterate through scooters that we havent assigned yet, and
                # assign their recharge payout to the accumlated payout variable
                else:
                    costs[i] = payout
                # Then we decrement payout by 1 and increase i by 1 until we've iterated
                # through all the tracked scooters that havent been assigned recharge payouts
                # in the range of i to  j
                payout -=1
                i+=1
    print("priority values of scooters: " + str(scooters))
    print("cost values of scooters based on prioritys: " + str(costs))
    print("sum of costs: " + str(sum(costs)))
    return sum(costs)

juicer([1,6,3])
juicer([2,6,7,9,4,2])
juicer([1,7,5,3,1,9])
juicer([3,6,3,2])
juicer([1,4,4])
juicer([1,4,4,2])