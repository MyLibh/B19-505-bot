import datetime

def Log(msg, type = 'Info'):
    now = datetime.datetime.now()
    log_msg = '<' + now.strftime("%Y-%m-%d %H:%M") + '> [' + type + '] {' + msg + '}'
    print(log_msg)

    # with open('logs/log-' + now.strftime("%Y-%m-%d") + '.log', 'a', encoding='utf-8') as log:
    #     log.write(log_msg);
    #     log.write('\n')

