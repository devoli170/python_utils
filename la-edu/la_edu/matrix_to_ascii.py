import numpy as np


def decorate(a: np.ndarray):
    """
    Takes a two dimensional numpy matrix and returns a string representation surrounded by brackets.

    example:
    >>> a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    >>> a
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
    >>> decorate(a)
    '┌       ┐\n| 1 2 3 |\n| 4 5 6 |\n| 7 8 9 |\n└       ┘'
    >>> print(decorate(a))
    ┌       ┐
    | 1 2 3 |
    | 4 5 6 |
    | 7 8 9 |
    └       ┘
    """
    if a.ndim != 2:
        raise ValueError(
            "ndarray has ndim {} and shape {}. Only arrays with ndim = 2 are considered for decoration".format(a.ndim,
                                                                                                               a.shape))
    fmt = gen_format_string(a)
    ret = fmt.format(*a.flatten())
    return ret


def decorate_aug(a: np.ndarray, b: np.ndarray):
    """
    Takes A and b from an equation A*x=b and returns the augmented form as string.

    example:
    >>> a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    >>> b = np.array([[1],[2],[3]])
    >>> decorate_aug(a,b)
    '┌           ┐\n| 1 2 3 | 1 |\n| 4 5 6 | 2 |\n| 7 8 9 | 3 |\n└           ┘'
    >>> print(decorate_aug(a,b))
    ┌           ┐
    | 1 2 3 | 1 |
    | 4 5 6 | 2 |
    | 7 8 9 | 3 |
    └           ┘
"""
    if a.ndim != 2:
        raise ValueError(
            "ndarray A has ndim {} and shape {}. Only arrays with ndim = 2 are considered for decoration".format(a.ndim,
                                                                                                                 a.shape))
    if b.ndim != 2:
        raise ValueError(
            "ndarray b has ndim {} and shape {}. Only arrays with ndim = 2 are considered for decoration".format(b.ndim,
                                                                                                                 b.shape))
    if a.shape[0] != b.shape[0]:
        raise ValueError("A and b must have same amount of columns")

    delim = np.array(["|" for x in b], dtype="str")
    delim = delim.reshape((-1, 1))
    ab = np.concatenate((a, delim, b), axis=1)
    fmt = gen_format_string(ab)
    ret = fmt.format(*ab.flatten())
    return ret


def gen_format_string(a: np.array):
    """
    Generates a matrix format in the shape of a.
    >>> a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(gen_format_string(a))
    ┌       ┐
    |{:>2}{:>2}{:>2} |
    |{:>2}{:>2}{:>2} |
    |{:>2}{:>2}{:>2} |
    └       ┘

    The template can be rendered with the help of the unboxing operator, e.g.:
    >>> gen_format_string(a).format(*a.flatten())
    or
    >>> gen_format_string(a).format(*[x for x in np.nditer(a)])
    """
    str_arr = copy_as_str(a)
    max_lens = max_len_in_col(str_arr) + 1
    rows = a.shape[0]
    inner_juice = "".join(map(lambda x: "{{:>{}}}".format(x), max_lens))
    # bad readability :(, but apparently faster than invoking list constructor like with [map(lambda x: " ", max_lens)]
    spacers = *map(lambda x: " ", max_lens),
    header = "┌" + inner_juice.format(*spacers) + " ┐\n"
    body = ""
    for x in range(rows):
        body += "|" + inner_juice + " |\n"
    footer = "└" + inner_juice.format(*spacers) + " ┘"

    ret = header + body + footer
    return ret


# returns a Matrix with elementwise string casts. Numpy's cast or string reps create fractions of the elements :/
def copy_as_str(a: np.array):
    """
    Creates a deep copy of a with each element cast to string.
    """
    matrix_like = []
    for x in np.nditer(a):
        matrix_like.append(str(x))
    str_arr = np.array(matrix_like, dtype="str")
    str_arr = str_arr.reshape(a.shape)
    return str_arr


# returns col vector with the maximum string length in column of matrix
def max_len_in_col(str_arr: np.array):
    """
    ┌                ┐
    | '1' '2'   '3'  |
    | '4' '555' '60' |     =>    [1,3,2]
    | '7' '8'   '9'  |
    └                ┘
    """
    len_arr = np.char.str_len(str_arr)
    return np.max(len_arr, axis=0)
