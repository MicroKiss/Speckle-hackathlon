from specklepy.objects.geometry import Interval


PIXEL = 0.0625
sideFenceHeight = 3*PIXEL
sideFenceLength = 6*PIXEL
sideFenceWidth = 2*PIXEL
intervalWhole = Interval(start=0, end=1)
intervalHalf = Interval(start=0, end=0.5)
interval4Middle = Interval(start=0, end=4*PIXEL)
interval2Middle = Interval(start=0, end=2*PIXEL)
intervalTopSideFenceHeight = Interval(start=0, end=sideFenceHeight)
intervalLowerSideFenceHeight = Interval(start=0, end=sideFenceHeight)
intervalSideFence = Interval(start=0, end=sideFenceLength)
