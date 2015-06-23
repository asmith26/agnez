

def image_sequence(X, shape):
    '''Image Sequence converts a matrix with different examples in each
    row to a sequence of resized image

    Paramters
    ---------
    X: 2D `numpy.array`
    Matrix with flatten examples on each row

    shape: list
    list with the shape to resize the flatten elements in X

    '''
    X = X.reshape((-1,)+shape)
    if len(shape) == 3:
        X = X.swapaxes(0, 2)
        X = X.reshape(shape[0], X.shape[2], shape[1]*shape[2])
    else:
        X = X.swapaxes(0, 1)
        X = X.reshape((X.shape[0], X.shape[1]*X.shape[2]))
    return X
