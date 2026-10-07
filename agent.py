import argparse
import subprocess
from datetime import datetime
from pathlib import Path


PROJECT_DIR = Path("target_project")
LOG_DIR = Path("logs")


def run_tests():
    LOG_DIR.mkdir(exist_ok=True)

    print("\nRunning project tests...\n")

    result = subprocess.run(
        ["python3", "-m", "pytest", "-q", str(PROJECT_DIR)],
        capture_output=True,
        text=True
    )

    output = result.stdout + result.stderr
    print(output)

    log_file = LOG_DIR / "test_run.log"

    with open(log_file, "a") as file:
        file.write("\n" + "=" * 60 + "\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write(output)

    if result.returncode == 0:
        print("SUCCESS: All tests passed.")
    else:
        print("FAILED: Some tests need attention.")

    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="AI Coding Agent - Execute and Observe"
    )

    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the target project's tests"
    )

    args = parser.parse_args()

    if args.test:
        run_tests()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
