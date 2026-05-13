#CTMC SIS.
N = 100
beta = 1
gamma = 0.25
b = 0.25
def buildrates(i, N, beta, gamma, b):
    Pplus  = beta * i * (N - i) / N
    Pminus = (b + gamma) * i
    return Pplus, Pminus
n_events = 5000
I_traj = np.zeros(n_events, dtype=int)
times  = np.zeros(n_events)
I_traj[0] = 1
for step in range(n_events - 1):
    current = I_traj[step]
    Pplus, Pminus = buildrates(current, N, beta, gamma, b)
    total = Pplus + Pminus
    if total == 0:
        I_traj[step + 1:] = current
        times[step + 1:]  = times[step]
        break
    times[step + 1] = times[step] + (-np.log(np.random.rand()) / total)
    if np.random.rand() < Pplus / total:
        I_traj[step + 1] = current + 1
    else:
        I_traj[step + 1] = current - 1
S_traj = N - I_traj
plt.plot(times, S_traj, label='S(t)')
plt.plot(times, I_traj, label='I(t)')
plt.xlabel('Time t')
plt.ylabel('Population')
plt.legend()
plt.show()
