import os
import matplotlib.pyplot as plt

try:
    import seaborn as sns
except ImportError:
    sns = None


def set_plot_style():

    if sns:
        sns.set_theme(style="whitegrid")
    else:
        plt.style.use("seaborn-v0_8-whitegrid")

    os.makedirs("images", exist_ok=True)


# ---------------- Histogram ----------------

def plot_distribution(df):

    plt.figure(figsize=(12,6))

    sns.histplot(
        data=df,
        x="Global_active_power",
        bins=50,
        kde=True,
        edgecolor="black"
    )

    plt.tight_layout()
    plt.savefig("images/global_active_power_distribution.png",dpi=300)
    plt.close()


# ---------------- Daily ----------------

def plot_daily(df):

    daily=df["Global_active_power"].resample("D").sum()

    plt.figure(figsize=(15,6))

    plt.plot(daily)

    plt.title("Daily Global Active Power Consumption")

    plt.tight_layout()

    plt.savefig("images/daily_global_active_power.png",dpi=300)

    plt.close()


# ---------------- Monthly ----------------

def plot_monthly(df):

    monthly=df["Global_active_power"].resample("ME").sum()

    plt.figure(figsize=(15,6))

    plt.plot(monthly,marker="o")

    plt.title("Monthly Global Active Power Consumption")

    plt.tight_layout()

    plt.savefig("images/monthly_global_active_power.png",dpi=300)

    plt.close()


# ---------------- Correlation ----------------

def plot_heatmap(df):

    plt.figure(figsize=(10,8))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.tight_layout()

    plt.savefig("images/correlation_heatmap.png",dpi=300)

    plt.close()


# ---------------- Boxplot ----------------

def plot_boxplot(df):

    plt.figure(figsize=(14,7))

    sns.boxplot(data=df.select_dtypes(include="number"))

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("images/boxplot_numeric_columns.png",dpi=300)

    plt.close()


# ---------------- Voltage Distribution ----------------

def plot_voltage_distribution(df):

    plt.figure(figsize=(12,6))

    sns.histplot(df["Voltage"],bins=40,kde=True)

    plt.tight_layout()

    plt.savefig("images/voltage_distribution.png",dpi=300)

    plt.close()


# ---------------- Hourly Consumption ----------------

def plot_hourly(df):

    hourly=df.groupby(df.index.hour)["Global_active_power"].mean()

    plt.figure(figsize=(12,6))

    plt.plot(hourly,marker="o")

    plt.xlabel("Hour")

    plt.ylabel("Average Power")

    plt.tight_layout()

    plt.savefig("images/hourly_consumption.png",dpi=300)

    plt.close()


# ---------------- Sub Metering ----------------

def plot_submetering(df):

    sub=df[
        [
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3"
        ]
    ].mean()

    plt.figure(figsize=(8,5))

    plt.bar(sub.index,sub.values)

    plt.tight_layout()

    plt.savefig("images/sub_metering_comparison.png",dpi=300)

    plt.close()


# ---------------- Scatter Power vs Voltage ----------------

def plot_power_voltage(df):

    sample=df.sample(5000,random_state=42)

    plt.figure(figsize=(8,6))

    plt.scatter(
        sample["Voltage"],
        sample["Global_active_power"],
        alpha=0.5
    )

    plt.xlabel("Voltage")

    plt.ylabel("Global Active Power")

    plt.tight_layout()

    plt.savefig("images/scatter_power_vs_voltage.png",dpi=300)

    plt.close()


# ---------------- Scatter Power vs Intensity ----------------

def plot_power_intensity(df):

    sample=df.sample(5000,random_state=42)

    plt.figure(figsize=(8,6))

    plt.scatter(
        sample["Global_intensity"],
        sample["Global_active_power"],
        alpha=0.5
    )

    plt.xlabel("Global Intensity")

    plt.ylabel("Global Active Power")

    plt.tight_layout()

    plt.savefig("images/scatter_power_vs_intensity.png",dpi=300)

    plt.close()



    