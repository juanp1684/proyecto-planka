def assert_status_code_200(response):
    assert response.status_code == 200

def assert_status_code_400(response):
    assert response.status_code == 400