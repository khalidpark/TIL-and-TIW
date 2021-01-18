# https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=ai&limit=50
# https://stackoverflow.com/jobs?q=ai

from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file


indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = so_jobs + indeed_jobs
save_to_file(jobs)