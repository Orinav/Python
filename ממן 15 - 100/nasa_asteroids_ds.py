"""
Title - Maman 15
Author - Ori Nave
Date - 20/02/25
Description - This file will include functions that will implement the answers to Maman 15
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def load_data(file_name):
    """
    Description:
    The function will load data from a .csv file into a pandas DataFrame object.

    Parameters:
    file_name - a String.

    Output:
    The function will return a pandas DataFrame object that contains the data of the .csv file.
    """
    if type(file_name) != str:
        raise TypeError("file_name must be a string")

    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        print("FileNotFoundError: The file doesn't exist")
    except OSError:
        print("OSError: Invalid file name")
    except Exception as error:
        print(f"{error}")


def mask_data(df):
    """
    Description:
    The function will filter the DataFrame by removing every row that the year of the "Close Approach Date" column is less than 2000.

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will return an updated Pandas DataFrame object with only the rows that its year of the "Close Approach Date" column are 2000 above.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    years2000 = []

    for i in range(len(df)):
        date = df.iloc[i]["Close Approach Date"]
        year = int(date.split("-")[0])

        if year >= 2000:
            years2000.append(df.iloc[i])

    df = pd.DataFrame(years2000)
    return df


def data_details(df):
    """
    Description:
    The function wil get a Pandas DataFrame object and will remove the columns "Orbiting Body", "Neo Reference ID", "Equinox" from it,
    Then it will return a tuple that will represent (number of rows in df, number of columns in df, columns titles).

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will return a tuple that will represent (number of rows in df, number of columns in df, columns titles).
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    df = df.drop(columns = ["Orbiting Body", "Neo Reference ID", "Equinox"])
    rows, columns = df.shape
    df_columns = df.columns.tolist()
    result = (rows, columns, df_columns)
    return result


def max_absolute_magnitude(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will return a tuple that its indices are:
    index[0] - the Name of the astroid with the maximum Absolute Magnitude among the other asteroids.
    index[1] - The value of the maximal Absolute Magnitude.

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    a tuple that it's indices are:
    index[0] - the Name of the astroid with the maximum Absolute Magnitude among the other asteroids.
    index[1] - The value of the maximal Absolute Magnitude.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    max_astroid_name = df.iloc[0]["Name"]
    max_magnitude = df.iloc[0]["Absolute Magnitude"]

    for i in range(1, len(df)):
        current_astroid_name = df.iloc[i]["Name"]
        current_magnitude = df.iloc[i]["Absolute Magnitude"]

        if current_magnitude > max_magnitude:
            max_magnitude = current_magnitude
            max_astroid_name = current_astroid_name

    result = (int(max_astroid_name), float(max_magnitude))
    return result


def closest_to_earth(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will return the Name of the astroid
    that its closest to earth, determined by the column "Miss Dist.(kilometers)".

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will return the Name of the astroid that its closest to earth.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    astroid_name = df.iloc[0]["Name"]
    minimum_distance = df.iloc[0]["Miss Dist.(kilometers)"]

    for i in range(1, len(df)):
        distance = df.iloc[i]["Miss Dist.(kilometers)"]

        if distance < minimum_distance:
            minimum_distance = distance
            astroid_name = df.iloc[i]["Name"]

    return astroid_name


def common_orbit(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will return a dictionary that:
    key - Orbit ID.
    value - The amount of asteroids that are in that Orbit ID.

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    a dictionary that contains the key,value pairs so that:
    key - Orbit ID.
    value - The amount of asteroids that are in that Orbit ID.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    orbit_dictionary = {}

    for i in range(len(df)):
        orbit_id = int(df.iloc[i]["Orbit ID"])

        if orbit_id in orbit_dictionary:
            orbit_dictionary[orbit_id] += 1
        else:
            orbit_dictionary[orbit_id] = 1

    return orbit_dictionary


def min_max_diameter(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will return the amount of asteroids
    that their "Est Dia in KM(max)" is above the average of the "Est Dia in KM(max)" among all the asteroids.

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will return the amount of asteroids
    that their "Est Dia in KM(max)" is above the average of the "Est Dia in KM(max)" among all the asteroids.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    average = 0

    for i in range(len(df)):
        average += df.iloc[i]["Est Dia in KM(max)"]

    average /= len(df)
    count = 0

    for i in range(len(df)):
        if df.iloc[i]["Est Dia in KM(max)"] > average:
            count += 1

    return count


def plt_hist_diameter(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will display a histogram that shows the amount of asteroids
    in correlation to their average diameter in kilometers, determined by the columns "Est Dia in KM(min)", "Est Dia in KM(max)".

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will display a histogram that shows the amount of asteroids
    in correlation to their average diameter in kilometers, determined by the columns "Est Dia in KM(min)", "Est Dia in KM(max)".
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    plt.title("Distribution of Average diameter size")
    plt.xlabel("Average Value")
    plt.ylabel("Count")

    average_df = (df["Est Dia in KM(min)"] + df["Est Dia in KM(max)"]) / 2

    plt.hist(average_df, alpha = 0.7, bins = 100, color = "steelblue", edgecolor = "black")
    plt.grid(True, axis = "y", linestyle = "--")
    plt.show()


def plt_hist_common_orbit(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will display a histogram that shows the amount of asteroids
    in correlation to their "Minimum Orbit Intersection".

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will display a histogram that shows the amount of asteroids in correlation to their "Minimum Orbit Intersection".
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    plt.title("Distribution of Asteroids by Minimum Orbit Intersection")
    plt.xlabel("Min Orbit Intersection")
    plt.ylabel("Number of Asteroids")

    minimum_orbit = df["Minimum Orbit Intersection"].min()
    maximum_orbit = df["Minimum Orbit Intersection"].max()

    plt.hist(df["Minimum Orbit Intersection"], alpha = 0.7, bins = 10, color = "steelblue", edgecolor = "black", range = (minimum_orbit, maximum_orbit))
    plt.grid(True, axis = "y", linestyle = "--")
    plt.show()


def plt_pie_hazard(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will display a pie chart that shows the percentage of asteroids
    that are hazardous and the percentage of asteroids that aren't hazardous, determined by the column "Hazardous".

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will display a pie chart that shows the percentage of asteroids that are hazardous
    and the percentage of asteroids that aren't hazardous, determined by the column "Hazardous".
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    plt.title("Percentage of Hazardous and Non-Hazardous Asteroids")
    titles = ["False", "True"]

    counts = df["Hazardous"].value_counts()

    paints = ["lightcoral", "lightsteelblue"]
    lift = (0, 0.1)
    plt.pie(counts, labels = titles, colors = paints, autopct = "%1.1f%%", startangle = 90, explode = lift)
    plt.show()


def plt_linear_motion_magnitude(df):
    """
    Description:
    The function will get a Pandas DataFrame object and will display a linear regression graph
    that tests whether there's linear relationship between "Miss Dist.(kilometers)" and "Miles per hour" columns.
    *Note* - According to the regression line there's a positive correlation between "Miss Dist.(kilometers)" and "Miles per hour" columns
             as the slope of the line is positive, means there's a slightly positive relationship between them.

    Parameters:
    df - a Pandas DataFrame object.

    Output:
    The function will display a linear regression graph that tests whether there's linear relationship between
    "Miss Dist.(kilometers)" and "Miles per hour" columns.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a DataFrame object of pandas library")

    plt.title("Linear Regression: Miss Dist.(kilometers) vs Miles per hour")
    plt.xlabel("Miss Dist.(kilometers)")
    plt.ylabel("Miles per hour")

    x = df["Miss Dist.(kilometers)"]
    y = df["Miles per hour"]

    a,b, r_value, p_value, std_err, = linregress(x,y)
    regress_line = a*x + b
    legend_titles = ("Data points", "Regression line")

    plt.scatter(x, y, alpha = 0.5)
    plt.plot(x, regress_line, color = "red")
    plt.grid(True)
    plt.legend(legend_titles)
    plt.show()