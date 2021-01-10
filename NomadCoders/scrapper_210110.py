# https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=ai&limit=50
# https://stackoverflow.com/jobs?q=ai

from indeed import extract_indeed_pages,extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page)


#for n in range(max_page):
#  print(f"start={n * 50}")