package com.tuan800.list.rule.manager.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Created with IntelliJ IDEA.
 * User: madfeng
 * Date: 13-5-13
 * Time: 下午2:48
 * To change this template use File | Settings | File Templates.
 */
@Controller
@RequestMapping(value = "/")
public class TestController {

    private static final String PREFIX = "/test/";

    @RequestMapping("/test")
    public String test() {
        return PREFIX + "test";
    }
}
