import numpy as np

def markovDecision(layout,circle):
    dice = np.zeros(14)
    expec = [17,15,13,14,12,10,8,6,4,2,8,6,4,2,0]

    for _ in range(100): # need to find when algo has converged
        #print(expec)
        for position in range(13,-1,-1):
            best_a,cost = find_best_action(position,layout,expec,circle)
            dice[position] = best_a
            expec[position] = cost

    return expec,dice

def find_best_action(position,layout,expec,circle):
    safe_cost = 1
    normal_cost = 1
    risky_cost = 1

    for i in range(14):
        tmp = 0
        if layout[i] == 3:
            tmp = 1
            
        safe_cost += proba(i,position,"safe",layout,circle)*expec[i]
        normal_cost += proba(i,position,"normal",layout,circle)*(expec[i]+tmp/2)
        risky_cost += proba(i,position,"risky",layout,circle)*(expec[i]+tmp) 

    
    if (safe_cost <= normal_cost and safe_cost <= risky_cost) : return 1,safe_cost
    if (normal_cost <= safe_cost and normal_cost <= risky_cost) : return 2,normal_cost
    if (risky_cost <= safe_cost and risky_cost <= normal_cost) : return 3,risky_cost

def proba(i,position,action,layout,circle):

    next = {0:[1], 1:[2], 2:[3,10], 3:[4], 4:[5], 5:[6], 6:[7], 7:[8], 8:[9], 
    9:[14], 10:[11], 11:[12], 12:[13], 13:[14],14:[]}

    next_with_circle = {0:[1], 1:[2], 2:[3,10], 3:[4], 4:[5], 5:[6], 6:[7], 7:[8], 8:[9], 
    9:[14], 10:[11], 11:[12], 12:[13], 13:[14],14:[-1],-1:[0]}

    minus_3 = {13:[10], 12:[2], 11:[1], 10:[0], 9:[6], 8:[5], 7:[4], 6:[3], 
    5:[2], 4:[1], 3:[0], 2:[0], 1:[0]}

    p = np.zeros(15)

    if action == "safe":
        p[position] += 0.5
        if position == 2:
            p[3] += 0.25
            p[10] += 0.25
        elif position == 9:
            p[14] = 0.5
        else:
            p[position+1] += 0.5
    

    if action == "risky":

        # 0 jump
        if layout[position] == 0 :
            p[position] += 0.25
        elif layout[position] == 1:
            p[0] += 0.25
        elif layout[position] == 2:
            p[minus_3[position]] += 0.25
        elif layout[position] == 3:
            p[position] += 0.25
        elif layout[position] == 4:
            for j in range(15):
                p[j] += 0.25/15


        pb = 0.25
        if position == 2:
            pb /= 2

        # 1 jump
        for neighbor in next[position]:

            if layout[neighbor] == 0:
                p[neighbor] += pb
            elif layout[neighbor] == 1:
                p[0] += pb
            elif layout[neighbor] == 2:
                p[minus_3[neighbor]] += pb
            elif layout[neighbor] == 3:
                p[neighbor] += pb
            elif layout[neighbor] == 4:
                for j in range(15):
                    p[j] += pb/15


        if position == 1:
            pb /= 2

        # 2 jumps

        if circle == False:
            for x in next[position]:
                for neighbor in next[x]:

                    if layout[neighbor] == 0:
                        p[neighbor] += pb
                    elif layout[neighbor] == 1:
                        p[0] += pb
                    elif layout[neighbor] == 2:
                        p[minus_3[neighbor]] += pb
                    elif layout[neighbor] == 3:
                        p[neighbor] += pb
                    elif layout[neighbor] == 4:
                        for j in range(15):
                            p[j] += pb/15
        else:
            for x in next_with_circle[position]:
                for neighbor in next_with_circle[x]:
                    if neighbor == -1:
                        neighbor = 0
                    
                    if layout[neighbor] == 0:
                        p[neighbor] += pb
                    elif layout[neighbor] == 1:
                        p[0] += pb
                    elif layout[neighbor] == 2:
                        p[minus_3[neighbor]] += pb
                    elif layout[neighbor] == 3:
                        p[neighbor] += pb
                    elif layout[neighbor] == 4:
                        for j in range(15):
                            p[j] += pb/15            


        if position == 0:
            pb /= 2

        # 3 jumps

        if circle == False:
            for x in next[position]:
                for y in next[x]:
                    for neighbor in next[y]:

                        if layout[neighbor] == 0:
                            p[neighbor] += pb
                        elif layout[neighbor] == 1:
                            p[0] += pb
                        elif layout[neighbor] == 2:
                            p[minus_3[neighbor]] += pb
                        elif layout[neighbor] == 3:
                            p[neighbor] += pb
                        elif layout[neighbor] == 4:
                            for j in range(15):
                                p[j] += pb/15
        else:
            for x in next_with_circle[position]:
                for y in next_with_circle[x]:
                    for neighbor in next_with_circle[y]:
                        if y == -1 or neighbor == -1:
                            neighbor = 0

                        if layout[neighbor] == 0:
                            p[neighbor] += pb
                        elif layout[neighbor] == 1:
                            p[0] += pb
                        elif layout[neighbor] == 2:
                            p[minus_3[neighbor]] += pb
                        elif layout[neighbor] == 3:
                            p[neighbor] += pb
                        elif layout[neighbor] == 4:
                            for j in range(15):
                                p[j] += pb/15            


    if action == "normal":

        # 0 jump
        if layout[position] == 0 :
            p[position] += 1/3
        elif layout[position] == 1:
            p[0] += 1/3/2
            p[position] += 1/3/2
        elif layout[position] == 2:
            p[minus_3[position]] += 1/3/2
            p[position] += 1/3/2
        elif layout[position] == 3:
            p[position] += 1/3
        elif layout[position] == 4:
            for j in range(15):
                p[j] += 1/3/15/2
            p[position] += 1/3/2

        pb = 1/3

        if position == 2:
            pb /= 2

        # 1 jump
        for neighbor in next[position]:

            if layout[neighbor] == 0:
                p[neighbor] += pb
            elif layout[neighbor] == 1:
                p[0] += pb/2
                p[neighbor] += pb/2
            elif layout[neighbor] == 2:
                p[minus_3[neighbor]] += pb/2
                p[neighbor] += pb/2
            elif layout[neighbor] == 3:
                p[neighbor] += pb
            elif layout[neighbor] == 4:
                for j in range(15):
                    p[j] += pb/15/2
                p[neighbor] += pb/2


        if position == 1:
            pb /= 2

        # 2 jumps

        if circle == False:
            for x in next[position]:
                for neighbor in next[x]:

                    if layout[neighbor] == 0:
                        p[neighbor] += pb
                    elif layout[neighbor] == 1:
                        p[0] += pb/2
                        p[neighbor] += pb/2
                    elif layout[neighbor] == 2:
                        p[minus_3[neighbor]] += pb/2
                        p[neighbor] += pb/2
                    elif layout[neighbor] == 3:
                        p[neighbor] += pb
                    elif layout[neighbor] == 4:
                        for j in range(15):
                            p[j] += pb/15/2
                        p[neighbor] += pb/2
        else:
            for x in next_with_circle[position]:
                for neighbor in next_with_circle[x]:
                    if neighbor == -1:
                        neighbor = 0

                    if layout[neighbor] == 0:
                        p[neighbor] += pb
                    elif layout[neighbor] == 1:
                        p[0] += pb/2
                        p[neighbor] += pb/2
                    elif layout[neighbor] == 2:
                        p[minus_3[neighbor]] += pb/2
                        p[neighbor] += pb/2
                    elif layout[neighbor] == 3:
                        p[neighbor] += pb
                    elif layout[neighbor] == 4:
                        for j in range(15):
                            p[j] += pb/15/2
                        p[neighbor] += pb/2

    return p[i]


import random


def simulate(start,layout,circle,action):
    
    cur = start
    cost = 0
    while cur < 14:
        
        cost += 1
        rdm = random.random()
        to_move = 0

        # how many jumps to do ?
        if action[cur] == 3: # risky dice
            if rdm >= 0 and rdm < 0.25:
                to_move = 0
            elif rdm >= 0.25 and rdm < 0.5:
                to_move = 1
            elif rdm >= 0.5 and rdm < 0.75:
                to_move = 2
            else:
                to_move = 3
        elif action[cur] == 1: # safe dice
            if rdm < 0.5:
                to_move = 0
            else:
                to_move = 1
        elif action[cur] == 2: # normal dice
            if rdm < 1/3:
                to_move = 0
            elif rdm >= 1/3 and rdm < 2/3:
                to_move = 1
            else:
                to_move = 2

        # save the old position
        old_cur = cur
        

        # move the pointer 
        if (cur == 0 and to_move == 3) or (cur == 1 and to_move == 2) or (cur == 2 and to_move == 1):
            rdm = random.random()
            if rdm < 0.5:
                cur = 3
            else:
                cur = 10

        elif (cur == 1 and to_move == 3) or (cur == 2 and to_move == 2):
            rdm = random.random()
            if rdm < 0.5:
                cur = 4
            else:
                cur = 11

        elif (cur == 2 and to_move == 3):
            rdm = random.random()
            if rdm < 0.5:
                cur = 5
            else:
                cur = 12

        elif (cur == 7 and to_move == 3) or (cur == 8 and to_move == 2) or (cur == 9 and to_move == 1):
            cur = 14
        elif cur == 8 and to_move == 3:
            cur = 15
        elif cur == 9 and to_move > 1:
            cur = 15

        else:
            cur += to_move

        # condition to win 
        if (circle == False and cur >= 14) or (circle == True and cur == 14):
            break

        # condition to restart
        if circle == True and cur > 14:
            cur = 0
            continue
        

        # apply the trap if any 
        if layout[cur] == 1:
            if action[old_cur] == 3 or (action[old_cur] == 2 and random.random() > 0.5):
                cur = 0
        elif layout[cur] == 2:
            if action[old_cur] == 3 or (action[old_cur] == 2 and random.random() > 0.5):
                if cur <= 3 or cur == 10:
                    cur = 0
                elif cur == 11:
                    cur = 1
                elif cur == 12:
                    cur = 2
                else:
                    cur -= 3
        elif layout[cur] == 3:
            if action[old_cur] == 3 or (action[old_cur] == 2 and random.random() > 0.5):
                cost += 1
        elif layout[cur] == 4:
            if action[old_cur] == 3 or (action[old_cur] == 2 and random.random() > 0.5):
                cur = random.randint(0,14)
        
    return cost


layout = [0,1,0,2,0,3,0,4,0,3,0,2,0,1,0]
circle = True
expec,dice = markovDecision(layout,circle)
print(expec)
print(dice)

# simulate the game with the dice choices found above, a lot of time
for j in range(14):
    c = 0
    n = 300000
    for i in range(n):
        c += simulate(j,layout,circle,dice)
    print(j,c/n)
    
