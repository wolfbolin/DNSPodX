# coding=utf-8
import csv
import DNSPodX
import configparser

field_name = ['_id', 'id', 'name', 'type', 'line', 'value', 'ttl', 'mx', 'status']

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('key.conf', encoding='utf-8')
    user_id = config.get('user', 'id')
    token = config.get('user', 'token')
    domain_name = config.get('domain', 'target')

    user = DNSPodX.User(user_id, token)
    domain = DNSPodX.Domain(user, domain_name)
    record_data = domain.record_list()[1]

    file = open('%s.csv' % domain_name, 'w', encoding='gbk', newline='')
    writer = csv.DictWriter(file, fieldnames=field_name, extrasaction='ignore')
    writer.writeheader()
    for index, info in enumerate(record_data['records']):
        print('Save record %s.%s' % (info['name'], domain_name))
        info['_id'] = index + 1
        writer.writerow(info)
