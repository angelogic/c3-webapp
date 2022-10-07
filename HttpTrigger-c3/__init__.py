import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info(
        'Python ServiceBus queue trigger processed message: %s', notification_id)

    # TODO: Get connection to database
    # Update connection string information
    host = "techconfdb-udacity.postgres.database.azure.com"
    dbname = "techconfdb-udacity"
    user = "chauadmin@techconfdb-udacity"
    password = "Post@chou88"
    sslmode = "require"
    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    ("Connection established")
    cursor = conn.cursor()
    try:
        # TODO: Get notification message and subject from database using the notification_id
       cursor.execute("SELECT message FROM notification;")
       cursor.execute("SELECT subject FROM notification;")
       rows = cursor.fetchall()
       for row in rows:
        print("Data row = (%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))
        # TODO: Get attendees email and name

        # Fetch all rows from table
       cursor.execute("SELECT email FROM attendee;")
       cursor.execute("SELECT name FROM attendee;")
       rows = cursor.fetchall()

# Print all rows

       for row in rows:
        print("Data row = (%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))
        # TODO: Loop through each attendee and send an email with a personalized subject

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
    finally:
        # TODO: Close connection
        # Clean up
     conn.commit()
     cursor.close()
     conn.close()
