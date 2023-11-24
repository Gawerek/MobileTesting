from Utilities.scroll_util import ScrollUtil
import pytest
import time
from TestCases.BaseTest import BaseTestSP

from PagesSP.HomeScreen import HomeScreen

from Utilities import dataProvider


class Test_ActionAgainstVisits(BaseTestSP):
    def test_action_against_visits(self):
        home = HomeScreen(self.driver)
        news = home.go_to_news()

        news.accept_visit()

        news.click_more(1)
        news.reject_visit()

        news.click_more(0)
        news.cancel_visit()

