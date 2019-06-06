import pandas as pd


def my_cut(x, bins,
           lower_infinite=True, upper_infinite=True,
           **kwargs):
    """Wrapper around pandas cut() to create infinite lower/upper bounds with proper labeling.

    Takes all the same arguments as pandas cut(), plus two more.

    Args :
        lower_infinite (bool, optional) : set whether the lower bound is infinite
            Default is True. If true, and your first bin element is something like 20, the
            first bin label will be '<= 20' (depending on other cut() parameters)
        upper_infinite (bool, optional) : set whether the upper bound is infinite
            Default is True. If true, and your last bin element is something like 20, the
            first bin label will be '> 20' (depending on other cut() parameters)
        **kwargs : any standard pandas cut() labeled parameters

    Returns :
        out : same as pandas cut() return value
        bins : same as pandas cut() return value
    Source: https://stackoverflow.com/questions/30127427/pandas-cut-with-infinite-upper-lower-bounds
    """

    # Quick passthru if no infinite bounds
    if not lower_infinite and not upper_infinite:
        return pd.cut(x, bins, **kwargs)

    # Setup
    num_labels = len(bins) - 1
    include_lowest = kwargs.get("include_lowest", False)
    right = kwargs.get("right", False)

    # Prepend/Append infinities where indiciated
    bins_final = bins.copy()
    if upper_infinite:
        bins_final.insert(len(bins), float("inf"))
        num_labels += 1
    if lower_infinite:
        bins_final.insert(0, float("-inf"))
        num_labels += 1

    # Decide all boundary symbols based on traditional cut() parameters
    symbol_lower = "<=" if include_lowest and right else "<"
    left_bracket = "(" if right else "["
    right_bracket = "]" if right else ")"
    symbol_upper = ">" if right else ">="

    # Inner function reused in multiple clauses for labeling
    def make_label(i, lb=left_bracket, rb=right_bracket):
        return "{0}{1}, {2}{3}".format(lb, bins_final[i], bins_final[i + 1], rb)

    # Create custom labels
    labels = []
    for i in range(0, num_labels):
        new_label = None

        if i == 0:
            if lower_infinite:
                new_label = "{0} {1}".format(symbol_lower, bins_final[i + 1])
            elif include_lowest:
                new_label = make_label(i, lb="[")
            else:
                new_label = make_label(i)
        elif upper_infinite and i == (num_labels - 1):
            new_label = "{0} {1}".format(symbol_upper, bins_final[i])
        else:
            new_label = make_label(i)

        labels.append(new_label)

    # Pass thru to pandas cut()
    return pd.cut(x, bins_final, labels=labels, **kwargs)
