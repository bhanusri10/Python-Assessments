def read_marks(filename):
    try:
        marks_data = []
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                parts = line.strip().split(',')
                if len(parts) != 4:
                    print(f"Malformed line {line_num}: {line.strip()}")
                    continue
                student_id, student_name, subject, marks = parts
                try:
                    student_id = int(student_id)
                    marks = int(marks)
                    marks_data.append({
                        'student_id': student_id,
                        'student_name': student_name,
                        'subject': subject,
                        'marks': marks
                    })
                except ValueError:
                    print(f"Invalid student id or marks at line {line_num}: {line.strip()}")
                    continue
        return marks_data
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return []

def generate_report(marks_data):
    students = {}
    for entry in marks_data:
        sid = entry['student_id']
        name = entry['student_name']
        subject = entry['subject']
        score = entry['marks']
        if sid not in students:
            students[sid] = {
                'name': name,
                'subjects': {},
                'total': 0,
            }
        students[sid]['subjects'][subject] = score
        students[sid]['total'] += score
    report = []
    for sid, info in students.items():
        subjects = info['subjects']
        scores = list(subjects.values())
        avg = info['total'] / len(scores)
        high_sub = max(subjects, key=lambda k: subjects[k])
        low_sub = min(subjects, key=lambda k: subjects[k])
        report.append({
            'student_id': sid,
            'name': info['name'],
            'total': info['total'],
            'average': avg,
            'highest_subject': high_sub,
            'highest_score': subjects[high_sub],
            'lowest_subject': low_sub,
            'lowest_score': subjects[low_sub]
        })
    # Sort by average descending
    report.sort(key=lambda x: x['average'], reverse=True)
    return report

def write_summary(report, filename):
    try:
        with open(filename, 'w') as f:
            for r in report:
                f.write(f"Student ID: {r['student_id']}\n")
                f.write(f"Name: {r['name']}\n")
                f.write(f"Total Marks: {r['total']}\n")
                f.write(f"Average Marks: {r['average']:.1f}\n")
                f.write(f"Highest Scored Subject: {r['highest_subject']} ({r['highest_score']})\n")
                f.write(f"Lowest Scored Subject: {r['lowest_subject']} ({r['lowest_score']})\n")
                f.write("--------------------------------------\n")
        print(f"Report written to {filename}")
    except Exception as e:
        print(f"Error writing report: {e}")

marks_data = read_marks('marks.txt')
report = generate_report(marks_data)
write_summary(report, 'report.txt')
