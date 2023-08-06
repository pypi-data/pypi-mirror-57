"""
sklearn-specific API.
"""

def _load_svmlight_file(
    f,
    dtype,
    multilabel,
    zero_based,
    query_id,
    offset,
    length,
):
    """
    An ``sklearn``-compatible svmlight loader.

    Drop-in replacement for
    `sklearn.datasets._svmlight_format._load_svmlight_file` (the
    internal function, not the one with all the parameter munging).
    """

    if multilabel:
        loads = multilabel_classification_from_lines
    else:
        loads = classification_from_lines
    X, y = loads(f, zero_based=zero_based)
    query = numpy.array([])
    return (
        X.dtype,
        X.data,
        X.indices.astype(numpy.longlong),
        X.indptr.astype(numpy.longlong),
        y,
        query,
    )
