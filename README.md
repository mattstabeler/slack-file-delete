# Delete files from slack

The script automatically deletes your most recent 50 files, older than 10 days.


# Setup

Give execute permissions to the file `deleteoldfiles.py`
```
chmod +x deleteoldfiles.py
```

Get a Legacy token for your workspace here: https://api.slack.com/custom-integrations/legacy-tokens

Create `secrets.conf` with your token


```
[slack]
token : slacktokenxxxxxx
```

# Run
In terminal run the following command
```
./deleteoldfiles.py
```

