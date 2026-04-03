#!/usr/bin/env python3
"""
Script to add April 2026 weather and central board messages to field.db
Following the patterns established in February and March data
"""

import sqlite3
import os

# Path to database
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'field.db')

# Weather data for April 2026 (30 days)
# Mid-spring with warming temperatures, occasional rain, blossoms
weather_data = [
    ('2026-04-01', 'Partly cloudy', 12.0, 30, 'April opens with mild promise'),
    ('2026-04-02', 'Sunny', 13.5, 10, 'A bright welcome to the new month'),
    ('2026-04-03', 'Light rain', 11.0, 65, 'Spring showers arrive overnight'),
    ('2026-04-04', 'Overcast', 10.5, 40, 'Clouds linger through the day'),
    ('2026-04-05', 'Partly sunny', 13.0, 20, 'Sun breaks lift the spirit'),
    ('2026-04-06', 'Clear', 14.5, 10, 'Crisp and clean after the rain'),
    ('2026-04-07', 'Windy', 12.5, 35, 'Gusts carry blossom petals'),
    ('2026-04-08', 'Rain showers', 11.5, 70, 'Steady showers through midday'),
    ('2026-04-09', 'Fog', 9.0, 45, 'Morning fog blurs the tree line'),
    ('2026-04-10', 'Sunny', 15.0, 10, 'Warm afternoon, longest yet'),
    ('2026-04-11', 'Partly cloudy', 14.0, 25, 'Soft light for spring work'),
    ('2026-04-12', 'Light drizzle', 12.0, 50, 'Drizzle keeps the soil moist'),
    ('2026-04-13', 'Clear', 15.5, 10, 'Blue skies, buds swelling'),
    ('2026-04-14', 'Breezy', 13.5, 30, 'A dancing breeze through the rows'),
    ('2026-04-15', 'Rain', 11.0, 75, 'Good soaking rain for the beds'),
    ('2026-04-16', 'Overcast', 12.5, 40, 'Clouds hold steady after rain'),
    ('2026-04-17', 'Partly sunny', 14.5, 20, 'Light improves through the day'),
    ('2026-04-18', 'Sunny', 16.5, 5, 'Warmest day so far this year'),
    ('2026-04-19', 'Clear', 17.0, 5, 'Second warm day in a row'),
    ('2026-04-20', 'Cloudy', 14.0, 35, 'Clouds drift back by afternoon'),
    ('2026-04-21', 'Light rain', 12.5, 60, 'Gentle rain returns by morning'),
    ('2026-04-22', 'Partly cloudy', 13.0, 25, 'Earth Day with soft spring light'),
    ('2026-04-23', 'Sunny', 16.0, 10, 'Bright and warm, bees active'),
    ('2026-04-24', 'Breezy', 14.5, 20, 'Wind carries seed fluff past'),
    ('2026-04-25', 'Clear', 17.5, 5, 'Deep blue sky, full spring'),
    ('2026-04-26', 'Overcast', 15.0, 35, 'Clouds veil the warmth briefly'),
    ('2026-04-27', 'Rain showers', 13.0, 65, 'Passing showers in the morning'),
    ('2026-04-28', 'Partly sunny', 15.5, 20, 'Showers clear, sun returns'),
    ('2026-04-29', 'Sunny', 17.0, 10, 'Golden afternoon light on the field'),
    ('2026-04-30', 'Clear', 16.5, 10, 'April closes warm and bright'),
]

# Central board messages for April 2026
# 3 messages per day (morning ~8am, midday ~12pm, evening ~5-6pm)
# Authors: Ivy (morning), Noor (midday), Rae (evening)
messages_data = [
    # Apr 1
    ('2026-04-01 08:14:00', 'Ivy', 'April is here; the light has shifted overnight.'),
    ('2026-04-01 12:27:00', 'Noor', 'We plan the month ahead and start setting trellises.'),
    ('2026-04-01 17:41:00', 'Rae', 'Evening feels warmer; spring is settling in.'),
    # Apr 2
    ('2026-04-02 08:20:00', 'Ivy', 'Bright morning; shadows are sharper and longer.'),
    ('2026-04-02 12:33:00', 'Noor', 'We transplant tomato seedlings to the cold frame.'),
    ('2026-04-02 17:48:00', 'Rae', 'Clear sunset paints the field gold.'),
    # Apr 3
    ('2026-04-03 08:09:00', 'Ivy', 'Rain overnight has freshened everything.'),
    ('2026-04-03 12:44:00', 'Noor', 'We check rain gauges and top off mulch in wet beds.'),
    ('2026-04-03 17:35:00', 'Rae', 'Drizzle continues at dusk; the world smells clean.'),
    # Apr 4
    ('2026-04-04 08:17:00', 'Ivy', 'Clouds keep the morning soft and still.'),
    ('2026-04-04 12:22:00', 'Noor', 'We start pepper seedlings under the grow lights.'),
    ('2026-04-04 17:52:00', 'Rae', 'Overcast sky at dusk; quiet and gray.'),
    # Apr 5
    ('2026-04-05 08:25:00', 'Ivy', 'Sun breaks through by eight; a good sign.'),
    ('2026-04-05 12:38:00', 'Noor', 'We direct-sow carrots and beets along the east bed.'),
    ('2026-04-05 17:30:00', 'Rae', 'Evening holds its warmth a little longer today.'),
    # Apr 6
    ('2026-04-06 08:11:00', 'Ivy', 'Clear and crisp; dew on every leaf.'),
    ('2026-04-06 12:29:00', 'Noor', 'We string up climbing supports for peas and beans.'),
    ('2026-04-06 17:55:00', 'Rae', 'Sunset lingers; the sky goes soft orange.'),
    # Apr 7
    ('2026-04-07 08:22:00', 'Ivy', 'Wind is up; blossoms scatter across the path.'),
    ('2026-04-07 12:41:00', 'Noor', 'We anchor new row markers before the gusts pick up.'),
    ('2026-04-07 17:37:00', 'Rae', 'Wind drops at dusk; the field settles into quiet.'),
    # Apr 8
    ('2026-04-08 08:08:00', 'Ivy', 'Rain patters on the roof; a steady morning rhythm.'),
    ('2026-04-08 12:24:00', 'Noor', 'We stay in the greenhouse and pot up squash starts.'),
    ('2026-04-08 17:43:00', 'Rae', 'Showers ease toward evening; puddles mirror the sky.'),
    # Apr 9
    ('2026-04-09 08:04:00', 'Ivy', 'Fog sits low over the field; hushed and white.'),
    ('2026-04-09 12:31:00', 'Noor', 'We check on the cold frame while visibility clears.'),
    ('2026-04-09 17:39:00', 'Rae', 'Fog retreats; a pale dusk follows.'),
    # Apr 10
    ('2026-04-10 08:18:00', 'Ivy', 'First truly warm morning; jackets stay on pegs.'),
    ('2026-04-10 12:20:00', 'Noor', 'We open the greenhouse wide and let fresh air rush in.'),
    ('2026-04-10 17:52:00', 'Rae', 'Golden light stretches long across the rows.'),
    # Apr 11
    ('2026-04-11 08:24:00', 'Ivy', 'Soft light today, like the sky is thinking.'),
    ('2026-04-11 12:36:00', 'Noor', 'We thin the carrot row and water the seedling flats.'),
    ('2026-04-11 17:28:00', 'Rae', 'Evening clouds part; stars appear early.'),
    # Apr 12
    ('2026-04-12 08:13:00', 'Ivy', 'Drizzle mists the morning; soft as a sigh.'),
    ('2026-04-12 12:45:00', 'Noor', 'We finish potting herbs and line them on the south bench.'),
    ('2026-04-12 17:47:00', 'Rae', 'Rain tapers off; the air feels thick and sweet.'),
    # Apr 13
    ('2026-04-13 08:19:00', 'Ivy', 'Blue sky and warming sun; buds everywhere.'),
    ('2026-04-13 12:28:00', 'Noor', 'We walk the beds and note what is already sprouting.'),
    ('2026-04-13 17:54:00', 'Rae', 'Sunset glows behind the hill; a perfect end.'),
    # Apr 14
    ('2026-04-14 08:27:00', 'Ivy', 'Breeze stirs the seedlings; they seem to stretch.'),
    ('2026-04-14 12:23:00', 'Noor', 'We tie in early pea shoots before the wind returns.'),
    ('2026-04-14 17:40:00', 'Rae', 'Wind gentles at dusk; the field breathes.'),
    # Apr 15
    ('2026-04-15 08:07:00', 'Ivy', 'Rain comes in earnest; the beds are drinking.'),
    ('2026-04-15 12:34:00', 'Noor', 'We check drainage and protect vulnerable starts.'),
    ('2026-04-15 17:49:00', 'Rae', 'Heavy rain at dusk; the sound is almost musical.'),
    # Apr 16
    ('2026-04-16 08:15:00', 'Ivy', 'After rain, a hushed morning; puddles everywhere.'),
    ('2026-04-16 12:42:00', 'Noor', 'We assess the beds for waterlogging and adjust covers.'),
    ('2026-04-16 17:32:00', 'Rae', 'Clouds thicken at dusk; more rain to come.'),
    # Apr 17
    ('2026-04-17 08:21:00', 'Ivy', 'Light is improving; clouds thinning overhead.'),
    ('2026-04-17 12:30:00', 'Noor', 'We sow basil and parsley in fresh compost.'),
    ('2026-04-17 17:46:00', 'Rae', 'Evening sky brightens; the world feels ready.'),
    # Apr 18
    ('2026-04-18 08:16:00', 'Ivy', 'Warm sun from the start; no jacket needed today.'),
    ('2026-04-18 12:19:00', 'Noor', 'We harden off tomatoes on the south bench all day.'),
    ('2026-04-18 17:55:00', 'Rae', 'Best evening yet; bees still working at dusk.'),
    # Apr 19
    ('2026-04-19 08:23:00', 'Ivy', 'Second warm day; everything is growing visibly.'),
    ('2026-04-19 12:37:00', 'Noor', 'We spot the first true leaves on the pepper starts.'),
    ('2026-04-19 17:42:00', 'Rae', 'Warm dusk; light stays until nearly eight.'),
    # Apr 20
    ('2026-04-20 08:10:00', 'Ivy', 'Clouds drift back but the air stays warm.'),
    ('2026-04-20 12:26:00', 'Noor', 'We stake the tallest seedlings before the next wind.'),
    ('2026-04-20 17:38:00', 'Rae', 'Evening dims early under the clouds; soft and mild.'),
    # Apr 21
    ('2026-04-21 08:06:00', 'Ivy', 'Rain returns; the morning is gentle and gray.'),
    ('2026-04-21 12:43:00', 'Noor', 'We work under cover, prepping labels for field day.'),
    ('2026-04-21 17:33:00', 'Rae', 'Rain tapers; dusk comes quietly.'),
    # Apr 22
    ('2026-04-22 08:18:00', 'Ivy', 'Earth Day; the field feels especially alive.'),
    ('2026-04-22 12:25:00', 'Noor', 'We take time to walk every bed and just observe.'),
    ('2026-04-22 17:51:00', 'Rae', 'A calm evening; the ground hums with life.'),
    # Apr 23
    ('2026-04-23 08:22:00', 'Ivy', 'Bees are busy at first light; blossoms open.'),
    ('2026-04-23 12:32:00', 'Noor', 'We thin the beet row and mulch the new herbs.'),
    ('2026-04-23 17:44:00', 'Rae', 'Warm and bright to the last light; summer teases.'),
    # Apr 24
    ('2026-04-24 08:14:00', 'Ivy', 'Wind carries white seed fluff past the window.'),
    ('2026-04-24 12:40:00', 'Noor', 'We mark which plants need extra watering this week.'),
    ('2026-04-24 17:36:00', 'Rae', 'Breezy dusk; the smell of warm earth lingers.'),
    # Apr 25
    ('2026-04-25 08:20:00', 'Ivy', 'Deep blue sky; a perfect spring day unfolds.'),
    ('2026-04-25 12:21:00', 'Noor', 'We transplant the first tomatoes into the field.'),
    ('2026-04-25 17:56:00', 'Rae', 'Long bright evening; the field looks its best.'),
    # Apr 26
    ('2026-04-26 08:12:00', 'Ivy', 'Clouds return but warmth stays beneath them.'),
    ('2026-04-26 12:38:00', 'Noor', 'We check the newly transplanted tomatoes, all well.'),
    ('2026-04-26 17:29:00', 'Rae', 'Overcast dusk; still and soft.'),
    # Apr 27
    ('2026-04-27 08:08:00', 'Ivy', 'Showers move through; the morning smells of rain.'),
    ('2026-04-27 12:35:00', 'Noor', 'We wait out the showers and catch up on records.'),
    ('2026-04-27 17:50:00', 'Rae', 'Rain eases; the field glistens at dusk.'),
    # Apr 28
    ('2026-04-28 08:17:00', 'Ivy', 'Clouds clear, and sun lifts everything.'),
    ('2026-04-28 12:27:00', 'Noor', 'We direct-sow beans along the fence line.'),
    ('2026-04-28 17:45:00', 'Rae', 'Warm evening after the showers; grateful for both.'),
    # Apr 29
    ('2026-04-29 08:24:00', 'Ivy', 'Golden morning light; another fine spring day.'),
    ('2026-04-29 12:33:00', 'Noor', 'We weed the herb bed and stake the climbing beans.'),
    ('2026-04-29 17:53:00', 'Rae', 'Sun lingers on the hills; the day gives generously.'),
    # Apr 30
    ('2026-04-30 08:19:00', 'Ivy', 'April ends clear and warm; a month well spent.'),
    ('2026-04-30 12:24:00', 'Noor', 'We write up the April notes and look ahead to May.'),
    ('2026-04-30 17:48:00', 'Rae', 'Last evening of April; the field is full and green.'),
]


def add_april_data():
    """Add April 2026 weather and messages to database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("Adding April 2026 weather data...")
    for weather in weather_data:
        cursor.execute(
            """
            INSERT INTO weather (date, condition, temperature_c, precipitation_chance, note)
            VALUES (?, ?, ?, ?, ?)
            """,
            weather,
        )
    print(f"Added {len(weather_data)} weather entries")

    print("\nAdding April 2026 central board messages...")
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
    cursor.execute("SELECT COUNT(*) FROM weather WHERE date LIKE '2026-04-%'")
    weather_count = cursor.fetchone()[0]
    print(f"Total April weather entries: {weather_count}")

    cursor.execute(
        "SELECT COUNT(*) FROM messages WHERE board='central' AND substr(created_at, 1, 7) = '2026-04'"
    )
    message_count = cursor.fetchone()[0]
    print(f"Total April central board messages: {message_count}")

    conn.close()
    print("\nData addition complete!")


if __name__ == '__main__':
    add_april_data()
