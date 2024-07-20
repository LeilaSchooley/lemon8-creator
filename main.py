import uiautomator2 as u2
from time import sleep

# Connect to the device (replace 'emulator-5554' with your device's serial)
d = u2.connect()


def create_account():
    # Automate account creation
    d(resourceId="com.lemon8.app:id/create_account_button").click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/username").set_text("username")
    d(resourceId="com.lemon8.app:id/password").set_text("password")
    d(resourceId="com.lemon8.app:id/submit").click()
    sleep(2)


def add_profile_picture():
    # Navigate to profile and add profile picture
    d(resourceId="com.bd.nproject:id/bottomTabItemProfile").click()
    sleep(2)
    d(resourceId="com.bd.nproject:id/profileEdit").click()
    sleep(2)
    d(resourceId="com.bd.nproject:id/profileCameraIv").click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/select_from_gallery").click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/image").click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/confirm").click()
    sleep(2)


def make_post(images):
    # Create a post with a slideshow
    d(resourceId="com.bd.nproject:id/bottomTabItemUgc").click()
    sleep(2)
    for image in images:
        d(resourceId="com.lemon8.app:id/add_image_button").click()
        sleep(2)
        d.xpath(f'//android.widget.TextView[@text="{image}"]').click()
        sleep(2)
    d(resourceId="com.lemon8.app:id/submit_post").click()
    sleep(2)


def log_out():
    # Log out from the account
    d(resourceId="com.lemon8.app:id/profile_tab").click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/settings").click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/logout").click()
    sleep(2)


def mass_dm(follower_list):
    # DM all followers
    for follower in follower_list:
        d(resourceId="com.lemon8.app:id/search").click()
        sleep(2)
        d(resourceId="com.lemon8.app:id/search_input").set_text(follower)
        sleep(2)
        d(resourceId="com.lemon8.app:id/followers").click()
        sleep(2)
        d(resourceId="com.lemon8.app:id/message_button").click()
        sleep(2)
        d(resourceId="com.lemon8.app:id/message_input").set_text("Hello!")
        sleep(2)
        d(resourceId="com.lemon8.app:id/send_message").click()
        sleep(2)


def mass_tag(users, parent_post):
    # Tag users in a parent post
    d(resourceId="com.lemon8.app:id/post_tab").click()
    sleep(2)
    d(resourceId=f'com.lemon8.app:id/{parent_post}').click()
    sleep(2)
    d(resourceId="com.lemon8.app:id/tag_button").click()
    sleep(2)
    for user in users:
        d(resourceId="com.lemon8.app:id/tag_input").set_text(user)
        sleep(2)
        d(resourceId="com.lemon8.app:id/tag_user").click()
        sleep(2)
    d(resourceId="com.lemon8.app:id/confirm_tag").click()
    sleep(2)


def main():
    accounts_to_create = 10
    images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"]

    for _ in range(accounts_to_create):
        create_account()
        add_profile_picture()
        for _ in range(3):
            make_post(images)
        log_out()

    # For mass DM and tagging
    follower_list = ["user1", "user2", "user3"]
    parent_post = "post_id"
    users_to_tag = ["user4", "user5", "user6"]

    mass_dm(follower_list)
    mass_tag(users_to_tag, parent_post)


if __name__ == "__main__":
    #main()
    print(d.dump_hierarchy())
