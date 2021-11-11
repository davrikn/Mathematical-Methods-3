import numpy as np

def fitExponential(t, y):
   n = len(t) #Antall dager/målinger
   A = np.zeros((n,2)) #Systemmatrise for inkonsistent system
   b = np.zeros((n,1)) #Systemets venstre side

   A[:,0] = [1 for i in range(n)]
   A[:,1] = [i for i in t] #Fullfør
   b = [np.log(i) for i in y]  #Fullfør
   ATA = A.T@A #Fullfør - Matrise på venstreside i normalligningen for minste kvadraters metode
   ATb = A.T@b #Fullfør - Høyreside i normalligningen for minste kvadraters metode
   params = np.linalg.solve(ATA,ATb) #Fullfør - Parametere fra løsning av normalligning

   c1 = np.exp(params[0]) #Fullfør - Parameter 1 i eksponentiell modall
   c2 = params[1] #Fullfør - Parameter 2 i eksponentiell modell
   return c1, c2


konsentrasjon = np.array([1000.0, 1095.57, 1255.88, 1439.49, 1559.16,
1719.35, 1817.89, 1923.63, 2204.12, 2541.18,
2699.56, 3056.82, 3409.18, 3743.08]) #Målt algekonsentrasjon

t = np.linspace(0,13,14) #Dager vi målte algekonsentrasjon
c1, c2 = fitExponential(t,konsentrasjon)

