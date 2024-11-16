import sys
sys.path.append('../easybus')
import crawl

def test_get_data():
    data = crawl.WebData('izmir-otogari','ankara-otogari','17.11.2024')
    print(data.get_data())
test_get_data()