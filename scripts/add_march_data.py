#!/usr/bin/env python3
"""
Script to add March 2026 weather and central board messages to field.db
Following the patterns established in February data
"""

import sqlite3
import os

# Path to database
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'field.db')

# Weather data for March 2026 (31 days)
# Early spring with mixed rain, sun, and gradual warming
weather_data = [
    ('2026-03-01', 'Light rain', 6.0, 60, 'March arrives damp and mild'),
    ('2026-03-02', 'Overcast', 5.5, 45, 'Low clouds drift all day'),
    ('2026-03-03', 'Rain showers', 7.0, 70, 'Passing showers sweep through'),
    ('2026-03-04', 'Windy', 6.5, 50, 'Gusts rattle the greenhouse'),
    ('2026-03-05', 'Partly cloudy', 7.5, 30, 'Sun breaks between clouds'),
    ('2026-03-06', 'Clear', 8.0, 20, 'Bright morning, cool night'),
    ('2026-03-07', 'Light drizzle', 6.0, 55, 'Soft rain settles in'),
    ('2026-03-08', 'Fog', 4.5, 40, 'Morning fog, slow to lift'),
    ('2026-03-09', 'Sunny', 9.0, 15, 'First true springlike day'),
    ('2026-03-10', 'Cloudy', 7.0, 35, 'Muted light across the field'),
    ('2026-03-11', 'Rain', 6.5, 65, 'Steady rain for most of the day'),
    ('2026-03-12', 'Clear and cold', 3.5, 20, 'Chilly dawn after the rain'),
    ('2026-03-13', 'Partly sunny', 8.5, 25, 'Mild afternoon warmth'),
    ('2026-03-14', 'Overcast', 7.0, 40, 'Gray returns, softer now'),
    ('2026-03-15', 'Light rain', 6.0, 60, 'Gentle rain on early buds'),
    ('2026-03-16', 'Sunny intervals', 9.5, 30, 'Sun and clouds trade places'),
    ('2026-03-17', 'Breezy', 8.0, 35, 'St. Patrick wind in the trees'),
    ('2026-03-18', 'Clear', 10.0, 20, 'Blue sky and longer light'),
    ('2026-03-19', 'Rain showers', 8.5, 55, 'Quick showers, then sun'),
    ('2026-03-20', 'Partly cloudy', 10.5, 25, 'Equinox arrives with balance'),
    ('2026-03-21', 'Sunny', 11.0, 15, 'Warm afternoon, cool night'),
    ('2026-03-22', 'Overcast', 9.0, 40, 'Clouds settle without rain'),
    ('2026-03-23', 'Light drizzle', 8.0, 50, 'Moisture hangs in the air'),
    ('2026-03-24', 'Clear', 11.5, 20, 'Crisp morning, bright day'),
    ('2026-03-25', 'Rain', 9.0, 70, 'Soaking rain for the beds'),
    ('2026-03-26', 'Partly sunny', 10.0, 30, 'Sun returns after rain'),
    ('2026-03-27', 'Windy', 9.5, 45, 'Gusts tug at covers'),
    ('2026-03-28', 'Sunny', 12.0, 20, 'Warmest day so far'),
    ('2026-03-29', 'Cloudy', 10.5, 35, 'Soft light, steady mild'),
    ('2026-03-30', 'Light rain', 9.5, 55, 'April-like drizzle'),
    ('2026-03-31', 'Partly cloudy', 11.0, 25, 'Month closes with gentle warmth')
]

# Central board messages for March 2026
# 3 messages per day (morning ~8am, midday ~12pm, evening ~5-6pm)
# Authors: Ivy (morning), Noor (midday), Rae (evening)
messages_data = [
    # Mar 1
    ('2026-03-01 08:12:00', 'Ivy', 'Rain taps the shed roof; March opens with a steady rhythm.'),
    ('2026-03-01 12:24:00', 'Noor', 'We map out March tasks and shift seedlings into brighter light.'),
    ('2026-03-01 17:40:00', 'Rae', 'Damp dusk settles in; the month begins softly.'),
    # Mar 2
    ('2026-03-02 08:18:00', 'Ivy', 'Clouds hang low, keeping the morning quiet and gray.'),
    ('2026-03-02 12:32:00', 'Noor', 'We mix fresh soil for new trays, warm and earthy.'),
    ('2026-03-02 17:28:00', 'Rae', 'Evening stays muted; no shadows to mark the hour.'),
    # Mar 3
    ('2026-03-03 08:10:00', 'Ivy', 'Showers pass in bursts; puddles shimmer and vanish.'),
    ('2026-03-03 12:45:00', 'Noor', 'We check drainage ditches before the next rain band.'),
    ('2026-03-03 17:50:00', 'Rae', 'Air smells of wet soil; the field drinks deeply.'),
    # Mar 4
    ('2026-03-04 08:25:00', 'Ivy', 'Wind rattles the fence line; morning arrives restless.'),
    ('2026-03-04 12:30:00', 'Noor', 'We secure row covers and tighten greenhouse latches.'),
    ('2026-03-04 17:18:00', 'Rae', 'Gusts fade at dusk; calm returns in slow waves.'),
    # Mar 5
    ('2026-03-05 08:20:00', 'Ivy', 'Sun slips between clouds, bright and brief.'),
    ('2026-03-05 12:22:00', 'Noor', 'We harden off a few trays outside, testing the air.'),
    ('2026-03-05 17:35:00', 'Rae', 'Light lingers longer; evening feels less hurried.'),
    # Mar 6
    ('2026-03-06 08:15:00', 'Ivy', 'Clear morning, crisp edges on every leaf.'),
    ('2026-03-06 12:40:00', 'Noor', 'We turn compost and watch steam rise in the sun.'),
    ('2026-03-06 17:42:00', 'Rae', 'A clean sunset; the day ends bright and calm.'),
    # Mar 7
    ('2026-03-07 08:28:00', 'Ivy', 'Drizzle returns, soft as a whisper on the soil.'),
    ('2026-03-07 12:36:00', 'Noor', 'We prep seed packets, lining them up by planting week.'),
    ('2026-03-07 17:30:00', 'Rae', 'Mist hangs low; twilight feels close.'),
    # Mar 8
    ('2026-03-08 08:05:00', 'Ivy', 'Fog wraps the field; even the trees seem hushed.'),
    ('2026-03-08 12:25:00', 'Noor', 'We label new flats, careful and slow in the dim light.'),
    ('2026-03-08 17:48:00', 'Rae', 'Fog lifts late; the day ends with a pale glow.'),
    # Mar 9
    ('2026-03-09 08:22:00', 'Ivy', 'Sunlight spills across the field; it feels like a gift.'),
    ('2026-03-09 12:20:00', 'Noor', 'We open the greenhouse doors for air and warmth.'),
    ('2026-03-09 17:55:00', 'Rae', 'Evening stays gentle; spring feels closer tonight.'),
    # Mar 10
    ('2026-03-10 08:14:00', 'Ivy', 'Clouds soften the morning; light is diffuse and calm.'),
    ('2026-03-10 12:34:00', 'Noor', 'We start onions and leeks, tiny seeds in careful rows.'),
    ('2026-03-10 17:36:00', 'Rae', 'Gray light fades; the field rests in quiet tones.'),
    # Mar 11
    ('2026-03-11 08:18:00', 'Ivy', 'Rain beats steady; the day begins with its own drum.'),
    ('2026-03-11 12:48:00', 'Noor', 'We work indoors, mending trays and sorting labels.'),
    ('2026-03-11 17:33:00', 'Rae', 'Rain continues at dusk; the world is all water and soil.'),
    # Mar 12
    ('2026-03-12 08:08:00', 'Ivy', 'Clear sky but cold air; the rain left a chill behind.'),
    ('2026-03-12 12:29:00', 'Noor', 'We move tender starts away from drafts and keep them warm.'),
    ('2026-03-12 17:47:00', 'Rae', 'A sharp sunset, colors crisp against the cold.'),
    # Mar 13
    ('2026-03-13 08:26:00', 'Ivy', 'Morning sun peeks through; the ground loosens a little.'),
    ('2026-03-13 12:18:00', 'Noor', 'We sow herbs today, small scents for the coming weeks.'),
    ('2026-03-13 17:52:00', 'Rae', 'Mild evening light stretches toward the horizon.'),
    # Mar 14
    ('2026-03-14 08:30:00', 'Ivy', 'Clouds roll back in, softening every edge.'),
    ('2026-03-14 12:42:00', 'Noor', 'We tidy the tool shed, making space for field work soon.'),
    ('2026-03-14 17:26:00', 'Rae', 'Gray evening settles; the day slips away quietly.'),
    # Mar 15
    ('2026-03-15 08:16:00', 'Ivy', 'Light rain beads on the greenhouse glass.'),
    ('2026-03-15 12:33:00', 'Noor', 'We check seedlings for damping off and adjust airflow.'),
    ('2026-03-15 17:41:00', 'Rae', 'Rain tapers; dusk smells sweet and wet.'),
    # Mar 16
    ('2026-03-16 08:24:00', 'Ivy', 'Sun breaks through in patches, warming the path.'),
    ('2026-03-16 12:27:00', 'Noor', 'We transplant the strongest starts into larger cells.'),
    ('2026-03-16 17:53:00', 'Rae', 'Clouds thicken again; evening stays mild.'),
    # Mar 17
    ('2026-03-17 08:12:00', 'Ivy', 'Breezy morning; flags and grasses sway together.'),
    ('2026-03-17 12:40:00', 'Noor', 'We mark beds for early greens, measuring twice.'),
    ('2026-03-17 17:38:00', 'Rae', 'Wind drops as light fades; calm settles in.'),
    # Mar 18
    ('2026-03-18 08:20:00', 'Ivy', 'Clear blue and a bright chill; the field feels wide open.'),
    ('2026-03-18 12:23:00', 'Noor', 'We turn the first bed, soil dark and fragrant.'),
    ('2026-03-18 17:50:00', 'Rae', 'Sunset stays golden longer now; days keep stretching.'),
    # Mar 19
    ('2026-03-19 08:14:00', 'Ivy', 'Quick showers race across the morning.'),
    ('2026-03-19 12:37:00', 'Noor', 'We pause between showers to set out irrigation lines.'),
    ('2026-03-19 17:34:00', 'Rae', 'Evening clears; the air smells fresh and new.'),
    # Mar 20
    ('2026-03-20 08:27:00', 'Ivy', 'Equinox light feels balanced; day and night in peace.'),
    ('2026-03-20 12:22:00', 'Noor', 'We sow the first hardy greens in the field.'),
    ('2026-03-20 17:45:00', 'Rae', 'Sun sets true west; the season turns officially.'),
    # Mar 21
    ('2026-03-21 08:19:00', 'Ivy', 'Warm morning sun; jackets hang unused on hooks.'),
    ('2026-03-21 12:31:00', 'Noor', 'We water in the new seeds, gentle and thorough.'),
    ('2026-03-21 17:52:00', 'Rae', 'Evening stays soft; night arrives without bite.'),
    # Mar 22
    ('2026-03-22 08:23:00', 'Ivy', 'Overcast but bright; the light feels silver.'),
    ('2026-03-22 12:44:00', 'Noor', 'We repair a wheelbarrow and sharpen the hoe blades.'),
    ('2026-03-22 17:30:00', 'Rae', 'Clouds hold fast; the field rests under a blanket.'),
    # Mar 23
    ('2026-03-23 08:11:00', 'Ivy', 'Drizzle hangs in the air; everything dampens softly.'),
    ('2026-03-23 12:39:00', 'Noor', 'We keep seedlings inside, waiting for clearer skies.'),
    ('2026-03-23 17:36:00', 'Rae', 'Evening mist blurs the horizon; quiet settles in.'),
    # Mar 24
    ('2026-03-24 08:17:00', 'Ivy', 'Clear again; dew glitters on the grass.'),
    ('2026-03-24 12:28:00', 'Noor', 'We lay out row covers, ready for cool nights.'),
    ('2026-03-24 17:49:00', 'Rae', 'Sun lingers on the shed wall; evening glows.'),
    # Mar 25
    ('2026-03-25 08:09:00', 'Ivy', 'Rain returns in earnest; the morning is a wash.'),
    ('2026-03-25 12:35:00', 'Noor', 'We adjust gutters and check the seedling benches for leaks.'),
    ('2026-03-25 17:43:00', 'Rae', 'Soaking rain keeps falling; the field drinks again.'),
    # Mar 26
    ('2026-03-26 08:21:00', 'Ivy', 'Sun peeks out, leaving raindrops to sparkle.'),
    ('2026-03-26 12:30:00', 'Noor', 'We move cool-weather starts outdoors for a few hours.'),
    ('2026-03-26 17:37:00', 'Rae', 'Sky clears by dusk; a gentle warmth remains.'),
    # Mar 27
    ('2026-03-27 08:13:00', 'Ivy', 'Wind tugs at tarps; the morning feels active.'),
    ('2026-03-27 12:42:00', 'Noor', 'We double-check stakes and re-secure the hoop house.'),
    ('2026-03-27 17:32:00', 'Rae', 'Wind drops as evening settles; the field exhales.'),
    # Mar 28
    ('2026-03-28 08:16:00', 'Ivy', 'Bright sun, warm air; a true spring day.'),
    ('2026-03-28 12:21:00', 'Noor', 'We plant early peas and mark the rows with twine.'),
    ('2026-03-28 17:54:00', 'Rae', 'Golden light stretches across the field; warmth lingers.'),
    # Mar 29
    ('2026-03-29 08:18:00', 'Ivy', 'Clouds return but the air stays mild.'),
    ('2026-03-29 12:26:00', 'Noor', 'We check the pea rows and top off watering.'),
    ('2026-03-29 17:40:00', 'Rae', 'Evening light soft and even; no sharp edges today.'),
    # Mar 30
    ('2026-03-30 08:07:00', 'Ivy', 'Drizzle cools the morning; fresh and quiet.'),
    ('2026-03-30 12:38:00', 'Noor', 'We update the planting chart and order extra compost.'),
    ('2026-03-30 17:46:00', 'Rae', 'Rain tapers off; the day ends in gentle gray.'),
    # Mar 31
    ('2026-03-31 08:19:00', 'Ivy', 'March ends with light clouds and warming air.'),
    ('2026-03-31 12:32:00', 'Noor', 'We set April goals, feeling the season turn in full.'),
    ('2026-03-31 17:55:00', 'Rae', 'Last dusk of March; spring is fully at the door.')
]


def add_march_data():
    """Add March 2026 weather and messages to database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("Adding March 2026 weather data...")
    for weather in weather_data:
        cursor.execute(
            """
            INSERT INTO weather (date, condition, temperature_c, precipitation_chance, note)
            VALUES (?, ?, ?, ?, ?)
            """,
            weather,
        )
    print(f"Added {len(weather_data)} weather entries")

    print("\nAdding March 2026 central board messages...")
    for created_at, author, text in messages_data:
        cursor.execute(
            """
            INSERT INTO messages (board, author, text, created_at)
            VALUES ('central', ?, ?, ?)
            """,
            (author, text, created_at),
        )
    print(f"Added {len(messages_data)} messages")

    conn.commit()

    # Verify data was added
    print("\nVerifying data...")
    cursor.execute("SELECT COUNT(*) FROM weather WHERE date LIKE '2026-03-%'")
    weather_count = cursor.fetchone()[0]
    print(f"Total March weather entries: {weather_count}")

    cursor.execute(
        "SELECT COUNT(*) FROM messages WHERE board='central' AND substr(created_at, 1, 7) = '2026-03'"
    )
    message_count = cursor.fetchone()[0]
    print(f"Total March central board messages: {message_count}")

    conn.close()
    print("\nData addition complete!")


if __name__ == '__main__':
    add_march_data()
