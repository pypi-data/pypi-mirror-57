[![CircleCI](https://circleci.com/gh/coderepocenter/AxisUtilities.svg?style=svg)](https://circleci.com/gh/coderepocenter/AxisUtilities)
[![codecov](https://codecov.io/gh/coderepocenter/AxisUtilities/branch/master/graph/badge.svg)](https://codecov.io/gh/coderepocenter/AxisUtilities)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3543710.svg)](https://doi.org/10.5281/zenodo.3543710)
[![Documentation Status](https://readthedocs.org/projects/axisutilities/badge/?version=latest)](https://axisutilities.readthedocs.io/en/latest/?badge=latest)
 



# What is `AxisUtilities`
`Axis Utilities` was originally developed to manages Time Axis and different operations related to time with the main 
focus on Earth & Atmospheric Science Community. For example, you might have a daily 3D spatially distributed temperature
and you want to calculate the monthly average of this data. This result in the same spatial coordinate, however, with
a different time axis/coordinate. 

However, similar operations could be performed on any one-dimensional axis. Let's say your data is distributed along the
z-coordinate in certain way, and now you want to average them in a different vertical distribution. Although, your 
source axis is not time anymore, the mathematical operation that is being performed is the same. For this reason, it was
decided to rename the package from [`TimeAxis`](https://github.com/maboualidev/TimeAxis) to 
[`AxisUtilities`](https://github.com/coderepocenter/AxisUtilities).

During the axis conversion (conversion from source axis to destination axis), for example computing the monthly mean
from the daily data, there are a lot of computations that needs to be done which does not involve the data itself. This
means that we could cache these computations and reuse them to achieve a better performance. As long as the source and
the destination axis have not changed, we could use the cached computation to perform the axis conversion. One of the
features that `AxisUtilities` provide is caching these computations and allowing you to reuse it to achieve better 
performance. The same concept is being used in other packages such as 
[`ESMF`](https://www.earthsystemcog.org/projects/esmf/), 
[`SCRIP`](https://github.com/SCRIP-Project/SCRIP), and 
[`2D and 3D Remapping`](https://www.mathworks.com/matlabcentral/fileexchange/41669-2d-and-3d-remapping). In those 
packages, the cached computation is referred as ***Remapping Weights***.

# How To Install?
## using pip
As usual, you could use `pip` installation as follows:

```
pip install axisutilities
```

# How to use `AxisUtilities`?
The general procedure is:

1. Create a source axis, i.e. the axis that your original data is on,
2. Create a destination axis, i.e. the axis that you want to convert your data to,
3. Create an `AxisRemapper` object by passing the source and destination axis you created previously,
4. Finally, convert your data from the source axis to the destination axis, using the `AxisRemapper` object you created
in previous step.

You could repeat step (4) as many time as you want, as long as the source and destination axis are the same. The true
benefit of this approach is in the reuse of the same computations, a.k.a. ***remapping weights***.

For some examples refer to the following examples or the API documentations.

# Documentation
For `AxisUtilities` documentation click [here](https://axisutilities.readthedocs.io/en/latest/?badge=latest).

# Examples:
## Daily data averaged to weekly
**Step 1:** Create a source Axis

In this example, first we create a daily time-axis of length 14 days, i.e. we just have 14 data points
along the time axis:

```python
from axisutilities import DailyTimeAxis
from datetime import date
from_axis = DailyTimeAxis(
    start_date=date(2019, 1, 1),
    n_interval=14
)
```

**Step 2:** Create a destination Axis

Now we create a weekly time-axis of length 3, i.e. the time axis would have three elements with
span of 3 weeks:

```python
from axisutilities import WeeklyTimeAxis
from datetime import date
to_axis = WeeklyTimeAxis(
    start_date=date(2019, 1, 1),
    n_interval=3
)
```

**Step 3:** Create a `AxisRemapper` object

now we create a time axis converter object, as follows:

```python
from axisutilities import AxisRemapper
tc = AxisRemapper(
    from_axis=from_axis, 
    to_axis=to_axis
)
```

**Step 4:** Converting data from source axis to destination axis

Now we can use `tc` to convert data from the `from_axis` to `to_axis`, as follows:

```python
to_data = tc.average(from_data)
```

the resulting `to_data` is the weekly average of the `from_data`. By default, we are assuming
that the first dimension is the time dimension. If the time dimension (source axis) is not the first dimension,
you could define it as follows:

```python
to_data = tc.average(from_data, dimension=n)
```

where `n` is the time dimension (or source axis if the axis you have created is not time).

**Repeating Step 4:** as many time as needed

If we have other data sources that are on the same source axis (in this case the same time axis), you could use the 
same `tc` or `AxisRemapper` object that you created before to convert them to your new destination axis:

```python
to_data = tc.average(another_data_field)
```

**NOTE:** Please do note that only the 1D axis that you are converting from needs to be the same along all these 
different data sources. Their other dimensions could be completely different.

### A note on building time axis
Methods, such as `WeeklyTimeAxis` or `DailyTimeAxis`, are provided to facilitate the construction of the time axis. They
all instantiate and initialize an object of type `Axis`. You could use that class directly to create your own custom
made axis. However, in order to use the `Axis` object directly, you would need to know the upper and lower bound of each
data tick or element. In that case, you could create your own axis directly, using `Axis` class as follows:

```python
my_axis = Axis(lower_bound, upper_bound, binding="middle")
```

For more information on different ways of creating axis by using `Axis` class refer to the API documentations.

The helper methods, such as `WeeklyTimeAxis` or `DailyTimeAxis`, essentially collect the minimum information required
from the user, and computes the lower/upper bound and internally calls the `Axis` class to create the axis.

`Axis` class does not hold any unit information about the axis. That's another reason that although this package was 
originally developed to handle time axis, it could be used for any other type of axis as well. However, this unit-less
feature becomes important one you are mixing the axis that are created by directly calling `Axis` class and those that
are generated using one of the helper methods. All the helper methods, by default store the time as microseconds passed
January 1st, 1970 UTC time. 

Let's have a look at two-day daily axis starting from January 1st, 1970:

```python
from axisutilities import DailyTimeAxis
from datetime import date
my_axis_ms = DailyTimeAxis(
    start_date=date(1970, 1, 1), 
    n_interval=2
)
print("lower bound: ", my_axis.lower_bound.tolist())
print("upper bound: ", my_axis.upper_bound.tolist())
```

The above code would print:

```
lower bound:  [[0, 86400000000]]
upper bound:  [[86400000000, 172800000000]]
```
You are able to change the unit by providing an extra parameter, called `second_conversion_factor`. For example, to 
convert the unit to second you could call

```python
from axisutilities import DailyTimeAxis
from datetime import date
my_axis_s = DailyTimeAxis(
    start_date=date(1970, 1, 1), 
    n_interval=2, 
    second_conversion_factor=1
)
print("lower bound: ", my_axis.lower_bound.tolist())
print("upper bound: ", my_axis.upper_bound.tolist())
# Will print:
# lower bound:  [[0, 86400]]
# upper bound:  [[86400, 172800]]
```

or if you want day as the unit:

```python
from axisutilities import DailyTimeAxis
from datetime import date
my_axis_d = DailyTimeAxis(
    start_date=date(1970, 1, 1), 
    n_interval=2, 
    second_conversion_factor=(1 / 24 / 60 / 60)
)
print("lower bound: ", my_axis.lower_bound.tolist())
print("upper bound: ", my_axis.upper_bound.tolist())
# Will print:
# lower bound:  [[0, 1]]
# upper bound:  [[1, 2]]
```

Likewise, the hour unit would be:

```python
from axisutilities import DailyTimeAxis
from datetime import date
my_axis_h = DailyTimeAxis(
    start_date=date(1970, 1, 1), 
    n_interval=2, 
    second_conversion_factor=(1 / 60 / 60)
)
print("lower bound: ", my_axis.lower_bound.tolist())
print("upper bound: ", my_axis.upper_bound.tolist())
# Will print:
# lower bound:  [[0, 24]]
# upper bound:  [[24, 48]]
```

If you are using `Axis` class to generate your custom axis from the lower/upper bound values that you have and mixing it
with the axis that is generated by one of these helper methods, just make sure that:

1. They have the Same Unit, (helper methods for time axis use microseconds passed from January 1st, 1970)
2. In case of time, you need to measure from January 1st, 1970 in the unit that you have chosen above. At this point 
it is not possible to change the reference date, i.e. January 1st, 1970. May be in future releases, this option would
be provided as well.

Also, notice that the reference date has nothing to do with the use of `start_date`. It is always from January 1st, 
1970. Here is an example:

```python
from axisutilities import DailyTimeAxis
from datetime import date
my_axis_d = DailyTimeAxis(
    start_date=date(2019, 1, 1), 
    n_interval=2, 
    second_conversion_factor=(1 / 24 / 60 / 60)
)
print("lower bound: ", my_axis.lower_bound.tolist())
print("upper bound: ", my_axis.upper_bound.tolist())
# Will print:
# lower bound:  [[17897, 17898]]
# upper bound:  [[17898, 17899]]
```

## Rolling/moving weekly avarage
You could easily calculate a rolling or moving average of your data. Here is an example:

```python
from axisutilities import DailyTimeAxis, RollingWindowTimeAxis, AxisRemapper
from datetime import date
from_axis = DailyTimeAxis(
    start_date=date(2019, 1, 1),
    n_interval=14
)

to_axis = RollingWindowTimeAxis(
    start_date=date(2019, 1, 1),
    end_date=date(2019, 1, 15),
    window_size=7
)

tc = AxisRemapper(from_axis=from_axis, to_axis=to_axis)

to_data = tc.average(from_data)
```

as you can see, the only difference is the construction og the `to_axis`. In this example,
we are building a rolling time axis that starts on `Jan. 1st, 2019` and ends on `Jan. 15th, 2019`
with a window size of `7`. Since the base time delta, if not provided, is one day, our window is
one week (`7 * 1 day`). However, this is a rolling time axis, meaning that the next element on 
time axis is shifted only one day. Yes, the intervals in the time-axis are overlapping each other.

## Daily Averaged to Monthly

```python
# Daily time axis spanning ten years.
from axisutilities import DailyTimeAxis, MonthlyTimeAxis, AxisRemapper
from_axis = DailyTimeAxis(
    start_date=date(2010, 1, 1),
    end_date=date(2020, 1, 1)
)

# Monthly Time Axis spanning 10 years.
to_axis = MonthlyTimeAxis(
    start_year=2010,
    end_year=2019,
)

tc = AxisRemapper(from_axis=from_axis, to_axis=to_axis)
monthly_avg = tc.average(daily_data)
```

if you do not provide any month, the start month is assumed to be the January and the end month is assumed to be
the December. If you want to control that you could pass the `start_month` and/or `end_month` to change this
behavior:

```python
from axisutilities import MonthlyTimeAxis
to_axis = MonthlyTimeAxis(
    start_year=2010,
    start_monnth=4,
    end_year=2019,
    end_month=10
)
```

## Min and Max
The same way that you could calculate average, you could calculate the min and max.

```python
from axisutilities import AxisRemapper
tc = AxisRemapper(from_axis=from_axis, to_axis= to_axis)

tc.min(data)
tc.max(data)
```

for example, if the form axis is a daily axis, and to_axis is a monthly axis, `tc.min(data)` calculates the minimum 
daily data within the month.

## User-defined functions
The users are able to define their own function to apply. All you need to do is to pass the data along with the function
that you want to apply. Let's say the user is interested to calculate the standard deviation:

```python
from axisutilities import AxisRemapper
tc = AxisRemapper(from_axis=daily_axis, to_axis=monthly_axis)

to_data = tc.apply_function(from_data, np.nanstd)
```
**NOTES:** 
- Pay attention that there is no parenthesis after `np.nanstd`. You need to pass the function object itself. Any thing
that is conisdered `Callable` within Python.
- Note that instead of passing `np.std`, we are passing the version of the function that handles the `NaN`. The 
function that you pass must handle the `NaN` and missing values properly. If you pass the regular standard deviation and
your source data contains `NaN` your converted results would become also NaN. Also note that the function is forced
to performed the operation along axis=0; These are the requirements.
You could pass any function that you want:

```python
tc = AxisRemapper(from_axis=daily_axis, to_axis=monthly_axis)

def myfunction(data):
    return np.nansum(data, axis=0) * 42

to_data = tc.apply_function(from_data, myfunction)
```

Again, pay attention that when passing `myfunction` there is no parenthesis and we are handling the `NaN` inside
the function by using `np.nansum` instead of `np.sum`. Also, pay attention to the `axis=0`; The user-defined function
must perform it's operation along this axis only.


# Authors:
- Abouali, Mohammad (maboualidev@gmail.com; mabouali@ucar.edu)
- Banihirwe, Anderson (abanihi@ucar.edu)
- Long, Matthew (mclong@ucar.edu)





