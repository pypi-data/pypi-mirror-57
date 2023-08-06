import requests


def trigger_build(project: str, api_key: str, branch: str) -> None:

    headers = {
        'X-API-Token': api_key,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    url = f'https://api.appcenter.ms/v0.1/apps/celadon/{project}/branches/{branch}/builds'

    print(f'Fetching {url}')
    response = requests.post(
        url,
        headers=headers
    )
    print(f'Response: {response.json()}')
