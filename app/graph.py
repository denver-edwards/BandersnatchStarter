import pandas as pd
from altair import Chart, Tooltip, Color, Scale


def chart(df: pd.DataFrame, x: str, y: str, target: str) -> Chart:
    """
    Creates a scatter plot using Altair with specified columns from a
    Pandas DataFrame.

        The function removes a column named '_id' from the DataFrame,
        and then creates a chart with circles representing each data
        point. The x and y axes are determined by the corresponding
        column names provided. The color of the points is determined by
        the 'target' column.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data to plot.
        x (str): The column name to use for the x-axis.
        y (str): The column name to use for the y-axis.
        target (str): The column name to use for coloring the data points.

        Returns:
        Chart: An Altair Chart object representing the scatter plot.
        """

    new_df = df.drop("_id", axis=1)

    graph = (Chart(
        new_df,
        title=f"{y} by {x} for {target}",
        background="#1F1F1F",
        padding={"left": 50, "top": 50, "right": 50, "bottom": 50},
        width=450,
        height=450
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        tooltip=Tooltip(new_df.columns.to_list()),
        color=Color(f"{target}", scale=Scale(
            scheme='blues'))
    ).configure_title(
        fontSize=20,
        color="gray"
    )
    .configure_axis(
        labelColor="gray",
        titleColor="gray"
    ).configure_legend(
        labelColor="gray",
        titleColor="gray"
    ))

    return graph
