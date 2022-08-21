# Python Tech Challenge

* The challenge is to create a program that computes some
  basic statistics on a collection of small positive integers. You
  can assume all values will be less than 1,000.
* Implement this challenge in whatever programming language
  best highlights your skills. Also, please supply a README with
  details on how to setup and run your application.

## Requirements

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.\
Here’s the program skeleton in Python to explain the structure:

```
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater
than 4)
```

## Conditions

* You cannot import a library that solves it instantly
* The methods add(), less(), greater(), and between() should have constant time O(1)
* The method build_stats() can be at most linear O(n)
* Apply the best practices you know
* Share a public repo with your project

## Solution

In order to meet the constraints of this challenge I'll trade off memory space to gain compute speed.

Points to consider:
* Since there are no constraints about memory space, using a list of 1000 elements representing each possible number is allowed.
* Each value will be the index of the list and the element in the list will be a counter of how many that value was added.
* The final step will be traverse the list in order and store the amount of number that are less and greater of each
  number using a data class.
* Finally, to get the amount of values less or greater than a given number the function will return the less or greater value of the data object located in the list using the given number as index.
* In order to return the result between two numbers, the function will return the total minus the sum of the lowest less and the highest greater values

## Setup

- Install Python 3.10 or a higher version.
- Clone this repo
- Go to the root folder.
- Create a virtual environment `python -m venv .env`.
- Activate the virtual environment.
- Install the requirements`pip install -r requirements.txt`.

## Usage

Run the command: `python main.py`

## Testing

Run the command: `mypy . && python -m unittest tests.py` 





