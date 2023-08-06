// class App{
//     constructor(el){
//         this.email=el.find('.email-input');
//         this.password=el.find('.password-input');
//         this.submit=el.find('.btn-submit');
//         this.msg=el.find('.msg-box');
//     }
//     bind(){
//         var app=this;
//         this.submit.click(()=>{
//             var data={
//                 user_email:app.email.val(),
//                 user_password:app.password.val()
//             };
//
//         })
//     }
//     postJson(url,data){
//         return $.post({url:url,data:JSON.stringify(data),async:false}).responseJSON;
//     }
//
// }
wp={};
console.log('my.js loaded.');
wp.debug=true;
function tlog(text) {
    if(wp.debug){
        console.log(message="tlog message:");
        console.log(text);
    }
}
function postJson(url, data) {
    return $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: url,
        data: JSON.stringify(data),
        async: false,
        dataType: "json"
    });
}


var myjs = 'Myjs is loaded;';

function disable_ctrl_s() {
    document.onkeydown = function (e) {
        e = e || window.event;//Get event

        if (!e.ctrlKey) return;

        var code = e.which || e.keyCode;//Get key code

        switch (code) {
            case 83://Block Ctrl+S
            case 87://Block Ctrl+W -- Not work in Chrome and new Firefox
                e.preventDefault();
                e.stopPropagation();
                break;
        }
    };
}

wp.postJson = postJson;
wp.disable_ctrl_s = disable_ctrl_s;
T = {
    NOT_FOUND: "NOT_FOUND",
    NOT_EXISTS: "NOT_EXISTS",
    NO_VALUE: "NO_VALUE",
    NOT_IMPLEMENTED: "NOT_IMPLEMENTED",
    NOT_ALLOWED: "NOT_ALLOWED",
    EMPTY: "EMPTY",
    NO_SUCH_VALUE: "NO_SUCH_VALUE",
    NO_SUCH_ATTR: "NO_SUCH_ATTR",
    NOT_GIVEN: "NOT_GIVEN",
    FILE: "FILE",
    DIR: "DIR",
    LINK: "LINK",
    MOUNT: "MOUNT"
}
wp.makeResizable=function(el){
//    dragresize.js needed.

}
wp.simpleMakeResizable=function(el){
    el.style.resize='both';
    el.style.overflow='auto';
}
wp.makeDraggable = function (el,head) {
    // Make the DIV element draggable:
    dragElement(el);

    function dragElement(elmnt) {
        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
        if (head) {
            // if present, the header is where you move the DIV from:
            head.onmousedown = dragMouseDown;
        } else {
            // otherwise, move the DIV from anywhere inside the DIV:
            elmnt.onmousedown = dragMouseDown;
        }

        function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            // get the mouse cursor position at startup:
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            // calculate the new cursor position:
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            // set the element's new position:
            elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
            elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
        }

        function closeDragElement() {
            // stop moving when mouse button is released:
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }
}

$(document).ready(function () {
    wp.makeDraggable($('.draggable')[0],$('.draggable > .draggable-head')[0]);
    tlog($('.draggable > .draggable-head')[0]);
})