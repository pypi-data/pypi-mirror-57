# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['eufy_security']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp==3.6.1']

setup_kwargs = {
    'name': 'python-eufy-security',
    'version': '0.3.0',
    'description': 'A Python library for Eufy Security devices',
    'long_description': '# python-eufy-security\n\nThis is an experimental Python library for Eufy Security devices (cameras, doorbells, \netc.).\n\n# Python Versions\n\nThe library is currently supported on\n\n* Python 3.6\n* Python 3.7\n\n# Installation\n\nTBD\n\n# Account Information\n\nBecause of the way the Eufy Security private API works, an email/password combo cannot\nwork with _both_ the Eufy Security mobile app _and_ this library. It is recommended to\nuse the mobile app to create a secondary "guest" account with a separate email address\nand use it with this library.\n\n# Usage\n\nEverything starts with an:\n[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n        # YOUR CODE HERE\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nLogin and get to work:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom eufy_security import async_login\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n        # Create an API client:\n        api = await async_login(EUFY_EMAIL, EUFY_PASSWORD, websession)\n\n        # Loop through the cameras associated with the account:\n        for camera in api.cameras.values():\n            print("------------------")\n            print("Camera Name: %s", camera.name)\n            print("Serial Number: %s", camera.serial)\n            print("Station Serial Number: %s", camera.station_serial)\n            print("Last Camera Image URL: %s", camera.last_camera_image_url)\n\n            print("Starting RTSP Stream")\n            stream_url = await camera.async_start_stream()\n            print("Stream URL: %s", stream_url)\n\n            print("Stopping RTSP Stream")\n            stream_url = await camera.async_stop_stream()\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nCheck out `example.py`, the tests, and the source files themselves for method\nsignatures and more examples.\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/FuzzyMistborn/python-eufy-security/issues)\n  or [initiate a discussion on one](https://github.com/FuzzyMistborn/python-eufy-security/issues/new).\n2. [Fork the repository](https://github.com/FuzzyMistborn/python-eufy-security/fork).\n3. Install the dev environment: `make init`.\n4. Enter the virtual environment: `source ./venv/bin/activate`\n5. Code your new feature or bug fix.\n6. Write a test that covers your new functionality.\n7. Update `README.md` with any new documentation.\n8. Run tests and ensure 100% code coverage: `make coverage`\n9. Ensure you have no linting errors: `make lint`\n10. Ensure you have typed your code correctly: `make typing`\n11. Submit a pull request!\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'url': 'https://github.com/FuzzyMistborn/python-eufy-security',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
