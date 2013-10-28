package com.tuan800.list.rule.manager.controller;

import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;

/**
 * Created by IntelliJ IDEA.
 * User: madfeng
 * Date: 13-5-13
 * Time: 上午11:34
 * To change this template use File | Settings | File Templates.
 */
public abstract class AbstractController {
    public static final String LIST_PAGE = "list_page";
    public static final String LIST = "list";
    public static final String ADD = "add";
    public static final String SAVE = "save";
    public static final String EDIT = "edit";
    public static final String UPDATE = "update";
    public static final String DELETE = "delete";
    public static final String MSG = "msg";
    public static final String PAGER = "pager";
    public static final String TIP = "tip";
    public static final Integer DEFAULT_PAGE_SIZE = 20;

    public static String redirect(String path) {
        return "redirect:/" + path;
    }

    public static String forward(String path) {
        return "forward:/" + path;
    }

    public static void write(ServletResponse response, String text) {
        try {
            response.getWriter().write(text);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void writeJson(ServletResponse response, String text) {
        response.setContentType("application/json");
        write(response, text);
    }

    public static Boolean isSuperAdmin(HttpServletRequest request) {
        Object sa = request.getSession().getAttribute("sa");
        return null != sa && (Boolean) sa;
    }

}
