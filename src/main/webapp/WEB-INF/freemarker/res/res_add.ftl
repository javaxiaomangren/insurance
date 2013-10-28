<div class="modal hide" id="myModal">

    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">×</button>
        <h3 id="h3Title">添加资源</h3>
    </div>

    <div class="modal-body">
        <p>

        <form class="form-horizontal" id="editForm">
            <fieldset>
                <div class="control-group">
                    <label class="control-label" for="resName">资源名称</label>

                    <div class="controls">
                        <input type="text" class="input-xlarge" name="resName" maxlength="20" id="resName">
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="resDesc">资源描述</label>

                    <div class="controls">
                        <input type="text" class="input-xlarge" maxlength="20" name="resDesc" id="resDesc">
                    </div>
                </div>
            </fieldset>
        </form>
        </p>
    </div>

    <div class="modal-footer">
        <a href="#" class="btn" data-dismiss="modal">取消</a>
        <a href="#" class="btn btn-primary" onclick="$('#editForm').submit();">保存</a>
    </div>

</div>

<script type="text/javascript">
    $(document).ready(function() {
        $("#editForm").validate({
            submitHandler : function() {
                $.ajax({
                    url:'${rc.getContextPath()}/res/res_add.json',
                    dataType:'json',
                    type:'post',
                    data:$('#editForm').serialize(),
                    error:function() {
                    },
                    success:function(data) {
                        alert(data.tip);
                        reloadPage();
                        $('#myModal').modal('hide');
                    }
                });
                return false;
            },
            invalidHandler : function() {
                return false;
            },
            rules: {
                resName: {
                    required: true,
                    minlength: 2,
                    maxlength: 20
                },
                resDesc: {
                    required: true,
                    maxlength: 255
                }
            },
            messages: {
                resName: {
                    required: "请输入资源名称",
                    minlength: "资源名称必须包含至少2个字符",
                    maxlength: "资源名称不能超过20个字符"
                },
                resDesc: {
                    required: "请输入资源描述",
                    maxlength: "资源描述不能超过255个字符"
                }
            }
        });
    });
</script>