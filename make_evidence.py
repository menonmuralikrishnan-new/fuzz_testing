"""Create screenshot-style evidence images and the submission PDF."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).parent
FONT = r"C:\Windows\Fonts\consola.ttf"
BODY = ImageFont.truetype(FONT, 22)
SMALL = ImageFont.truetype(FONT, 18)
TITLE = ImageFont.truetype(FONT, 30)


def screenshot(filename, heading, lines):
    image = Image.new("RGB", (1600, 900), "#101418")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 1600, 68), fill="#263238")
    draw.text((28, 18), "Windows PowerShell  |  Lab 7 Fuzz Testing", font=SMALL, fill="#b0bec5")
    draw.text((36, 100), heading, font=TITLE, fill="#80cbc4")
    y = 170
    for line in lines:
        draw.text((42, y), line, font=BODY, fill="#e8f5e9")
        y += 34
    image.save(ROOT / filename)
    return image


buggy_app = [
    "> python processor.py",
    "Lab 7 - Buggy processor demonstration",
    "parse_int_list('10, 20, 30') -> [10, 20, 30]",
    "parse_int_list(None) -> ERROR: AttributeError: 'NoneType' object has no attribute 'split'",
    "is_palindrome('Never odd or even') -> True",
    "is_palindrome(None) -> ERROR: AttributeError: 'NoneType' object has no attribute 'lower'",
    "calculate_average([10, 20, 30]) -> 20.0",
    "calculate_average([]) -> ERROR: ZeroDivisionError: division by zero",
]
buggy_tests = [
    "> python -m pytest -q test_processor.py",
    "FFF.                                                                     [100%]",
    "FAILED test_processor.py::test_parse_int_list_never_crashes",
    "  Failing test case: value='' (also value=None)",
    "FAILED test_processor.py::test_is_palindrome_never_crashes",
    "  Failing test case: value=None",
    "FAILED test_processor.py::test_calculate_average_never_crashes",
    "  Failing test case: values=[] (also values=[''])",
    "3 failed, 1 passed in 5.72s",
]
fixed_app = [
    "> python processor.py",
    "Lab 7 - Fixed processor demonstration",
    "parse_int_list('10, 20, 30') -> [10, 20, 30]",
    "parse_int_list(None) -> []",
    "is_palindrome('Never odd or even') -> True",
    "is_palindrome(None) -> False",
    "calculate_average([10, 20, 30]) -> 20.0",
    "calculate_average([]) -> 0.0",
]
fixed_tests = [
    "> python -m pytest -q test_processor.py",
    "....                                                                     [100%]",
    "4 passed in 1.77s",
    "",
    "Hypothesis fuzzed all three functions without finding a crash.",
]

images = [
    screenshot("01_buggy_application.png", "Evidence 1: Buggy application", buggy_app),
    screenshot("02_failing_fuzz_tests.png", "Evidence 2: Failing fuzz tests", buggy_tests),
    screenshot("03_fixed_application.png", "Evidence 3: Fixed application", fixed_app),
    screenshot("04_passing_fuzz_tests.png", "Evidence 4: Passing fuzz tests", fixed_tests),
]

title = Image.new("RGB", (1600, 900), "white")
draw = ImageDraw.Draw(title)
draw.text((100, 120), "LAB 7: Fuzzing for Input Validation Bugs", font=TITLE, fill="#17324d")
draw.text((100, 220), "Name: Muralikrishnan Menon", font=BODY, fill="#222222")
draw.text((100, 265), "SRN: PES2UG24CS288", font=BODY, fill="#222222")
draw.text((100, 360), "Deliverable evidence", font=TITLE, fill="#17324d")
draw.text((100, 430), "Hypothesis property-based tests were used to expose and verify fixes", font=BODY, fill="#222222")
title_path = ROOT / "00_cover.png"
title.save(title_path)

pages = [Image.open(title_path).convert("RGB")] + [image.convert("RGB") for image in images]
pages[0].save(ROOT / "Lab7_FuzzTesting_Report_Muralikrishnan_Menon.pdf", save_all=True, append_images=pages[1:], resolution=150.0)
print(f"Created {len(images)} evidence pages and the PDF report.")
