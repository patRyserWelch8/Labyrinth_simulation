from time import perf_counter

from labyrinth_solver.load_labyrinth import get_png_files, load_png
from labyrinth_solver.solver import Solver


def test(filename: str) -> dict:
    maze = load_png(f"./test_inputs/{filename}")
    solver = Solver(maze)
    solver.parse()
    solution_exists = solver.solve
    return {
        "solution_exists": solution_exists,
        "solution": solver.solution,
    }


def main() -> dict:
    results = {}
    print("main")
    list_files = get_png_files("test_inputs")
    print(list_files)# Labyrinth/test_inputs
    for filename in list_files:  # indefinite loop
        print(filename)
        maze = load_png(f"./test_inputs/{filename}")

        start_parse = perf_counter()
        solver = Solver(maze)
        solver.parse()
        end_parse = perf_counter()
        parse_time = end_parse - start_parse

        start_solve = perf_counter()
        solution_exists = solver.solve
        end_solve = perf_counter()
        solve_time = end_solve - start_solve

        results[filename] = {
            "parse_time": parse_time,
            "solve_time": solve_time,
            "solution_exists": solution_exists,
            "solution": solver.solution,
        }

        print(results)
    return results


if __name__ == "__main__":

    main()
#print("tester ")
#    print(test("labyrinth-0-E1.png"))
#    print("-----")
#    for x in  range(63):
#        print(x)
#        print(test("labyrinth-1.png"))

