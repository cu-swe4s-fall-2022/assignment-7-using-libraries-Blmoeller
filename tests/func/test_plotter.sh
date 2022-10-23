set -u
set -o pipefail
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_in_stdout python3 src/plotter.py
assert_in_stdout "This created 3 plots: iris_boxplot.png,
petal_length_v_width_scatter.png, and multi_panel_figure.png."

run test_stdout python3 src/plotter.py
assert_in_stdout "Finished making plots"

run test_stdout python3 src/plotter.py
assert_stdout 

echo 'Looking for image files'
[ -s src/iris_boxplot.png ] && echo "Found" || echo "Not found"
[ -s src/petal_length_v_width_scatter.png ] && echo "Found" || echo "Not found"
[ -s src/multi_panel_figure.png ] && echo "Found" || echo "Not found"

echo 'Looking for iris data file'
[ -s iris.data ] && echo "Found" || echo "Not found"
