Python
Run

# Q6 - Railway Timetable using Nested Data

# Railway database
trains = {
    "101": {
        "name": "Chennai Express",
        "stations": [
            ("Chennai", "06:00", "06:15"),
            ("Villupuram", "08:00", "08:05"),
            ("Trichy", "10:30", "10:35")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "102": {
        "name": "Pandian Express",
        "stations": [
            ("Chennai", "20:00", "20:15"),
            ("Villupuram", "22:00", "22:05"),
            ("Madurai", "05:00", "05:10")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "103": {
        "name": "Vaigai Express",
        "stations": [
            ("Chennai", "13:00", "13:10"),
            ("Villupuram", "15:00", "15:05"),
            ("Madurai", "21:00", "21:10")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "104": {
