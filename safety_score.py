def safety_score(distance_m, duration_s, crime_level=None):

    # Shorter distance = safer
    if distance_m <= 3000:
        distance_factor = 1.0
    elif distance_m <= 6000:
        distance_factor = 0.7
    else:
        distance_factor = 0.5

   # Faster route = safer
    if duration_s <= 600:  
        time_factor = 1.0
    elif duration_s <= 1800:  
        time_factor = 0.7
    else:
        time_factor = 0.5

    
    # If no crime data → assume medium safety
    if crime_level is None:
        crime_factor = 0.6
    else:
        # crime_level: 0 (safe) → 10 (dangerous)
        crime_factor = max(0, min(1, 1 - (crime_level / 10)))

    # Weighted scoring
    score = (
        (distance_factor * 0.4) +
        (time_factor * 0.4) +
        (crime_factor * 0.2)
    ) * 100

    return int(score)
