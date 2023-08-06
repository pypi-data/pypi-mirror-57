//Code started by Michael Ortega for the LIG
//December 06th, 2016


var select_op_divs      = []
var select_op_selected  = []
var nb_cols_in_displayed_table = 4
var svg_up_div  = null;

//This function ask about all the operators, and then update the "operators selection" modal
function select_op_new_modal() {

    //cleaning
    $('#select_op_tags_select').empty();
    $('#select_op_names_select').empty();
    document.getElementById('select_op_panel_title').value = '';

    $("#select_op_make_button").removeClass('btn btn-secondary').addClass('btn btn-primary');
    $("#select_op_update_button").hide();

    //Before opening the modal, we have to ask about the existing operators, and then make the tags list
    sakura.apis.hub.op_classes.list().then(function (result) {
        var tags_list = [];
        var sostl = document.getElementById('select_op_tags_select');
        var sosnl = document.getElementById('select_op_names_select');

        var div = document.getElementById('select_op_panel');
        while(div.firstChild){
            div.removeChild(div.firstChild);
        }

        global_ops_cl = JSON.parse(JSON.stringify(result));
        global_ops_cl.forEach( function (op) {
            op['tags'].forEach( function (tag) {
                if (tags_list.indexOf(tag) == -1) {
                        tags_list.push(tag);
                        var option = document.createElement("option");
                        option.text = tag;
                        sostl.add(option);
                }
            });
            var option = document.createElement("option");
            option.text = op['name'];
            option.value = op['id'];
            sosnl.add(option);
        });

        $('#select_op_tags_select').selectpicker('refresh');
        $('#select_op_names_select').selectpicker('refresh');
        $('#modal_op_selector').modal();
    });
}


function select_op_reopen_modal(id) {
    panel = panel_from_id(id);
    panel_focus_id = id;

    $('#select_op_tags_select').empty();
    $('#select_op_names_select').empty();
    document.getElementById('select_op_panel_title').value = '';

    $("#select_op_make_button").removeClass('btn btn-primary').addClass('btn btn-secondary');
    $("#select_op_update_button").show();

    //Before opening the modal, we have to ask about the existing operators, and then make the tags list
    sakura.apis.hub.op_classes.list().then(function (result) {
        var tags_list = [];
        var sostl = document.getElementById('select_op_tags_select');
        var sosnl = document.getElementById('select_op_names_select');

        var div = document.getElementById('select_op_panel');
        while(div.firstChild){
            div.removeChild(div.firstChild);
        }

        global_ops_cl = JSON.parse(JSON.stringify(result));
        global_ops_cl.forEach( function (op) {
            op['tags'].forEach( function (tag) {
                if (tags_list.indexOf(tag) == -1) {
                        tags_list.push(tag);
                        var option = document.createElement("option");
                        option.text = tag;
                        sostl.add(option);
                }
            });
            var option = document.createElement("option");
            option.text = op['name'];
            option.value = op['id'];
            sosnl.add(option);
        });

        document.getElementById('select_op_panel_title').value = panel.title;
        for (var i=0; i< panel.names.length; i++)
            document.getElementById("select_op_names_select").options[i].selected = panel.names[i];
        for (var i=0; i< panel.tags.length; i++)
            document.getElementById("select_op_tags_select").options[i].selected = panel.tags[i];

        select_op_on_change();

        //Cleaning
        while(div.firstChild){
            div.removeChild(div.firstChild);
        }

        var divs = [];
        panel.selected_ops.forEach( function(op) {
            divs.push(select_op_new_operator(op, true));
        });

        var pdiv = document.getElementById('select_op_panel');
        pdiv.appendChild(select_op_make_table(nb_cols_in_displayed_table, divs));

        $('#select_op_tags_select').selectpicker('refresh');
        $('#select_op_names_select').selectpicker('refresh');

        $('#modal_op_selector').modal();
    });
}


function select_op_make_table(nb_cols, divs) {

    //table creation
    var tbl = document.createElement('table');
    var tbdy = document.createElement('tbody');
    var nb_rows = Math.ceil(divs.length/nb_cols);

    tbl.style.width = '100%';

    var index = 0;
    for (var i=0; i< nb_rows; i++) {
        var tr = document.createElement('tr');
        for (var j=0; j<nb_cols; j++) {
            if (divs[index] != null) {
                var td = document.createElement('td');
                td.setAttribute('align', 'center');
                td.style.width = '20px';
                td.appendChild(divs[index]);
                tr.appendChild(td);
                index = index + 1;
            }
            else {
                var td = document.createElement('td');
                td.setAttribute('align', 'center');
                td.style.width = '20px';
                tr.appendChild(td);
                index = index + 1;
            }
        }
        tbdy.appendChild(tr);
    }
    tbl.appendChild(tbdy);
    return tbl;
}


function select_op_on_change() {

    var ops_to = document.getElementById("select_op_tags_select").options;
    var ops_no = document.getElementById("select_op_names_select").options;

    //cleaning
    var pdiv = document.getElementById('select_op_panel');
    select_op_selected = []
    select_op_divs = []

    //tags
    for (var o=0; o<ops_to.length; o++) {
        if (ops_to[o].selected) {
            global_ops_cl.forEach( function (op) {
                if (op['tags'].indexOf(ops_to[o].text) >= 0 && select_op_selected.indexOf(op['id']) == -1) {
                    select_op_divs.push(select_op_new_operator(parseInt(op['id']), true));
                    select_op_selected.push(parseInt(op['id']));
                }
            });
        }
    }

    //names
    for (var o=0; o<ops_no.length; o++) {
        if (ops_no[o].selected && select_op_selected.indexOf(parseInt(ops_no[o].value)) == -1) {
            select_op_divs.push(select_op_new_operator(parseInt(ops_no[o].value), true));
            select_op_selected.push(parseInt(ops_no[o].value));
        }
    }

    //Cleaning
    while(pdiv.firstChild){
        pdiv.removeChild(pdiv.firstChild);
    }
    pdiv.appendChild(select_op_make_table(nb_cols_in_displayed_table, select_op_divs));
}

function dragging_svg(event, id) {
    svg_up_div = document.getElementById(id);
}

function select_op_new_operator(id, removable) {
    var cl = class_from_id(id);
    var ndiv = document.createElement('div');
    var s = '';
    var svg = cl.svg;

    if (!cl.enabled) {
        var v0 = cl.svg.indexOf('<svg');
        if (v0 == -1)
            v0 = cl.svg.indexOf('< svg');
        var v1 = cl.svg.indexOf('>', v0);
        var v2 = cl.svg.lastIndexOf('</');
        var v3 = cl.svg.lastIndexOf('>');
        var head  = cl.svg.substring(0, v1+1);
        var end   = cl.svg.substring( v2, v3+1);
        var middle= cl.svg.substring(v1+1, v2);

        var new_layer = '<rect x="-500" y="-500" fill-opacity="0.4" fill="white" width="1000" height="1000"/> \
                        <rect x="-500" y="0" fill="white" width="1000" height="15"/> \
                        <text x="0" y="13" font-size="10"> disabled</text>';
        svg = head+middle+new_layer+end;
    }

    ndiv.id = "select_op_selected_"+cl.id+"_static";
    if (removable) {
        ndiv.id = "select_op_selected_"+cl.id+'_rem';
    }

    //Main div with svg
    var div1  = $('<div>');
    var table = $('<table>');
    var tr    = $('<tr>');
    if (removable) {
        var td1 = $('<td>', {align: "center"});
        var td2 = $('<td>', {valign: "top"});
        var td_span = $('<span>', {class: "glyphicon glyphicon-remove", onclick: "select_op_delete_op(\'"+cl.id+"\');", style: "cursor: pointer;"});
        td1.html(svg);
        table.append(tr.append([td1, td2.append(td_span)]));
    }
    else {
      var td = $('<td>', {align: "center"});
      var svg_div = $('<div>', {draggable:"true", ondragstart:"dragging_svg(event,\'"+ndiv.id+"\')"});
      svg_div.html(svg);
      table.append(tr.append(td.append(svg_div)));
    }

    var l = cl.name.length;
    var fname = cl.name;
    if (l > 7) {
        fname = cl.name.substring(0,7)+'.';
    }
    var tr2 = $('<tr>');
    var td3 = $('<td>', {align: "center"});
    td3.html('<font size="1">'+fname+'</font>');
    table.append(tr2.append(td3));

    $(ndiv).append(div1.append(table));

    //exclamation
    var excl_div = $('<div>', {style: "position: absolute; top:8px; left: 13px;visibility: hidden;"});
    var excl_span = $('<span>', {class: "glyphicon glyphicon-exclamation-sign", style: "cursor: pointer;"});
    excl_div.append(excl_span);

    //list button
    if (!removable) {
      var list_div = $('<div>', {style: "position: absolute; font-size: 1.2em; top:-5px; left: 32px; visibility: hidden;"});
      var list_span = $('<span>', {class: "glyphicon glyphicon-menu-hamburger", style:"cursor: pointer;"});
      $(ndiv).append(list_div.append(list_span));
    }
    $(ndiv).append(excl_div);

    return (ndiv);
}


function select_op_delete_op(id) {

    var index = select_op_selected.indexOf(parseInt(id));

    select_op_selected.splice(index, 1);
    select_op_divs.splice(index, 1);

    var pdiv = document.getElementById('select_op_panel');

    //Cleaning div
    while(pdiv.firstChild){
        pdiv.removeChild(pdiv.firstChild);
    }
    pdiv.appendChild(select_op_make_table(nb_cols_in_displayed_table, select_op_divs));

    //Cleaning name selection
    var options = document.getElementById("select_op_names_select").options;
    for (var i=0; i<options.length;i++) {
        options[i].selected = false;
        select_op_divs.forEach( function(op) {
            var val = op.id.split('_')[3];
            if (val == options[i].value)
                options[i].selected = true;
        });
    }
    $('#select_op_names_select').selectpicker('refresh');
}


function select_op_add_panel() {

    var title = document.getElementById('select_op_panel_title').value;

    //Here we manage a panel title by default
    if (title == '') {
        title  = "Panel 0";
        var cpt = 0;
        global_op_panels.forEach( function (p) {
            if (p['title'] == title) {
                 cpt += 1;
            }
        title = "Panel "+cpt;
        });
    }

    var divs = []
    select_op_selected.forEach( function(item) {
        divs.push(select_op_new_operator(item, false));
    });

    var tbl = select_op_make_table(nb_cols_in_displayed_table, divs);
    var tmp_el = document.createElement("div");
    tmp_el.appendChild(tbl);

    var acc_id = global_op_panels.length;
    global_op_panels.forEach( function (op) {
        if (op['id'] == acc_id)
            acc_id ++;
    });

    var names = []
    var options = document.getElementById("select_op_names_select").options;
    for (var i=0; i<options.length;i++) {
        names.push(options[i].selected);
    }

    var tags = []
    options = document.getElementById("select_op_tags_select").options;
    for (var i=0; i<options.length;i++) {
        tags.push(options[i].selected);
    }

    var panel = {'id': acc_id, 'title': title, 'selected_ops': select_op_selected, gui: {'opened': true}, 'names': names, 'tags': tags}
    panel.id = "accordion_"+acc_id;

    global_op_panels.push(panel);

    select_op_create_accordion(panel, tmp_el.innerHTML);

    //update global variable
    $('#modal_op_selector').modal('hide');

    //Send the the current global var to the hub
    save_dataflow()
}


function select_op_update_panel() {
    select_op_delete_accordion(panel_focus_id);
    select_op_add_panel();
}


function change_chevron(a, panel_id) {

    var panel = panel_from_id(panel_id);
    var span_class = a.find('span').attr('class');

    if (span_class == "glyphicon glyphicon-chevron-up") {
        a.find('span').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
        panel.gui.opened = false;
    }
    else {
        a.find('span').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');
        panel.gui.opened = true;
    }

    save_dataflow();
}


function select_op_create_accordion(panel, ops) {

    var wrapper= document.createElement('div');
    load_from_template(
                    wrapper,
                    "panel.html",
                    {'id': panel.id, 'title': panel.title, 'title_escaped': panel.title.replace(' ', '_')},
                    function () {
                        var modal = wrapper.firstChild;
                        $(modal).find("#panel_"+panel.id+"_body").html(ops);
                        var acc_div = document.getElementById('op_left_accordion');
                        var butt = document.getElementById('select_op_add_button');

                        acc_div.insertBefore(wrapper.firstChild, butt);

                        if (!panel.gui.opened)
                            $('#panel_'+panel.title.replace(' ', '_')+'_chevron').trigger('click');
                    });
}


function select_op_delete_accordion(id) {
    var panel = panel_from_id(id);
    var acc = document.getElementById(panel.id);
    document.getElementById('op_left_accordion').removeChild(acc);

    var index = panel_index_from_id(panel.id);
    global_op_panels.splice(index,1);

    save_dataflow();
}


function panel_from_id(id) {
    return global_op_panels.find( function (e) {
        return e['id'] === id;
    });
}

function panel_index_from_id(id) {
    for (var i=0; i< global_op_panels.length; i++)
        if (global_op_panels[i]['id'] == id)
            return i;
    return -1
}
