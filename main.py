from webserver import keep_alive
import requests

channelID = 797073867591516170
headers = {
    "authorization":
    "Nzg0MzY0Nzg3MzExMTgxODU0.GqUTGp.e955UFBCArxCK3i7UN3_vZvYl-vrNKrvLGko9Y"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
