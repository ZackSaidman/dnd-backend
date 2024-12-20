import json

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        sender = body.get("sender")
        content = body.get("content")

        if not sender or not content:
            raise ValueError("Invalid input: 'sender' and 'content' are required.")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Received message from {sender}: {content}"
            }),
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)}),
        }