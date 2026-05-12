#Dynamical SIS

t = sp.symbols('t', positive=True)
S = sp.Function('S')(t)
I = sp.Function('I')(t)
beta  = sp.symbols('beta',  positive=True)
gamma = sp.symbols('gamma', positive=True)
b     = sp.symbols('b',     positive=True)
N     = sp.symbols('N',     positive=True)
I0    = sp.symbols('I0',    positive=True)
 
eq1 = sp.Eq(S.diff(t), -(beta*S*(N - S)/N) + (b + gamma)*(N - S))
eq2 = sp.Eq(I.diff(t),  (beta*(N - I)*I/N) - (b + gamma)*I)
r = beta - (b + gamma)
K = N * (1 - (b + gamma)/beta)
 
I_t = K / (1 + ((K - I0)/I0) * sp.exp(-r*t))
S_t = N - I_t
 
beta_v, gamma_v, b_v, N_v, I0_v = 0.2, 0.1, 0.02, 1000, 1
 
f_I = sp.lambdify((t, beta, gamma, b, N, I0), I_t, 'numpy')
f_S = sp.lambdify((t, beta, gamma, b, N, I0), S_t, 'numpy')
 
ts = np.linspace(0, 600, 600)
I_vals = f_I(ts, beta_v, gamma_v, b_v, N_v, I0_v)
S_vals = f_S(ts, beta_v, gamma_v, b_v, N_v, I0_v)
 
plt.figure(figsize=(10, 6))
plt.plot(ts, S_vals, label='S(t) - Susceptible', linewidth=2)
plt.plot(ts, I_vals, label='I(t) - Infected',    linewidth=2)
plt.xlabel('Time t')
plt.ylabel('Population')
plt.legend()
plt.show()
