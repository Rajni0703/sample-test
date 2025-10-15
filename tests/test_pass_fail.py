"""
COMPLETE DEMO SUITE - With all required imports
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest

class TestDemoSuite:
    
    def setup_method(self):
        """Setup before each test"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Auto-manage ChromeDriver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    
    def teardown_method(self):
        """Cleanup after each test"""
        self.driver.quit()
    
    # ========== PASSING TESTS ==========
    
    def test_google_title_correct(self):
        """PASS: Verify Google title"""
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

    def test_example_domain_accessible(self):
        """PASS: Example domain loads successfully"""
        self.driver.get("https://example.com")
        assert "Example" in self.driver.title

    # ========== FAILING TESTS ==========
    
    def test_wrong_google_title(self):
        """FAIL: Wrong title expectation"""
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Wrong Title", f"Expected 'Wrong Title' but got '{self.driver.title}'"

    def test_element_that_doesnt_exist(self):
        """FAIL: Element not found"""
        self.driver.get("https://example.com")
        self.driver.find_element(By.ID, "this-id-does-not-exist-12345")