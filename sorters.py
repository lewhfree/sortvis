from Bogo import Bogo
from Bubble import Bubble
from Selection import Selection

#allows main to detect and allow usage of algo
choices = {
    "bogo": Bogo,
    "bubble": Bubble,
    "selection": Selection
}

#Allows for fine-tuning of timing
delays = {
    "bogo": 0,
    "bubble": 0.051,
    "selection": 0.2
}
