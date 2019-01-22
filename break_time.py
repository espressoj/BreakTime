# Import the necessary libraries.
# Import "time" because we will be displaying the current date and time in the code .
import time
# Import webbrowser as we will be opening the client browser and sending to a webpage.
import webbrowser


breaks = input("How many breaks do you want to take?")
break_gap = input("How many minutes between the breaks?")
print("\nOnly add what comes after the '?v=' in the YouTube address (https://www.youtube.com/watch?v=hqCsg4U3iqQ).")
youtube_video_id = input("ID of the YouTube video to show (press enter for default):")

# Function to loop four times, a message and open a website every 2 hours.
def set_breaktime(hours, minutes, seconds, breaks, videoId):
    # Define loop_count and start it at 1.
    loop_count = 1
    # Check the video id
    if youtube_video_id == '':
        videoUrl = 'https://www.youtube.com/watch?v=hqCsg4U3iqQ'
    else:
        videoUrl = ('https://www.youtube.com/watch?v=%s' % videoId)
    print('\n\nYou\'ve asked for {} breaks in {} minute intervals.\n\nAt each break the following YouTube video will play:\n    {}'.format(breaks, minutes, videoUrl))
    # Process the contents of the loop the given number of breaks.
    while loop_count <= breaks:
        # Calculate the number of seconds the loop will pause based on user input.
        time.sleep((hours * 60 * 60) + (minutes * 60) + seconds)
        # Generate the printed message for each break.
        print_message = "Break number {}!  ({})"
        # Print the generated message using the current loop_count and the current date/time.
        print(print_message.format(loop_count, time.ctime()))
        # Open the user's web browser and send it to the desired URI.
        webbrowser.open(videoUrl)
        # Increment the loop by 1.
        loop_count += 1

# In RUN, display when the date/time the program was started.
print("You started this program at " + time.ctime())
# Run the set_breaktime function and input (Hours, Minutes, Seconds, Number of times to loop)
set_breaktime(0, int(break_gap), 0, int(breaks), youtube_video_id)
