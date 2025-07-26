import os
import tempfile
import pytest
import base64
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Global variable for html plugin
pytest_html = None

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-cache")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disk-cache-size=0")

    temp_user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_user_data_dir}")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

# Capture plugin for pytest-html
@pytest.fixture(autouse=True)
def inject_html_plugin(request):
    global pytest_html
    pytest_html = request.config.pluginmanager.getplugin("html")

# Hook to embed base64 screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Save screenshot
            driver.save_screenshot(file_path)

            # Read and encode screenshot
            with open(file_path, "rb") as image_file:
                encoded_screenshot = base64.b64encode(image_file.read()).decode("utf-8")

            # Attach to HTML report
            extra = getattr(rep, "extra", [])
            html_img = f'<div><img src="data:image/png;base64,{encoded_screenshot}" alt="screenshot" style="width:400px;height:auto;" onclick="window.open(this.src)" /></div>'
            extra.append(pytest_html.extras.html(html_img))
            rep.extra = extra
