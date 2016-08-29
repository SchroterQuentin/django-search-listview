function change_page(i)
{
    var page = document.getElementById("id_page")
    page.value = i
    document.getElementById("form_page").submit()
}

function toggle_search_box()
{
    $("#search_box").toggle('blind')
}

function start_search(){
    if(!window.jQuery)
    {
        console.log("Please install jQuery")
        return
    }
    window.onresize = NoWrap
    save_form()
    NoWrap()
}

var form_page_tmp

function save_form(){
    form_page_tmp = $("#form_page").find("input[name!='page'], select, textarea").serialize()
}

function check_change(){
    form_str = $("#form_page").find("input[name!='page'], select, textarea").serialize()
    if(form_page_tmp != form_str)
    {
        $("input[name='page']").val(1)
    }
}

function NoWrap()
{
    $("#paginator li").show()
    active_page = Math.floor($("#paginator a[class='active']").attr("rel"))
    last_page = Math.floor($("#paginator ul li").length)
    height = Math.floor($("#paginator ul").height())
    i_bottom = Math.floor((active_page - 1) /2)
    i_top = Math.floor(active_page + (last_page - active_page) /2 )
    
    width_paginator = Math.floor($("#paginator").width())
    width_list = Math.floor($("#paginator ul").width())

    width = width_list / width_paginator

    if(height > 40 || width > 0.9)
    {
        if(i_bottom > 1)
        {
            var replace = $("#paginator li").get(i_bottom)
            $(replace).find("a").text("...")
        }
        if(i_top < last_page - 1)
        {
            var replace = $("#paginator li").get(i_top)
            $(replace).find("a").text("...")
        }
        j = 1
        while(height > 40 || width > 0.9)
        {
            if(i_bottom - j > 0 && i_bottom + j < active_page - 2)
            {
                $("#paginator li")[i_bottom - j].style.display = "none"
                $("#paginator li")[i_bottom + j].style.display = "none"
            }
            if(i_top - j > active_page + 2 && i_top + j < last_page)
            {
                $("#paginator li")[i_top - j].style.display = "none"
                $("#paginator li")[i_top + j].style.display = "none"
            }
            height = $("#paginator ul").height()
            width_paginator = Math.floor($("#paginator").width())
            width_list = Math.floor($("#paginator ul").width())
            width = width_list / width_paginator

            j++;
            if(j>i_top)
            {
                return
            }
        }
    }
}