def calculate_score(urgency, importance, effort):
    """
    Basic scoring formula:
    Higher urgency + importance => higher score
    Higher effort => lowers score
    """

    try:
        urgency = float(urgency)
        importance = float(importance)
        effort = float(effort)
    except:
        return 0

    score = (urgency * 0.5) + (importance * 0.4) - (effort * 0.2)
    return round(score, 2)
