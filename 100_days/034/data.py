import requests

session_token = ""
BASE_URL = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_session_token():
    """Fetches a new session token."""
    global session_token
    try:
        response = requests.get("https://opentdb.com/api_token.php?command=request")
        session_token = response.json()['token']
    except requests.exceptions.HTTPError as err:
        print(err)


def get_questions():
    """Fetches 10 new boolean questions from the API."""
    global session_token

    url = f"{BASE_URL}&token={session_token}"

    try:
        response = requests.get(url)
        response_json = response.json()
        response_code = response_json['response_code']

        if response_code == 3 or response_code == 4:
            get_session_token()
            return get_questions()

        return response_json['results']

    except requests.exceptions.HTTPError as err:
        print(err)
        return []


question_data = get_questions()