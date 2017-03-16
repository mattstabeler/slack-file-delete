# Delete files from slack

The script automaticallys gets your unique id from the API, and then deletes the most recent 50 files, older than 10 days.


# Setup

Create `secrets.conf` with a token from slack: https://api.slack.com/docs/oauth-test-tokens


```
[slack]
token : slacktokenxxxxxx
```

# Run
then run `./deleteoldfiles.py`
