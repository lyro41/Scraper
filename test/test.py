import sys

sys.path.append("..")
import src.scraper as scraper

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
print(scraper.process(*sys.argv[1:]))