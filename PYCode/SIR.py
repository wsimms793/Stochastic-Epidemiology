#Dynamic SIR model

def sir(t, y, beta, gamma, N):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

beta, gamma, N = 5, 0, 1000
S0, I0, R0 = N - 1, 1, 0

t = np.linspace(0, 120, 500)
sol = solve_ivp(sir, (0, 120), [S0, I0, R0], args=(beta, gamma, N), t_eval=t)
S, I, R = sol.y
 

plt.figure(figsize=(10, 6))
plt.plot(t, S, label='S(t)')
plt.plot(t, I, label='I(t)')
plt.plot(t, R, label='R(t)')
plt.xlabel('Time t')
plt.ylabel('Population')
plt.legend()
