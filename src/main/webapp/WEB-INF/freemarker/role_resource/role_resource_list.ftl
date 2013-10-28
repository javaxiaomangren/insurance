<div class="hero-unit">

<@li.table list=pager.data;roleResc>
    <@li.tr title="角色ID">${roleResc.role.roleId}</@li.tr>
    <@li.tr title="角色名">${roleResc.role.roleName}(${roleResc.role.roleDesc})</@li.tr>
    <@li.tr title="已有权限">
        <#if roleResc.role.roleName="SuperAdmin">
            超级管理员,拥有全部权限
            <#else>
                <span title="<#list roleResc.resources as resc>${resc.resDesc} </#list>">
                    <#list roleResc.resources as resc>
                                    <#if resc_index < 5>
                    ${resc.resDesc}
                    </#if>
                                </#list>
                </span>
        </#if>
    </@li.tr>
    <@li.tr title="操作">
        <@li.op pm="role_resource.edit">
            <#if roleResc.role.roleName="SuperAdmin">
                <span title="已有全部权限">修改权限</span>
                <#else>
                    <a href="#" data-toggle="modal" data-backdrop="static"
                       onclick="javascript: edit('${roleResc.role.roleId}')">修改权限</a>
            </#if>
        </@li.op>
    </@li.tr>
</@li.table>

<@li.page url="/role_resource/list_page?start="/>

</div>

<script type="text/javascript">
    function edit(roleId) {
        $('#role_resource_edit_div').remove();
        $.get("${rc.getContextPath()}/role_resource/edit",
                {roleId:roleId},
                function(data) {
                    $(".hero-unit").append(data);
                    $('#role_resource_edit_div').modal({keyboard:false})
                }, "html"
        );
    }

    function reloadPage() {
        postRequest("${rc.getContextPath()}/role_resource/list_page?start=${pager.start}");
    }
</script>