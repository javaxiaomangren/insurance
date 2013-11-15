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

QR_COMPANY = """SELECT id, company_name, logo FROM company """
QR_CATEGORY = """SELECT id, category_name, description, parent_id FROM category"""
QR_TAGS = """SELECT id, tag_name FROM tags """
QR_IMG = """SELECT id, img_name, img_url, refered_id, type FROM images """
QR_INSURANCE = """SELECT id, pro_name, min_age, max_age, notice, description, tags, suitable, company_id, category_id, example, price, sales_volume, buy_count, valid_flag, create_time, update_time FROM insrurance"""


"""
SELECT 

UPDATE insurance
SET
id = {id: },
pro_name = {pro_name: },
min_age = {min_age: 0},
max_age = {max_age: },
notice = {notice: },
description = {description: },
tags = {tags: },
suitable = {suitable: },
company_id = {company_id: },
category_id = {category_id: },
example = {example: },
price = {price: },
sales_volume = {sales_volume: 0},
buy_count = {buy_count: 1},
valid_flag = {valid_flag: 1},
create_time = {create_time: CURRENT_TIMESTAMP},
update_time = {update_time: }
WHERE {where_condition};
"""
