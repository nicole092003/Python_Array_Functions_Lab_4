# Nicole Thomas
# LabCollectionsP1.py
# February 2, 2024

# (a) Ask the user to enter 5 test scores. Store the scores in a list. Display the list.
test_scores = []
for i in range(5):
    score = float(input(f"Enter test score {i + 1}: "))
    test_scores.append(score)

print("Original Test Scores:", test_scores)

# (b) Copy all 5 test scores to another list. Use a loop to examine each test score in the new list.
# If the score is below 60, add 10 extra points to the score. Display the list.
modified_scores = test_scores.copy()
for i in range(len(modified_scores)):
    if modified_scores[i] < 60:
        modified_scores[i] += 10

print("Modified Test Scores:", modified_scores)

# (c) Compare the old score and new score of each student.
# If the old score and new score are different, display the two scores.
for i in range(5):
    if test_scores[i] != modified_scores[i]:
        print(f"Student {i + 1}: Old Score = {test_scores[i]}, New Score = {modified_scores[i]}")
