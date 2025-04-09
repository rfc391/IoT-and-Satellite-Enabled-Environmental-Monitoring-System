
import argparse
from environment_monitoring.main import main as run_main

def main():
    parser = argparse.ArgumentParser(description="IoT & Satellite Environmental Monitoring CLI")
    parser.add_argument('--start', action='store_true', help='Start the monitoring system')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    parser.add_argument('--offline', action='store_true', help='Launch in offline/airgap mode')
    args = parser.parse_args()

    if args.start:
        print("[+] Starting system...")
        run_main()
    elif args.debug:
        print("[*] Starting in DEBUG mode...")
        run_main(debug=True)
    elif args.offline:
        print("[*] Launching in offline mode...")
        run_main(offline=True)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
