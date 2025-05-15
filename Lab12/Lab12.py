import requests
import json
from datetime import datetime


def save_output(method, url, request_headers=None, request_body=None, response=None):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output_{method}_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"=== {method} Request to {url} ===\n\n")

        if method in ['GET', 'POST']:
            f.write("=== REQUEST DETAILS ===\n")
            f.write(f"Request Method: {method}\n")
            f.write(f"Request URL: {url}\n")

            if request_headers:
                f.write("\nRequest Headers:\n")
                for key, value in request_headers.items():
                    f.write(f"{key}: {value}\n")

            if request_body and method == 'POST':
                f.write("\nRequest Body:\n")
                if isinstance(request_body, dict):
                    f.write(json.dumps(request_body, indent=2))
                else:
                    f.write(str(request_body))
                f.write("\n")

        if response:
            f.write("\n=== RESPONSE DETAILS ===\n")
            f.write(f"Status Code: {response.status_code}\n")

            f.write("\nResponse Headers:\n")
            for key, value in response.headers.items():
                f.write(f"{key}: {value}\n")

            f.write("\nResponse Body:\n")
            try:
                json_data = response.json()
                f.write(json.dumps(json_data, indent=2))
            except ValueError:
                f.write(response.text)

    print(f"Output saved to {filename}")
    return filename


def http_options(url):
    try:
        print(f"\nSending OPTIONS request to {url}")
        response = requests.options(url)
        return save_output('OPTIONS', url, response=response)
    except Exception as e:
        print(f"Error in OPTIONS request: {e}")
        return None


def http_get(url, headers=None):
    try:
        print(f"\nSending GET request to {url}")
        response = requests.get(url, headers=headers)
        return save_output('GET', url,
                           request_headers=headers,
                           response=response)
    except Exception as e:
        print(f"Error in GET request: {e}")
        return None


def http_post(url, data=None, headers=None):
    try:
        print(f"\nSending POST request to {url}")
        if headers and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'
            data = json.dumps(data) if data else None

        response = requests.post(url, data=data, headers=headers)
        return save_output('POST', url,
                           request_headers=headers,
                           request_body=data,
                           response=response)
    except Exception as e:
        print(f"Error in POST request: {e}")
        return None


def main():
    base_url = "https://httpbin.org/"
    opt_file = http_options(base_url)
    get_file = http_get(base_url)

    post_data = {
        "title": "Sample Post",
        "body": "This is a test post",
        "userId": 1
    }
    post_headers = {
        "User-Agent": "HTTP Client Program"
    }
    post_file = http_post(base_url, data=post_data, headers=post_headers)

    print("\nExecution complete. Check the output files for results.")


if __name__ == "__main__":
    main()
