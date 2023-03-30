import matplotlib.pyplot as plt
import numpy as np


def plot_graph(layout,circle,theoretical_dice,theoretical_cost,
empirical_cost_1,empirical_cost_2,empirical_cost_3,empirical_cost_rdm_1,empirical_cost_rdm_2,
empirical_dice_rdm_1,empirical_dice_rdm_2,empirical_cost_best_dice):
    x = np.arange(14)

    barWidth = 0.12
    fig,ax = plt.subplots(1,1,figsize =(15, 10))
    
    

    br1 = np.arange(14)-barWidth*2.5
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    br6 = [x + barWidth for x in br5]

    plt.scatter(x-barWidth*2.5,theoretical_cost,color='green',s=33,marker='x',zorder=10,alpha=0.6,label='theoretical best strat')


    plt.xticks(x,x)
    plt.bar(br1,empirical_cost_best_dice,width=barWidth,label='optimal',color='limegreen')
    plt.bar(br2,empirical_cost_1,width=barWidth,label="only dice 1",color='black')
    plt.bar(br3,empirical_cost_2,width=barWidth,label='only dice 2',color='gray')
    plt.bar(br4,empirical_cost_3,width=barWidth,label='only dice 3',color='silver')
    plt.bar(br5,empirical_cost_rdm_1,width=barWidth,label='random dice 1st try',color='darkviolet')
    plt.bar(br6,empirical_cost_rdm_2,width=barWidth,label='random dice 2nd try',color='violet')

    plt.xlabel('Tiles')
    plt.ylabel('Cost')

    title = 'Comparison of empirical cost between optimal strategy and sub-optimal strategies\n'
    title += "layout = " + str(layout) + " with"
    if circle == False:
        title += "out"
    title += " circle \n"
    title += "optimal dice = " + str(theoretical_dice) + "\n"
    title += "random dice 1st try = " + str(empirical_dice_rdm_1) + "\n"
    title += "random dice 2nd try = " + str(empirical_dice_rdm_2) + "\n"


    plt.title(title)
    plt.legend()
    #plt.savefig("layout = " + str(layout) + '.pdf')

    plt.show()


layout = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
circle = True
theoretical_dice = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 3, 3, 2, 1]
theoretical_cost = [7.26, 6.693, 5.366, 5.715, 4.994, 4.371, 3.778, 2.833, 2.5, 2.0, 3.778, 2.833, 2.5, 2.0]
empirical_cost_1 = [17.003, 14.989, 13.005, 13.994, 12.002, 10.008, 7.997, 6.001, 3.996, 2.0, 8.0, 5.998, 4.001, 1.996]
empirical_cost_2 = [13.897, 13.301, 11.538, 11.98, 10.912, 10.142, 8.657, 8.597, 5.757, 8.434, 8.651, 8.569, 5.722, 8.447]
empirical_cost_3 = [13.426, 12.788, 11.476, 11.964, 10.935, 10.515, 10.441, 7.835, 9.272, 10.282, 10.453, 7.818, 9.24, 10.279]
empirical_cost_rdm_1 = [22.663, 21.765, 21.116, 21.064, 19.066, 17.801, 17.282, 15.359, 14.815, 12.81, 17.263, 12.919, 18.509, 16.431]
empirical_dice_rdm_1 = [3, 3, 1, 1, 2, 2, 1, 2, 1, 2, 2, 3, 1, 3]
empirical_cost_rdm_2 = [13.978, 11.992, 8.748, 11.778, 11.467, 10.952, 8.929, 8.612, 5.744, 8.479, 4.825, 2.833, 2.5, 1.997]
empirical_dice_rdm_2 = [1, 3, 3, 3, 2, 1, 3, 2, 2, 2, 1, 3, 2, 1]
empirical_cost_best_dice = [7.255, 6.69, 5.36, 5.721, 4.988, 4.369, 3.777, 2.834, 2.495, 2.001, 3.779, 2.836, 2.498, 2.005]
plot_graph(layout,circle,theoretical_dice,theoretical_cost,empirical_cost_1,empirical_cost_2,empirical_cost_3,empirical_cost_rdm_1,empirical_cost_rdm_2,empirical_dice_rdm_1,empirical_dice_rdm_2,empirical_cost_best_dice)


layout = [0, 4, 0, 0, 3, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0]
circle = False
theoretical_dice = [3, 3, 3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3]
theoretical_cost = [7.837, 7.942, 7.096, 7.927, 7.26, 6.39, 5.126, 3.778, 1.778, 1.333, 4.331, 2.37, 1.778, 1.333]
empirical_cost_1 = [16.989, 15.01, 13.007, 14.002, 12.01, 9.99, 8.0, 5.999, 3.996, 1.998, 7.998, 5.999, 4.002, 2.001]
empirical_cost_2 = [9.772, 9.783, 8.952, 9.83, 8.499, 7.65, 5.854, 4.393, 2.245, 1.498, 5.41, 3.378, 2.247, 1.503]
empirical_cost_3 = [8.065, 8.342, 7.346, 8.275, 8.244, 6.39, 5.133, 3.836, 1.778, 1.334, 4.38, 2.372, 1.775, 1.335]
empirical_cost_rdm_1 = [9.63, 9.714, 8.66, 9.884, 7.861, 7.112, 5.128, 4.173, 2.166, 1.332, 6.533, 4.505, 3.999, 1.998]
empirical_dice_rdm_1 = [2, 2, 3, 1, 2, 1, 3, 2, 2, 3, 2, 2, 1, 1]
empirical_cost_rdm_2 = [11.435, 12.386, 10.366, 12.074, 11.342, 9.335, 7.33, 5.333, 4.0, 2.001, 5.491, 3.163, 1.834, 1.501]
empirical_dice_rdm_2 = [2, 1, 2, 2, 1, 2, 1, 3, 1, 1, 3, 2, 3, 2]
empirical_cost_best_dice = [7.798, 7.948, 7.06, 7.903, 7.409, 6.119, 5.173, 3.776, 1.78, 1.333, 4.371, 2.37, 1.775, 1.334]
plot_graph(layout,circle,theoretical_dice,theoretical_cost,empirical_cost_1,empirical_cost_2,empirical_cost_3,empirical_cost_rdm_1,empirical_cost_rdm_2,empirical_dice_rdm_1,empirical_dice_rdm_2,empirical_cost_best_dice)


layout = [0, 4, 2, 1, 3, 3, 2, 1, 4, 1, 2, 3, 2, 1, 0]
circle = True
theoretical_dice = [3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
theoretical_cost = [11.509, 11.881, 11.671, 12.7, 11.995, 10.0, 8.0, 6.0, 4.0, 2.0, 8.0, 6.0, 4.0, 2.0]
empirical_cost_1 = [17.009, 14.998, 12.987, 14.005, 11.995, 9.999, 8.004, 6.0, 4.0, 2.0, 8.003, 6.0, 4.001, 2.003]
empirical_cost_2 = [33.751, 34.151, 34.419, 35.867, 35.218, 33.498, 29.608, 27.99, 17.58, 21.427, 30.421, 28.943, 19.102, 21.484]
empirical_cost_3 = [29.943, 31.226, 31.265, 33.791, 33.867, 31.577, 31.032, 22.534, 22.535, 23.567, 29.59, 22.123, 23.8, 23.567]
empirical_cost_rdm_1 = [33.354, 35.194, 33.101, 36.296, 34.288, 32.256, 33.267, 19.26, 17.286, 21.232, 25.848, 23.723, 23.227, 21.251]
empirical_dice_rdm_1 = [2, 1, 1, 1, 1, 2, 3, 1, 2, 2, 1, 3, 1, 2]
empirical_cost_rdm_2 = [55.675, 53.452, 55.419, 56.743, 55.371, 53.305, 46.545, 44.347, 27.812, 34.665, 47.816, 45.639, 30.357, 34.585]
empirical_dice_rdm_2 = [1, 3, 3, 3, 1, 3, 1, 2, 2, 2, 1, 2, 2, 2]
empirical_cost_best_dice = [11.287, 11.713, 11.562, 12.658, 11.998, 10.01, 8.004, 6.001, 3.997, 1.998, 7.999, 6.004, 4.004, 2.0]
plot_graph(layout,circle,theoretical_dice,theoretical_cost,empirical_cost_1,empirical_cost_2,empirical_cost_3,empirical_cost_rdm_1,empirical_cost_rdm_2,empirical_dice_rdm_1,empirical_dice_rdm_2,empirical_cost_best_dice)
