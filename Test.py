import sender_stand_request
import data


def test_diploma():
    track_number = sender_stand_request.create_order(data.user_body)['track']
    find_order_number = sender_stand_request.find_order_by_track(track_number)
    assert find_order_number.status_code == 200
