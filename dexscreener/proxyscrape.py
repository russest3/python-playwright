import requests
import base64
name = "dexscreener_tokens"

def get_page_contents(url):
    data = {
        "url": url,
        "browserHtml": True
    }

    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': ''
    }

    start_url = 'https://api.proxyscrape.com/v3/accounts/freebies/scraperapi/request'
    response = requests.post(start_url, headers=headers, json=data)

    if response.status_code == 200:
        json_response = response.json()
        if 'browserHtml' in json_response['data']:
            html = json_response['data']['browserHtml']
        else:
            html = base64.b64decode(json_response['data']['httpResponseBody']).decode()
    else:
        print("Error:", response.status_code)

    with open(name + '.html', "w") as file:
        file.write(html)
    return html