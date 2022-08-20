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
than a value, or within a range.
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

In order to meet the constraints of this challenge I'll trade off memory space to gain compute speed.\

Points to consider:
* Since there are few values (1000) it is sensible to think about using a list of 1000 elements.
* I'll use the value as index in the list.
* Repeated numbers should be allowed,so I will store how many times a number is repeated in the list.
* The final step will be traverse the list in order and store the amount of number that are less and greater of each
  number in a model.
* Finally, to get to amount of values less or greater than a given number It will be mater of accessing the object and
  returning the desire value
* In order to return the result between two numbers, the function will return the total minus the abs from the less from
  one value minus the greater from the other

## Setup

- Install Python 3.10 or a higher version.
- Clone this repo
- Go to the root folder.
- Create a virtual environment.
- Activate the virtual environment.
- Install the requirements in the `requirements.txt` file.

## Usage

With the Setup steps done.\
Run the command: `python main.py`

## Testing

With the Setup steps done.\
Run the command: `mypy . & python -m unittest tests.py` 





