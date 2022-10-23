set -u
set -o pipefail
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_in_stdout python3 src/plotter.py
assert_in_stdout "This created 3 plots: iris_boxplot.png, petal_length_v_width_scatter.png, and multi_panel_figure.png."

run test_stdout python3 src/plotter.py
assert_in_stdout "This created 3 plots: iris_boxplot.png, petal_length_v_width_scatter.png, and multi_panel_figure.png."

run test_stdout python3 src/plotter.py
assert_stdout 

echo 'Looking for image files'
[ -s output_data/iris_boxplot.png ] && echo "Found" || echo "Not found"
[ -s output_data/petal_width_v_length_scatter.png ] && echo "Found" || echo "Not found"
[ -s output_data/multi_panel_figure.png ] && echo "Found" || echo "Not found"

echo 'Looking for iris data file'
[ -s iris.data ] && echo "Found" || echo "Not found"
