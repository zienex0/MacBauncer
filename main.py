from services.app_block import block_mac_app, unblock_mac_app
import argparse

def main(apps):
    for app_name in apps:
        block_mac_app(app_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Block or unblock macOS application.')
    parser.add_argument('-app', '--application', nargs='+', help='Application name on your macOS. E.g. "Spotify".')

    args = parser.parse_args()
    main(args.application)
