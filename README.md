# Description

A simple timer for measuring your code.

# Usage

## Simple timing

```python
from Timer import Timer

timer = Timer()
timer.start()
# Code to be timed
timer.mark()
timer.print()
# Prints out something like: 'Time 1: 0.125s'
```

## Multiple timing (continuous)

```python
from Timer import Timer

timer = Timer()
timer.start()
# First code to be timed
timer.mark()
# Second code to be timed
timer.mark()
timer.print()
# Prints out something like: 
# Time 1: 0.125s
# Time 2: 0.226s
```

## Multiple timing (non-continuous)

```python
from Timer import Timer

timer = Timer()
timer.start()
# First code to be timed
timer.pause()
# Other code you don't want to time
timer.resume()
# Second code to be timed
timer.mark() # Or timer.pause()
timer.print()
# Prints out something like: 
# Time 1: 0.321s
# Time 2: 0.125s
```

## Adding labels

```python
from Timer import Timer

timer = Timer()
timer.start()
# First code to be timed
timer.pause('Processed data')
# Other code you don't want to time
timer.resume()
# Second code to be timed
timer.mark('Calculated complex operation') # Or timer.pause()
timer.print()
# Prints out something like: 
# Processed data: 0.321s
# Calculated complex operation: 0.125s
```

## Get the times instead of printing

```python
from Timer import Timer

timer = Timer()
timer.start()
# First code to be timed
timer.pause('Processed data')
# Other code you don't want to time
timer.resume()
# Second code to be timed
timer.mark('Calculated complex operation') # Or timer.pause()

# This will give a list of the timed values
times_measured = timer.times_measured()
# This will give a list of tuples with a pair (label, time)
times_measured_with_labels = timer.times_measured_with_labels()
# This will give only the last time measured
last_time = timer.latest_time_measured()
```

## Chose where to print

```python
from IPrinter import IPrinter
from Timer import Timer
from typing import AnyStr

# Create your printer class
class StringPrinter(IPrinter):
    def __init__(self):
        self._str = ''

    def print(self, string: AnyStr, end='\n'):
        self._str += string+end

    def content(self):
        return self._str
my_printer = StringPrinter()
timer = Timer()
timer.set_printer(my_printer)
timer.start()
# First code to be timed
timer.pause('Processed data')
# Other code you don't want to time
timer.resume()
# Second code to be timed
timer.mark('Calculated complex operation') # Or timer.pause()
# Will use the passed printer object, not the default one
timer.print()

```