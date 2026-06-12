class RK:
    def __init__(self, f, t0, tf, N, alpha):
        self.f = f
        self.t0 = t0
        self.tf = tf
        self.N = N
        self.alpha = alpha

    def solve(self):
        h = (self.tf - self.t0) / self.N
        t = self.t0
        w = self.alpha

        results = [(t,w)]
        for i in range(self.N):
                k1 = self.f(t,w)
                k2 = self.f( (t + (h/2)), w + (k1/2)*h )
                k3 = self.f( (t + (h/2)), w + (k2/2)*h )
                k4 = self.f( (t+h), w + k3*h)
                w += (h/6) * (k1 + 2*k2 + 2*k3 + k4)
                t += h
                results.append((t,w))
                
        return results