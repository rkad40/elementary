"use strict";

function PleaseWait(enable)
{
    // Add please-wait-overlay and please-wait-dialog if they don't already exist.
    if ($('#please-wait-overlay').length == 0) 
    {
        $('body').append('<div id="please-wait-overlay" style="display: none;"><div><div id="please-wait-dialog" style="display: none;"><div class="Image"><img src="/assets/static/img/misc/spinner.gif"></div><div class="Text">Loading content ...</div></div>');
        $('#please-wait-overlay').css({'position': 'fixed', 'padding': 0, 'margin': 0, 'top': 0, 'left': 0, 'width': '100%', 'height': '100%', 'background': 'rgba(80,80,80,0.3)', 'z-index': 10000});
        $('#please-wait-dialog').css({'position': 'absolute', 'width': 280, 'height': 100, 'top': '50%', 'left': '50%', 'margin': '0 0 0 0', 'background': 'rgb(0,0,0)', 'z-index': 10001, 'border-radius': 10});
        $('#please-wait-dialog .Image').css({'display': 'inline-block'});
        $('#please-wait-dialog .Text').css({'display': 'inline-block'});
        $('#please-wait-dialog .Image img').css({'position': 'relative', 'top': 25, 'left': 20, 'width': 48, 'height': 'auto'});
        $('#please-wait-dialog .Text').css({'position': 'relative', 'top': '28px', 'left': '35px', 'color': '#fff', 'font-size': '18px', 'font-family': 'Verdana', 'font-weight': 500});
        $('#please-wait-dialog').css('top', ($(window).height() - $('#please-wait-dialog').height()) / 2);
        $('#please-wait-dialog').css('left', ($(window).width() - $('#please-wait-dialog').width()) / 2);
    }
    if(enable)
    {
        $('#please-wait-overlay').fadeIn(100);
        $('#please-wait-dialog').fadeIn(500);
    }
    else
    {
        $('#please-wait-dialog').fadeOut(200);
        $('#please-wait-overlay').fadeOut(100);
    }
};

function PassCodeAppend(value)
{
    let passCode = $('#entry-passcode').val();
    $('#entry-passcode').val(passCode + String(value));
};
