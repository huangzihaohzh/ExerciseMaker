from entity import Exercise

if __name__ == "__main__":
    exercise = Exercise.Exercise()
    exercise.makeExerciseByStr("1/2","0")
    print(exercise.isRight())
    """
    for exercise in exerciselist:
        print(exercise.getExerciseStr()+"\n")
        print(exercise.getAnswerStr())
    """