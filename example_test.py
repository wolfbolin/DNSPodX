# coding=utf-8
import DNSPodX

if __name__ == '__main__':
    user_id = '117683'
    token = 'e427615a0220e25e951ae6d55b573754'
    # DNSPodX.http_proxy = 'http://127.0.0.1:12639'
    # DNSPodX.https_proxy = 'http://127.0.0.1:12639'
    user = DNSPodX.User(user_id, token)
    print(user.version())
    domain_data, domain_list = user.domain_list()
    print(domain_data)
    domain = domain_list[0]
    record_data, record_list = domain.record_list()
    print(record_data)
