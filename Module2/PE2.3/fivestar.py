"""
instructions:
Five Star Retro Video rents VHS tapes and DVDs to the
same connoisseurs who like to buy LP record albums.
The store rents new videos for $3.00 a night,
and oldies for $2.00 a night.

Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals.

The program should prompt the user for the
number of each type of video and output the total cost.

Enter the number of new videos: 3
Enter the number of oldies: 2
The total cost is $13.0
"""

# global constants
NEW_VIDEOS = 3.00
OLD_VIDEOS = 2.00

# prompt for the video number
newVideos = float(input("Enter the number of new videos: "))
oldVideos = float(input("Enter the number of oldies: "))

# calculate results
totalCost = (newVideos * NEW_VIDEOS) + (oldVideos * OLD_VIDEOS)

# display results
print("The total cost is ", totalCost, end="")
