# Solutions to [Leetcode](http://leetcode.com/) problems in Python3

## Requirements
* Python3
* Pytest

## Repo structure and naming
`src/`: Source modules.

`tests/`: Unit tests.

Each source module is the solution to one question. Source modules are named according to the problem numbers in Leetcode followed by a short description of the problem.

Each source module has its own test file. Test file names follow Python test discovery convention: `test_p{xxxx}.py`

## Run unit tests
To run all tests, in the repo root run:

```
pytest
```

To run a specific test file such as `test_p0547.py`:

```
pytest tests/test_p0547.py
```
