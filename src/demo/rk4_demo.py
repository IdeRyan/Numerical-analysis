from src.core.runge_kutta import RK
from src.problems.example_1 import f

def print_results(results):
    for i, (t, w) in enumerate(results):
        print(f"t = {t:.2f} | w{i} = {w:.6f}")


if __name__ == "__main__":
    solver = RK(f, 0, 2, 10, 0.5)
    results = solver.solve()

    print_results(results)