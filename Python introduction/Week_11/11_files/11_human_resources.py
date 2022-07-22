# Human Resources System

#open file
with open("./Week_11/11_files/hr_system.txt") as book_file:

    for text in book_file:
        lines = text.strip()
        text_parts = lines.split(" ")
        name = text_parts[0]
        id_number = text_parts[1]
        job_title = text_parts[2]
        salary = text_parts[3]
        
        salary = float(salary)
        salary_month = salary/24

        if job_title == "Engineer":
            print(f"{name} (ID: {id_number}), {job_title} - ${salary_month+1000:.2f}")
        else:
            print(f"{name} (ID: {id_number}), {job_title} - ${salary_month:.2f}")
