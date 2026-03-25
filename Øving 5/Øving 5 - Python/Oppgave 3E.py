import numpy as np

#Oppgave 3E
def simuler_testobservator(n=20, a=5, r0=12.5):
    data_gamma = np.random.gamma(shape=a, scale=1/r0, size=n)

    r_hat_gamma = a / np.mean(data_gamma)

    Z = (r_hat_gamma - r0) /  (r0 / np.sqrt(n * a))

    return Z

#Lager en funksjon for å estimere med flere m, og konfidensintervall
def estimer_alpha_og_konfidensintervall(M=100000):
    Z_values = [simuler_testobservator() for i in range(M)]

    z_alpha = 1.2816

    #Finner antallet som skal forkastes
    forkast = [z > z_alpha for z in Z_values]

    #Estimator for alpha
    alpha_hat = np.mean(forkast)

    se = np.sqrt(alpha_hat * (1-alpha_hat) / M)

    lower = (alpha_hat - 1.96 * se).round(4) #Nedre grense for intervallet
    upper  = (alpha_hat + 1.96 * se).round(4) #Og øvre

    return alpha_hat.round(4), (lower, upper)

alpha_hat, konfidensintervall = estimer_alpha_og_konfidensintervall(M=100000)

print("alpha_hat er lik: ", alpha_hat) #Output = 0.1259
print("Konfidensintervall: ", konfidensintervall) #Output: {min, max} = {0.1238, 0.128}





