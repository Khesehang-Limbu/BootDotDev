from main import *


run_cases = [
    (
        {"Hawkman": "The Winged Warrior"},
        [
            ("Boots", "The Lover of Salmon"),
            ("Superman", "The Big Blue Boyscout"),
            ("Batman", "The Caped Crusader"),
            ("Woman Wonder", ""),
        ],
    ),
]


submit_cases = run_cases + [
    (
        {"Hawkgirl": "Fierce Thanagarian"},
        [
            ("Green Lantern", "The Man Without Fear"),
            ("AquaMan", "Dweller in the Depths"),
            ("The Flash", "The Crimson Comet"),
            ("The Martian Manhunter", "Mars' Sole Survivor"),
            ("Cyborg", "Tech Titan"),
        ],
    ),
]


def test(input_clipboard, input_list):
    print("---------------------------------")
    copy_to_clipboard, paste_from_clipboard = new_clipboard(input_clipboard)
    failed_count = 0
    passed_count = 0
    for item in input_list:
        print("Copying to Clipboard:")
        print(f"*   Key: {item[0]}")
        print(f"* Value: {item[1]}")
        copy_to_clipboard(*item)

        print("Pasting From Clipboard:")
        print(f"*      Key: {item[0]}")
        result = paste_from_clipboard(item[0])
        expected_output = item[1]
        print(f"* Expected: '{expected_output}'")
        print(f"*   Actual: '{result}'")
        if item[0] in input_clipboard:
            print("Fail: modified original input dictionary")
            failed_count += 1
        if result != expected_output:
            print("Fail")
            failed_count += 1
        else:
            print("Pass")
            passed_count += 1
        print("---------------------------------")

    # check pasting missing key
    missing_key = "Joker"
    print("Pasting:")
    print(f"* Key: {missing_key}")
    result = paste_from_clipboard(missing_key)
    expected_output = ""
    print(f"* Expected: '{expected_output}'")
    print(f"*   Actual: '{result}'")
    if result != expected_output:
        print("Fail: missing key should return an empty string")
        failed_count += 1
    else:
        print("Pass")
        passed_count += 1

    return passed_count, failed_count


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        passed_count, failed_count = test(*test_case)
        passed += passed_count
        failed += failed_count

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
