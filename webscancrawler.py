import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class WebScanCrawler:
    def __init__(self, start_url, max_depth=3):
        self.start_url = start_url
        self.visited_urls = set()  # array of visited_urls
        self.vulnerabilities = []
        self.max_depth = max_depth

    def crawl(self, url, depth=0):   # this method visits all pages starting from given url
        if url in self.visited_urls or depth>self.max_depth:
            return
        self.visited_urls.add(url)

        try:
            response = requests.get(url, timeout=10)   #fetches the content of url
            if response.status_code != 200:
                print(f"Failed to fetch {url}: Status code {response.status_code}")
                return

            # checks for vulnerabilities
            self.check_security_headers(response.headers, url)  # checks for missing http security headers like Strict-Transport-Security
            self.check_outdated_software(response.text, url)   # checks for outdated software like Apache 2.4.6 in html content
            self.check_forms(response.text, url)   # checks forms for insecure method="GET"

            # Parse the page and extract links
            soup = BeautifulSoup(response.text, "html.parser")   # uses the BeautifulSoup library to parse the html content of a webpage
            for link in soup.find_all("a", href=True):   # finds all anchor tags in html with href attribute
                full_url = urljoin(url, link["href"])   # link["href"] gives us the relative url or absolute url but urljoin combines the base url with the relative url to generate a full url
                if full_url.startswith(self.start_url):  # ensure we stay on the same domain
                    self.crawl(full_url)     # recursively calls the crawl method

        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")

    def check_security_headers(self, headers, url):
        """Check for missing security headers."""
        required_headers = [
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Content-Security-Policy",
        ]
        for header in required_headers:
            if header not in headers:
                self.vulnerabilities.append(f"MISSING HTTP SECURITY HEADER: {header} on {url}")

    def check_outdated_software(self, html, url):
        """Check for outdated software versions."""
        # example Check for outdated Apache version
        if "Apache/2.4.6" in html:
            self.vulnerabilities.append(f"OUTDATED SOFTWARE VERSION DETECTED: Apache 2.4.6 on {url}")

    def check_forms(self, html, url):
        """Check for forms with missing or insecure attributes."""
        soup = BeautifulSoup(html, "html.parser")
        for form in soup.find_all("form"):
            action = form.get("action", "")
            method = form.get("method", "").upper()

            if not action:
                self.vulnerabilities.append(f"FORM WITHOUT ACTION ATTRIBUTE: {url}")
            if method == "GET":
                self.vulnerabilities.append(f"FORM WITH INSECURE METHOD (GET): {url}")

    def generate_report(self):
        """Generate a vulnerability report."""
        report = f"Green Tick Technical Assessment\nVULNERABILITY SCAN REPORT FOR {self.start_url}:\n"
        for vulnerability in self.vulnerabilities:
            report += f"- {vulnerability}\n"
        return report

# Example usage
if __name__ == "__main__":
    start_url = input("https://www.sophiebritt.com/").strip()
    crawler = WebScanCrawler(start_url)
    crawler.crawl(start_url)
    print(crawler.generate_report())