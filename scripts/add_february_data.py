#!/usr/bin/env python3
"""
Script to add February 2026 weather and central board messages to field.db
Following the patterns established in January data
"""

import sqlite3
import os

# Path to database
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'field.db')

# Weather data for February 2026 (28 days)
# Continuing winter patterns with gradual warming as month progresses
weather_data = [
    ('2026-02-01', 'Light snow', -0.5, 55, 'February begins with flurries'),
    ('2026-02-02', 'Freezing fog', -2.0, 40, 'Morning frost, afternoon fog'),
    ('2026-02-03', 'Clear', -1.0, 20, 'Cold and bright'),
    ('2026-02-04', 'Overcast', 2.5, 45, 'Gray skies settle in'),
    ('2026-02-05', 'Light drizzle', 3.5, 60, 'Damp and mild'),
    ('2026-02-06', 'Partly cloudy', 4.0, 30, 'Clouds break occasionally'),
    ('2026-02-07', 'Sunny intervals', 5.0, 25, 'Hints of spring light'),
    ('2026-02-08', 'Frost', 0.0, 20, 'Night freeze returns'),
    ('2026-02-09', 'Cold rain', 2.0, 70, 'Steady winter rain'),
    ('2026-02-10', 'Windy', 4.5, 40, 'Gusts sweep the field'),
    ('2026-02-11', 'Clear', 1.5, 15, 'Calm after wind'),
    ('2026-02-12', 'Light snow', -0.5, 50, 'Snow dusts morning'),
    ('2026-02-13', 'Overcast', 3.0, 35, 'Dense cloud cover'),
    ('2026-02-14', 'Partly sunny', 5.5, 20, 'Valentine sun breaks through'),
    ('2026-02-15', 'Frost', -1.0, 25, 'Frost patterns on glass'),
    ('2026-02-16', 'Freezing drizzle', 0.5, 65, 'Ice forms slowly'),
    ('2026-02-17', 'Sunny', 6.0, 15, 'Warmest day yet'),
    ('2026-02-18', 'Partly cloudy', 5.0, 30, 'Mild for late winter'),
    ('2026-02-19', 'Rain showers', 4.0, 75, 'Passing storms'),
    ('2026-02-20', 'Cloudy', 3.5, 40, 'Soft gray day'),
    ('2026-02-21', 'Clear and cold', 0.0, 10, 'Winter lingers'),
    ('2026-02-22', 'Partly sunny', 4.5, 25, 'Sun and shadow'),
    ('2026-02-23', 'Light rain', 5.5, 55, 'Gentle rainfall'),
    ('2026-02-24', 'Overcast', 4.0, 45, 'Month wanes gray'),
    ('2026-02-25', 'Sunny intervals', 6.5, 20, 'Spring glimpses'),
    ('2026-02-26', 'Clear', 5.0, 15, 'Bright late winter day'),
    ('2026-02-27', 'Partly cloudy', 6.0, 30, 'Warming trend continues'),
    ('2026-02-28', 'Sunny', 7.0, 15, 'February ends mild')
]

# Central board messages for February 2026
# 3 messages per day (morning ~8am, midday ~12pm, evening ~5-6pm)
# Authors: Ivy (morning), Noor (midday), Rae (evening)
# Following the poetic, observational style of existing messages
messages_data = [
    # Feb 1
    ('2026-02-01 08:15:00', 'Ivy', 'February opens with snow; small flakes catch in bare branches.'),
    ('2026-02-01 12:20:00', 'Noor', 'We start fresh seed orders; calendars marked with planting dates.'),
    ('2026-02-01 17:45:00', 'Rae', 'First day of a new month; the field lies patient under white.'),
    # Feb 2
    ('2026-02-02 08:05:00', 'Ivy', 'Fog thick as wool; everything vanishes ten feet out.'),
    ('2026-02-02 12:35:00', 'Noor', 'We inventory winter supplies, count what remains.'),
    ('2026-02-02 17:30:00', 'Rae', 'Frost persists where fog lifted; ice crystals catch last light.'),
    # Feb 3
    ('2026-02-03 08:22:00', 'Ivy', 'Cold but clear; blue sky sharp enough to cut.'),
    ('2026-02-03 12:18:00', 'Noor', 'We plan greenhouse seeding; tomatoes and peppers first.'),
    ('2026-02-03 17:55:00', 'Rae', 'Stars visible early; winter\'s clarity persists.'),
    # Feb 4
    ('2026-02-04 08:30:00', 'Ivy', 'Gray returns, heavy and complete; no shadows today.'),
    ('2026-02-04 12:42:00', 'Noor', 'We prepare seed trays, label each with care and date.'),
    ('2026-02-04 17:20:00', 'Rae', 'Cloud ceiling low; the field feels enclosed, quiet.'),
    # Feb 5
    ('2026-02-05 08:12:00', 'Ivy', 'Light rain begins; softer than yesterday\'s gray.'),
    ('2026-02-05 12:25:00', 'Noor', 'Drizzle on the greenhouse roof sounds like patience.'),
    ('2026-02-05 17:38:00', 'Rae', 'Damp evening; the kind that seeps into everything slowly.'),
    # Feb 6
    ('2026-02-06 08:28:00', 'Ivy', 'Clouds break apart; brief sun warms the morning air.'),
    ('2026-02-06 12:15:00', 'Noor', 'We sow first seeds—tiny promises pressed into soil.'),
    ('2026-02-06 17:48:00', 'Rae', 'Light changes by the hour; winter yields in small ways.'),
    # Feb 7
    ('2026-02-07 08:35:00', 'Ivy', 'Sun breaks through more often; shadows return to the field.'),
    ('2026-02-07 12:30:00', 'Noor', 'Greenhouse warms in afternoon; we open vents for air.'),
    ('2026-02-07 17:25:00', 'Rae', 'Spring feels possible today, though weeks remain.'),
    # Feb 8
    ('2026-02-08 08:08:00', 'Ivy', 'Frost overnight; all gains reversed in darkness.'),
    ('2026-02-08 12:22:00', 'Noor', 'We check greenhouse temperature; seedlings safe inside.'),
    ('2026-02-08 17:40:00', 'Rae', 'Winter reminds us not to count it out too soon.'),
    # Feb 9
    ('2026-02-09 08:18:00', 'Ivy', 'Rain returns cold and steady; winter rain, not spring.'),
    ('2026-02-09 12:38:00', 'Noor', 'We stay indoors, repair tools, sharpen blades.'),
    ('2026-02-09 17:52:00', 'Rae', 'Rain continues into evening; the field drinks deep.'),
    # Feb 10
    ('2026-02-10 08:25:00', 'Ivy', 'Wind whips through bare branches; everything bends east.'),
    ('2026-02-10 12:45:00', 'Noor', 'We secure anything loose; wind rattles greenhouse frames.'),
    ('2026-02-10 17:15:00', 'Rae', 'Evening wind dies down; sudden stillness after gusts.'),
    # Feb 11
    ('2026-02-11 08:32:00', 'Ivy', 'Calm morning after wind; the field settles again.'),
    ('2026-02-11 12:28:00', 'Noor', 'First seedlings emerge—tiny green points breaking soil.'),
    ('2026-02-11 17:42:00', 'Rae', 'Clear night coming; cold but peaceful after storm.'),
    # Feb 12
    ('2026-02-12 08:10:00', 'Ivy', 'Light snow falls; February shows its winter side again.'),
    ('2026-02-12 12:35:00', 'Noor', 'Snow melts on greenhouse glass; inside stays warm.'),
    ('2026-02-12 17:28:00', 'Rae', 'Snow stops by dusk; just enough to dust the ground.'),
    # Feb 13
    ('2026-02-13 08:20:00', 'Ivy', 'Dense clouds settle low; no hint of sun today.'),
    ('2026-02-13 12:18:00', 'Noor', 'We water seedlings carefully; small leaves need gentle care.'),
    ('2026-02-13 17:50:00', 'Rae', 'Gray day fades to gray night; monotone February.'),
    # Feb 14
    ('2026-02-14 08:38:00', 'Ivy', 'Sun breaks through on Valentine\'s Day; gift of light.'),
    ('2026-02-14 12:40:00', 'Noor', 'We share lunch in warm greenhouse; celebrate small growing things.'),
    ('2026-02-14 17:35:00', 'Rae', 'Evening brings clouds back, but the day was bright enough.'),
    # Feb 15
    ('2026-02-15 08:15:00', 'Ivy', 'Frost patterns on windows; intricate ice geometry.'),
    ('2026-02-15 12:25:00', 'Noor', 'Cold morning but seedlings thrive in protected warmth.'),
    ('2026-02-15 17:45:00', 'Rae', 'Temperature drops with sun; stars will be sharp tonight.'),
    # Feb 16
    ('2026-02-16 08:22:00', 'Ivy', 'Freezing drizzle coats everything in thin, clear ice.'),
    ('2026-02-16 12:32:00', 'Noor', 'Paths treacherous; we move slowly, test each step.'),
    ('2026-02-16 17:20:00', 'Rae', 'Ice glitters at dusk; dangerous but beautiful.'),
    # Feb 17
    ('2026-02-17 08:30:00', 'Ivy', 'Warmest morning yet; ice melts, water drips from eaves.'),
    ('2026-02-17 12:48:00', 'Noor', 'Sun warms greenhouse too much; we open doors for cooling.'),
    ('2026-02-17 17:55:00', 'Rae', 'February sun has strength today; real warmth in the air.'),
    # Feb 18
    ('2026-02-18 08:28:00', 'Ivy', 'Mild morning continues; winter\'s grip loosens slowly.'),
    ('2026-02-18 12:22:00', 'Noor', 'We plan spring transplanting; weeks away but coming closer.'),
    ('2026-02-18 17:38:00', 'Rae', 'Evening stays mild; no frost expected tonight.'),
    # Feb 19
    ('2026-02-19 08:18:00', 'Ivy', 'Rain showers blow through; brief but thorough soaking.'),
    ('2026-02-19 12:35:00', 'Noor', 'Between storms we check drainage; water flows where it should.'),
    ('2026-02-19 17:42:00', 'Rae', 'Evening shower passes; cleared air smells of wet earth.'),
    # Feb 20
    ('2026-02-20 08:25:00', 'Ivy', 'Soft gray day; clouds without weight or threat.'),
    ('2026-02-20 12:28:00', 'Noor', 'Greenhouse seedlings need more space; we thin and transplant.'),
    ('2026-02-20 17:30:00', 'Rae', 'Quiet evening; the field rests under gentle clouds.'),
    # Feb 21
    ('2026-02-21 08:12:00', 'Ivy', 'Clear and cold; winter makes a brief return.'),
    ('2026-02-21 12:40:00', 'Noor', 'We cover tender plants; protect what we\'ve started.'),
    ('2026-02-21 17:48:00', 'Rae', 'Cold settles in for the night; frost likely by dawn.'),
    # Feb 22
    ('2026-02-22 08:35:00', 'Ivy', 'Sun and shadow alternate; clouds chase across blue sky.'),
    ('2026-02-22 12:20:00', 'Noor', 'Seedlings grow stronger each day; true leaves emerging.'),
    ('2026-02-22 17:25:00', 'Rae', 'Late February light has spring\'s angle now.'),
    # Feb 23
    ('2026-02-23 08:20:00', 'Ivy', 'Light rain falls gently; more like spring than winter.'),
    ('2026-02-23 12:38:00', 'Noor', 'Rain waters the field for us; everything drinks deep.'),
    ('2026-02-23 17:50:00', 'Rae', 'Rain continues soft and steady; good for the earth.'),
    # Feb 24
    ('2026-02-24 08:28:00', 'Ivy', 'Gray returns but warmer gray; February wanes quietly.'),
    ('2026-02-24 12:45:00', 'Noor', 'We prepare for March; organize seeds, clean tools again.'),
    ('2026-02-24 17:35:00', 'Rae', 'Month nears its end; we\'ve survived another winter month.'),
    # Feb 25
    ('2026-02-25 08:15:00', 'Ivy', 'Sun breaks through cloud; hints of spring in the warmth.'),
    ('2026-02-25 12:30:00', 'Noor', 'Greenhouse full of green now; small plants everywhere.'),
    ('2026-02-25 17:40:00', 'Rae', 'Days grow noticeably longer; dusk comes later each evening.'),
    # Feb 26
    ('2026-02-26 08:32:00', 'Ivy', 'Clear bright morning; February shows its best face.'),
    ('2026-02-26 12:25:00', 'Noor', 'We plan field preparation; soil work begins next week.'),
    ('2026-02-26 17:45:00', 'Rae', 'Beautiful late winter day; warmth lingers into evening.'),
    # Feb 27
    ('2026-02-27 08:18:00', 'Ivy', 'Clouds return but bring warmth, not cold; spring-like.'),
    ('2026-02-27 12:42:00', 'Noor', 'Seedlings need hardening off soon; prepare them for outside.'),
    ('2026-02-27 17:30:00', 'Rae', 'February\'s last full day; winter nearly behind us.'),
    # Feb 28
    ('2026-02-28 08:25:00', 'Ivy', 'February ends sunny; warmest day of the month.'),
    ('2026-02-28 12:35:00', 'Noor', 'Month closes well; we ready ourselves for March planting.'),
    ('2026-02-28 17:55:00', 'Rae', 'Last evening of winter\'s shortest month; spring ahead.')
]

def add_february_data():
    """Add February 2026 weather and messages to database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("Adding February 2026 weather data...")
    for weather in weather_data:
        cursor.execute("""
            INSERT INTO weather (date, condition, temperature_c, precipitation_chance, note)
            VALUES (?, ?, ?, ?, ?)
        """, weather)
    print(f"Added {len(weather_data)} weather entries")
    
    print("\nAdding February 2026 central board messages...")
    for created_at, author, text in messages_data:
        cursor.execute("""
            INSERT INTO messages (board, author, text, created_at)
            VALUES ('central', ?, ?, ?)
        """, (author, text, created_at))
    print(f"Added {len(messages_data)} messages")
    
    conn.commit()
    
    # Verify data was added
    print("\nVerifying data...")
    cursor.execute("SELECT COUNT(*) FROM weather WHERE date LIKE '2026-02-%'")
    weather_count = cursor.fetchone()[0]
    print(f"Total February weather entries: {weather_count}")
    
    cursor.execute("SELECT COUNT(*) FROM messages WHERE board='central' AND substr(created_at, 1, 7) = '2026-02'")
    message_count = cursor.fetchone()[0]
    print(f"Total February central board messages: {message_count}")
    
    conn.close()
    print("\nData addition complete!")

if __name__ == '__main__':
    add_february_data()
