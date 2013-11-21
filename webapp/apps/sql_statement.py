#coding:utf8
INST_COMPANY = """INSERT INTO company(company_name, logo) VALUES(%s, %s)"""
INST_CATEGORY = """INSERT INTO category(category_name, description, parent_id) VALUES(%s, %s, %s)"""
INST_TAGS = """INSERT INTO tags (tag_name) VALUES(%s)"""
INST_IMAGE = """INSERT INTO images(img_name, img_url, refered_id, type) VALUES(%s, %s, %s, %s);"""
INST_INSURANCE = """INSERT INTO insurance(pro_name,min_age,max_age,notice,description,tags,suitable,
								company_id,category_id,example,price,sales_volume,buy_count, update_time)
						VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

INST_CLAUSE = """INSERT INTO clause(clause_name,description,category_id) VALUES(%s, %s, %s)"""
INST_INSU_CLAUSE = """INSERT INTO insu_clause(insu_id,clause_id,limits,insu_days,price,update_time)
							VALUES(%s, %s, %s, %s, %s, %s)"""

REPLACE_TAGS = """REPLACE INTO tags (tag_name) VALUES(%s)"""

QR_COMPANY = """SELECT id, company_name, logo FROM company """
QR_SIMPLE_COMPANY = """SELECT id, company_name FROM company """

QR_CATEGORY = """SELECT c.* ,c1.category_name as parent_name
                    FROM category c left join category c1 on c.parent_id = c1.id
               """
QR_SIMPLE_CATEGORY = "SELECT id, category_name FROM category"

QR_CLAUSE = """SELECT c.* ,c1.category_name
                    FROM clause c left join category c1 on c.category_id = c1.id
               """

QR_TAGS = """SELECT id, tag_name FROM tags """
QR_IMG = """SELECT id, img_name, img_url, refered_id, type FROM images """

QR_INSURANCE = """SELECT * FROM insurance"""


# id, pro_name, min_age, max_age, notice, description,
# tags,suitable,company_id, category_id, example, price,
# sales_volume, buy_count, valid_flag, create_time, update_time