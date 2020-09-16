import psycopg2
import sys

commands = [
    '''
    CREATE TABLE covid (
        id INT NOT NULL PRIMARY KEY,
        country VARCHAR(30) NOT NULL,
        total VARCHAR(15),
        new VARCHAR(15),
        deaths VARCHAR(15),
        recovered VARCHAR(15),
        new_recovered VARCHAR(15),
        active VARCHAR(15),
        critical VARCHAR(15),
        total_over_mpop VARCHAR(15),
        deaths_over_mpop VARCHAR(15),
        tests VARCHAR(15),
        tests_mpop VARCHAR(15),
        case_over_ppl VARCHAR(15),
        death_over_ppl VARCHAR(15),
        test_over_ppl VARCHAR(15)
    )
    ''',
    '''
    CREATE TABLE pop_by_country (
        id INT NOT NULL PRIMARY KEY,
        country VARCHAR(30) NOT NULL,
        population VARCHAR(13),
        yearly_change VARCHAR(8),
        net_change VARCHAR(12),
        density VARCHAR(7),
        area VARCHAR(15),
        migrants VARCHAR(15),
        fertility VARCHAR(4),
        med_age VARCHAR(4),
        urban VARCHAR(5),
        world_share VARCHAR(7),
    )
    ''',
    '''
    CREATE TABLE world_pop (
        year INT NOT NULL PRIMARY KEY,
        population VARCHAR(13),
        yearly_change_percent VARCHAR(6),
        yearly_change VARCHAR(11),
        med_age VARCHAR(4),
        fertility VARCHAR(4),
        density VARCHAR(2),
        urban_percent VARCHAR(6),
        urban VARCHAR(13)
    )
    ''',
    '''
    CREATE TABLE world_projections (
        year INT NOT NULL PRIMARY KEY,
        population VARCHAR(14),
        yearly_change VARCHAR(6),
        net_change VARCHAR(10),
        density VARCHAR(2),
        urban VARCHAR(13),
        urban_percent VARCHAR(6)
    )
    '''
]

def create_tables():
    try:
        con = psycopg2.connect(os.environ['DATABASE_URL'])
        c = con.cursor()
        for command in commands:
            c.execute(command)
        con.commit()
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    create_tables()
