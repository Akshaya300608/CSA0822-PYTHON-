Python
Run

# Farmer Helpline Complaint Analysis

complaints = [
    ("Madurai", "Rice", "Seeds not received seeds delayed"),
    ("Chennai", "Wheat", "Fertiliser price high"),
    ("Madurai", "Rice", "Seeds price high subsidy not received"),
    ("Trichy", "Cotton", "Water supply problem"),
    ("Chennai", "Wheat", "Seeds not received")
]

stop_words = {"not", "high", "the", "is", "a"}

word_count = {}
district_complaints = {}
crop_count = {}

# Count word frequency
for district, crop, complaint in complaints:
    words = complaint.lower().split()

    for word in words:
        if word not in stop_words:
            word_count[word] = word_count.get(word, 0) + 1

# Group complaints by district
    district_complaints.setdefault(district, []).append(complaint)

# Count complaints by crop
    crop_count[crop] = crop_count.get(crop, 0) + 1

# Sort words by frequency and alphabetical order
top_words = sorted(
    word_count.items(),
    key=lambda item: (-item[1], item[0])
)
