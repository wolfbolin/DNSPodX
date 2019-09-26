# coding=utf-8
import csv
import DNSPodX
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('key.conf', encoding='utf-8')
    user_id = config.get('user', 'id')
    token = config.get('user', 'token')
    domain_name = 'tinoy.cn'

    user = DNSPodX.User(user_id, token)
    domain = DNSPodX.Domain(user, domain_name)
    record_list = domain.record_list()[0]

    for record in record_list:
        print('Remove record %s.%s' % (record.name, record.domain.name))
        record.remove()

    with open('%s.csv' % domain_name, 'r', encoding='gbk', newline='') as file:
        reader = csv.DictReader(file)
        for info in reader:
            print('Create record %s.%s' % (info['name'], domain.name))
            record = DNSPodX.Record(user, domain, info['name'], info['type'], info['value'], info['line'],
                                    ttl=info['ttl'], mx=info['mx'], status=['status'])
            record.create()
