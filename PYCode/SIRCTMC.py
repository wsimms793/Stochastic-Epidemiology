N = 100
beta = 1.0
gamma = 0.25
I0 = 1
n_events = 5000
S, I, R = N - I0, I0, 0
S_traj = np.zeros(n_events, dtype=int)
I_traj = np.zeros(n_events, dtype=int)
R_traj = np.zeros(n_events, dtype=int)
times  = np.zeros(n_events)
S_traj[0], I_traj[0], R_traj[0] = S, I, R
for step in range(1, n_events):
    Pinf = beta * S * I / N
    Prec = gamma * I
    total = Pinf + Prec
    if total == 0:
        S_traj[step:] = S
        I_traj[step:] = I
        R_traj[step:] = R
        times[step:]  = times[step - 1]
        break
    times[step] = times[step - 1] + (-np.log(np.random.rand()) / total)
    if np.random.rand() < Pinf / total:
        S -= 1
        I += 1
    else:
        I -= 1
        R += 1
    S_traj[step] = S
    I_traj[step] = I
    R_traj[step] = R
plt.figure(figsize=(10, 6))
plt.plot(times, S_traj, label='S(t)')
plt.plot(times, I_traj, label='I(t)')
plt.plot(times, R_traj, label='R(t)')
plt.xlabel('Time t')
plt.ylabel('Population')
plt.legend()
plt.show()
