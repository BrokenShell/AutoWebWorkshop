import os

jobs_path = "static/jobs"
html_str = """
<!DOCTYPE html>
<html lang="en">
<body>
{}
</body>
</html>
"""


def process_job(job_id: str) -> str:
    job_meta = f"{jobs_path}/{job_id}/meta.txt"
    job_details = {}
    with open(job_meta, 'r') as file:
        for line in file:
            key, val = line.split(": ", 1)
            job_details[key] = val.strip()
    return f"""<div>
    <h3>{job_id}</h3>
    <ul>
        <li>Prompt: {job_details["Prompt"]}</li>
        <li>Model: {job_details["Model"]}</li>
        <li>Quality: {job_details["Quality"]}</li>
    </ul>
</div>"""


if __name__ == '__main__':
    job_entries = [process_job(job) for job in os.listdir(jobs_path)]
    print(*job_entries, sep="\n\n")
