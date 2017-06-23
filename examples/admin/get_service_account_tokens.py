# [START get_service_account_tokens]
from firebase_admin import credentials

cred = credentials.Certificate('path/to/serviceAccountKey.json')
access_token_info = cred.get_access_token()

access_token = access_token_info.access_token
expiration_time = access_token_info.expiry
# Attach access_token to HTTPS request in the "Authorization: Bearer" header
# After expiration_time, you must generate a new access token
# [END get_service_account_tokens]

print('The access token {} expires at {}'.format(access_token, expiration_time))
