import twenty_four_hour_time

def test_hours():
    assert twenty_four_hour_time.solve("05:30pm") == "17:30", "It should be 17:30"
    assert twenty_four_hour_time.solve("12:00pm") == "12:00", "It should be 12:00"
    assert twenty_four_hour_time.solve("12:00am") == "00:00", "It should be 00:00"
    assert twenty_four_hour_time.solve("03:00pm") == "15:00", "It should be 15:00"
    assert twenty_four_hour_time.solve("03:00am") == "03:00", "It should be 03:00"

if __name__ == "__main__":
    test_hours()
    print("Everything is okay")