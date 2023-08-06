//Code started by Michael Ortega for the LIG
//August, 22nd, 2017


var database_infos = null;
var columns_tags_list = null;
var mouse = {x: 0, y: 0};
var chunk_size = 100000;

function not_yet() {
    alert("not yet implemented");
}


function datasets_sort_func(a, b) {
    return a.name > b.name ? 1 : -1;
}

function min(a, b) {
    if (a <= b) return a;
    return b;
}

$(document).mousemove(function(e) {
    mouse.x = e.pageX;
    mouse.y = e.pageY;
}).mouseover(); // call the handler immediately



function datasets_info(header_str, body_str) {
    var h = $('#datasets_info_header');
    var b = $('#datasets_info_body');
    h.html("<h3><font color=\"black\">"+header_str+"</font></h3>");
    b.html("<p>"+body_str+"</p>");
    $('#datasets_info_modal').modal();
}


function datasets_alert(header_str, body_str) {
    var h = $('#datasets_alert_header');
    var b = $('#datasets_alert_body');
    h.html("<h3><font color=\"white\">"+header_str+"</font></h3>");
    b.html("<p>"+body_str+"</p>");
    $('#datasets_alert_modal').modal();
}


function datasets_asking(header_str, body_str, rgba_color, func_yes, func_no) {
    var h = $('#datasets_asking_header');
    var b = $('#datasets_asking_body');
    var b_yes = $('#datasets_asking_button_yes');
    var b_no = $('#datasets_asking_button_no');

    h.css('background-color', rgba_color);
    h.html("<h3><font color=\"white\">"+header_str+"</font></h3>");
    b.html("<p>"+body_str+"</p>");

    b_yes.unbind("click");
    b_no.unbind("click");

    b_yes.click(function() {  func_yes(); });
    b_no.click(function() { func_no();  });

    $('#datasets_asking_modal').modal();
}


function datasets_extension_check(f_name, ext) {
    //check the name: should have .csv extension
    var s_name = f_name.split('.');
    if (s_name[s_name.length - 1].toLowerCase() != ext.toLowerCase()) {
        datasets_alert("File Extension Issue", "The extension of this file is not .csv !!\nPlease be sure it is a csv file, and rename it with extension.");
        return false;
    }
    return true;

}
function recover_datasets() {

    var searchParams = new URLSearchParams(window.location.search);
    var database_id = null;
    if (searchParams.has('database_id')) {
        database_id = searchParams.get('database_id')
    }

    sakura.apis.hub.databases[parseInt(database_id)].info().then(function (result) {
        console.log(result);
        if (result.grant_level != 'list') {

            if (result.tables == undefined)
                result.tables = [];
            //Sorting tables by name
            result.tables.sort(datasets_sort_func);

            //Saving the db infos
            database_infos = result;

            $('#datasets_name').html(result.name);
            if (result.short_desc) {
                $('#datasets_description').html(result.short_desc);
            }
            else {
                $('#datasets_description').html('<font color="lightgrey">No short description</font>');
            }


            //Filling dataset
            var body = $('#table_of_datasets').find('tbody');
            body.empty();
            if (result.tables.length == 0) {
                var tr = $('<tr>');
                var td = $('<td>', {html: "The list is empty for now"});
                tr.append(td);
                body.append(tr);
            }

            result.tables.forEach( function(dataset, index) {
                var dataset_id = dataset.table_id;
                var new_row = $(document.createElement('tr'));
                new_row.load('templates/dataset.html', function () {
                    var tds = new_row.find('td');
                    var spans = $(tds[2]).find('span');

                    $(tds[0]).empty();
                    $(tds[0]).append($('<a>',{  text: dataset.name,
                                                style: "cursor: pointer;",
                                                onclick: "datasets_visu_dataset("+dataset_id+");"
                                                })
                                    );

                    $(tds[1]).empty();
                    if (dataset.short_desc)
                        $(tds[1]).append(dataset.short_desc);
                    else
                        $(tds[1]).append("<font color='lightgrey'>__</font>");
                    if (result.grant_level == 'write' || result.grant_level == 'own')
                        spans.toArray().forEach( function(span) {
                            if ($(span).attr('onclick')) {
                                var new_oc = $(span).attr('onclick').replace('ds_id', dataset_id);
                                $(span).attr('onclick', new_oc);
                            }
                        });
                    else if (result.grant_level == 'read')
                        spans.toArray().forEach( function(span) {
                            var className = $(span).attr('class');
                            if (className.indexOf('download') == -1)
                                $(span).css('display', 'none');
                            else {
                                var new_oc = $(span).attr('onclick').replace('ds_id', dataset_id);
                                $(span).attr('onclick', new_oc);
                            }
                        });
                });
                body.append(new_row);
            });

            if (result.grant_level == 'write' || result.grant_level == 'own') {
                $('#datasets_open_creation_button').attr('onclick', 'datasets_open_creation('+database_id+');');
                $('#datasets_open_creation_button').css('display', 'inline');
            }
            else
                $('#datasets_open_creation_button').css('display', 'none');

            //Ask for the existing tags
            sakura.apis.hub.datastores[database_infos.datastore_id].list_expected_columns_tags().then(function (tags_list) {
                columns_tags_list = tags_list;
            });
        }
        else {
            var body = $('#table_of_datasets').find('tbody');
            body.empty();
            var tr = $('<tr>');
            var td = $('<td>', {html: "You need a read access for seeing the datasets (MetaData/Access)"});
            tr.append(td);
            body.append(tr);
            $('#datasets_open_creation_button').css('display', 'none');
        }
    });
}


function datasets_send_file(dataset_id, f, dates, modal, from_what) {
    var first_chunk     = true;
    var f_size          = f.size;
    var sent_data_size  = 0;
    var date            = new Date();
    var nb_cols         = 0;
    var length_alert_done = false;


    Papa.LocalChunkSize = chunk_size;
    var chunks_to_do = [];

    Papa.parse(f, {
        comments: true,
        header: false,
        skipEmptyLines: true,
        chunk: function(chunk, parser) {

            if (first_chunk) {
                nb_cols = chunk.data[0].length;
                chunk.data.splice(0, 1);
                first_chunk = false;
            }
            chunk.data.forEach( function(line) {
                if (line.length != nb_cols) {
                    if (! length_alert_done) {
                        $('#datasets_alert_header').html('<h3>Data Upload</h3>');
                        $('#datasets_alert_body').html('One or more lines of your file doesn\'t have the correct number of columns. These lines are truncated, or filled with null values.');
                        $('#datasets_alert_modal').modal('show');
                    }
                    var diff = nb_cols - line.length;
                    if (diff > 0)
                        for (var i =0; i< diff; i++)
                            line.push('');
                    else
                        line.splice(line.length + diff, - diff)
                }
                //Dates
                dates.forEach(function(date) {
                    d = line[date.column_id];
                    line[date.column_id] = moment(d, date.format).unix();
                });

                //null values
                for (i=0; i<line.length; i++)
                  if (line[i].length == 0)
                      line[i] = null;
            });

            if (chunk.data.length) {
                parser.pause();

                chunks_to_do.push(1);
                sakura.apis.hub.tables[dataset_id].add_rows(chunk.data).then(function(result) {
                    sent_data_size += Papa.LocalChunkSize;
                    var perc = parseInt(sent_data_size/f.size * 100);
                    $('#datasets_'+from_what+'_button').removeClass("btn-primary");
                    $('#datasets_'+from_what+'_button').addClass("btn-success");
                    $('#datasets_'+from_what+'_button').html('Uploading ...'+ perc + '%');
                    $('#datasets_'+from_what+'_progress_bar').css("width", ""+perc+"%");
                    $('#datasets_'+from_what+'_progress_bar').css("aria-valuenow", ""+perc);

                    if (parser)
                        parser.resume();
                    chunks_to_do.pop();

                    if (chunks_to_do.length == 0) {
                        datasets_send_file_ended(date, modal);
                    }
                }).catch( function(error_msg){

                    //We delete the freshly created table
                    sakura.apis.hub.tables[dataset_id].delete().then( function(result) {

                        //Update the display
                        $('#datasets_cancel_creation_button').prop("disabled", false);
                        $('#datasets_creation_button').prop("disabled", false);
                        $('#datasets_creation_button').html('Create Dataset');
                        $('#datasets_creation_button').addClass('btn-primary');
                        $('#datasets_creation_button').removeClass('btn-success');
                        $('#datasets_creation_div_progress_bar').hide();

                        //Testing chunk
                        //-- Test on types
                        var cols_list = []
                        var nb_rows = chunk.data.length;
                        var nb_cols = chunk.data[0].length;
                        for (var c=0; c<nb_cols; c++) {
                            var types = [$('#datasets_ff_type_select_'+c).val()];
                            for (var r=0; r<nb_rows; r++) {
                                types.push(get_type(chunk.data[r][c]));
                            }
                            var ntype = check_types(types);
                            if (ntype != $('#datasets_ff_type_select_'+c).val()) {
                                cols_list.push([$('#datasets_creation_col_name_ff_'+c).val(), ntype]);
                            }
                            $('#datasets_ff_type_select_'+c).val(ntype);
                            $('#datasets_ff_type_select_'+c).selectpicker('refresh');
                        }

                        //Then give the message
                        var msg = 'According to the error, the type of the following columns <b>has been udpated</b>:<br>';
                        cols_list.forEach( function(e) {
                            msg += '- <b>'+e[0]+'</b> >> '+e[1]+'<br>';
                        });
                        msg += '<br><b>Do you want to create the dataset with these column types?</b>';

                        if (cols_list.length) {
                            datasets_asking('Error in adding rows into the dataset',
                                            error_msg+'<br><br>'+msg,
                                            'rgba(217,83,79)',
                                            function() {  datasets_send_new(database_infos.database_id)},
                                            function() {  console.log("NO");}   );
                        }
                        else {
                            datasets_alert('Error in adding rows into the dataset',error_msg);
                        }
                        return false;
                    }).catch(
                    function (error_msg) {
                        console.log('Error in deleting Table !!!');
                    });
                });
            }
        },
        complete: function() {
            if (chunks_to_do.length == 0) {
                datasets_send_file_ended(date, modal);
            }
        },
        error: function (error) {
            datasets_alert("Parsing error", error);
        }
    });
}

function datasets_send_file_ended(date, modal) {
    var ndate = new Date();
    var s = parseInt((ndate.getTime() - date.getTime())/1000);
    var m = parseInt(s/60);
    console.log("Uploading time: "+m+"min:"+s+"s");
    modal.modal('hide');
    recover_datasets();
}


function datasets_check_date_format(date, format_div, format_input, result_div, result_input) {
    var m2 = moment(date, format_input.val());
    if (! m2._isValid) {
        format_div.attr("class", "has-error");
        result_div.attr("class", "has-error");
        result_input.val("Invalid format");
    }
    else{
        format_div.attr("class", "");
        result_div.attr("class", "has-success");
        result_input.val(m2._d);
    }
}


function this_col_is_a_date(col) {
    if (col[1] != 'date')
        return false;
    return true;
}


function datasets_delete(dataset_id) {
    datasets_asking('Delete a Dataset',
                    'Are you sure you want to definitely delete this dataset ??',
                    'rgba(217,83,79)',
                    function() {datasets_delete_yes(dataset_id, true);},
                    function(){});
}

function datasets_delete_yes(dataset_id, alert) {
    console.log('Deleting !!!', dataset_id);
    sakura.apis.hub.tables[dataset_id].delete().then(function() {
        console.log("Dataset deleted");
        //refresh datasets list
        recover_datasets();
    }).catch( function (error_msg) {
        if (alert)
            datasets_alert('Error deleting Dataset', error_msg);
        else
            console.log('Error deleting Dataset:', error_msg);
    });
}
