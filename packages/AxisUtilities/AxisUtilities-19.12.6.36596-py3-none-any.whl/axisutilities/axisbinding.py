from enum import Enum
from numbers import Number


class AxisBinding(Enum):
    """
    This class/Enumeration defines the different way that a data tick could be bound to an interval. The available
    options are:
    - `Beginning`: This means the data tick is bound to the beginning of the interval or the lower bound. The
    fraction in this case is 0.0.
    - `end`: The data is bound to the end of the interval or the upper bound. The fraction is 1.0.
    - `middle`: The data is bound in the middle, i.e. half-way through between lower bound and upper bound. The
    fraction is 0.5.
    - `custom_fraction`: The is bounded to a user-defined location between the upper bound and or lower bound. The
    fraction could be any value between 0.0 and 1.0.
    """
    BEGINNING = ("beginning", 0.0)
    END = ("end", 1.0)
    MIDDLE = ("middle", 0.5)
    CUSTOM_FRACTION = ("custom_fraction", None)

    def __str__(self):
        return self.value[0]

    def __repr__(self):
        return self.__str__()

    def fraction(self):
        return self.value[1]

    @staticmethod
    def valueOf(v):
        if isinstance(v, str):
            possibleCases = {
                "beginning": AxisBinding.BEGINNING,
                "lef": AxisBinding.BEGINNING,
                "end": AxisBinding.END,
                "right": AxisBinding.END,
                "middle": AxisBinding.MIDDLE,
                "center": AxisBinding.MIDDLE,
                "custom": AxisBinding.CUSTOM_FRACTION,
                "custom_fraction": AxisBinding.CUSTOM_FRACTION
            }
            lowerV = v.lower()
            if lowerV in possibleCases:
                return possibleCases[lowerV]
            else:
                raise ValueError(f"could not find the Time Axis Binding associated to {str(v)}. "
                                  f"possible options are [{', '.join(possibleCases.keys())}]")
        if isinstance(v, Number):
            if v == 0.0:
                return AxisBinding.BEGINNING
            if v == 1.0:
                return AxisBinding.END
            if v == 0.5:
                return AxisBinding.MIDDLE
            if (v >= 0.0) and (v <= 1.0):
                return AxisBinding.CUSTOM_FRACTION
            else:
                raise ValueError("a number between 0 and 1 must be provided.")
        elif isinstance(v, AxisBinding):
            return v
        else:
            raise TypeError("Either an str or TimeAxisBinding object is accepted.")




