2. 字段还需要增加“保险公司名称”“险种类别”“重要告知”
3. 图片：保险公司需要对应的logo，每款产品有可能对应一张或几张图片；
4. 条款、保额、价格，是这样一种关系
总价：如果是固定产品，只有总价没有条款价格；如果是可选产品，总价可以由条款价格相加确定
条款
条款保额
条款价格

5. 需要一个维护整体条款内容的功能，增删改、分类的操作，跟查询页面是对应的；
6. 除添加新产品，还需要对已有产品进行编辑、删除、失效等处理，需要对应的查询界面
http://www.zhongmin.cn/accid/product/accidha276.html
http://www.zhongmin.cn/accid/

CREATE TABLE company(
  id int(11) NOT NULL AUTO_INCREMENT,
  company_name varchar(32) NOT NULL COMMENT '保险公司名称',
  logo varchar(100)  COMMENT '保险公司logo名称',
  PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE category(
  id int(11) NOT NULL AUTO_INCREMENT,
  category_name varchar(32) NOT NULL COMMENT '保险分类',
  parent_id int(11) ,
  PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE images(
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(32) NOT NULL COMMENT '图片名称',
  localtion varchar(32) NOT NULL COMMENT '图片地址',
  refered_id int(11) COMMENT '关联到的ID,如产品id,或者保险公司id'
  type int(1) NOT NULL COMMENT '图片分类,0是logo,1产品图片'
  PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE insurance (
  id int(11) NOT NULL AUTO_INCREMENT,
  pro_name varchar(32) NOT NULL COMMENT '产品名称',
  min_age int(11) DEFAULT '0' COMMENT '最小年龄',
  max_age int(11) NOT NULL COMMENT '最大年龄',
  insu_days varchar(255) DEFAULT NULL COMMENT '保期(逗号分割)',
  claus_limit_id int(11) DEFAULT NULL COMMENT '条款/保额',
  tags varchar(255) DEFAULT NULL COMMENT '标签',
  price decimal(10,0) DEFAULT NULL COMMENT '保费',
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time datetime,
  
  notice text COMMENT '重要告知',
  description text COMMENT '描述',

  company_id int(11) NOT NULL COMMENT '保险公司',
  category_id int(11) NOT NULL COMMENT '保险分类',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE clause_limit (
  id int(11) NOT NULL AUTO_INCREMENT,
  insu_id int(11) DEFAULT NULL COMMENT '保险id',
  clause_name varchar(32) NOT NULL COMMENT '条款名称',
  limits float NOT NULL COMMENT '保额',
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time datetime NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;

CREATE TABLE user (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(32) NOT NULL,
  password varchar(32) DEFAULT NULL,
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ;
