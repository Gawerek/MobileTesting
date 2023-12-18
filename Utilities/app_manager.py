import requests
from requests.auth import HTTPBasicAuth


class AppManager:
    def __init__(self, driver, user=None, password=None):
        self.driver = driver
        self.user = user
        self.password = password

    def launch_cli_app(self):
        if self.driver.current_package != "bbox.pl.client.app.development":
            self.driver.start_activity("bbox.pl.client.app.development", "bbox.pl.client.app.MainActivity")


    def launch_sp_app(self):
        if self.driver.current_package != "bbox.pl.sp.app.development":
            self.driver.start_activity("bbox.pl.sp.app.development", "bbox.sp.pl.app.MainActivity")

    def terminate_sp_app(self):
        self.driver.terminate_app("bbox.sp.pl.app.development")

    def terminate_cli_app(self):
        self.driver.terminate_app("bbox.pl.client.app.development")






    # def get_cli_app(self):
    #     auth = HTTPBasicAuth(self.user, self.password)
    #     URL = "https://api.appcenter.ms/v0.1/apps/windeveloper/beautybox-droid-staging-1/releases/latest"
    #     headers = {'Content-type': 'application/json', 'X-Api-Token': 'YOUR_API_TOKEN'}
    #     response = requests.get(URL, headers=headers)
    #     link = response.json()['download_url']
    #     URL = "https://api-cloud.browserstack.com/app-automate/upload"
    #     data = {'url': link}
    #     response = requests.post(URL, auth=auth, json=data)
    #     return response.json()['app_url']
    #
    # def get_sp_app(self):
    #     pass
