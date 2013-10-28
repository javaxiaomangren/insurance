<div class="modal hide" style="width: 720px;" id="role_resource_edit_div">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">×</button>
        <h3 id="h3Title">修改权限</h3>
    </div>

    <div class="modal-body">

        <form class="form-horizontal" id="role_resource_edit_form">
            <table>

                <tr>
                    <td>
                        <label>角色名:</label>
                        <input type="text" readonly="readonly" contenteditable="false" id="rolename" name="rolename"
                               value="${roleResc.role.roleName}">
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <p>已有权限</p>
                        <select size="5" id="haveroles" style="width:320px" name="haveroles" multiple="true">
                        <#list roleResc.resources?sort_by("resName") as resc>
                            <option value="${resc.resourceId}" ondblclick="javascript:removebtn()"
                                    title="${resc.resName} (${resc.resDesc})">${resc.resName}
                                (${resc.resDesc})
                            </option>
                        </#list>
                        </select></td>
                    <td>
                        <div class="">
                            <br>
                            <input class="btn" type="button" value="←" onclick="addbtn()">
                            <br>
                            <input class="btn" type="button" value="→" onclick="removebtn()">
                        </div>
                    </td>
                    <td align="center">
                        <p>未有权限</p>
                        <select size="5" id="roles" style="width:320px" multiple="true">
                        <#list notHaveRescs as resc>
                            <option value="${resc.resourceId}" ondblclick="javascript:addbtn()"
                                    title="${resc.resName} (${resc.resDesc})">${resc.resName}
                                (${resc.resDesc})
                            </option>
                        </#list>
                        </select></td>
                </tr>
            </table>
        </form>
    </div>

    <div class="modal-footer">
        <a href="#" class="btn" data-dismiss="modal">取消</a>
        <a href="#" class="btn btn-primary" data-dismiss="modal" onclick="save(${roleResc.role.roleId})">保存</a>
    </div>

</div>

<script type="text/javascript">
    function removebtn() {
        if (!$("#haveroles").val()) {
            alert("请先选中一个已有权限！");
            $("#haveroles").focus();
            return false;
        }
        $("#haveroles").find("option:selected").each(function(){
            var selval = $(this).val();
            var seltext = $(this).text();
            $("#haveroles option:selected").remove();
            $("#roles").append("<option value='" + selval + "' ondblclick='javascript:addbtn()' title='" + seltext + "'>" + seltext + "</option>");
        });
    }
    function addbtn() {
        if (!$("#roles").val()) {
            alert("请先选中一个未有权限！");
            $("roles").focus();
            return false;
        }
        $("#roles").find("option:selected").each(function(){
            var selval = $(this).val();
            var seltext = $(this).text();
            $("#roles option:selected").remove();
            $("#haveroles").append("<option value='" + selval + "' ondblclick='javascript:removebtn()' title='" + seltext + "'>" + seltext + "</option>");
        });
    }

    function save(roleId) {
        var newResIds = new Array();
        $("#haveroles").find("option").each(function() {
            newResIds.push($(this).val())
        });
        $.post(
                "${rc.getContextPath()}/role_resource/update.json",
                { roleId : roleId,newResIds: newResIds.toLocaleString()},
                function(data) {
                    alert(data.msg);
                    reloadPage();
                }, "json"
        );
    }
</script>