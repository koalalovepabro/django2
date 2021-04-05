from guestbook01.models import findall, insert, deleteby_no_and_password


def test_findall():
    results = findall()
    print(results)
    for result in results:
        print(f'{result["no"]}:{result["name"]}:{result["reg_date"]}:result["message"]')



def test_insert():
    name = '둘리2'
    password = '123456'
    message = '호이호이~'

    result = insert(name, password, message)
    print(f'insert result: {result}')


def test_deleteby_no_and_password():
    no = 4
    password = '1234'

    result = deleteby_no_and_password(no, password)
    print(f'delete result: {result}')


def main():
    # test_insert()
    # test_deleteby_no_and_password()
    test_findall()


if __name__ == '__main__':
    main()
