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
    save_form()
    // NoWrap()
    // window.onresize = NoWrap
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
    $("#paginator li").each(function(){
        var node = $(this).find("a")
        $(node).text($(node).attr("rel"))
        $(this).show()
    })
    active_page = Math.floor($("#paginator li[class='active'] a").attr("rel"))
    last_page = Math.floor($("#paginator ul li").length)
    height = Math.floor($("#paginator ul").height())
    i_bottom = Math.floor((active_page - 1) /2)
    i_top = Math.floor(active_page + (last_page - active_page) /2 )
    
    width_paginator = Math.floor($("#paginator").width())
    width_list = Math.floor($("#paginator ul").width())

    width = width_list / width_paginator

    var seuil = 1

    count_left = $("ul.pagination li:first").nextUntil(".active").length
    if(count_left == last_page - 1)
    {
        count_left = 0
    }
    count_right = $("ul.pagination li.active").nextAll().length

    if(height > 40 || width > 0.9)
    {
        if(i_bottom > 4)
        {
            var replace = $("#paginator li").get(i_bottom)
            $(replace).find("a").text("...")
        }
        if(i_top < last_page - 4)
        {
            var replace = $("#paginator li").get(i_top)
            $(replace).find("a").text("...")
        }
        j_left = 1
        j_right = 1
        while(height > 40 || width > 0.9)
        {
            if(count_left > count_right)
            {
                if(i_bottom - j_left > seuil)
                {
                    $("#paginator li")[i_bottom - j_left].style.display = "none"
                    count_left --
                }
                if(i_bottom + j_left < active_page - seuil)
                {
                    $("#paginator li")[i_bottom + j_left].style.display = "none"
                    count_left --
                }
                j_left ++
            } 
            else{
                if(i_top - j_right > active_page + seuil)
                {
                    $("#paginator li")[i_top - j_right].style.display = "none"
                    count_right --
                }
                if(i_top + j_right < last_page  - seuil)
                {
                    $("#paginator li")[i_top + j_right].style.display = "none"
                    count_right --
                }
                j_right ++
            }

            height = $("#paginator ul").height()
            width_paginator = Math.floor($("#paginator").width())
            width_list = Math.floor($("#paginator ul").width())
            width = width_list / width_paginator

            if(j_left + j_right > last_page)
            {
                return false
            }
        }
    }
}