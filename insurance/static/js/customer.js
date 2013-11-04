//设置下拉框的事件
setEvents("#min_age_list", "a", function(){
	$("#age_min").val(this.text)
})

setEvents("#max_age_list", "a", function(){
	$("#age_max").val(this.text)
})

setEvents("#clause_list", "a", function(){
	$("#clause").val(this.text)
})

setEvents("#limit_list", "a", function(){
	$("#limit").val(this.text)
})


setEvents("#tags_list", "a", function(){
	var oldval = $("#tags").val()
	$("#tags").val(this.text+","+oldval)
	$("#tags").css("display","inline")
})
//表单验证
$("#insu_form").submit(function(){
	if($("#pro_name").val() === ""){
		alert("产品名称不能为空")
		return false
	}
	var min_age = $("#age_min").val() 
	var max_age = $("#age_max").val() 
	if (max_age === ""){
		alert("请填写年龄")
		return false
	}
	if(min_age != ""){
		a = handle_age(min_age)
		if (a > 0){
			$("#age_min").val(a)
		}
	}
	a = handle_age(max_age)
	if (a > 0){
		$("#age_max").val(a)
	}

	if($("#insu_days").val() === ""){
		alert("保期不能为空")
		return false
	}
	if($("#clause_limit").val() === ""){
		alert("条款！！！")
		return false
	}


})

function handle_age(age){
	var reg = new RegExp("^[0-9]*$");
	var _year = 1
	if(age.indexOf("年") != -1){
		age = age.replace("年", "")
		_year = 365
	}
	if (reg.test(age)){
		return parseInt(age) * _year
	}else{
		return 0
	}
}

function setEvents(id, find, func){
	$(id).find(find).each(function(i, elem){
		$(elem).click(func)
	})
}

function generate(){
	var oldval = $("#clause_limit").val()
	var clause = $("#clause").val()
	var limit = $("#limit").val()
	if (clause != "" && limit != ""){
		var value = clause + ":" + limit
		if(oldval != ""){
			value = oldval + ", " + value
		}
		$("#clause_limit").val(value)
		limit = $("#limit").val("")
	}
}
