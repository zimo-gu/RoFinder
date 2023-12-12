![Python](https://a11ybadges.com/badge?logo=python)
![Roblox](https://a11ybadges.com/badge?logo=roblox)

# RoFinder - Roblox Group Finder

RoFinder is a Python script that helps you discover unclaimed Roblox groups by randomly checking group IDs. The script utilizes the Roblox API to determine whether a group is publicly accessible and unowned, allowing you to find potential groups to claim.

## How to Use

1. **Setup:**
   - Ensure you have Python installed on your system.
   - Clone this repository to your local machine.

2. **Dependencies:**
   - Install the required Python packages using the following command:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuration:**
   - Create a `.env` file and set your Discord webhook URL as `DISCORD_WEBHOOK`.
     ```
     DISCORD_WEBHOOK=https://your-discord-webhook-url
     ```

4. **Run the Script:**
   - Execute the main script using the following command:
     ```bash
     python main.py
     ```
   - The script will continuously check random group IDs and notify you through Discord when it finds an unclaimed group.

## Code Claiming

This project is proudly created by [RXNationGaming](https://github.com/RXNationGMG). Feel free to use, modify, and contribute to the project. If you have any questions or suggestions, please open an issue on the GitHub repository.

**Note:** Use this script responsibly and in compliance with Roblox's terms of service. Claiming groups should be done ethically and within the guidelines set by the Roblox platform.

---

*RoFinder | By: RXNationGaming*
