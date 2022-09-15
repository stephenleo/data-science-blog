
# Exploratory Data Analysis

## Pandas Profiling

Automate your exploratory data analysis (EDA) analysis with one line of
code!

-   When I start working on any new dataset, I subconsciously follow the
    same set of EDA steps to understand the data better.
-   The pandas’ `#!python df.describe()` function is too basic for
    serious EDA work, so I manually create many plots and summary
    statistics. Most of the time, I need to Google for some specific
    syntax or solve some coding bug. All this makes the whole EDA
    process quite tedious at times.

Enter Pandas profiling!

-   Pandas profiling is an open-source Python library that automates
    many of those “best-known methods” in EDA to prepare a detailed
    interactive report with just 1 line of code!
-   You can then click through the various tabs and analyze the results
    without manually creating everything yourself. What a time saver!
-   Specifically, Pandas profiling automatically calculates column
    statistics, plots histograms, correlation coefficients, etc.

<!-- -->

    pip install pandas-profiling

🌟 Github: <https://github.com/ydataai/pandas-profiling>

▶️ Play with it on
[Binder](https://mybinder.org/v2/gh/ydataai/pandas-profiling/master?filepath=examples%2Ftitanic%2Ftitanic.ipynb)

<iframe width="560" height="315" src="https://www.youtube.com/embed/aKqkiwhnvCY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
</iframe>
