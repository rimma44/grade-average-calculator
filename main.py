def score_average(score1, score2, score3, score4):
  total_score = (score1 + score2 + score3 + score4) / 4
  if total_score >= 70:
    grade = "A"
  elif total_score >= 60:
    grade = "B"
  elif total_score >= 50:
    grade = "C"
  elif total_score >= 40:
    grade = "D"
  else:
    grade = "F"
  return grade

print(score_average(20, 20, 20, 60))