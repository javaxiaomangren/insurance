<div class="modal hide" id="myModal">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">×</button>
        <h3>修改角色</h3>
    </div>
    <div class="modal-body">
        <p>

        <form class="form-horizontal" id="editForm">
            <fieldset>

                <div class="control-group">
                    <label class="control-label " for="rolename">角色名:</label>

                    <div class="controls">
                        <input type="text" name="roleId" id="roleId" value="${role.roleId}"/>
                        <input type="text" class="input-xlarge " id="rolename" readonly="readonly" maxlength="20"
                               name="roleName" value="${role.roleName}">
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="roledesc">角色描述:</label>

                    <div class="controls">
                        <input type="text" class="input-xlarge" id="roledesc" maxlength="20" name="roleDesc"
                               value="${role.roleDesc}">
                    </div>
                </div>
            </fieldset>
        </form>
        </p>
    </div>
    <div class="modal-footer">
        <a href="#" class="btn" data-dismiss="modal" onclick="clearVal();">取消</a>
        <a href="#" class="btn btn-primary" id="submitBtn" onclick="$('#editForm').submit();">保存</a>
    </div>
</div>

<script type="text/javascript">
    $(document).ready(function() {
        // 使用 jQuery 异步提交表单
        $("#editForm").validate({
            submitHandler : function() {
                $.ajax({
                    url:'${rc.getContextPath()}/role/update.json',
                    dataType:'json',
                    type:'post',
                    data:$('#editForm').serialize(),
                    error:function() { },
                    success:function(data) {
                        alert(data.tip);
                        $('#myModal').modal('hide');
                        reloadPage();
                    }
                });
                return false;
            },
            invalidHandler : function() {
                return false;
            },
            rules: {
                roleName: {
                    required: true,
                    minlength: 2,
                    maxlength: 255
                },
                roleDesc: {
                    required: true,
                    maxlength: 255
                }
            },
            messages: {
                roleName: {
                    required: "请输入角色名",
                    minlength: "角色名必须包含至少2个字符",
                    maxlength: "角色名不能超过255个字符"
                },
                roleDesc: {
                    required: "请输入角色描述",
                    maxlength: "角色描述不能超过255个字符"
                }
            }
        });

        $("#roleId").hide();
    });

</script>