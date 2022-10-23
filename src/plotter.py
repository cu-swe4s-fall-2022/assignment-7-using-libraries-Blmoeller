"""Plotting script to produce 3 png files that are populated from the iris.data
    file.
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


def main():
    """Plotting function that produces 3 png files that are populated from the
    iris.data file.
    """
    # Define inputs for the plotting function
    file_name = 'iris.data'
    colum_name = ['Sepal_Width', 'Sepal_Length', 'Petal_Width',
                  'Petal_Length', 'Species']
    iris = pd.read_csv(file_name, sep=',', header=None)
    iris.columns = colum_name
    measurement_name = ['Sepal_Width', 'Sepal_Length', 'Petal_Width',
                        'Petal_Length']
    # Plotting for boxplot
    f1 = plt.figure()
    plt.boxplot(iris[measurement_name], labels=measurement_name)
    plt.ylabel('cm')
    plt.savefig('output_data/iris_boxplot.png')
    # Plotting for scatter
    f2 = plt.figure()
    for species_name in set(iris['Species']):
        iris_subset = iris[iris['Species'] == species_name]
        plt.scatter(iris_subset['Sepal_Length'], iris_subset['Sepal_Width'],
                    label=species_name)
    plt.ylabel('Sepal_Width (cm)')
    plt.xlabel('Sepal_Length (cm)')
    plt.legend(loc='upper right')
    plt.savefig('output_data/petal_width_v_length_scatter.png')
    # Plotting for multi panel figure
    # Setting matplotlib parameters to remove plot lines
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.top'] = False
    fig, axes = plt.subplots(ncols=2, nrows=1, layout="constrained")
    fig.set_size_inches(10, 5)
    axes[0].boxplot(iris[measurement_name], labels=measurement_name)
    axes[0].set_ylabel('cm')
    for species_name in set(iris['Species']):
        iris_subset = iris[iris['Species'] == species_name]
        plt.scatter(iris_subset['Sepal_Length'], iris_subset['Sepal_Width'],
                    label=species_name)
    axes[1].set_ylabel('Sepal_Width (cm)')
    axes[1].set_xlabel('Sepal_Length (cm)')
    axes[1].legend(loc='upper right')
    plt.savefig('output_data/multi_panel_figure.png')

    print("This created 3 plots: iris_boxplot.png, "
          + "petal_length_v_width_scatter.png, and multi_panel_figure.png.")


if __name__ == '__main__':
    main()
