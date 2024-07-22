import subprocess

import uiautomator2 as u2
from time import sleep


class Lemon8Automation:
    def __init__(self, device_serial=None):
        self.d = u2.connect(device_serial)

    def create_account(self):
        # Automate account creation
        self.d(resourceId="com.lemon8.app:id/create_account_button").click()
        sleep(2)
        self.d(resourceId="com.lemon8.app:id/username").set_text("username")
        self.d(resourceId="com.lemon8.app:id/password").set_text("password")
        self.d(resourceId="com.lemon8.app:id/submit").click()
        sleep(2)

    def add_profile_picture(self):
        # Navigate to profile and add profile picture
        self.d(resourceId="com.bd.nproject:id/bottomTabItemProfile").click()
        sleep(2)
        self.d(resourceId="com.bd.nproject:id/profileEdit").click()
        sleep(2)
        self.d(resourceId="com.bd.nproject:id/profileCameraIv").click()
        sleep(2)
        self.d(resourceId="com.lemon8.app:id/select_from_gallery").click()
        sleep(2)
        self.d(resourceId="com.lemon8.app:id/image").click()
        sleep(2)
        self.d(resourceId="com.lemon8.app:id/confirm").click()
        sleep(2)

    def make_post(self):
        # Create a post with a slideshow
        self.d(resourceId="com.bd.nproject:id/bottomTabItemUgc").click()
        sleep(2)
        for _ in range(3):
            self.d(resourceId="com.lemon8.app:id/add_image_button").click()
            sleep(2)
            self.d(resourceId="com.lemon8.app:id/image").click()  # Adjust the resource ID if necessary
            sleep(2)
        self.d(resourceId="com.bd.nproject:id/post_hot_view").click()
        sleep(2)

    def log_out(self):
        # Log out from the account
        self.d(resourceId="com.bd.nproject:id/navigation_bar_item_icon_view").click()
        sleep(2)
        self.d(resourceId="com.bd.nproject:id/lemonNavigationBarRightClickMultipleThreeViewThreeClick").click()
        sleep(2)
        self.d(text="Log out").click()
        sleep(2)
        self.d(text="Log out").click()
        if (self.d(text="When is your date of birth?")).exists:
            return True
        else:
            return False

    def dismiss_keyboard(self):
        self.d.press("back")
        print("Dismissed keyboard.")

    def mass_dm(self, follower_list, message):
        results = []
        # DM all followers
        for follower in follower_list:
            self.d(resourceId="com.bd.nproject:id/navigation_bar_item_icon_view").click()
            sleep(2)
            self.d(resourceId="com.bd.nproject:id/newLemonSearchbarEditText").set_text(follower)
            sleep(2)
            self.d(text="Accounts").click()
            self.d(className="com.lynx.tasm.behavior.ui.text.FlattenUIText").click()
            sleep(2)
            self.d(resourceId="com.bd.nproject:id/lemonButtonIc").click()
            sleep(2)

            self.d(text="Send a message...").set_text(message)
            sleep(2)
            subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_ENTER"])
            sleep(2)
            self.dismiss_keyboard()

            results.append(True)
        return results
    def mass_tag(self, users, parent_post):
        # Tag users in a parent post
        self.d(resourceId="com.lemon8.app:id/post_tab").click()
        sleep(2)
        self.d(resourceId=f'com.lemon8.app:id/{parent_post}').click()
        sleep(2)
        self.d(resourceId="com.lemon8.app:id/tag_button").click()
        sleep(2)
        for user in users:
            self.d(resourceId="com.lemon8.app:id/tag_input").set_text(user)
            sleep(2)
            self.d(resourceId="com.lemon8.app:id/tag_user").click()
            sleep(2)
        self.d(resourceId="com.lemon8.app:id/confirm_tag").click()
        sleep(2)

    def run(self):
        accounts_to_create = 10
        images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"]

        for _ in range(accounts_to_create):
            self.create_account()
            self.add_profile_picture()
            for _ in range(3):
                self.make_post(images)
            self.log_out()

        # Read the follower list from a file
        follower_list = self.read_follower_list("follow_list.txt")
        parent_post = "post_id"
        users_to_tag = ["user4", "user5", "user6"]

        self.mass_dm(follower_list)
        self.mass_tag(users_to_tag, parent_post)

    def read_follower_list(self, file_path):
        with open(file_path, "r") as file:
            follower_list = [line.strip() for line in file.readlines()]
        return follower_list


if __name__ == "__main__":
    # Initialize the automation class
    automation = Lemon8Automation()

    # Uncomment to run the main function
    # automation.run()

    # Print the UI hierarchy for debugging
    print(automation.d.dump_hierarchy())
