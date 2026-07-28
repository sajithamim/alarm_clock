# Python CLI Alarm Clock

## Design Decisions

- Used threading for background alarm monitoring
- Separated CLI and business logic
- Used JSON storage for simplicity
- Used datetime module for time comparison

## Architecture

User
 |
CLI
 |
Alarm Manager
 |
Scheduler
 |
Alarm Trigger

## Installation

Clone the repository:

git clone https://github.com/sajithamim/alarm_clock

Run the application:

python main.py
