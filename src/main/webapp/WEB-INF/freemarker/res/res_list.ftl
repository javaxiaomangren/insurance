<div class="hero-unit">
    <table class="table table-striped">
        <thead>
        <tr>
            <th>资源编号</th>
            <th>资源名字</th>
            <th>资源描述</th>
            <th>操作</th>
        </tr>
        </thead>
        <tbody>
        <#list resPager.data as res>
        <tr>
            <td>${res.resourceId}</td>
            <td>${res.resName}</td>
            <td>${res.resDesc}</td>
            <td>
                <a href="javascript:void(0);" onclick="del(${res.resourceId});">删除</a>
            </td>
        </tr>
        </#list>
        </tbody>
    </table>

<#--<@page.show url="${rc.getContextPath()}/res/list_page?start=" totalPages="${resPager.totalPageCount}" totalRecords="${resPager.totalCount}" currPage="${resPager.currentPageNo}" />-->

    <@li.page url="/res/list_page?start=" pg=resPager/>

    <a class="btn btn-info" style="position: relative; left: 0px;  top: -5px;" href="javascript:void(0);"
       onclick="goAdd();"><i
            class="icon-plus icon-white"></i> 添加资源</a>
</div>

<script type="text/javascript">
    function goAdd() {
        $('#myModal').remove();
        $.get("${rc.getContextPath()}/res/res_goAdd",
                function(data) {
                    $(".hero-unit").append(data);
                    $('#myModal').modal({keyboard:false})
                }, "html"
        );
    }

    function del(resId) {
        if (confirm("确认删除该资源？")) {
            $.post("${rc.getContextPath()}/res/res_delete.json", {id:resId},
                    function(data) {
                        alert(data.tip);
                        reloadPage();
                    }, "json"
            );
        }
    }

    function reloadPage() {
        postRequest('${rc.getContextPath()}/res/list_page?start=${resPager.start}')
    }
</script>