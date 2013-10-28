<div class="hero-unit">
    <table class="table table-striped">
        <thead>
        <tr>
            <th>角色名</th>
            <th>角色描述</th>
            <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <#list rolePager.data as role>
        <tr>
            <td>${role.roleName}</td>
            <td>${role.roleDesc}</td>
            <td>
                <a href="#" onclick="edit('${role.roleId}');">修改</a>
                <a href="#" onclick="del(${role.roleId});">删除</a>
            </td>
        </tr>

        </#list>

        </tbody>
    </table>
<@page.show url="${rc.getContextPath()}/role/list_page?start=" totalPages="${rolePager.totalPageCount}" totalRecords="${rolePager.totalCount}" currPage="${rolePager.currentPageNo}" />
    <a style="position: relative; left: 0px;  top: -5px;" class="btn btn-info" href="#" onclick="javascript:addRole();"><i
            class="icon-plus icon-white"></i> 添加角色</a>

</div>
<script type="text/javascript">


    function reloadPage() {
        postRequest("${rc.getContextPath()}/role/list_page?start=${rolePager.start}");
    }

    function del(roleId) {
        if (confirm("确认删除该角色？")) {

            $.post("${rc.getContextPath()}/role/delete.json",
                    {roleId: roleId},
                    function(data) {
                        alert(data.tip);
                        reloadPage();
                    }, "json"
            );
        }
    }

    function edit(roleId) {
        $('#myModal').remove();
        $.get("${rc.getContextPath()}/role/edit",
                {roleId: roleId},
                function(data) {
                    $(".hero-unit").append(data);
                    $('#myModal').modal({keyboard:false})
                }, "html"
        );
    }

    function addRole() {
        $('#myModal').remove();
        $.get("${rc.getContextPath()}/role/add",
                {},
                function(data) {
                    $(".hero-unit").append(data);
                    $('#myModal').modal({keyboard:false})
                }, "html"
        );
    }

</script>