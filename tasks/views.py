from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scoring import calculate_score

@api_view(['POST'])
def analyze_tasks(request):
    tasks = request.data.get('tasks', [])

    results = []
    for t in tasks:
        score = calculate_score(
            t.get("urgency", 0),
            t.get("importance", 0),
            t.get("effort", 0)
        )

        results.append({
            "title": t.get("title", ""),
            "urgency": t.get("urgency"),
            "importance": t.get("importance"),
            "effort": t.get("effort"),
            "score": score
        })

    # sort highest score first
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return Response({"results": results})
