import uiautomator2 as u2
from time import sleep

# Connect to the device (replace 'emulator-5554' with your device's serial)
d = u2.connect()

def scroll_and_select_date():
    # Get screen dimensions
    screen_width = d.info['displayWidth']
    screen_height = d.info['displayHeight']

    # Coordinates for the month, day, and year pickers
    # Adjust these values as needed based on the actual picker locations
    month_x = screen_width * 0.5
    day_x = screen_width * 0.75
    year_x = screen_width * 0.25
    picker_y = screen_height * 0.5

    # Define drag distances for scrolling (adjust as necessary)
    drag_distance = screen_height * 0.2

    # Select month (scrolling example, adjust as needed)
    for _ in range(5):  # Scroll up 5 times to reach the desired month
        d.drag(month_x, picker_y, month_x, picker_y + drag_distance, 0.5)
        sleep(1)

    # Select day (scrolling example, adjust as needed)
    for _ in range(3):  # Scroll up 3 times to reach the desired day
        d.drag(day_x, picker_y, day_x, picker_y + drag_distance, 0.5)
        sleep(1)

    # Select year (scrolling example, adjust as needed)
    for _ in range(2):  # Scroll up 2 times to reach the desired year
        d.drag(year_x, picker_y, year_x, picker_y + drag_distance, 0.5)
        sleep(1)

    # Click the "Next" button to confirm the date selection
    #d(resourceId="com.lemon8.app:id/next_button").click()

# Call the function to scroll and select the date
scroll_and_select_date()
