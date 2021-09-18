import argparse
import random
from typing import List


def run_monty_hall(n: int, swap: bool) -> List[bool]:
    res = []
    doors = [1, 0, 0]
    for _ in range(n):
        random.shuffle(doors)
        result = doors[-1]
        if swap:
            result = doors[1] if not doors[0] else doors[0]
        res.append(result)
    return res


def main() -> None:
    parser = argparse.ArgumentParser(description='Monty Hall problem.')
    parser.add_argument('--iter', '-n', type=int, default=100,
                        help='number of times to run the Monty Hall problem')
    parser.add_argument("--no-switch", action='store_true',
                        help='do not switch when given the chance')

    args = parser.parse_args()
    results = run_monty_hall(args.iter, not args.no_switch)
    print(f"Won {sum(results)} out of {len(results)} times ({sum(results) / len(results)})")


if __name__ == "__main__":
    main()
