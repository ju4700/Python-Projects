import argparse
import json
import os
import time
import urllib.request

# Constants for caching
CACHE_DIR = "./cache"
CACHE_EXPIRY = 60 * 60  # Cache expires after 1 hour

# Fetch GitHub activity function with caching
def fetch_github_activity(username):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    cache_file = f"{CACHE_DIR}/{username}.json"

    # Check if cached file exists and is valid
    if os.path.exists(cache_file) and (time.time() - os.path.getmtime(cache_file)) < CACHE_EXPIRY:
        with open(cache_file, "r") as file:
            print("Using cached data.")
            return json.load(file)

    url = f"https://api.github.com/users/{username}/events"

    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                events = json.loads(data)

                # Save to cache
                with open(cache_file, "w") as file:
                    json.dump(events, file)

                return events
            else:
                print(f"Error: Received HTTP {response.status}")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Display activity with filtering and formatting
def display_activity(events, event_type=None, output_format="text"):
    if not events:
        print("No recent activity found or an error occurred.")
        return

    activity_summary = {}

    for event in events:
        if event_type and event["type"] != event_type:
            continue

        event_type = event.get("type", "Unknown Event")
        repo_name = event["repo"]["name"] if "repo" in event else "Unknown Repo"
        
        if event_type == "PushEvent":
            commits = len(event["payload"]["commits"])
            key = f"Pushed commits to {repo_name}"
            activity_summary[key] = activity_summary.get(key, 0) + commits
        elif event_type == "CreateEvent":
            description = f"Created a new {event['payload']['ref_type']} in {repo_name}"
            activity_summary[description] = activity_summary.get(description, 1)
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            description = f"{action.capitalize()} an issue in {repo_name}"
            activity_summary[description] = activity_summary.get(description, 1)
        elif event_type == "WatchEvent":
            description = f"Starred {repo_name}"
            activity_summary[description] = activity_summary.get(description, 1)
        else:
            description = f"{event_type} in {repo_name}"
            activity_summary[description] = activity_summary.get(description, 1)

    if not activity_summary:
        print(f"No events found for type: {event_type}")
        return

    if output_format == "json":
        print(json.dumps(activity_summary, indent=4))
    elif output_format == "table":
        try:
            from tabulate import tabulate
            table = [[key, count] for key, count in activity_summary.items()]
            print(tabulate(table, headers=["Activity", "Count"]))
        except ImportError:
            print("Tabulate library not installed. Please install it using `pip install tabulate`.")
            print(json.dumps(activity_summary, indent=4))
    else:
        print("\nRecent Activity Summary:")
        for activity, count in activity_summary.items():
            if count > 1:
                print(f"- {activity} ({count} times)")
            else:
                print(f"- {activity}")

# Main function to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity for a user.")
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("--event-type", help="Filter by specific event type (e.g., PushEvent)")
    parser.add_argument("--output-format", choices=["text", "json", "table"], default="text", help="Output format (text, json, table)")
    args = parser.parse_args()

    username = args.username
    event_type = args.event_type
    output_format = args.output_format

    print(f"Fetching recent activity for GitHub user: {username}")
    events = fetch_github_activity(username)
    display_activity(events, event_type, output_format)

if __name__ == "__main__":
    main()
