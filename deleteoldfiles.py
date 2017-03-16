#!/usr/local/bin/python
import urllib, json, time
import os, ConfigParser


# Token https://api.slack.com/docs/oauth-test-tokens
# find files older than X and delete them

token = None
user = None

def main():
    global token
    global user
    olderthan = 10
    numberoffiles = 50

    config = load_config()

    if config.has_section('slack'):
        if(config.has_option('slack', 'token')):
            token = config.get('slack', 'token')
        if(config.has_option('slack', 'user')):
            user = config.get('slack', 'user')

    if token is not None or user is not None:
        delete_files(olderthan, numberoffiles)

def load_config(path=None):

    if path:
        configfile = path
    else:
        configfile =  os.path.expanduser('secrets.conf')

    config = ConfigParser.RawConfigParser()
    try:
        config.read(configfile)
    except Exception as e:
        print "Unable to read config file at {}: {}".format(configfile, e)

    return config

def file_list(daysago=100, filecount=1):
    ts = long(time.time()) - (60 * 60 * daysago)
    url = "https://slack.com/api/files.list?token={}&user={}&ts_to={}&count={}".format(token, user, ts, filecount)
    return call(url)


def delete_files(olderthan, numberoffiles):
    print "Deleting up to {} files older than {} days".format(numberoffiles, olderthan)
    files = file_list(olderthan, numberoffiles)

    if len(files['files']) == 0:
        print "No files found"
    for file in files['files']:
        resp = delete_file(file['id'])
        if resp['ok']:
            print "Deleted {} : {}".format(file['id'], file['permalink'])
        elif resp['error']:
            print "ERROR: {} when deleting: {} : {}".format(resp['error'], file['id'], file['permalink'])

def delete_file(file_id):
    url = "https://slack.com/api/files.delete?token={}&file={}".format(token, file_id)
    return call(url)

def list_users():
    url = "https://slack.com/api/users.list?token={}&count=500".format(token)
    return call(url)

def call(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data


if __name__ == "__main__":
    main()
