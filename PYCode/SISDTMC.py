#Stochastic SIS
N = 100
dt = 0.01
beta = 1
gamma = 0.25
b = 0.25

def buildtransition(N, dt, beta, gamma, b):
    P = np.zeros((N+1, N+1))
    for i in range(N+1):
        Pplus  = beta * i * (N - i) * dt / N
        Pminus = (b + gamma) * i * dt
        if i == 0:
            P[i, i] = 1                      
        elif i == N:
            P[i, i-1] = Pminus
            P[i, i]   = 1 - Pminus
        else:
            P[i, i+1] = Pplus
            P[i, i-1] = Pminus
            P[i, i]   = 1 - Pplus - Pminus
    return P

P = buildtransition(N, dt, beta, gamma, b)

n_steps = 5000
I_traj = np.zeros(n_steps, dtype=int)
I_traj[0] = 1                                  

states = np.arange(N + 1)
for step in range(n_steps - 1):
    current = I_traj[step]
    I_traj[step + 1] = np.random.choice(states, p=P[current])

times = np.arange(n_steps) * dt
S_traj = N - I_traj                            

plt.plot(times, S_traj, label='S(t)')
plt.plot(times, I_traj, label='I(t)')
plt.xlabel('Time t')
plt.ylabel('Population')
plt.legend()
plt.show()
