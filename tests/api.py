import time
from dotenv import load_dotenv
import os

conn = ''


def configure():
    load_dotenv()


def main():

    configure()

    # Returns `default_value` if the key doesn't exist
    proj = os.environ.get('working_env', 'local')

    if proj == 'remote':
        print("remote")
        with open('/run/secrets/db_conn') as f:
            conn = f.readlines()[0]
            print(conn)
    else:
        print("local")
        print(os.getenv('conn'))

    while True:
        time.sleep(3)
        print("x")


if __name__ == "__main__":
    main()
