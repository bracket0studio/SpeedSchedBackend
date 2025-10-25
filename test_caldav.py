from caldav import DAVClient, Calendar
from datetime import datetime, timedelta
import time

total_start_time = time.time()

step_start_time = time.time()

client = DAVClient(
    'https://caldav.icloud.com',
    username='mondchchanun@gmail.com',
    password='vhje-mfsc-mppr-kfac'
)


connection_time = time.time() - step_start_time
print(f"Time to establish connection: {connection_time:.4f} seconds")

# Step 2: Fetch Principal
step_start_time = time.time()
principal = client.principal()
fetch_principal_time = time.time() - step_start_time
print(f"Time to fetch principal: {fetch_principal_time:.4f} seconds")

# Step 3: Fetch Calendars
step_start_time = time.time()
calendars = principal.calendars()
fetch_calendars_time = time.time() - step_start_time
print(f"Time to fetch calendars: {fetch_calendars_time:.4f} seconds")

if not calendars:
    print("No calendars found.")
else:
    calendar = calendars[0]

    # Prepare event data
    start = datetime.now()
    end = start + timedelta(hours=1)  # 1-hour event
    event_data = (
        "BEGIN:VCALENDAR\n"
        "VERSION:2.0\n"
        "BEGIN:VEVENT\n"
        "UID:example1234@example.com\n"
        f"DTSTAMP:{start.strftime('%Y%m%dT%H%M%SZ')}\n"
        f"DTSTART:{start.strftime('%Y%m%dT%H%M%SZ')}\n"
        f"DTEND:{end.strftime('%Y%m%dT%H%M%SZ')}\n"
        "SUMMARY:Dinner with Krit\n"
        "DESCRIPTION:Meeting at the restaurant.\n"
        "END:VEVENT\n"
        "END:VCALENDAR"
    )

    # Step 4: Add Event
    step_start_time = time.time()
    try:
        calendar.add_event(event_data)
        add_event_time = time.time() - step_start_time
        print("Event added successfully.")
        print(f"Time to add event: {add_event_time:.4f} seconds")
    except Exception as e:
        print("Error adding event:", e)

# Calculate total elapsed time
total_elapsed_time = time.time() - total_start_time
print(f"Total elapsed time: {total_elapsed_time:.4f} seconds")
