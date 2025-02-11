import unittest
from unittest.mock import MagicMock, patch
import uiautomator2 as u2
from main import Lemon8Automation  # Replace with the actual script name


class TestLemon8Automation(unittest.TestCase):

    def setUp(self):


        # Initialize the Lemon8Automation class with the mock device
        self.automation = Lemon8Automation()


    def test_create_account(self):
        # Simulate the account creation process
        result = self.automation.create_account()

        # Assert that the correct UI elements were interacted with

        self.assertTrue(result)
    def test_add_profile_picture(self):
        # Simulate adding a profile picture
        result = self.automation.add_profile_picture()
        self.assertTrue(result)

    def test_make_post(self):
        images = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"]

        # Simulate making a post
        self.automation.make_post(images)

        # Assert that the correct UI elements were interacted with
        self.mock_device(resourceId="com.bd.nproject:id/bottomTabItemUgc").click.assert_called_once()
        self.assertEqual(self.mock_device(resourceId="com.lemon8.app:id/add_image_button").click.call_count,
                         len(images))
        for image in images:
            self.mock_device.xpath(f'//android.widget.TextView[@text="{image}"]').click.assert_called_once()
        self.mock_device(resourceId="com.lemon8.app:id/submit_post").click.assert_called_once()

    def test_log_out(self):
        # Simulate logging out
        result = self.automation.log_out()
        self.assertTrue(result)

    def test_mass_dm(self):
        follower_list = ["user1", "user2", "user3"]

        # Simulate sending mass DMs
        self.automation.mass_dm(follower_list)

        # Assert that the correct UI elements were interacted with
        self.assertEqual(
            self.mock_device(resourceId="com.bd.nproject:id/navigation_bar_item_icon_view").click.call_count,
            len(follower_list))
        self.assertEqual(
            self.mock_device(resourceId="com.bd.nproject:id/newLemonSearchbarEditText").set_text.call_count,
            len(follower_list))

    def test_all_features(self):
        result = self.automation.run()
        self.assertTrue(result)