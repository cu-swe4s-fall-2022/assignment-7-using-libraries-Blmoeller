# libraries
> This repo demonstrates the use of libraries for data processing and plotting
> use cases
### Table of Contents

- [libraries](#libraries)
    - [Table of Contents](#table-of-contents)
    - [Environment Setup](#environment-setup)
    - [Installation / Setup](#installation--setup)
    - [Example](#example)
    - [Example for running functional and unit test](#example-for-running-functional-and-unit-test)
    - [Change log](#change-log)



### Environment Setup
- Environment setup for this project below. This is assuming conda is already
  installed.
    ```
    conda env create -f environment.yaml
    ```

### Installation / Setup
- Clone this repository and cd into it
    ```
    git@github.com:cu-swe4s-fall-2022/assignment-7-using-libraries-Blmoeller.git
    ```
    ```
    cd assignment-7-using-libraries-Blmoeller
    ```

### Example
- Once everything is setup in the repository, the following line can be ran
  from the home directory in the repo (assignment-7-using-libraries-Blmoeller)

- The output in the terminal will look like the following

<details>
  <summary>Terminal Output</summary>
  <br>

```
This created 3 plots: iris_boxplot.png, petal_length_v_width_scatter.png, and multi_panel_figure.png.

```
- These files will be placed in the output_data folder and will not appear as
  a popup window or in the terminal. However, the output will look something
  like this.
<center><img src="/output_data/iris_boxplot.png" width="100%"/></center>
<center><img src="/output_data/petal_width_v_length_scatter.png" width="100%"/></center>
<center><img src="/output_data/multi_panel_figure.png" width="100%"/></center>

</details>

### Example for running functional and unit test 
- To run all of the new function and unit test simply paste this line in your
  terminal from the home directory for the repo (assignment-7-using-libraries
  -Blmoeller)
- For the Functional test paste this line
```
bash tests/func/test_plotter.sh
```
- The output of functional test should look like the below block of text.

<details>
  <summary> Terminal Output</summary>
  <br>

```
test_in_stdout ran in 2 sec with 0/1 lines to STDERR/OUT
 PASS STDOUT CONTAINS "This created 3 plots: iris_boxplot.png, petal_length_v_width_scatter.png, and multi_panel_figure.png." (LINE 7)

test_stdout ran in 2 sec with 0/1 lines to STDERR/OUT
 PASS STDOUT CONTAINS "This created 3 plots: iris_boxplot.png, petal_length_v_width_scatter.png, and multi_panel_figure.png." (LINE 10)

test_stdout ran in 2 sec with 0/1 lines to STDERR/OUT
 PASS NON-EMPTY STDOUT (LINE 13)
Looking for image files
Found
Found
Found
Looking for iris data file
Found

sshtest v0.1.5

3         Tests
0         Failures
3         Successes

```

</details>

- For the unit test paste this line

```
python -m unittest tests/unit/test_data_processor.py
```

- The output of unit test should look like the below block of text.

<details>
  <summary> Terminal Output</summary>
  <br>

```
......
----------------------------------------------------------------------
Ran 6 tests in 0.022s

OK
```
</details>

### Change log
- v1.0
  - This version contains all the functionality specified the homework prompt.
