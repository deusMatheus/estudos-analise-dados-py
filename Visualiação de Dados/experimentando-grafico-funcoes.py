import matplotlib.pyplot as plt

def funcao_linear(a, b):
    y = []
    x = []
    for i in range(-100,100):
        x.append(i)
        y.append(a*i + b)
    return [x,y]

def funcao_quadratica(a,b,c):
    y = []
    x = []
    for i in range(-100,100):
        x.append(i)
        y.append(a*i**2 + b*i + c )
    return [x,y]

a = -17
b = 328
c = 1

func = funcao_quadratica(a, b, c)
#func = funcao_linear(a,b)

plt.plot(
    func[0],
    func[1]
)
plt.show()