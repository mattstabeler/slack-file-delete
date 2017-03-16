# Delete files from slack

The script automatically deletes your most recent 50 files, older than 10 days.


# Setup

Create `secrets.conf` with a token from slack: https://api.slack.com/docs/oauth-test-tokens

```
[slack]
token : slacktokenxxxxxx
```

# Run
`chmod +x deleteoldfiles.py` then run `./deleteoldfiles.py`
