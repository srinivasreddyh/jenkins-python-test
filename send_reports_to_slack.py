from slackclient import SlackClient

sc = SlackClient('slack_legacy_token')

sc.api_call("files.upload", filename='final_cl_reports', \
    channels='#jenkin_slack_notifier', username='srinivas_reddy_h', \
    file=open('/path/to/file/filename.txt', 'r').read())
