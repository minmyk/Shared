
class Sle:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector

    def seidel(self, e):
        A = self.matrix
        b = self.vector
        x = self.vector.copy()
        file = open('output.txt', 'w')
        for i in range(len(A)):
            b[i] = b[i] / A[i][i]
            x[i] = b[i]
        A = [[0 if i == j else -A[i][j]/A[i][i] for j in range(len(A))] for i in range(len(A))]
        vdif = x.copy()
        while norm(vdif) > e:
            vdif = x.copy()
            for i in range(len(x)):
                linex = 0
                for j in range(len(x)):
                    linex += x[j] * A[i][j]
                x[i] = linex + b[i]
                vdif[i] -= x[i]
            file.write("VECTOR OF RESIDUES: " + str(vdif) + "\n")
            file.write("NORM OF VECTOR OF RESIDUES: " + str(norm(vdif))+ "\n")
        file.write("VECTOR OF SOLUTIONS: " + str(x))
        file.close()


def getsle():
        file = open('inputSle.txt', 'r')
        ln = [list(map(float, line.split())) for line in file]
        vector = ln[0]
        ln.pop(0)
        return [ln, vector]


def norm(x):
    return pow(sum(x[i]*x[i] for i in range(len(x))) , 0.5)


sle = Sle(getsle()[0], getsle()[1])
sle.seidel(0.00001)