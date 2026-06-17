from src.core.rk4 import RK4
from src.problems.example_2 import f

def print_results(results):
    for i, (t, w) in enumerate(results):
        print(f"t = {t:.2f} | w{i} = {w:.6f}")


if __name__ == "__main__":
    solver = RK4(f, 0, 1, 15, 0.5)
    results = solver.solve()

    print_results(results)