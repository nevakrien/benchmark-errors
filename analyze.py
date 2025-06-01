import sys
import numpy as np
from scipy import stats

# ANSI color codes
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

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
    print(f"{BOLD}{name} result:{RESET} {results[0]}")
    print(f"{BOLD}{name} timings:{RESET}")
    print("  Mean:   ", np.mean(times))
    print("  Stddev: ", np.std(times))
    print("  Min:    ", np.min(times))
    print("  Max:    ", np.max(times))
    print()

def null_hypothesis_test(slow_times, fast_times):
    assert len(slow_times) == len(fast_times), "Sample sizes must match for paired test"

    print(f"{BOLD}Null Hypothesis Test (paired two-tailed t-test):{RESET}")
    t_stat, p_value = stats.ttest_rel(slow_times, fast_times)

    print(f"  t-statistic: {t_stat:.4f}")
    print(f"  p-value:     {p_value:.6f}")

    if p_value < 0.05:
        direction = np.mean(slow_times) - np.mean(fast_times)
        if direction > 0:
            print(f"{GREEN}  Result: Reject the null hypothesis.")
            print(f"          The 'fast' code is faster in a statistically significant way.{RESET}")
        else:
            print(f"{RED}  Result: Reject the null hypothesis.")
            print(f"          The 'slow' code is faster in a statistically significant way (unexpected).{RESET}")
    else:
        print(f"{YELLOW}  Result: Fail to reject the null hypothesis.")
        print(f"          No statistically significant difference between the two versions.{RESET}")
    print()

def main():
    if len(sys.argv) != 3:
        print(f"{RED}Usage: python3 analyze.py slow.txt fast.txt{RESET}")
        sys.exit(1)

    slow_results, slow_times = parse_file(sys.argv[1])
    fast_results, fast_times = parse_file(sys.argv[2])

    print(f"\n{BOLD}{CYAN}================ ANALYSIS RESULTS ================\n{RESET}")

    report_stats("Slow", slow_results, slow_times)
    report_stats("Fast", fast_results, fast_times)

    speedups = slow_times / fast_times
    print(f"{BOLD}Speedup stats:{RESET}")
    print("  Mean speedup: ", np.mean(speedups))
    print("  Speedup std:  ", np.std(speedups))
    print()

    null_hypothesis_test(slow_times, fast_times)

if __name__ == "__main__":
    main()
