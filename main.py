import os
import requests

def resend(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    target_url = os.environ.get('TARGET_URL')
    resp = requests.post(target_url, data = event['data'])

    print(resp.status_code)

