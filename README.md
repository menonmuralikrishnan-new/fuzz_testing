# Lab 7 — Fuzzing for Input Validation Bugs

Student: **Muralikrishnan Menon**  
SRN: **PES2UG24CS288**

## Deliverables

- `processor.py` — fixed application script.
- `test_processor.py` — Hypothesis fuzz tests for all three functions.
- `Lab7_FuzzTesting_Report_Muralikrishnan_Menon.pdf` — evidence of the buggy run, failing fuzz tests, fixed run, and passing fuzz tests.

## Verification

```text
python processor.py
python -m pytest -q test_processor.py
....                                                                     [100%]
4 passed in 1.77s
```

The fixed implementation handles non-string values, empty tokens, malformed integer tokens, empty collections, and mixed-type collections without raising unexpected exceptions.
