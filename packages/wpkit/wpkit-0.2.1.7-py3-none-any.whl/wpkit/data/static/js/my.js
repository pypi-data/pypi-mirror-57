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
console.log('my.js loaded.');
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

var myjs='Myjs is loaded;';
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