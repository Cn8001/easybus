import sys
import os
sys.path.append(os.path.abspath('../easybus'))
import crawl

def test_get_data():
    data = crawl.WebData('izmir-otogari','ankara-otogari','17.11.2024')
    