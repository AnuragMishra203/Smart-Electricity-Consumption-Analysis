from data_loader import load_data
from eda import *
from visualization import *

FILE_PATH = "E:\DATA ANALYSIS\smart_electric_consumption_analysis\data\cleaned_household_power_consumption.csv"


def main():

    df = load_data(FILE_PATH)

    
    dataset_summary(df)

    missing_values(df)

    duplicate_rows(df)

    correlation_matrix(df)



    set_plot_style()

    plot_distribution(df)

    plot_daily(df)

    plot_monthly(df)

    plot_heatmap(df)

    plot_boxplot(df)

    plot_voltage_distribution(df)

    plot_hourly(df)

    plot_submetering(df)

    plot_power_voltage(df)

    plot_power_intensity(df)

    print("All visualizations generated successfully!")


if __name__ == "__main__":
    main()

print(dataset_summary())