package com.tuan800.list.rule.manager.test.dao;

import com.tuan800.list.rule.core.dao.RoleDao;
import com.tuan800.list.rule.core.model.pojo.Role;
import junit.framework.TestCase;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.util.List;

/**
 * Created with IntelliJ IDEA.
 * User: madfeng
 * Date: 13-5-13
 * Time: 下午5:32
 * To change this template use File | Settings | File Templates.
 */
@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations = {"classpath*:/spring/*.xml"})
public class DaoTest extends TestCase {

    @Autowired
    private RoleDao roleDao;

    @Test
    public void testRoleDao(){
        List<Role> roleList =roleDao.findRoles();
        System.out.println("");
    }

}
