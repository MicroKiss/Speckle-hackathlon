from specklepy.objects.geometry import Interval


PIXEL = 0.0625

def GetIntervalFromSize(size):
    return Interval(start=0, end=size)

sideFenceHeight = 3*PIXEL
sideFenceLength = 6*PIXEL
sideFenceWidth = 2*PIXEL
stairsStepWidth = 8*PIXEL
intervalWhole = Interval(start=0, end=1)
intervalHalf = Interval(start=0, end=0.5)
interval14Middle = Interval(start=0, end=14*PIXEL)
interval8Middle = Interval(start=0, end=8*PIXEL)
interval6Middle = Interval(start=0, end=6*PIXEL)
interval5Middle = Interval(start=0, end=5*PIXEL)
interval4Middle = Interval(start=0, end=4*PIXEL)
interval2Middle = Interval(start=0, end=2*PIXEL)
intervalTopSideFenceHeight = Interval(start=0, end=sideFenceHeight)
intervalLowerSideFenceHeight = Interval(start=0, end=sideFenceHeight)
intervalSideFence = Interval(start=0, end=sideFenceLength)