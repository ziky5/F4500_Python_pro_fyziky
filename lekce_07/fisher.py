import pandas
import scipy.optimize

def graphinit():
    import matplotlib.pyplot as plt

    fontsize=25
    plt.rcParams['figure.autolayout'] = False
    plt.rcParams['figure.figsize'] = 12, 7
    plt.rcParams['axes.labelsize'] = 25
    plt.rcParams['axes.titlesize'] = 25
    plt.rcParams['font.size'] = 25
    plt.rcParams['lines.linewidth'] = 2.0
    plt.rcParams['lines.markersize'] = 12
    plt.rcParams['legend.fontsize'] = 25

class Fisher:
    
    def __init__(self,filename):
        data = pandas.read_csv(filename)
        
        # vztah C = A * B
        self.T = data['T']
        self.C = data['A'] * data['B']
    
    def f(self,x,C0,C1):
          return C0 * x + C1  
    
    def fit(self):
        self.popt, self.pcov = scipy.optimize.curve_fit(self.f, self.T, self.C)
        print(self.popt)

class FisherGraph(Fisher):
    def __init__(self,filename):
        
        # initializace Fishera
        Fisher.__init__(self,filename)

    def graph(self,xlim,xlabel,ylabel,title):

        y = self.f(self.T, self.popt[0], self.popt[1]) # y = C0 * x + C1        
        plt.clf()
        plt.cla()
        plt.plot(self.T, self.C, 'o', label='data')
        plt.plot(self.T, y, label=r'$y = C_0 \, x + C_1$')
        plt.legend(loc='best')
        plt.xlim(xlim)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)

import sys

if __name__=="__main__":
    ff=FisherGraph(sys.argv[1])
    print(ff.fit())