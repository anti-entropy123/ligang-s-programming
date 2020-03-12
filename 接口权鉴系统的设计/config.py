id_password = {
    'test_id' : 'test_password'
}

authenticate_id_address = ['127.0.0.1', 'some other']

known_error = 400
auth_success = 200
non_auth_ip = 101
wrong_id_or_passwd = 102

refuse_response = {
    known_error: "未知错误",
    non_auth_ip: "不是允许的ip地址",
    wrong_id_or_passwd: "错误的口令或id"
}
