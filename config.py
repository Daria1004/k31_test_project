import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from k31_test_project.utils import file

context = os.getenv('CONTEXT', 'bstack')

load_dotenv(file.abs_path_from_project(f'.env.{context}'))
load_dotenv(file.abs_path_from_project(f'.env.credentials'))

user_login = os.getenv('USER_LOGIN')
user_password = os.getenv('USER_PASSWORD')
user_web_name = os.getenv('USER_WEB_NAME')
user_mobile_name = os.getenv('USER_MOBILE_NAME')

base_url = os.getenv('BASE_URL')
base_url_api = os.getenv('BASE_URL_API')

remote_url = os.getenv('URL_WD_HUB')
device_udid = os.getenv('DEVICE_UDID')

app = os.getenv('APP_STRING')

if app.startswith('./'):
    app = file.abs_path_from_project(app)

hub_timeout = os.getenv('HUB_TIMEOUT', 15.0)

selenoid_url = os.getenv('URL_SELENOID')
selenoid_login = os.getenv('SELENOID_LOGIN')
selenoid_password = os.getenv('SELENOID_PASSWORD')

user_wrong_password = '222222'

bstack_user_name = os.getenv('BS_USERNAME')
bstack_access_key = os.getenv('BS_ACCESSKEY')
bstack_platform_version = os.getenv('PLATFORM_VERSION')
bstack_device_name = os.getenv('DEVICE_NAME')


def to_driver_options():
    options = UiAutomator2Options()

    if context == 'local_emulator':
        options.set_capability('app', app)
        options.set_capability('udid', device_udid)

    elif context == 'local_real':
        options.set_capability('app', app)
        options.set_capability('udid', device_udid)

    elif context == 'bstack':
        options.set_capability('app', app)
        options.set_capability('deviceName', bstack_device_name)
        options.set_capability('platform_version', bstack_platform_version)
        options.set_capability(
            'bstack:options', {
                'projectName': 'homework_19',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack K31 tests',

                'userName': bstack_user_name,
                'accessKey': bstack_access_key,
            },
        )

    return options
