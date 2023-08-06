# How to run unit test
Need to install berfore run unit test:
  - pytest (pip install pytest)
  - pytest-cov (pip install pytest-cov)

Command to run unit test:
  - pytest (Output only pass or failed testing)
  - pytest --cov-report term --cov=kueri tests/  (Give percentage coverage of unit testing)
  - pytest --cov-report term-missing --cov=kueri tests/ (Give line of code function that not covered in unit test)
