# coding=utf-8
import csv
import DNSPodX
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('key.conf', encoding='utf-8')
    user_id = config.get('user', 'id')
    token = config.get('user', 'token')
    domain_name = config.get('domain', 'target')

    user = DNSPodX.User(user_id, token)
    domain = DNSPodX.Domain(user, domain_name)
    record_list = domain.record_list()[0]

    file = open('%s.csv' % domain_name, 'r', encoding='gbk', newline='')
    reader = csv.DictReader(file)
    for info in reader:
        if info['id'] != '':
            print('Modify record %s.%s' % (info['name'], domain.name))
            record = DNSPodX.Record(user, domain, info['name'], info['type'], info['value'], info['line'],
                                    ttl=info['ttl'], mx=info['mx'], status=['status'], r_id=info['id'])
            record.modify()
        else:
            print('Create record %s.%s' % (info['name'], domain.name))
            record = DNSPodX.Record(user, domain, info['name'], info['type'], info['value'], info['line'],
                                    ttl=info['ttl'], mx=info['mx'], status=['status'])
            record.create()
