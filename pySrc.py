import argparse

from flask import Flask

import routes

parser = argparse.ArgumentParser('pySrc')
parser.add_argument('--host', type=str, default='0.0.0.0')
parser.add_argument('--port', type=int, default=4000)
parser.add_argument('--title', type=str, default='pySrc')


def main():
    config = parser.parse_args()

    app = Flask('pySrc')
    routes.route_all(app, config)
    app.run(host=config.host, port=config.port)


if __name__ == '__main__':
    main()
