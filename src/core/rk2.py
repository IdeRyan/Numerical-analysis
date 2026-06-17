class RK2:
    def __init__(self, f, t0, tf, N, y0):
        self.f = f
        self.t0 = t0
        self.tf = tf
        self.N = N
        self.y0 = y0

    def solve(self):
        h = (self.tf - self.t0) / self.N
        t = self.t0
        w = self.y0

        results = [(t,w)]
        for i in range(self.N):
                k1 = self.f(t,w)
                k2 = self.f( (t + h), w + h*k1 )
                w += (h/2) * (k1 + k2)
                t += h
                results.append((t,w))
                
        return results