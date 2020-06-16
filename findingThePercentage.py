if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        record = input()
        record = record.split(' ')
        student_marks[record[0]] = record[1:]

    name = input()

    if name in student_marks:
        marks = student_marks.get(name)
        total = 0
        for i in range(3):
            total = total + float(marks[i])

    print("%.2f" % round(total/3,2))
