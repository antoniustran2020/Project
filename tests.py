from main import app
with app.test_client() as c:
    response = c.get('/')
    #assert response.data == b'{"Predictions":{"Involuntary":0.21973916888237,"Voluntary Controllable":0.723499059677124,"Voluntary Other":0.05676174908876419}}'
    assert response.status_code == 200