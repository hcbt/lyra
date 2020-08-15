#!/usr/bin/env python3

import os
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube"]

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

ROOT_DIR = os.path.dirname(os.path.abspath("../../setup.py"))

def api_auth():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = ROOT_DIR + "/lyra/lyra/auth/client_secret.json"
    credentials_pickle_file = ROOT_DIR + "/lyra/lyra/auth/credentials"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)

    if os.path.exists(credentials_pickle_file):
        with open(credentials_pickle_file, 'rb') as f:
            credentials = pickle.load(f)
    else:
        credentials = flow.run_console()
        with open(credentials_pickle_file, 'wb') as f:
            pickle.dump(credentials, f)

    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    return youtube