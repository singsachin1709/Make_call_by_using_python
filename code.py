from twilio.rest import Client

client = Client("ACCOUNT_SID", "AUTH_TOKEN")

call = client.calls.create(
    twiml='<Response><Say>Hello! This is an automated Python call 🚀</Say></Response>',
    to="+919876543210",
    from_="+1234567890"
)

print("✅ Call initiated! SID:", call.sid)
