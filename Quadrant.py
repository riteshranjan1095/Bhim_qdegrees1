import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def quad(a):
    import pandas as pd
    a1 = a[['Rating','Categories','Total Nps Score Cat Wise','Total Nps Score']]
    Importance =[]
    Categories = []
    Nps_score_cat = []
    for i in a1['Categories'].unique():
        Importance.append(len(a1[a1['Categories']==i])/len(a1))
        Categories.append(i)
    for i in a1['Total Nps Score Cat Wise'].unique():
        Nps_score_cat.append(i)
    a2 = pd.DataFrame({'Categories':Categories,'Importance':Importance,'Nps_score_cat':Nps_score_cat})
    return a2


def quad_visual(a2):
    X2 =a2['Nps_score_cat']
    Y2 =a2['Importance']
    x_line =a2['Nps_score_cat'].mean()
    y_line =a2['Importance'].mean()
    annotations=[i for i in a2['Categories']]
    nps =[i for i in a2['Nps_score_cat']]
    Importance = [i for i in a2['Importance']]
    figure(figsize=(50, 60), dpi=80)
    plt.scatter(X2, Y2,c='magenta',s =500)
    plt.title('BHIM Quadrant',fontsize=25)
    plt.xlabel('NPS score',fontsize=25)
    plt.ylabel('Importnace',fontsize=25)
    plt.axhline(y = y_line, color = 'r', linestyle = '-')
    plt.axvline(x = x_line, color = 'r', linestyle = '-')
    plt.xticks([i for i in a2['Nps_score_cat']])
    plt.yticks([i for i in a2['Importance']])

    for i, label in enumerate(annotations):
        plt.annotate(label, (X2[i], Y2[i]),fontsize=25)
    plt.show()