package com.tuan800.list.rule.manager.controller;

import com.tuan800.list.rule.core.model.pojo.User;
import com.tuan800.list.rule.manager.controller.AbstractController;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.util.ArrayList;

/**
 * Created with IntelliJ IDEA.
 * User: madfeng
 * Date: 13-5-13
 * Time: 上午11:34
 * To change this template use File | Settings | File Templates.
 */
@Controller
@RequestMapping(value = "/")
public class LoginController extends AbstractController {

    private static final String PREFIX = "/";


    @RequestMapping(value = {"/login","relogin"}, method = RequestMethod.GET)
    public String login(Model model) {
        model.addAttribute(MSG, "");
        return PREFIX + "login";
    }

    @RequestMapping(value = "login", method = RequestMethod.POST)
    public String login(Model model,User user , HttpServletRequest request, HttpServletResponse response) {
        //TODO: get the user
        // this is a test..
        if (user != null) {
            HttpSession session = request.getSession();
            session.setAttribute("user", user);
            session.setAttribute("user_permissions", new ArrayList().add("pm.list"));
            session.setAttribute("sa", true);
            return redirect("main?login-success");
        } else {
            model.addAttribute(MSG, "用户名或密码错误");
            response.setHeader("Cache-Control", "no-cache");
            response.setHeader("Cache-Control", "no-store");
            response.setHeader("Pragma", "no-cache");
            response.setHeader("Expires", "0");
            return PREFIX + "login";
        }
    }


    @RequestMapping("logout")
    public String logout(HttpServletRequest request) {
        request.getSession().invalidate();
        return redirect("login?from-logout");
    }

    @RequestMapping("/main")
    public String main(HttpServletRequest request, Model model) {
        if (null == request.getSession().getAttribute("user")) {
            return "redirect:/login?from-main";
        }
        return PREFIX + "main";
    }

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public String index() {
        return  redirect("login");
    }

    @RequestMapping("/denied")
    public String denied(Model model) {
        return PREFIX + "denied";
    }







}
