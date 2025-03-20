# import random

# # 🔹 Simulated agent votes with confidence scores
# votes = {
#     "Solar Panels": {"score": 8, "confidence": 70},
#     "Solar Windows": {"score": 9, "confidence": 85},
#     "Wind Turbines": {"score": 6, "confidence": 60},
# }

# # ✅ Compute final decision using weighted voting
# def compute_final_score(votes):
#     total_weight = sum(v["confidence"] for v in votes.values())
#     weighted_score = sum(v["score"] * (v["confidence"] / total_weight) for v in votes.values())
#     return weighted_score

# # Example Run
# if __name__ == "__main__":
#     final_score = compute_final_score(votes)
#     print(f"Final Decision Score: {final_score:.2f}")
# ✅ Compute final decision using weighted voting
def compute_final_score(votes):
    total_weight = sum(v["confidence"] for v in votes.values())
    weighted_score = sum(v["score"] * (v["confidence"] / total_weight) for v in votes.values())
    return weighted_score

# Example Run
if __name__ == "__main__":
    votes = {
        "Solar Panels": {"score": 8, "confidence": 70},
        "Solar Windows": {"score": 9, "confidence": 85},
        "Wind Turbines": {"score": 6, "confidence": 60},
    }
    final_score = compute_final_score(votes)
    print(f"Final Decision Score: {final_score:.2f}")
