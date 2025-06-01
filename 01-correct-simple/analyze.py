import sys
import numpy as np

def parse_file(filename):
    results = []
    times = []
    with open(filename) as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            result_line = lines[i].strip()
            time_line = lines[i + 1].strip()
            if result_line.startswith("result:") and time_line:
                result = int(result_line.split(":")[1])
                t = float(time_line)
                results.append(result)
                times.append(t)
    return np.array(results), np.array(times)

def report_stats(name, results, times):
    assert np.all(results == results[0]), f"{name} produced inconsistent results: {results}"
    print(f"{name} result: {results[0]}")
    print(f"{name} timings:")
    print("  Mean:   ", np.mean(times))
    print("  Stddev: ", np.std(times))
    print("  Min:    ", np.min(times))
    print("  Max:    ", np.max(times))
    print()

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 analyze.py slow.txt fast.txt")
        sys.exit(1)

    slow_results, slow_times = parse_file(sys.argv[1])
    fast_results, fast_times = parse_file(sys.argv[2])

    report_stats("Slow", slow_results, slow_times)
    report_stats("Fast", fast_results, fast_times)

    speedups = slow_times / fast_times
    print("Speedup stats:")
    print("  Mean speedup: ", np.mean(speedups))
    print("  Speedup std:  ", np.std(speedups))
    print()

if __name__ == "__main__":
    main()
