import datetime

file = open(f'Debug/log_'
            f'{str(datetime.datetime.now()).replace(" ", "_").replace(".", "-").replace(":", "-")}.log', 'w')
counter = 0


def log(text, name='undefined'):
    global counter
    counter += 1
    file.write(f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:'
               f'{datetime.datetime.now().second}.{datetime.datetime.now().microsecond}'
               f' - {name}, {counter} - {text}\n')
    print(f'{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:'
          f'{datetime.datetime.now().second}.{datetime.datetime.now().microsecond} - {name}, {counter} - {text}\n')


log('Started', 'debugger.py')
