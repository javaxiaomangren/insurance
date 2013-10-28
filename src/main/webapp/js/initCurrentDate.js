jQuery.extend({
            setInitDate:function () {
            	var newDate = new Date(),
            	year=newDate.getFullYear();
            	month=newDate.getMonth()+1;
            	date=newDate.getDate();
            	hours=newDate.getHours();
            	minutes=newDate.getMinutes();
            	seconds=newDate.getSeconds();
            	if(month<10)month="0"+month;
            	if(date<10)date="0"+date;
            	if(hours<10)hours="0"+hours;
            	if(minutes<10)minutes="0"+minutes;
            	if(seconds<10)seconds="0"+seconds;
        		var currentDate = year+"-"+month+"-"+date+" "+hours+":"+minutes+":"+seconds;
        		return currentDate;
            }
      });