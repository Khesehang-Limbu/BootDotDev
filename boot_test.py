from main import *
from itertools import zip_longest

run_cases = [
    (
        1,
        16,
        [
            1,
            2,
            "fizz",
            4,
            "buzz",
            "fizz",
            7,
            8,
            "fizz",
            "buzz",
            11,
            "fizz",
            13,
            14,
            "fizzbuzz",
        ],
    ),
    (
        5,
        31,
        [
            "buzz",
            "fizz",
            7,
            8,
            "fizz",
            "buzz",
            11,
            "fizz",
            13,
            14,
            "fizzbuzz",
            16,
            17,
            "fizz",
            19,
            "buzz",
            "fizz",
            22,
            23,
            "fizz",
            "buzz",
            26,
            "fizz",
            28,
            29,
            "fizzbuzz",
        ],
    ),
]

submit_cases = run_cases + [
    (0, 0, []),
    (
        1,
        100,
        [
            1,
            2,
            "fizz",
            4,
            "buzz",
            "fizz",
            7,
            8,
            "fizz",
            "buzz",
            11,
            "fizz",
            13,
            14,
            "fizzbuzz",
            16,
            17,
            "fizz",
            19,
            "buzz",
            "fizz",
            22,
            23,
            "fizz",
            "buzz",
            26,
            "fizz",
            28,
            29,
            "fizzbuzz",
            31,
            32,
            "fizz",
            34,
            "buzz",
            "fizz",
            37,
            38,
            "fizz",
            "buzz",
            41,
            "fizz",
            43,
            44,
            "fizzbuzz",
            46,
            47,
            "fizz",
            49,
            "buzz",
            "fizz",
            52,
            53,
            "fizz",
            "buzz",
            56,
            "fizz",
            58,
            59,
            "fizzbuzz",
            61,
            62,
            "fizz",
            64,
            "buzz",
            "fizz",
            67,
            68,
            "fizz",
            "buzz",
            71,
            "fizz",
            73,
            74,
            "fizzbuzz",
            76,
            77,
            "fizz",
            79,
            "buzz",
            "fizz",
            82,
            83,
            "fizz",
            "buzz",
            86,
            "fizz",
            88,
            89,
            "fizzbuzz",
            91,
            92,
            "fizz",
            94,
            "buzz",
            "fizz",
            97,
            98,
            "fizz",
        ],
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Start: {input1}")
    print(f"  End: {input2}")
    result = fizzbuzz(input1, input2)
    for expected, actual in zip_longest(expected_output, result, fillvalue=""):
        print(f"Expected: {expected}")
        print(f"  Actual: {actual}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    if len(result) != len(expected_output):
        print(f"Expected Output Length: {len(expected_output)}")
        print(f"  Actual Output Length: {len(result)}")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
