function fill(val, dimensions) {
    // create an N-d array with size as dimensions filled with values `val`
    var array = []
    for (var i = 0; i < dimensions[0]; ++i) {
        array.push(
            dimensions.length == 1 ? val : fill(val, dimensions.slice(1))
        )
    }
    return array
}

export default fill
