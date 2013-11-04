CREATE TABLE insurance (
  id int(11) NOT NULL AUTO_INCREMENT,
  pro_name varchar(32) NOT NULL COMMENT '产品名称',
  age_min int(11) DEFAULT '0' COMMENT '最小年龄',
  age_max int(11) NOT NULL COMMENT '最大年龄',
  category int(11) DEFAULT NULL COMMENT '分类（意外，人寿）',
  insu_days varchar(255) DEFAULT NULL COMMENT '保期(逗号分割)',
  claus_limit_id int(11) DEFAULT NULL COMMENT '条款/保额',
  tags varchar(255) DEFAULT NULL COMMENT '标签',
  price decimal(10,0) DEFAULT NULL COMMENT '保费',
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time datetime,
  description text COMMENT '描述',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8


CREATE TABLE clause_limit (
  id int(11) NOT NULL AUTO_INCREMENT,
  insu_id int(11) DEFAULT NULL COMMENT '保险id',
  clause_name varchar(32) NOT NULL COMMENT '条款名称',
  limits float NOT NULL COMMENT '保额',
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  update_time datetime NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

CREATE TABLE user (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(32) NOT NULL,
  password varchar(32) DEFAULT NULL,
  create_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
