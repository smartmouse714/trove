ComputeMA <- function(x, n = 3) {
  # Calculate the moving average of a vector.
  #
  # Args:
  #   x: a vector
  #   n: the number of points (size of the sliding window)
  #
  # Returns:
  #   a vector
  # Error handling
  if (n < 1 || n > length(x)) {
    stop('Invalid window size')
  }    
  cx <- c(0, cumsum(x))
  (cx[(n + 1):length(cx)] - cx[1:(length(cx) - n)]) / n
}
