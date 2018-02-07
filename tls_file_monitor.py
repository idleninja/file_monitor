#!/usr/bin/python
import time, os, logging, logging.handlers
from datetime import datetime


syslog_server = ""
syslog_port = 15514


# Setup logger and handler.
myLogger = logging.getLogger("mylogger")
myLogger.setLevel(logging.INFO)
handler = logging.handlers.SysLogHandler(address = (syslog_server,syslog_port))
myLogger.addHandler(handler)



def main():
    sendAlert = False
    tls_file = "/path/to/file"
    event_timestamp = datetime.now().isoformat()
    event_host = os.uname()[1]

    # Does the tls file even exist?
    if os.path.isfile(tlsdomains_file):
        last_modifed_epoch = os.stat(tlsdomains_file).st_mtime
        last_modifed_fdisplay = time.strftime("%Y-%m-%d", time.localtime(last_modifed_epoch))

        d1 = datetime.fromtimestamp(last_modifed_epoch)
        d2 = datetime.now()
        days_old = (d2 - d1).days

        # Send trickle status event once a day.
        if (datetime.now()).hour == 23:
            sendAlert = True
            event_message = 'event_timestamp="%s",host="%s",file_path="%s",file_last_modified="%s",file_exists="true"' % (event_timestamp,event_host,tls_file,last_modifed_fdisplay)



    # tls file indeed is missing! ZOMG!
    else:
        # File not found, send alert!
        sendAlert = True
        event_message = 'event_timestamp="%s",host="%s",file_path="%s",file_last_modified="%s",file_exists="false"' % (event_timestamp,event_host,tls_file,"-")

    # Now send the alert.
    if sendAlert:
        myLogger.info(event_message)
        #m = MailServer()
        #m.sendMail(alert_subject, alert_body, fromAddr=alert_from, toAddr=alert_to)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        print("^C")
        exit()
