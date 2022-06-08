import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

a = -1
b = 0.05
x = np.linspace(a, b, num=1000)
y = (x**3) - (0.165 * (x**2)) + 0.0003993

plt.figure(dpi=400, figsize=(8, 6))
plt.title("Valores de f(x) = x³ - 0.165x² + 3993x10^-4 no intervalo [-1,0]")
plt.hlines(0, -2, 2)
plt.plot(x, y, 'b')
plt.scatter(0, 0, c="red")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.savefig('valores.png', dpi=400)
plt.show()

a_alg = a
b_alg = b
FTOL = 1e-15

p = (a_alg + b_alg) / 2
fp = (p**3) - (0.165 * (p**2)) + 0.0003993
qtd_itr = 1
ps_encontrados = [p]
table = np.array([qtd_itr, a, b, p, np.abs(p), fp])

while np.abs(fp) > FTOL:
    if ((a_alg**3) - (0.165 * (a_alg**2)) + 0.0003993) * fp < 0:
        b_alg = p
    else:
        a_alg = p

    qtd_itr = qtd_itr + 1
    p = (a_alg + b_alg) / 2
    ps_encontrados.append(p)
    fp = (p**3) - (0.165 * (p**2)) + 0.0003993
    table = np.vstack([table, [qtd_itr, a_alg, b_alg, p, np.abs(p), fp]])

print("Quantidade de interação até convergir:", qtd_itr)
print("Erro de aproximação da função:", np.abs(fp))
print("Erro do x:", np.abs(p)*100)
print("Resultado encontrado:", p)
print("Resultado esperado:", -0.044)

plt.figure(dpi=400, figsize=(8, 6))
plt.title("Erro ao longo da iterações")
plt.plot(np.arange(qtd_itr), np.abs(np.array(ps_encontrados)))
plt.hlines(y=0, xmin=0, xmax=qtd_itr - 1, alpha=0.5)
plt.xlabel("Iterações")
plt.ylabel("Erro absoluto de x")
plt.savefig('erro.png', dpi=400)
plt.show()


plt.figure(dpi=400, figsize=(8, 6))
column_labels = ["Iteração", "Xinf", "Xsup", "Xm", "| |%", "f(Xm)"]
plt.axis('tight')
plt.axis('off')
plt.table(cellText=table, colLabels=column_labels, loc="center")
plt.savefig('tabela.png', dpi=400)
plt.show()