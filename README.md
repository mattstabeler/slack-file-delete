# Delete files from slack

Create `secrets.conf` with a token from slack: https://api.slack.com/docs/oauth-test-tokens

Work our your unique userid and add to the config.

```
[slack]
token : slacktokenxxxxxx
user : userid
```

then run `./deleteoldfiles.py`

